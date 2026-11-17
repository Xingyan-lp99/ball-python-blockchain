import base64
import os
from datetime import date
from typing import Annotated, Literal

import psycopg
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, ConfigDict, Field, ValidationError
from requests.exceptions import RequestException
from web3 import Web3
from web3.exceptions import Web3Exception

from backend.auth import AuthenticatedAccount, BreederAccount
from backend.photos import (
    MAX_PHOTO_BYTES,
    get_snake_photo_path,
    save_snake_photo,
)
from backend.register_snake import (
    RegistrationTransactionError,
    SnakeAlreadyRegisteredError,
)
from backend.snake_registration import (
    SnakeProfileExistsError,
    UnknownParticipantError,
    register_snake_profile,
)

from urllib.parse import quote

from backend.snake_profiles import (
    get_random_snake_photo_references,
    get_random_snake_profiles,
    get_snake_profile,
)

router = APIRouter(prefix="/api/v1")

NonBlankText = Annotated[str, Field(strict=True, pattern=r"\S")]


class SnakeRegistrationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    snake_id: str = Field(min_length=1, strict=True)
    breeder_internal_id: NonBlankText
    species: NonBlankText
    sex: NonBlankText
    date_of_birth: date
    genetic_description: NonBlankText

    nickname: str | None = None
    introduction: str | None = None
    sire_description: str | None = None
    dam_description: str | None = None


class SnakeRegistrationResponse(BaseModel):
    transaction_hash: str
    receipt_status: Literal[1]
    snake_id: str
    initial_keeper: str


