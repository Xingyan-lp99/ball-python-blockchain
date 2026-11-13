import hashlib
import logging
from pathlib import Path

from sqlalchemy import select

from blockchain.transactions import (
    CHAIN_ERRORS, TransactionProblem, transaction_lock, transaction_report, persist_receipt,
)
from certificates.local_chain import CertificateSubject, CertificatePreflightError
from certificates.models import Certificate, CertificateHistory, CertificateVersion, IssuanceAttempt, Laboratory, StoredFile
from certificates.storage import MAX_PDF_BYTES, original_path, save_original
from snake_registry.local_chain import ChainConflict, ChainStale, hex_value
from snake_registry.models import Snake

logger = logging.getLogger(__name__)


def blocked_state(attempt, error: CertificatePreflightError):
    check = "conflict" if error.code in {"issuer_wallet_mismatch", "certificate_record_conflict"} else "verified"
    state = transaction_report(attempt, check, error.detail)
    state.error_code = error.code
    return state


def selected_certificate(session, certificate_id: str, version_number: int = 1, history_id=None):
    row = session.execute(
        select(Certificate, CertificateVersion, Snake, Laboratory, StoredFile)
        .join(CertificateVersion, CertificateVersion.certificate_id == Certificate.id)
        .join(Snake, Snake.id == Certificate.snake_id)
        .join(Laboratory, Laboratory.id == Certificate.laboratory_id)
        .join(StoredFile, StoredFile.id == CertificateVersion.file_id)
        .join(CertificateHistory, CertificateHistory.id == CertificateVersion.history_id)
        .where(Certificate.certificate_id == certificate_id.strip(), CertificateVersion.version_number == version_number,
               CertificateHistory.id == history_id if history_id else CertificateHistory.registry_kind == "legacy")
    ).first()
    if row is None:
        raise TransactionProblem(404, "Selected certificate version/deployment history not found")
    return row


def latest_attempt(session, version):
    return session.scalar(select(IssuanceAttempt).where(IssuanceAttempt.version_id == version.id)
                          .order_by(IssuanceAttempt.created_at.desc(), IssuanceAttempt.id.desc()).limit(1))


def subject_for(row) -> CertificateSubject:
    certificate, version, snake, _, _ = row
    return CertificateSubject(certificate.certificate_id, snake.snake_id, version.issuer_address, version.file_hash, version.version_number)


def metadata(row, state=None) -> dict:
    certificate, version, snake, laboratory, stored = row
    return {
        "certificate_id": certificate.certificate_id, "snake_id": snake.snake_id,
        "lab_id": laboratory.lab_id, "lab_name": laboratory.display_name,
        "issuer_address": version.issuer_address, "version": version.version_number,
        "sha256": version.file_hash.hex(), "original_filename": stored.original_filename,
        "size_bytes": stored.size_bytes, "created_at": version.created_at,
        "issuance": state or transaction_report(None),
        "latest_version_checked": False, "revocation_checked": False,
    }


