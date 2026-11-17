import os
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from datetime import datetime
from typing import Annotated, Literal

import psycopg
from fastapi import APIRouter, File, Form, HTTPException, Path, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field
from requests.exceptions import RequestException
from web3 import Web3
from web3.exceptions import Web3Exception

from backend.auth import AuthenticatedAccount, LaboratoryAccount
from backend.certificate_files import MAX_PDF_BYTES, get_certificate_pdf_path
from backend.certificates import (
    CertificateIssuanceError,
    CertificateRevisionConflictError,
    get_certificate_file_reference,
    issue_certificate,
    list_certificate_history,
    revise_certificate,
)


router = APIRouter(prefix="/api/v1")


class CertificateIssuanceResponse(BaseModel):
    snake_id: str
    laboratory_id: str
    title: str
    series_id: str
    version_id: str
    version_number: Literal[1]
    file_hash: str
    issuer_address: str
    status: Literal["current"]
    issued_at: datetime
    transaction_hash: str
    receipt_status: Literal[1]


class CertificateRevisionResponse(CertificateIssuanceResponse):
    version_number: int = Field(ge=2)
    previous_version_id: str
    previous_version_status: Literal["superseded"]


class CertificateVersionHistory(BaseModel):
    version_id: str
    version_number: int
    previous_version_id: str | None
    file_hash: str
    issuer_address: str
    issued_at: datetime | None
    status: Literal["current", "superseded"] | None
    evidence_status: Literal["confirmed", "unconfirmed", "unavailable", "mismatch"]
    download_url: str


class CertificateSeriesHistory(BaseModel):
    series_id: str
    title: str
    laboratory_id: str
    laboratory_name: str
    versions: list[CertificateVersionHistory]


class CertificateHistoryResponse(BaseModel):
    snake_id: str
    chain_block_number: int | None
    warnings: list[str]
    series: list[CertificateSeriesHistory]


@contextmanager
def _read_certificate_database() -> Iterator[psycopg.Connection]:
    password = os.environ.get("DEMO_DB_PASSWORD")
    if not password:
        raise HTTPException(503, "Database configuration is unavailable.")

    try:
        with psycopg.connect(
            host="127.0.0.1", port=5433, dbname="ballpython_demo",
            user="ballpython", password=password,
            connect_timeout=5, autocommit=True,
        ) as connection:
            yield connection
    except (psycopg.Error, OSError):
        raise HTTPException(503, "The certificate service is unavailable.") from None


# Purpose: share configuration, database access, and safe error responses.
# Without this helper, the two upload routes would duplicate this handling.
def _write_certificate(
    *,
    operation: Callable[..., dict],
    participant_id: str,
    pdf: UploadFile,
    parameters: dict,
) -> dict | JSONResponse:
    password = os.environ.get("DEMO_DB_PASSWORD")
    snake_address = os.environ.get("DEMO_REGISTRY_ADDRESS", "")
    certificate_address = os.environ.get(
        "DEMO_CERTIFICATE_REGISTRY_ADDRESS",
        "",
    )

    if (
        not password
        or not Web3.is_address(snake_address)
        or not Web3.is_address(certificate_address)
    ):
        return JSONResponse(
            status_code=503,
            content={
                "detail": "Certificate configuration is incomplete. "
                "No transaction was submitted.",
                "outcome": "not_submitted",
            },
        )

    result = None

    try:
        content = pdf.file.read(MAX_PDF_BYTES + 1)

        with psycopg.connect(
            host="127.0.0.1",
            port=5433,
            dbname="ballpython_demo",
            user="ballpython",
            password=password,
            connect_timeout=5,
            autocommit=True,
        ) as connection:
            result = operation(
                connection,
                participant_id=participant_id,
                pdf_content=content,
                certificate_address=certificate_address,
                snake_registry_address=snake_address,
                **parameters,
            )
    except CertificateIssuanceError as error:
        return JSONResponse(
            status_code=502
            if error.outcome in {"failed", "unverified"}
            else 503,
            content={
                "detail": str(error),
                "outcome": error.outcome,
                "series_id": error.series_id,
                "version_id": error.version_id,
                "transaction_hash": error.transaction_hash,
            },
        )
    except CertificateRevisionConflictError as error:
        return JSONResponse(
            status_code=409,
            content={"detail": str(error), "outcome": "not_submitted"},
        )
    except PermissionError as error:
        return JSONResponse(
            status_code=403,
            content={
                "detail": str(error),
                "outcome": "not_submitted",
            },
        )
    except LookupError as error:
        return JSONResponse(
            status_code=404,
            content={
                "detail": str(error),
                "outcome": "not_submitted",
            },
        )
    except ValueError:
        return JSONResponse(
            status_code=422,
            content={
                "detail": "Upload a PDF with a valid file header, "
                "no larger than 10 MB.",
                "outcome": "not_submitted",
            },
        )
    except (
        psycopg.Error,
        OSError,
        RuntimeError,
        RequestException,
        Web3Exception,
    ):
        return JSONResponse(
            status_code=503,
            content={
                "detail": (
                    "The transaction was confirmed, but the response could not "
                    "be completed. Do not submit again."
                    if result is not None
                    else "The certificate service is unavailable. "
                    "No transaction was submitted."
                ),
                "outcome": (
                    "storage_error"
                    if result is not None
                    else "not_submitted"
                ),
                "series_id": (
                    result["series_id"] if result is not None else None
                ),
                "version_id": (
                    result["version_id"] if result is not None else None
                ),
                "transaction_hash": (
                    result["transaction_hash"] if result is not None else None
                ),
            },
        )

    return result