# Purpose: register a profile and uploaded photo using the signed-in breeder.
# Workflow: demo step 1, frontend-to-backend registration.
# Without this route, the registration form cannot save its profile and photo.
@router.post(
    "/snakes",
    status_code=201,
    response_model=SnakeRegistrationResponse,
)
def create_snake(
    profile_json: Annotated[str, Form()],
    photo: Annotated[UploadFile, File()],
    account: BreederAccount,
) -> SnakeRegistrationResponse | JSONResponse:
    try:
        request = SnakeRegistrationRequest.model_validate_json(profile_json)
    except ValidationError as error:
        return JSONResponse(
            status_code=422,
            content={
                "detail": error.errors(
                    include_url=False,
                    include_context=False,
                    include_input=False,
                )
            },
        )

    contract_address = os.environ.get("DEMO_REGISTRY_ADDRESS", "")
    password = os.environ.get("DEMO_DB_PASSWORD")

    if not Web3.is_address(contract_address) or not password:
        return JSONResponse(
            status_code=503,
            content={
                "detail": "Registration configuration is incomplete.",
                "outcome": "not_submitted",
                "transaction_hash": None,
            },
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
            breeder = connection.execute(
                """
                SELECT wallet_address
                FROM participants
                WHERE participant_id = %s
                """,
                (account.participant_id,),
            ).fetchone()

            if breeder is None:
                raise UnknownParticipantError("Demo breeder is not configured.")

            existing = connection.execute(
                "SELECT 1 FROM snakes WHERE snake_id = %s",
                (request.snake_id,),
            ).fetchone()

            if existing is not None:
                raise SnakeProfileExistsError("Profile already exists.")

            content = photo.file.read(MAX_PHOTO_BYTES + 1)

            try:
                photo_reference = save_snake_photo(content)
            except ValueError as error:
                return JSONResponse(
                    status_code=422,
                    content={"detail": str(error)},
                )

            profile = request.model_dump()
            profile["photo_reference"] = photo_reference

            result = register_snake_profile(
                connection,
                rpc_url="http://127.0.0.1:8545",
                expected_chain_id=31337,
                contract_address=contract_address,
                sender_address=breeder[0],
                profile=profile,
            )
    except UnknownParticipantError:
        return JSONResponse(
            status_code=422,
            content={"detail": "The demo breeder is not configured."},
        )
    except SnakeProfileExistsError:
        return JSONResponse(
            status_code=409,
            content={"detail": "Snake identifier already has a stored profile."},
        )
    except SnakeAlreadyRegisteredError:
        return JSONResponse(
            status_code=409,
            content={"detail": "Snake identifier is already registered."},
        )
    except RegistrationTransactionError as error:
        messages = {
            "failed": "Registration transaction failed.",
            "unknown": (
                "Registration outcome is unknown. "
                "Check the transaction before submitting again."
            ),
            "unverified": (
                "Transaction succeeded, but registration could not be verified. "
                "Do not submit again automatically."
            ),
            "storage_error": (
                "Blockchain and database results could not be fully recorded. "
                "Check the transaction before submitting again."
            ),
        }

        return JSONResponse(
            status_code=503
            if error.outcome in ("unknown", "storage_error")
            else 502,
            content={
                "detail": messages[error.outcome],
                "outcome": error.outcome,
                "transaction_hash": error.transaction_hash,
            },
        )
    except (
        psycopg.Error,
        OSError,
        ValueError,
        RuntimeError,
        RequestException,
        Web3Exception,
    ):
        return JSONResponse(
            status_code=503,
            content={
                "detail": (
                    "Registration is unavailable; no success was confirmed. "
                    "Do not submit again automatically."
                ),
                "outcome": "unknown",
                "transaction_hash": None,
            },
        )

    return SnakeRegistrationResponse(**result)

class SnakeProfileResponse(SnakeRegistrationRequest):
    breeder_id: str
    breeder_name: str
    photo_url: str


class SnakeShowcaseItem(BaseModel):
    snake_id: str
    nickname: str | None
    species: str
    photo_url: str


class SnakeShowcaseResponse(BaseModel):
    snakes: list[SnakeShowcaseItem]


class SnakeShowcaseImage(BaseModel):
    content_type: Literal["image/jpeg", "image/png"]
    content_base64: str


class SnakeShowcaseImagesResponse(BaseModel):
    images: list[SnakeShowcaseImage]


def _load_stored_profile(snake_id: str) -> dict[str, object] | None:
    password = os.environ.get("DEMO_DB_PASSWORD")

    if not password:
        raise RuntimeError("Database configuration is unavailable.")

    with psycopg.connect(
        host="127.0.0.1",
        port=5433,
        dbname="ballpython_demo",
        user="ballpython",
        password=password,
        connect_timeout=5,
    ) as connection:
        return get_snake_profile(connection, snake_id=snake_id)


def _load_random_stored_profiles() -> list[dict[str, object]]:
    password = os.environ.get("DEMO_DB_PASSWORD")

    if not password:
        raise RuntimeError("Database configuration is unavailable.")

    with psycopg.connect(
        host="127.0.0.1",
        port=5433,
        dbname="ballpython_demo",
        user="ballpython",
        password=password,
        connect_timeout=5,
    ) as connection:
        return get_random_snake_profiles(connection, limit=3)


def _load_random_photo_references() -> list[str]:
    password = os.environ.get("DEMO_DB_PASSWORD")

    if not password:
        raise RuntimeError("Database configuration is unavailable.")

    with psycopg.connect(
        host="127.0.0.1",
        port=5433,
        dbname="ballpython_demo",
        user="ballpython",
        password=password,
        connect_timeout=5,
    ) as connection:
        return get_random_snake_photo_references(connection)


@router.get(
    "/snakes/random-profiles",
    response_model=SnakeShowcaseResponse,
)
def read_random_snake_profiles(
    account: AuthenticatedAccount,
) -> SnakeShowcaseResponse | JSONResponse:
    try:
        profiles = _load_random_stored_profiles()
    except (psycopg.Error, OSError, RuntimeError):
        return JSONResponse(
            status_code=503,
            content={"detail": "The profile service is unavailable."},
        )

    return SnakeShowcaseResponse(
        snakes=[
            SnakeShowcaseItem(
                snake_id=profile["snake_id"],
                nickname=profile["nickname"],
                species=profile["species"],
                photo_url=(
                    f"/api/v1/snakes/{quote(profile['snake_id'], safe='')}/photo"
                ),
            )
            for profile in profiles
        ]
    )


@router.get(
    "/snakes/showcase-images",
    response_model=SnakeShowcaseImagesResponse,
)
def read_public_snake_showcase_images() -> SnakeShowcaseImagesResponse | JSONResponse:
    try:
        photo_references = _load_random_photo_references()
        images = []
        for reference in photo_references:
            photo_path = get_snake_photo_path(reference)
            if photo_path is None:
                continue
            try:
                if photo_path.stat().st_size > MAX_PHOTO_BYTES:
                    continue
                photo_content = photo_path.read_bytes()
            except FileNotFoundError:
                continue
            content_type = (
                "image/png"
                if photo_path.suffix.lower() == ".png"
                else "image/jpeg"
            )
            images.append(
                SnakeShowcaseImage(
                    content_type=content_type,
                    content_base64=base64.b64encode(photo_content).decode("ascii"),
                )
            )
            if len(images) == 3:
                break
    except (OSError, psycopg.Error, RuntimeError, ValueError):
        return JSONResponse(
            status_code=503,
            content={"detail": "The profile photo service is unavailable."},
        )

    return SnakeShowcaseImagesResponse(images=images)


# Purpose: expose saved profile fields without exposing local file references.
# Workflow: demo step 1, loading the profile through HTTP.
# Without this route, Streamlit cannot retrieve the stored profile.
@router.get(
    "/snakes/{snake_id}",
    response_model=SnakeProfileResponse,
)
def read_snake_profile(
    snake_id: str,
    account: AuthenticatedAccount,
) -> SnakeProfileResponse | JSONResponse:
    try:
        profile = _load_stored_profile(snake_id)
    except (psycopg.Error, OSError, RuntimeError):
        return JSONResponse(
            status_code=503,
            content={"detail": "The profile service is unavailable."},
        )

    if profile is None:
        return JSONResponse(
            status_code=404,
            content={"detail": "Snake profile not found."},
        )

    profile.pop("photo_reference")

    return SnakeProfileResponse(
        **profile,
        photo_url=f"/api/v1/snakes/{quote(snake_id, safe='')}/photo",
    )


# Purpose: serve the saved photo without exposing its filesystem path.
# Workflow: demo step 1, displaying the persisted profile photo.
# Without this route, the page cannot load the photo through the backend.
@router.get(
    "/snakes/{snake_id}/photo",
    response_model=None,
)
def read_snake_photo(
    snake_id: str,
    account: AuthenticatedAccount,
) -> FileResponse | JSONResponse:
    try:
        profile = _load_stored_profile(snake_id)

        if profile is None:
            return JSONResponse(
                status_code=404,
                content={"detail": "Snake profile not found."},
            )

        photo_path = get_snake_photo_path(profile["photo_reference"])
    except (psycopg.Error, OSError, RuntimeError, ValueError):
        return JSONResponse(
            status_code=503,
            content={"detail": "The photo service is unavailable."},
        )

    if photo_path is None:
        return JSONResponse(
            status_code=404,
            content={"detail": "Photo not found."},
        )

    media_type = (
        "image/png"
        if photo_path.suffix.lower() == ".png"
        else "image/jpeg"
    )

    return FileResponse(photo_path, media_type=media_type)
