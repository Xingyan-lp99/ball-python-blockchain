import ipaddress
import os
from contextlib import contextmanager
from typing import Annotated, Iterator, Literal

import psycopg
from fastapi import APIRouter, File, Form, HTTPException, Path, Request, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field
from web3 import Web3

from backend.auth import AuthenticatedAccount, KeeperAccount, LaboratoryAccount
from backend.certificate_files import MAX_PDF_BYTES, get_certificate_pdf_path
from backend.certificate_routes import (
    CertificateIssuanceResponse,
    CertificateRevisionResponse,
    LaboratoryReportSummary,
)
from backend.keeper_transfer_routes import (
    KeeperTransferInitiationRequest,
    KeeperTransferInitiationResponse,
    KeeperTransferResolutionResponse,
    KeeperTransferStatusResponse,
)
from backend.sepolia_business import (
    SepoliaBusinessError,
    accept_sepolia_keeper_transfer,
    verify_sepolia_keeper_acceptance,
    recover_sepolia_keeper_acceptance,
    certificate_pdf_reference,
    initiate_sepolia_keeper_transfer,
    issue_certificate_on_sepolia,
    list_sepolia_laboratory_reports,
    revise_certificate_on_sepolia,
    sepolia_certificate_history,
    sepolia_keeper_state,
    recover_sepolia_certificate_transaction,
    run_sepolia_certificate_permission_demo,
    simulate_unauthorized_lab_call,
)
from backend.sepolia_registry import SepoliaRegistrationError, get_sepolia_signer


router = APIRouter(prefix="/api/v1/sepolia")


class UnauthorizedCheckRequest(BaseModel):
    snake_id: str = Field(min_length=1)


class CertificateRecoveryRequest(BaseModel):
    transaction_hash: str = Field(pattern=r"^0x[a-fA-F0-9]{64}$")


class CertificatePermissionDemoRequest(BaseModel):
    operation: Literal["unauthorized_issuance", "cross_lab_revision"]
    snake_id: Literal["BP-S004"] = "BP-S004"


@contextmanager
def _database() -> Iterator[psycopg.Connection]:
    password = os.environ.get("DEMO_DB_PASSWORD")
    if not password:
        raise HTTPException(503, "Database configuration is unavailable.")
    try:
        with psycopg.connect(
            host="127.0.0.1", port=5433, dbname="ballpython_demo",
            user="ballpython", password=password, connect_timeout=5,
            autocommit=True,
        ) as connection:
            yield connection
    except (psycopg.Error, OSError):
        raise HTTPException(503, "Sepolia demo database is unavailable.") from None


def _require_local_request(request: Request) -> None:
    try:
        local = bool(request.client and ipaddress.ip_address(request.client.host).is_loopback)
    except ValueError:
        local = False
    if not local:
        raise HTTPException(403, "Sepolia signing is available only through the local demo.")


def _write_error(error: Exception) -> JSONResponse:
    if isinstance(error, SepoliaBusinessError):
        status = 503 if error.outcome in {"unknown", "unverified", "storage_error"} else 502 if error.outcome == "failed" else 422
        payload = {
            "detail": str(error), "outcome": error.outcome,
            "transaction_hash": error.transaction_hash,
            "business_id": error.business_id,
        }
        if error.transaction_hash:
            payload["etherscan_url"] = f"https://sepolia.etherscan.io/tx/{error.transaction_hash}"
        return JSONResponse(status_code=status, content=payload)
    if isinstance(error, PermissionError):
        return JSONResponse(status_code=403, content={"detail": str(error), "outcome": "not_submitted"})
    if isinstance(error, LookupError):
        return JSONResponse(status_code=404, content={"detail": str(error), "outcome": "not_submitted"})
    if isinstance(error, ValueError):
        return JSONResponse(status_code=422, content={"detail": str(error), "outcome": "not_submitted"})
    if isinstance(error, psycopg.errors.UniqueViolation):
        return JSONResponse(status_code=409, content={"detail": "An equivalent Sepolia operation is already checkpointed; inspect its status before trying again.", "outcome": "unknown"})
    return JSONResponse(status_code=503, content={"detail": "The Sepolia operation could not be completed. Check any saved transaction before retrying.", "outcome": "unknown"})


@router.post("/certificate-series", status_code=201, response_model=CertificateIssuanceResponse)
def create_sepolia_certificate(
    request: Request,
    snake_id: Annotated[str, Form(min_length=1)],
    title: Annotated[str, Form(min_length=1, pattern=r"\S")],
    pdf: Annotated[UploadFile, File()],
    account: LaboratoryAccount,
) -> dict | JSONResponse:
    _require_local_request(request)
    try:
        with _database() as connection:
            return issue_certificate_on_sepolia(
                connection, participant_id=account.participant_id,
                snake_id=snake_id, title=title, pdf_content=pdf.file.read(MAX_PDF_BYTES + 1),
            )
    except Exception as error:
        return _write_error(error)