# Purpose: accept an authenticated laboratory's first report upload.
# Without this route, the frontend cannot start the V1 issuance workflow.
@router.post(
    "/certificate-series",
    status_code=201,
    response_model=CertificateIssuanceResponse,
)
def create_certificate_series(
    snake_id: Annotated[str, Form(min_length=1)],
    title: Annotated[str, Form(min_length=1, pattern=r"\S")],
    pdf: Annotated[UploadFile, File()],
    account: LaboratoryAccount,
) -> dict | JSONResponse:
    return _write_certificate(
        operation=issue_certificate,
        participant_id=account.participant_id,
        pdf=pdf,
        parameters={"snake_id": snake_id, "title": title},
    )


# Purpose: accept a correction for an existing report series.
# Without this route, laboratory staff cannot request an append-only revision.
@router.post(
    "/certificate-series/{series_id}/versions",
    status_code=201,
    response_model=CertificateRevisionResponse,
)
def create_certificate_revision(
    series_id: Annotated[str, Path(min_length=1)],
    pdf: Annotated[UploadFile, File()],
    account: LaboratoryAccount,
) -> dict | JSONResponse:
    return _write_certificate(
        operation=revise_certificate,
        participant_id=account.participant_id,
        pdf=pdf,
        parameters={"series_id": series_id},
    )


# Purpose: expose report history to signed-in demonstration participants.
# Without this route, buyers cannot select or distinguish earlier report versions.
@router.get(
    "/snakes/{snake_id}/certificate-series",
    response_model=CertificateHistoryResponse,
)
def read_certificate_history(
    snake_id: Annotated[str, Path(min_length=1)],
    account: AuthenticatedAccount,
) -> dict:
    try:
        with _read_certificate_database() as connection:
            return list_certificate_history(
                connection,
                snake_id=snake_id,
                certificate_address=os.environ.get(
                    "DEMO_CERTIFICATE_REGISTRY_ADDRESS", ""
                ),
                snake_registry_address=os.environ.get("DEMO_REGISTRY_ADDRESS", ""),
            )
    except LookupError:
        raise HTTPException(404, "Snake profile not found.") from None


# Purpose: download the preserved PDF without exposing a filesystem reference.
# Without this route, historical versions would be listed without their files.
@router.get("/certificate-versions/{version_id}/file", response_model=None)
def download_certificate_pdf(
    version_id: Annotated[str, Path(min_length=1)],
    account: AuthenticatedAccount,
) -> FileResponse:
    with _read_certificate_database() as connection:
        reference = get_certificate_file_reference(connection, version_id=version_id)
        path = get_certificate_pdf_path(reference) if reference is not None else None

    if path is None:
        raise HTTPException(404, "The original certificate PDF was not found.")

    return FileResponse(
        path,
        media_type="application/pdf",
        filename=f"{version_id}.pdf",
        headers={"Cache-Control": "private, no-store"},
    )
