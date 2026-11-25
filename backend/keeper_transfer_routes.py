import os
from collections.abc import Callable
from datetime import datetime
from typing import Annotated, Literal

import psycopg
from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field

from backend.auth import AuthenticatedAccount, KeeperAccount
from backend.keeper_transfer_requests import (
    KeeperTransferConflictError,
    KeeperTransferRequestError,
    initiate_keeper_transfer,
    resolve_keeper_transfer,
)
from backend.keeper_transfer_status import get_keeper_transfer_status


router = APIRouter(prefix="/api/v1")


class KeeperTransferInitiationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    recipient_username: str = Field(min_length=1, pattern=r"\S")


class KeeperTransferInitiationResponse(BaseModel):
    transfer_id: str
    snake_id: str
    from_participant_id: str
    to_participant_id: str
    recipient_username: str
    status: Literal["pending"]
    initiated_at: datetime
    resolved_at: None
    current_keeper_address: str
    transaction_hash: str
    receipt_status: Literal[1]


class KeeperTransferResolutionResponse(KeeperTransferInitiationResponse):
    status: Literal["accepted", "rejected", "cancelled"]
    resolved_at: datetime


class KeeperParticipantResponse(BaseModel):
    participant_id: str | None
    display_name: str | None
    username: str | None
    wallet_address: str


class KeeperTransferStatusResponse(BaseModel):
    snake_id: str
    current_keeper: KeeperParticipantResponse | None
    transfer_status: Literal[
        "no_pending_transfer", "pending_acceptance", "accepted",
        "rejected", "cancelled", "unable_to_confirm",
    ]
    transfer_id: str | None
    from_participant: KeeperParticipantResponse | None
    to_participant: KeeperParticipantResponse | None
    initiated_at: datetime | None
    resolved_at: datetime | None
    transaction_hash: str | None
    transaction_status: Literal["submitted", "confirmed", "failed"] | None
    chain_block_number: int | None
    detail: str | None


# Submit demo transfers using the authenticated participant and local test account.
def _execute_transfer_write(
    *,
    operation: Callable[..., dict],
    participant_id: str,
    arguments: dict,
) -> dict | JSONResponse:
    password = os.environ.get("DEMO_DB_PASSWORD")
    if not password:
        return JSONResponse(
            status_code=503,
            content={
                "detail": "Database configuration is unavailable.",
                "outcome": "not_submitted",
            },
        )

    result = None
    try:
        with psycopg.connect(
            host="127.0.0.1", port=5433, dbname="ballpython_demo",
            user="ballpython", password=password,
            connect_timeout=5, autocommit=True,
        ) as connection:
            result = operation(
                connection,
                participant_id=participant_id,
                **arguments,
            )
    except KeeperTransferRequestError as error:
        return JSONResponse(
            status_code=502 if error.outcome in {"failed", "unverified"} else 503,
            content={
                "detail": str(error), "outcome": error.outcome,
                "transfer_id": error.transfer_id,
                "transaction_hash": error.transaction_hash,
            },
        )
    except KeeperTransferConflictError as error:
        return JSONResponse(
            status_code=409,
            content={
                "detail": str(error), "outcome": "not_submitted",
                "transfer_id": error.transfer_id,
            },
        )
    except PermissionError as error:
        return JSONResponse(
            status_code=403,
            content={"detail": str(error), "outcome": "not_submitted"},
        )
    except LookupError as error:
        return JSONResponse(
            status_code=404,
            content={"detail": str(error), "outcome": "not_submitted"},
        )
    except ValueError as error:
        return JSONResponse(
            status_code=422,
            content={"detail": str(error), "outcome": "not_submitted"},
        )
    except (psycopg.Error, OSError, RuntimeError):
        return JSONResponse(
            status_code=503,
            content={
                "detail": (
                    "The transfer action was confirmed, but the response could not be "
                    "completed. Do not submit again."
                    if result is not None
                    else "The transfer service is unavailable. No transaction "
                    "was submitted. Confirm migration 007 and keeper configuration."
                ),
                "outcome": "storage_error" if result is not None else "not_submitted",
                "transfer_id": result["transfer_id"] if result is not None else None,
                "transaction_hash": (
                    result["transaction_hash"] if result is not None else None
                ),
            },
        )

    return result


