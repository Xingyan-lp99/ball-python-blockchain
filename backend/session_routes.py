import os
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime
from typing import Annotated, Literal

import psycopg
from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    SecretStr,
    field_validator,
)

from backend.account_routes import AccountRoute
from backend.accounts import NonBlankText
from backend.sessions import (
    AuthenticationError,
    create_session,
    get_session_account,
    revoke_session,
)


router = APIRouter(
    prefix="/api/v1",
    route_class=AccountRoute,
)

bearer = HTTPBearer(auto_error=False)


class LoginRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    username: NonBlankText
    password: SecretStr = Field(min_length=1, max_length=1024)

    @field_validator("username", mode="before")
    @classmethod
    def trim_username(cls, value: object) -> object:
        return value.strip() if isinstance(value, str) else value


class CurrentAccountResponse(BaseModel):
    account_id: int
    username: str
    display_name: str
    role: Literal["buyer", "breeder", "lab"]
    participant_id: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: Literal["bearer"]
    expires_at: datetime
    account: CurrentAccountResponse


@contextmanager
def _database() -> Iterator[psycopg.Connection]:
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
            yield connection
    except AuthenticationError as error:
        raise HTTPException(
            status_code=401,
            detail=str(error),
            headers={"WWW-Authenticate": "Bearer"},
        ) from None
    except (psycopg.Error, RuntimeError, OSError):
        raise HTTPException(
            status_code=503,
            detail="The sign-in service is unavailable.",
        ) from None


def _session_token(
    credentials: Annotated[
        HTTPAuthorizationCredentials | None,
        Depends(bearer),
    ],
) -> str:
    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Sign-in is required.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return credentials.credentials


SessionToken = Annotated[str, Depends(_session_token)]


# Purpose: exchange valid credentials for a new session.
# Without this route, the frontend cannot sign in.
@router.post("/sessions", response_model=LoginResponse)
def sign_in(
    request: LoginRequest,
    response: Response,
) -> LoginResponse:
    with _database() as connection:
        session = create_session(
            connection,
            username=request.username,
            password=request.password.get_secret_value(),
        )

    response.headers["Cache-Control"] = "no-store"
    return LoginResponse(**session)


# Purpose: expose only the identity associated with the supplied session.
# Without this route, the frontend cannot confirm its signed-in identity.
@router.get(
    "/sessions/current",
    response_model=CurrentAccountResponse,
)
def read_current_account(
    token: SessionToken,
    response: Response,
) -> CurrentAccountResponse:
    with _database() as connection:
        account = get_session_account(connection, token=token)

    response.headers["Cache-Control"] = "no-store"
    return CurrentAccountResponse(**account)


# Purpose: invalidate the current backend session.
# Without this route, the frontend cannot complete sign-out.
@router.delete("/sessions/current", status_code=204)
def sign_out(token: SessionToken) -> Response:
    with _database() as connection:
        revoke_session(connection, token=token)

    return Response(
        status_code=204,
        headers={"Cache-Control": "no-store"},
    )
