from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from database import get_session
from identity import get_current_breeder_id
from snake_registry.schemas import SnakeCreate, SnakeRead
from snake_registry.service import DuplicateSnakeId, find_snake, register_snake
from snake_registry.local_chain import get_local_chain
from snake_registry.registration import RegistrationProblem, registration_state, submit_registration
from snake_registry.schemas import RegistrationRead, RegistrationSubmit

router = APIRouter(prefix="/snakes", tags=["snakes"])
DatabaseSession = Annotated[Session, Depends(get_session)]
CurrentBreeder = Annotated[str, Depends(get_current_breeder_id)]


def require_snake(session: Session, snake_id: str):
    snake = find_snake(session, snake_id)
    if snake is None:
        raise HTTPException(status_code=404, detail="Snake not found")
    return snake


# Must precede the existing path-capturing profile route.
@router.post("/{snake_id:path}/registration", response_model=RegistrationRead)
def register_on_chain(snake_id: str, data: RegistrationSubmit, session: DatabaseSession, breeder_id: CurrentBreeder):
    try:
        return submit_registration(session, require_snake(session, snake_id), breeder_id, get_local_chain)
    except RegistrationProblem as error:
        raise HTTPException(status_code=error.status_code, detail=error.detail) from None
    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database unavailable; query registration status before retrying") from None


@router.get("/{snake_id:path}/registration", response_model=RegistrationRead)
def get_registration(snake_id: str, session: DatabaseSession):
    try:
        return registration_state(session, require_snake(session, snake_id), get_local_chain)
    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database unavailable") from None


@router.post("", response_model=SnakeRead, status_code=201)
def create_snake(data: SnakeCreate, session: DatabaseSession, breeder_id: CurrentBreeder):
    try:
        return register_snake(session, data, breeder_id)
    except DuplicateSnakeId:
        raise HTTPException(status_code=409, detail="snake_id already exists") from None
    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database unavailable") from None


@router.get("/{snake_id:path}", response_model=SnakeRead)
def get_snake(snake_id: str, session: DatabaseSession):
    try:
        snake = require_snake(session, snake_id)
        state = registration_state(session, snake, get_local_chain)
        profile = SnakeRead.model_validate(snake)
        profile.registration_status = state.status
        # Preserve the shape of existing database-only profiles.
        if state.recorded_status is not None:
            profile.chain_registration = state
        return profile
    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database unavailable") from None