# Purpose: receive the logged-in keeper's request for a registered buyer.
# Without this endpoint, the platform cannot start an offline sale's handover.
@router.post(
    "/snakes/{snake_id}/keeper-transfers",
    status_code=201,
    response_model=KeeperTransferInitiationResponse,
)
def create_keeper_transfer(
    snake_id: Annotated[str, Path(min_length=1)],
    request: KeeperTransferInitiationRequest,
    account: KeeperAccount,
) -> dict | JSONResponse:
    return _execute_transfer_write(
        operation=initiate_keeper_transfer,
        participant_id=account.participant_id,
        arguments={
            "snake_id": snake_id, "recipient_username": request.recipient_username,
        },
    )


# Purpose: let only the designated recipient complete the handover.
# Without this endpoint, a pending request cannot change the current keeper.
@router.post(
    "/keeper-transfers/{transfer_id}/accept",
    response_model=KeeperTransferResolutionResponse,
)
def accept_keeper_transfer(
    transfer_id: Annotated[str, Path(min_length=1)], account: KeeperAccount
) -> dict | JSONResponse:
    return _execute_transfer_write(
        operation=resolve_keeper_transfer,
        participant_id=account.participant_id,
        arguments={"transfer_id": transfer_id, "action": "accept"},
    )


# Purpose: let the designated recipient decline without changing keeper rights.
# Without this endpoint, the buyer cannot explicitly reject the proposal.
@router.post(
    "/keeper-transfers/{transfer_id}/reject",
    response_model=KeeperTransferResolutionResponse,
)
def reject_keeper_transfer(
    transfer_id: Annotated[str, Path(min_length=1)], account: KeeperAccount
) -> dict | JSONResponse:
    return _execute_transfer_write(
        operation=resolve_keeper_transfer,
        participant_id=account.participant_id,
        arguments={"transfer_id": transfer_id, "action": "reject"},
    )


# Purpose: let the initiating current keeper withdraw an unaccepted request.
# Without this endpoint, the breeder cannot cancel a pending proposal.
@router.post(
    "/keeper-transfers/{transfer_id}/cancel",
    response_model=KeeperTransferResolutionResponse,
)
def cancel_keeper_transfer(
    transfer_id: Annotated[str, Path(min_length=1)], account: KeeperAccount
) -> dict | JSONResponse:
    return _execute_transfer_write(
        operation=resolve_keeper_transfer,
        participant_id=account.participant_id,
        arguments={"transfer_id": transfer_id, "action": "cancel"},
    )


# Purpose: expose manager identity and confirmed transfer status to signed-in users.
# Without this route, the profile cannot explain who manages it after a handover.
@router.get(
    "/snakes/{snake_id}/keeper",
    response_model=KeeperTransferStatusResponse,
)
def read_keeper_transfer_status(
    snake_id: Annotated[str, Path(min_length=1)],
    account: AuthenticatedAccount,
) -> dict:
    password = os.environ.get("DEMO_DB_PASSWORD")
    if not password:
        raise HTTPException(503, "Database configuration is unavailable.")

    try:
        with psycopg.connect(
            host="127.0.0.1", port=5433, dbname="ballpython_demo",
            user="ballpython", password=password,
            connect_timeout=5, autocommit=True,
        ) as connection:
            return get_keeper_transfer_status(connection, snake_id=snake_id)
    except LookupError:
        raise HTTPException(404, "Snake profile not found.") from None
    except (psycopg.Error, OSError, RuntimeError):
        raise HTTPException(
            503, "The keeper status service is unavailable. Confirm migration 007."
        ) from None
