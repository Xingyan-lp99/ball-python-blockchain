from uuid import uuid4
from urllib.parse import quote

import psycopg
from psycopg.rows import dict_row
from requests.exceptions import RequestException
from web3 import Web3
from web3.exceptions import ContractCustomError, Web3Exception

from backend.certificate_chain import (
    CertificateTransactionError,
    connect_certificate_registry,
    issue_certificate_on_chain,
    prepare_certificate_issuance,
    revise_certificate_on_chain,
)
from backend.certificate_files import (
    save_certificate_pdf,
    validate_certificate_pdf,
)


class CertificateIssuanceError(RuntimeError):
    """Expose report and transaction identifiers without local file paths."""

    def __init__(
        self,
        message: str,
        *,
        series_id: str,
        version_id: str,
        transaction_hash: str | None,
        outcome: str,
    ) -> None:
        super().__init__(message)
        self.series_id = series_id
        self.version_id = version_id
        self.transaction_hash = transaction_hash
        self.outcome = outcome


class CertificateRevisionConflictError(RuntimeError):
    """Stop revision when stored and confirmed version states disagree."""


# Purpose: retain the known transaction state linked to this version.
# Without this row, a submitted transaction would lose its database link.
def _record_transaction(
    connection: psycopg.Connection,
    *,
    transaction_hash: str,
    snake_id: str,
    version_id: str,
    status: str,
    operation: str = "issue_certificate",
) -> None:
    connection.execute(
        """
        INSERT INTO blockchain_transactions (
            transaction_hash, operation, status, snake_id, version_id
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (transaction_hash)
        DO UPDATE SET status = EXCLUDED.status
        """,
        (transaction_hash, operation, status, snake_id, version_id),
    )


# Purpose: coordinate original-file storage, V1 metadata, and chain issuance.
# Without this operation, the HTTP route would have to mix database,
# file-storage, and blockchain business decisions.
def issue_certificate(
    connection: psycopg.Connection,
    *,
    participant_id: str,
    snake_id: str,
    title: str,
    pdf_content: bytes,
    certificate_address: str,
    snake_registry_address: str,
) -> dict:
    validate_certificate_pdf(pdf_content)

    laboratory = connection.execute(
        """
        SELECT laboratories.laboratory_id, participants.wallet_address
        FROM laboratories
        JOIN participants
          ON participants.participant_id = laboratories.participant_id
        WHERE laboratories.participant_id = %s
        """,
        (participant_id,),
    ).fetchone()

    if laboratory is None:
        raise PermissionError("The laboratory profile is not configured.")

    laboratory_id, sender_address = laboratory

    snake = connection.execute(
        "SELECT 1 FROM snakes WHERE snake_id = %s",
        (snake_id,),
    ).fetchone()

    if snake is None:
        raise LookupError("Snake profile not found.")

    client, registry = prepare_certificate_issuance(
        certificate_address=certificate_address,
        snake_registry_address=snake_registry_address,
        sender_address=sender_address,
        snake_id=snake_id,
    )

    series_id = f"SERIES-{uuid4().hex}"
    version_id = f"VERSION-{uuid4().hex}"
    file_reference, file_hash = save_certificate_pdf(pdf_content)

    with connection.transaction():
        connection.execute(
            """
            INSERT INTO certificate_series (
                series_id, snake_id, laboratory_id, title
            )
            VALUES (%s, %s, %s, %s)
            """,
            (series_id, snake_id, laboratory_id, title.strip()),
        )

        connection.execute(
            """
            INSERT INTO certificate_versions (
                version_id,
                series_id,
                version_number,
                previous_version_id,
                file_reference,
                file_hash,
                issuer_address,
                status,
                issued_at
            )
            VALUES (%s, %s, 1, NULL, %s, %s, %s, NULL, NULL)
            """,
            (
                version_id,
                series_id,
                file_reference,
                file_hash,
                sender_address,
            ),
        )

    def remember_submission(transaction_hash: str) -> None:
        with connection.transaction():
            _record_transaction(
                connection,
                transaction_hash=transaction_hash,
                snake_id=snake_id,
                version_id=version_id,
                status="submitted",
            )

    try:
        result = issue_certificate_on_chain(
            client=client,
            registry=registry,
            sender_address=sender_address,
            snake_id=snake_id,
            series_id=series_id,
            version_id=version_id,
            file_hash=file_hash,
            on_submitted=remember_submission,
        )
    except CertificateTransactionError as error:
        outcome = error.outcome

        if error.transaction_hash is not None:
            transaction_status = {
                "failed": "failed",
                "unverified": "confirmed",
            }.get(outcome, "submitted")

            try:
                with connection.transaction():
                    _record_transaction(
                        connection,
                        transaction_hash=error.transaction_hash,
                        snake_id=snake_id,
                        version_id=version_id,
                        status=transaction_status,
                    )
            except psycopg.Error:
                outcome = "storage_error"

        raise CertificateIssuanceError(
            str(error),
            series_id=series_id,
            version_id=version_id,
            transaction_hash=error.transaction_hash,
            outcome=outcome,
        ) from None

    try:
        with connection.transaction():
            connection.execute(
                """
                UPDATE certificate_versions
                SET status = 1, issued_at = %s
                WHERE version_id = %s
                """,
                (result["issued_at"], version_id),
            )

            _record_transaction(
                connection,
                transaction_hash=result["transaction_hash"],
                snake_id=snake_id,
                version_id=version_id,
                status="confirmed",
            )
    except psycopg.Error:
        raise CertificateIssuanceError(
            "Chain issuance was confirmed, but the database result "
            "could not be fully saved. Do not submit again.",
            series_id=series_id,
            version_id=version_id,
            transaction_hash=result["transaction_hash"],
            outcome="storage_error",
        ) from None

    return {
        **result,
        "snake_id": snake_id,
        "laboratory_id": laboratory_id,
        "title": title.strip(),
        "series_id": series_id,
        "version_id": version_id,
        "version_number": 1,
        "file_hash": file_hash,
        "issuer_address": sender_address,
        "status": "current",
    }