@router.post("/certificate-series/{series_id}/versions", status_code=201, response_model=CertificateRevisionResponse)
def create_sepolia_certificate_revision(
    request: Request,
    series_id: Annotated[str, Path(min_length=1)],
    pdf: Annotated[UploadFile, File()],
    account: LaboratoryAccount,
) -> dict | JSONResponse:
    _require_local_request(request)
    try:
        with _database() as connection:
            return revise_certificate_on_sepolia(
                connection, participant_id=account.participant_id,
                series_id=series_id, pdf_content=pdf.file.read(MAX_PDF_BYTES + 1),
            )
    except Exception as error:
        return _write_error(error)


@router.post("/certificate-transactions/recover", response_model=None)
def recover_sepolia_certificate_route(
    request: Request,
    body: CertificateRecoveryRequest,
    account: LaboratoryAccount,
) -> dict | JSONResponse:
    _require_local_request(request)
    try:
        with _database() as connection:
            return recover_sepolia_certificate_transaction(
                connection,
                participant_id=account.participant_id,
                transaction_hash=body.transaction_hash,
            )
    except Exception as error:
        return _write_error(error)


@router.post("/certificate-permission-demo", response_model=None)
def run_sepolia_certificate_permission_demo_route(
    request: Request,
    body: CertificatePermissionDemoRequest,
    account: LaboratoryAccount,
) -> dict:
    _require_local_request(request)
    if account.participant_id != "LAB002":
        raise HTTPException(403, "The permission demo is available in the LAB002 workspace only.")
    with _database() as connection:
        return run_sepolia_certificate_permission_demo(
            connection, operation=body.operation, snake_id=body.snake_id,
        )


@router.get("/laboratories/me/certificate-series", response_model=list[LaboratoryReportSummary])
def read_my_sepolia_laboratory_reports(request: Request, account: LaboratoryAccount) -> list[dict]:
    _require_local_request(request)
    with _database() as connection:
        return list_sepolia_laboratory_reports(connection, participant_id=account.participant_id)


@router.get("/snakes/{snake_id}/certificate-series")
def read_sepolia_certificate_history(
    request: Request, snake_id: Annotated[str, Path(min_length=1)],
    account: AuthenticatedAccount,
) -> dict:
    _require_local_request(request)
    with _database() as connection:
        rows = sepolia_certificate_history(connection, snake_id=snake_id)
    grouped: dict[str, dict] = {}
    for row in rows:
        series = grouped.setdefault(row["series_id"], {
            "series_id": row["series_id"], "title": row["title"],
            "laboratory_id": row["laboratory_id"], "laboratory_name": row["laboratory_id"],
            "versions": [],
        })
        series["versions"].append({
            "version_id": row["version_id"], "version_number": row["version_number"],
            "previous_version_id": row["previous_version_id"], "file_hash": row["file_hash"],
            "issuer_address": row["issuer_address"], "issued_at": row["issued_at"],
            "status": "current" if row["status"] == 1 else "superseded" if row["status"] == 2 else None,
            "evidence_status": "confirmed" if row["transaction_status"] == "confirmed" else "unconfirmed",
            "download_url": f"/api/v1/sepolia/certificate-versions/{row['version_id']}/file",
            "transaction_hash": row["transaction_hash"],
        })
    return {"snake_id": snake_id, "chain_block_number": None, "warnings": [], "series": list(grouped.values())}


@router.get("/certificate-versions/{version_id}/file", response_model=None)
def download_sepolia_certificate_pdf(
    request: Request, version_id: Annotated[str, Path(min_length=1)],
    account: AuthenticatedAccount,
) -> FileResponse:
    _require_local_request(request)
    with _database() as connection:
        reference = certificate_pdf_reference(connection, version_id=version_id)
    path = get_certificate_pdf_path(reference) if reference else None
    if path is None:
        raise HTTPException(404, "Sepolia certificate PDF not found.")
    return FileResponse(path, media_type="application/pdf", filename=f"{version_id}.pdf")


@router.post("/certificate-unauthorized-check")
def check_unauthorized_laboratory(request: Request, body: UnauthorizedCheckRequest, account: LaboratoryAccount) -> dict:
    _require_local_request(request)
    try:
        return {"detail": simulate_unauthorized_lab_call(snake_id=body.snake_id), "outcome": "rejected"}
    except SepoliaBusinessError as error:
        return JSONResponse(status_code=409, content={"detail": str(error), "outcome": "unexpected"})