def upload_v1(session, certificate_id, snake_id, content, filename, lab_id, chain_factory):
    if lab_id != "LAB001":
        raise TransactionProblem(403, "Only the server demo laboratory LAB001 may upload V1")
    certificate_id = certificate_id.strip()
    if not certificate_id or not snake_id.strip():
        raise TransactionProblem(422, "Certificate ID and snake ID are required")
    with transaction_lock(session):
        existing = session.scalar(select(Certificate).where(Certificate.certificate_id == certificate_id))
        if existing:
            row = selected_certificate(session, certificate_id)
            if row[2].snake_id != snake_id.strip() or row[3].lab_id != lab_id or row[1].file_hash != hashlib.sha256(content).digest():
                raise TransactionProblem(409, "V1 already exists; its subject and original bytes cannot be overwritten")
            return row, False
        snake = session.scalar(select(Snake).where(Snake.snake_id == snake_id.strip()))
        if snake is None:
            raise TransactionProblem(404, "Snake database profile not found")
        chain = chain_factory()  # Reads the server mapping; does not broadcast.
        laboratory = session.scalar(select(Laboratory).where(Laboratory.lab_id == lab_id))
        if laboratory is None:
            laboratory = Laboratory(lab_id=lab_id, display_name=chain.lab_name)
            session.add(laboratory)
            session.flush()
        key, digest = save_original(content)
        stored = StoredFile(storage_key=key, original_filename=Path(filename.replace("\\", "/")).name,
                            media_type="application/pdf", size_bytes=len(content), content_hash=digest)
        certificate = Certificate(certificate_id=certificate_id, snake_id=snake.id, laboratory_id=laboratory.id)
        session.add_all([stored, certificate])
        session.flush()
        history = CertificateHistory(certificate_id=certificate.id, registry_kind="legacy", chain_id=chain.chain_id,
                                     contract_address=chain.address, instance_id=chain.instance_id)
        session.add(history)
        session.flush()
        version = CertificateVersion(certificate_id=certificate.id, history_id=history.id, version_number=1, file_id=stored.id,
                                     file_hash=digest, hash_algorithm="sha256", issuer_address=chain.manager)
        session.add(version)
        session.commit()
        return selected_certificate(session, certificate_id), True


def assert_scope(chain, attempt):
    chain.validate_scope()
    if attempt and (
        attempt.chain_id != chain.chain_id or attempt.contract_address.lower() != chain.address.lower()
        or attempt.instance_id != chain.instance_id or attempt.manager_address.lower() != chain.manager.lower()
    ):
        raise ChainStale


def new_attempt(row, chain, **values):
    return IssuanceAttempt(version_id=row[1].id, chain_id=chain.chain_id, contract_address=chain.address,
                           instance_id=chain.instance_id, manager_address=chain.manager, **values)


def reconcile(session, row, attempt, chain):
    assert_scope(chain, attempt)
    history = session.get(CertificateHistory, row[1].history_id)
    if history.contract_address is None:
        # A migrated, never-submitted legacy draft has no historical chain evidence.
        # Its target becomes durable with the first intent/recovery commit.
        history.chain_id, history.contract_address, history.instance_id = chain.chain_id, chain.address, chain.instance_id
    subject = subject_for(row)
    record = chain.record(subject.certificate_id) if subject.version == 1 else chain.record(subject.certificate_id, subject.version)
    if record:
        chain.assert_record(subject, record)
        transaction_hash = chain.registration_hash(subject)
        if not transaction_hash:
            raise ChainConflict
        if attempt is None or (attempt.transaction_hash and attempt.transaction_hash != transaction_hash):
            attempt = new_attempt(row, chain, start_block=0, status="submitted", transaction_hash=transaction_hash)
            session.add(attempt)
            session.commit()
        elif attempt.transaction_hash != transaction_hash:
            attempt.transaction_hash = transaction_hash
            attempt.status = "submitted"
            session.commit()
    elif attempt and attempt.status == "confirmed":
        raise ChainStale
    if attempt and not attempt.transaction_hash and attempt.nonce is not None:
        transaction_hash = chain.recover_hash(attempt.nonce, attempt.start_block, subject)
        if transaction_hash:
            attempt.transaction_hash = transaction_hash
            attempt.status = "submitted"
            session.commit()
    if attempt and attempt.transaction_hash:
        if not persist_receipt(session, subject, attempt, chain):
            return transaction_report(attempt, "verified", "Awaiting receipt; issuance is not confirmed")
    return transaction_report(attempt, "verified", attempt.failure_code if attempt else None)