# Purpose: show all report series and versions with freshly read chain status.
# Without these reads, a cached V1 status could still appear Current after V2.
def list_certificate_history(
    connection: psycopg.Connection,
    *,
    snake_id: str,
    certificate_address: str,
    snake_registry_address: str,
) -> dict:
    if connection.execute(
        "SELECT 1 FROM snakes WHERE snake_id = %s", (snake_id,)
    ).fetchone() is None:
        raise LookupError("Snake profile not found.")

    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            """
            SELECT series.series_id, series.title, series.laboratory_id,
                   laboratories.name AS laboratory_name,
                   versions.version_id, versions.version_number,
                   versions.previous_version_id, versions.file_hash,
                   versions.issuer_address, versions.issued_at,
                   versions.status AS stored_status
            FROM certificate_series AS series
            JOIN laboratories USING (laboratory_id)
            LEFT JOIN certificate_versions AS versions USING (series_id)
            WHERE series.snake_id = %s
            ORDER BY series.laboratory_id, series.series_id,
                     versions.version_number
            """,
            (snake_id,),
        )
        rows = cursor.fetchall()

    registry = None
    block_number = None
    if any(row["version_id"] is not None for row in rows):
        try:
            client, registry = connect_certificate_registry(
                certificate_address=certificate_address,
                snake_registry_address=snake_registry_address,
            )
            block_number = client.eth.block_number
        except (OSError, ValueError, RequestException, Web3Exception):
            registry = None

    series_by_id = {}
    for row in rows:
        series = series_by_id.setdefault(
            row["series_id"],
            {
                "series_id": row["series_id"],
                "title": row["title"],
                "laboratory_id": row["laboratory_id"],
                "laboratory_name": row["laboratory_name"],
                "versions": [],
            },
        )
        if row["version_id"] is None:
            continue

        version = {
            field: row[field]
            for field in (
                "version_id", "version_number", "previous_version_id",
                "file_hash", "issuer_address", "issued_at",
            )
        }
        version.update(
            status=None,
            evidence_status="unavailable",
            download_url=(
                "/api/v1/certificate-versions/"
                f"{quote(row['version_id'], safe='')}/file"
            ),
        )

        if registry is not None:
            try:
                evidence = registry.functions.getVersion(row["version_id"]).call(
                    block_identifier=block_number
                )
                matches = (
                    list(evidence[:5])
                    == [
                        snake_id, row["series_id"], row["version_id"],
                        row["version_number"], row["previous_version_id"] or "",
                    ]
                    and evidence[5].lower() == row["issuer_address"].lower()
                    and bytes(evidence[6]).hex() == row["file_hash"]
                    and evidence[7] in {1, 2}
                )
                if matches:
                    version["status"] = {1: "current", 2: "superseded"}[evidence[7]]
                    version["evidence_status"] = "confirmed"
                else:
                    version["evidence_status"] = "mismatch"
            except ContractCustomError as error:
                missing_selector = Web3.to_hex(
                    Web3.keccak(text="VersionNotFound(string)")[:4]
                )
                if (
                    row["stored_status"] is None
                    and isinstance(error.data, str)
                    and error.data.startswith(missing_selector)
                ):
                    version["evidence_status"] = "unconfirmed"
            except (OSError, ValueError, RequestException, Web3Exception):
                pass

        series["versions"].append(version)

    evidence_states = {
        version["evidence_status"]
        for series in series_by_id.values()
        for version in series["versions"]
    }
    warnings = []
    if "unavailable" in evidence_states:
        warnings.append(
            "Chain evidence is unavailable for some versions. "
            "Their status could not be confirmed."
        )
    if "mismatch" in evidence_states:
        warnings.append(
            "Some certificate metadata does not match the chain. "
            "Those version statuses are not confirmed."
        )

    return {
        "snake_id": snake_id,
        "chain_block_number": block_number,
        "warnings": warnings,
        "series": list(series_by_id.values()),
    }


