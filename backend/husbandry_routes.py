import os
from collections.abc import Callable
from typing import Annotated, Any, Literal

import psycopg
from fastapi import APIRouter, HTTPException, Path, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, ValidationError

from backend.auth import AuthenticatedAccount, HusbandryAccount
from backend.husbandry import (
    add_husbandry_record,
    delete_husbandry_record,
    list_husbandry_records,
    update_husbandry_record,
)


router = APIRouter(prefix="/api/v1")

RecordType = Literal["growth", "shedding", "feeding", "health"]
RecordId = Annotated[int, Path(gt=0)]


class RecordWriteRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    data: dict[str, object]


# Purpose: provide a database connection and translate business errors to HTTP.
# Without this helper, each route would repeat connection and error handling.
def _execute(
    operation: Callable[..., Any],
    **arguments: Any,
) -> Any:
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
            return operation(connection, **arguments)

    except ValidationError as error:
        raise HTTPException(
            status_code=422,
            detail=error.errors(
                include_url=False,
                include_context=False,
                include_input=False,
            ),
        ) from None
    except PermissionError as error:
        raise HTTPException(
            status_code=403,
            detail=str(error),
        ) from None
    except LookupError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        ) from None
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail="Invalid husbandry record input.",
        ) from None
    except psycopg.IntegrityError:
        raise HTTPException(
            status_code=422,
            detail="The record does not satisfy database constraints.",
        ) from None
    except (psycopg.Error, OSError, RuntimeError):
        raise HTTPException(
            status_code=503,
            detail="The database or keeper lookup service is unavailable.",
        ) from None


# Purpose: expose retained husbandry history with original authorship.
# Without this route, the page cannot load the stored records.
@router.get("/snakes/{snake_id}/husbandry/{record_type}")
def read_records(
    snake_id: str,
    record_type: RecordType,
    account: AuthenticatedAccount,
) -> JSONResponse:
    records = _execute(
        list_husbandry_records,
        snake_id=snake_id,
        record_type=record_type,
    )

    return JSONResponse(content=jsonable_encoder(records))


# Purpose: create a record through the current-keeper permission check.
# Without this route, the page cannot add husbandry records.
@router.post(
    "/snakes/{snake_id}/husbandry/{record_type}",
    status_code=201,
)
def create_record(
    snake_id: str,
    record_type: RecordType,
    request: RecordWriteRequest,
    account: HusbandryAccount,
) -> JSONResponse:
    record = _execute(
        add_husbandry_record,
        snake_id=snake_id,
        record_type=record_type,
        participant_id=account.participant_id,
        data=request.data,
    )

    return JSONResponse(
        status_code=201,
        content=jsonable_encoder(record),
    )


# Purpose: edit a current keeper's own record without changing its author.
# Without this route, the page cannot correct permitted records.
@router.put("/snakes/{snake_id}/husbandry/{record_type}/{record_id}")
def edit_record(
    snake_id: str,
    record_type: RecordType,
    record_id: RecordId,
    request: RecordWriteRequest,
    account: HusbandryAccount,
) -> JSONResponse:
    record = _execute(
        update_husbandry_record,
        snake_id=snake_id,
        record_type=record_type,
        record_id=record_id,
        participant_id=account.participant_id,
        data=request.data,
    )

    return JSONResponse(content=jsonable_encoder(record))


# Purpose: delete only a current keeper's own husbandry row.
# Without this route, the page cannot remove permitted records.
@router.delete(
    "/snakes/{snake_id}/husbandry/{record_type}/{record_id}",
    status_code=204,
)
def remove_record(
    snake_id: str,
    record_type: RecordType,
    record_id: RecordId,
    account: HusbandryAccount,
) -> Response:
    _execute(
        delete_husbandry_record,
        snake_id=snake_id,
        record_type=record_type,
        record_id=record_id,
        participant_id=account.participant_id,
    )

    return Response(status_code=204)
