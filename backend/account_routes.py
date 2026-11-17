import os
from collections.abc import Callable, Coroutine
from typing import Any, Literal

import psycopg
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from pydantic import BaseModel

from backend.accounts import (
    AccountConflictError,
    AccountRegistrationData,
    DemoParticipantUnavailableError,
    create_account,
)


class AccountRoute(APIRoute):
    def get_route_handler(
        self,
    ) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        original_handler = super().get_route_handler()

        async def safe_handler(request: Request) -> Response:
            try:
                return await original_handler(request)
            except RequestValidationError:
                return JSONResponse(
                    status_code=422,
                    content={
                        "detail": "Please check the required account fields."
                    },
                )

        return safe_handler


router = APIRouter(
    prefix="/api/v1",
    route_class=AccountRoute,
)


class AccountRegistrationResponse(BaseModel):
    account_id: int
    username: str
    role: Literal["buyer", "breeder", "lab"]
    participant_id: str


# Purpose: expose account creation without returning credentials.
# Workflow: registration before login.
# Without this route, the frontend cannot save a registration.
@router.post(
    "/accounts",
    status_code=201,
    response_model=AccountRegistrationResponse,
)
def register_account(
    request: AccountRegistrationData,
) -> AccountRegistrationResponse:
    password = os.environ.get("DEMO_DB_PASSWORD")

    if not password:
        raise HTTPException(
            status_code=503,
            detail="Database configuration is unavailable.",
        )

    try:
        with psycopg.connect(
            host="127.0.0.1",
            port=5433,
            dbname="ballpython_demo",
            user="ballpython",
            password=password,
            connect_timeout=5,
            autocommit=True,
        ) as connection:
            account = create_account(connection, data=request)

    except AccountConflictError as error:
        raise HTTPException(
            status_code=409,
            detail=str(error),
        ) from None
    except DemoParticipantUnavailableError as error:
        raise HTTPException(
            status_code=503,
            detail=str(error),
        ) from None
    except (psycopg.Error, RuntimeError, OSError):
        raise HTTPException(
            status_code=503,
            detail="Account registration is unavailable.",
        ) from None

    return AccountRegistrationResponse(**account)