@router.get("/snakes/{snake_id}/keeper", response_model=KeeperTransferStatusResponse)
def read_sepolia_keeper_status(
    request: Request, snake_id: Annotated[str, Path(min_length=1)],
    account: AuthenticatedAccount,
) -> dict:
    _require_local_request(request)
    try:
        with _database() as connection:
            state = sepolia_keeper_state(connection, snake_id=snake_id)
            parties = {"current": state["current_keeper_address"]}
            if state["pending"]:
                parties["from"] = state["from_keeper_address"]
                parties["to"] = state["recipient_address"]
            mapped = {}
            for label, address in parties.items():
                participant_id = next(
                    (pid for pid in ("BREEDER001", "BUYER001", "LAB001", "LAB002")
                     if get_sepolia_signer(pid).address.lower() == address.lower()),
                    None,
                )
                participant = connection.execute(
                    "SELECT display_name FROM public.participants WHERE participant_id=%s",
                    (participant_id,),
                ).fetchone() if participant_id else None
                username = connection.execute(
                    "SELECT username FROM public.user_accounts WHERE participant_id=%s",
                    (participant_id,),
                ).fetchone() if participant_id else None
                mapped[label] = {
                    "participant_id": participant_id,
                    "display_name": participant[0] if participant else None,
                    "username": username[0] if username else None,
                    "wallet_address": address,
                }
            transfer = state["transfer"]
            status = "unable_to_confirm" if state["pending"] and transfer is None else "pending_acceptance" if state["pending"] else (
                {"accepted": "accepted", "failed": "unable_to_confirm", "unknown": "unable_to_confirm", "prepared": "unable_to_confirm"}.get(
                    transfer["status"], "no_pending_transfer"
                ) if transfer else "no_pending_transfer"
            )
            transfer_id = transfer["transfer_id"] if transfer else None
            transaction_hash = state["transaction_hash"]
            return {
                "snake_id": snake_id, "current_keeper": mapped["current"],
                "transfer_status": status, "transfer_id": transfer_id,
                "from_participant": mapped.get("from"), "to_participant": mapped.get("to"),
                "initiated_at": transfer["initiated_at"] if transfer else None,
                "resolved_at": transfer["resolved_at"] if transfer else None,
                "transaction_hash": transaction_hash,
                "transaction_status": state["transaction_status"],
                "chain_block_number": state["block_number"],
                "detail": (
                    "A chain pending transfer has no matching Sepolia database record."
                    if state["pending"] and transfer is None else None
                ),
                "etherscan_url": (
                    f"https://sepolia.etherscan.io/tx/{transaction_hash}"
                    if transaction_hash else None
                ),
            }
    except LookupError as error:
        raise HTTPException(404, str(error)) from None
    except (SepoliaBusinessError, SepoliaRegistrationError) as error:
        raise HTTPException(503, str(error)) from None


@router.post("/snakes/{snake_id}/keeper-transfers", status_code=201, response_model=KeeperTransferInitiationResponse)
def create_sepolia_keeper_transfer(
    request: Request,
    snake_id: Annotated[str, Path(min_length=1)],
    body: KeeperTransferInitiationRequest,
    account: KeeperAccount,
) -> dict | JSONResponse:
    _require_local_request(request)
    try:
        with _database() as connection:
            return initiate_sepolia_keeper_transfer(
                connection, snake_id=snake_id, participant_id=account.participant_id,
                recipient_username=body.recipient_username,
            )
    except Exception as error:
        return _write_error(error)


@router.post("/keeper-transfers/{transfer_id}/accept", response_model=KeeperTransferResolutionResponse)
def accept_sepolia_keeper_transfer_route(
    request: Request, transfer_id: Annotated[str, Path(min_length=1)],
    account: KeeperAccount,
) -> dict | JSONResponse:
    _require_local_request(request)
    try:
        with _database() as connection:
            return accept_sepolia_keeper_transfer(
                connection, transfer_id=transfer_id, participant_id=account.participant_id,
            )
    except Exception as error:
        return _write_error(error)


class KeeperAcceptanceVerificationResponse(KeeperTransferResolutionResponse):
    historical_verified: Literal[True]
    database_synced: bool
    verified: bool
    latest_keeper_address: str
    latest_pending: bool
    chain_block_number: int
    detail: str | None


class KeeperAcceptanceReference(BaseModel):
    transfer_id: str | None = Field(default=None, min_length=1)
    transaction_hash: str | None = Field(default=None, pattern=r"^0x[0-9a-fA-F]{64}$")


@router.get("/keeper-acceptance", response_model=KeeperAcceptanceVerificationResponse)
def verify_sepolia_keeper_acceptance_route(
    request: Request, account: KeeperAccount,
    transfer_id: str | None = None, transaction_hash: str | None = None,
) -> dict | JSONResponse:
    _require_local_request(request)
    try:
        with _database() as connection:
            return verify_sepolia_keeper_acceptance(
                connection, participant_id=account.participant_id,
                transfer_id=transfer_id, transaction_hash=transaction_hash,
            )
    except Exception as error:
        return _write_error(error)


@router.post("/keeper-acceptance/recover", response_model=KeeperTransferResolutionResponse)
def recover_sepolia_keeper_acceptance_route(
    request: Request, body: KeeperAcceptanceReference, account: KeeperAccount,
) -> dict | JSONResponse:
    _require_local_request(request)
    try:
        with _database() as connection:
            return recover_sepolia_keeper_acceptance(
                connection, participant_id=account.participant_id,
                transfer_id=body.transfer_id, transaction_hash=body.transaction_hash,
            )
    except Exception as error:
        return _write_error(error)