# Purpose: resolve a version to its preserved file reference inside this module.
# Without this lookup, the download route cannot find the selected original PDF.
def get_certificate_file_reference(
    connection: psycopg.Connection, *, version_id: str
) -> str | None:
    row = connection.execute(
        "SELECT file_reference FROM certificate_versions WHERE version_id = %s",
        (version_id,),
    ).fetchone()
    return row[0] if row is not None else None


# Purpose: append a report in the original issuer's series without replacing files.
# Without this operation, uploading a correction would create an unrelated V1.
def revise_certificate(
    connection: psycopg.Connection,
    *,
    participant_id: str,
    series_id: str,
    pdf_content: bytes,
    certificate_address: str,
    snake_registry_address: str,
) -> dict:
    validate_certificate_pdf(pdf_content)

    series = connection.execute(
        """
        SELECT certificate_series.snake_id,
               certificate_series.laboratory_id,
               certificate_series.title,
               laboratories.participant_id,
               participants.wallet_address
        FROM certificate_series
        JOIN laboratories USING (laboratory_id)
        JOIN participants
          ON participants.participant_id = laboratories.participant_id
        WHERE series_id = %s
        """,
        (series_id,),
    ).fetchone()

    if series is None:
        raise LookupError("Certificate series not found.")

    snake_id, laboratory_id, title, issuer_participant_id, sender_address = series

    if participant_id != issuer_participant_id:
        raise PermissionError(
            "Only the laboratory that issued this report may revise it."
        )

    client, registry = prepare_certificate_issuance(
        certificate_address=certificate_address,
        snake_registry_address=snake_registry_address,
        sender_address=sender_address,
        snake_id=snake_id,
    )

    block_number = client.eth.block_number
    summary = registry.functions.getSeries(series_id).call(
        block_identifier=block_number
    )

    if summary[0] != snake_id or summary[1].lower() != sender_address.lower():
        raise CertificateRevisionConflictError(
            "The stored series does not match the configured chain."
        )

    previous_version_id = summary[2]
    version_number = summary[3] + 1
    previous = registry.functions.getVersion(previous_version_id).call(
        block_identifier=block_number
    )
    stored_previous = connection.execute(
        """
        SELECT series_id, version_number, previous_version_id,
               file_hash, issuer_address, status
        FROM certificate_versions
        WHERE version_id = %s
        """,
        (previous_version_id,),
    ).fetchone()

    if stored_previous is None or not (
        stored_previous[0] == series_id
        and stored_previous[1] == summary[3]
        and stored_previous[4].lower() == sender_address.lower()
        and stored_previous[5] == 1
        and list(previous[:5])
        == [
            snake_id, series_id, previous_version_id,
            stored_previous[1], stored_previous[2] or "",
        ]
        and previous[5].lower() == sender_address.lower()
        and bytes(previous[6]).hex() == stored_previous[3]
        and previous[7] == 1
    ):
        raise CertificateRevisionConflictError(
            "The current version is not synchronized with the chain. "
            "Check the previous transaction before revising."
        )

    unresolved = connection.execute(
        """
        SELECT 1 FROM certificate_versions
        WHERE series_id = %s AND status IS NULL
        LIMIT 1
        """,
        (series_id,),
    ).fetchone()

    if unresolved is not None:
        raise CertificateRevisionConflictError(
            "This series has an unconfirmed version. "
            "Check its transaction before submitting another revision."
        )

    version_id = f"VERSION-{uuid4().hex}"
    file_reference, file_hash = save_certificate_pdf(pdf_content)

    try:
        with connection.transaction():
            connection.execute(
                """
                INSERT INTO certificate_versions (
                    version_id, series_id, version_number, previous_version_id,
                    file_reference, file_hash, issuer_address, status, issued_at
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, NULL, NULL)
                """,
                (
                    version_id, series_id, version_number, previous_version_id,
                    file_reference, file_hash, sender_address,
                ),
            )
    except psycopg.errors.UniqueViolation:
        raise CertificateRevisionConflictError(
            "A version with this number already exists. "
            "Check its transaction before revising."
        ) from None

    def remember_submission(transaction_hash: str) -> None:
        with connection.transaction():
            _record_transaction(
                connection,
                transaction_hash=transaction_hash,
                snake_id=snake_id,
                version_id=version_id,
                status="submitted",
                operation="revise_certificate",
            )

    try:
        result = revise_certificate_on_chain(
            client=client,
            registry=registry,
            sender_address=sender_address,
            snake_id=snake_id,
            series_id=series_id,
            version_id=version_id,
            version_number=version_number,
            previous_version_id=previous_version_id,
            file_hash=file_hash,
            on_submitted=remember_submission,
        )
    except CertificateTransactionError as error:
        outcome = error.outcome

        if error.transaction_hash is not None:
            transaction_status = {
                "failed": "failed",
                "unverified": "confirmed",
            }.get(outcome, "submitted")

            try:
                with connection.transaction():
                    _record_transaction(
                        connection,
                        transaction_hash=error.transaction_hash,
                        snake_id=snake_id,
                        version_id=version_id,
                        status=transaction_status,
                        operation="revise_certificate",
                    )
            except psycopg.Error:
                outcome = "storage_error"

        raise CertificateIssuanceError(
            str(error),
            series_id=series_id,
            version_id=version_id,
            transaction_hash=error.transaction_hash,
            outcome=outcome,
        ) from None

    try:
        with connection.transaction():
            updated_previous = connection.execute(
                """
                UPDATE certificate_versions SET status = 2
                WHERE version_id = %s AND series_id = %s AND status = 1
                """,
                (previous_version_id, series_id),
            )
            updated_revision = connection.execute(
                """
                UPDATE certificate_versions SET status = 1, issued_at = %s
                WHERE version_id = %s AND status IS NULL
                """,
                (result["issued_at"], version_id),
            )

            if updated_previous.rowcount != 1 or updated_revision.rowcount != 1:
                raise RuntimeError("The stored version states changed.")

            _record_transaction(
                connection,
                transaction_hash=result["transaction_hash"],
                snake_id=snake_id,
                version_id=version_id,
                status="confirmed",
                operation="revise_certificate",
            )
    except (psycopg.Error, RuntimeError):
        raise CertificateIssuanceError(
            "Chain revision was confirmed, but the database result could not "
            "be fully saved. Do not submit again.",
            series_id=series_id,
            version_id=version_id,
            transaction_hash=result["transaction_hash"],
            outcome="storage_error",
        ) from None

    return {
        **result,
        "snake_id": snake_id,
        "laboratory_id": laboratory_id,
        "title": title,
        "series_id": series_id,
        "version_id": version_id,
        "version_number": version_number,
        "previous_version_id": previous_version_id,
        "previous_version_status": "superseded",
        "file_hash": file_hash,
        "issuer_address": sender_address,
        "status": "current",
    }