def issuance_state(session, row, chain_factory):
    attempt = latest_attempt(session, row[1])
    try:
        with transaction_lock(session):
            chain = chain_factory()
            state = reconcile(session, row, attempt, chain)
            if state.status == "not_submitted":
                # Refresh must expose a missing prerequisite, even before any attempt.
                # This only reads state; it never registers a snake or signs a certificate.
                chain.assert_can_issue(subject_for(row))
            return state
    except CertificatePreflightError as error:
        return blocked_state(attempt, error)
    except ChainStale:
        return transaction_report(attempt, "stale", "Deployment changed or reset; historical issuance is not current")
    except ChainConflict:
        return transaction_report(attempt, "conflict", "Chain certificate evidence conflicts with the selected version")
    except CHAIN_ERRORS:
        return transaction_report(attempt, "unavailable", "Chain unavailable; issuance cannot be confirmed")
    except TransactionProblem:
        return transaction_report(attempt, "not_checked", "Another transaction is processing; refresh shortly")


def issue_v1(session, row, lab_id, chain_factory):
    if lab_id != "LAB001" or row[3].lab_id != lab_id:
        raise TransactionProblem(403, "Only the original server demo laboratory may issue this version")
    with transaction_lock(session):
        attempt = latest_attempt(session, row[1])
        try:
            chain = chain_factory()
            state = reconcile(session, row, attempt, chain)
            attempt = latest_attempt(session, row[1])
            if state.status == "confirmed" or (attempt and attempt.transaction_hash and attempt.status != "failed"):
                return state
            chain.assert_can_issue(subject_for(row))
            if attempt is None or attempt.status == "failed":
                nonce, gas_price, start_block = chain.transaction_parameters()
                reserved = session.scalar(select(IssuanceAttempt).where(
                    IssuanceAttempt.chain_id == chain.chain_id,
                    IssuanceAttempt.manager_address == chain.manager, IssuanceAttempt.nonce == nonce,
                    IssuanceAttempt.status.in_(["prepared", "submitted"]),
                ).limit(1))
                if reserved:
                    raise TransactionProblem(409, "Another issuance reserves this laboratory nonce; recover it first")
                attempt = new_attempt(row, chain, nonce=nonce, gas_price=gas_price, start_block=start_block)
                session.add(attempt)
                session.commit()
            attempt.transaction_hash = chain.send(subject_for(row), attempt.nonce, attempt.gas_price)
            attempt.status = "submitted"
            session.commit()
            if persist_receipt(session, subject_for(row), attempt, chain):
                return transaction_report(attempt, "verified", attempt.failure_code)
            return transaction_report(attempt, "verified", "Awaiting receipt; issuance is not confirmed")
        except CertificatePreflightError as error:
            logger.warning("certificate_issue_blocked code=%s certificate_id=%r snake_id=%r",
                           error.code, row[0].certificate_id, row[2].snake_id)
            raise TransactionProblem(409, error.detail, code=error.code) from None
        except ChainStale:
            raise TransactionProblem(409, "Deployment changed/reset; original PDF and historical evidence retained", code="deployment_stale") from None
        except ChainConflict:
            raise TransactionProblem(409, "On-chain transaction, receipt or event conflicts with the selected version; confirmation and overwrite are refused", code="issuance_evidence_conflict") from None
        except CHAIN_ERRORS:
            if attempt:
                return transaction_report(attempt, "unavailable", "RPC response unavailable; refresh before retrying")
            raise TransactionProblem(503, "Local certificate deployment/RPC unavailable; issuance not submitted") from None


def verify_file(session, row, content, chain_factory, source="external"):
    uploaded_hash = hashlib.sha256(content).digest()
    attempt = latest_attempt(session, row[1])
    state = transaction_report(attempt)
    result = {"certificate_id": row[0].certificate_id, "snake_id": row[2].snake_id,
              "lab_id": row[3].lab_id, "lab_name": row[3].display_name, "version": row[1].version_number,
              "issuer_address": row[1].issuer_address, "file_source": source, "file_sha256": uploaded_hash.hex(),
              "on_chain_sha256": None, "file_result": "unable_to_verify",
              "registration": state, "latest_version_checked": False, "revocation_checked": False,
              "version_status": "unknown", "latest_version": None,
              "history_id": str(row[1].history_id)}
    if source == "external":
        result["uploaded_sha256"] = uploaded_hash.hex()
    try:
        chain = chain_factory()
        assert_scope(chain, attempt)
        record = chain.record(row[0].certificate_id) if row[1].version_number == 1 else chain.record(row[0].certificate_id, row[1].version_number)
        if record is None:
            result["message"] = "No current on-chain record for the selected version; file comparison could not be completed"
            if attempt and attempt.status == "confirmed":
                result["registration"] = transaction_report(attempt, "stale", result["message"])
            return result
        # Hash the actual supplied bytes and compare with LIVE chain evidence.
        # Neither source uses a cached DB digest or the filename as the comparison.
        subject = CertificateSubject(row[0].certificate_id, row[2].snake_id, row[1].issuer_address, record["file_hash"], row[1].version_number)
        chain.assert_record(subject, record)
        transaction_hash = chain.registration_hash(subject)
        if not transaction_hash:
            raise ChainConflict
        receipt = chain.receipt(transaction_hash)
        if receipt is None or receipt["status"] != 1:
            raise ChainConflict
        chain.verify_success(subject, transaction_hash, receipt)
        result["registration"] = {
            "status": "confirmed", "chain_check": "verified", "transaction_hash": transaction_hash,
            "chain_id": chain.chain_id, "contract_address": chain.address, "instance_id": chain.instance_id,
            "manager_address": record["issuer_address"], "block_number": receipt["blockNumber"],
            "block_hash": hex_value(receipt["blockHash"]),
        }
        result["on_chain_sha256"] = record["file_hash"].hex()
        result["file_result"] = "match" if uploaded_hash == record["file_hash"] else "mismatch"
        result.update(version_information(chain, row[0].certificate_id, row[1].version_number))
        label = "The platform-stored PDF" if source == "platform" else "The uploaded external PDF"
        result["message"] = (
            f"{label} matches this registered version. Hash matching does not prove biological findings."
            if result["file_result"] == "match" else
            f"{label} differs from this registered version. This does not identify who changed it."
        )
    except ChainStale:
        result["registration"] = transaction_report(attempt, "stale", "Deployment invalid; historical evidence is not current")
        result["message"] = "Deployment invalid; file comparison could not be completed"
    except ChainConflict:
        result["registration"] = transaction_report(attempt, "conflict", "Certificate evidence could not be established")
        result["message"] = "Chain record/receipt conflict; file comparison could not be completed"
    except CHAIN_ERRORS:
        result["registration"] = transaction_report(attempt, "unavailable", "RPC unavailable; confirmation cannot be checked")
        result["message"] = "RPC unavailable; file comparison could not be completed"
    return result


def version_information(chain, certificate_id, version_number):
    result = {"version_status": "unknown", "latest_version": None, "latest_version_checked": False}
    try:
        # The real adapters always read current contract state. Legacy is provably V1-only.
        latest = chain.latest_version(certificate_id)
        if latest >= version_number:
            result.update(version_status="latest" if latest == version_number else "superseded",
                          latest_version=latest, latest_version_checked=True)
    except (ChainStale, ChainConflict, *CHAIN_ERRORS):
        pass
    return result


def verify_stored_file(session, row, chain_factory):
    # Read the actual platform file on EVERY click; do not read its cached digest.
    try:
        with original_path(row[4].storage_key).open("rb") as document:
            content = document.read(MAX_PDF_BYTES + 1)
        if len(content) > MAX_PDF_BYTES:
            raise OSError("Stored file exceeds the bounded read limit")
    except (OSError, TransactionProblem):
        result = metadata(row, issuance_state(session, row, chain_factory))
        result["registration"] = result.pop("issuance")
        result.pop("sha256", None)
        result.update(file_source="platform", file_sha256=None, on_chain_sha256=None,
                      version_status="unknown", latest_version=None,
                      file_result="unable_to_verify", message="Platform PDF is unavailable; no file comparison could be completed")
        return result
    # Even invalid/changed PDF bytes should be compared rather than regenerated.
    return verify_file(session, row, content, chain_factory, source="platform")
