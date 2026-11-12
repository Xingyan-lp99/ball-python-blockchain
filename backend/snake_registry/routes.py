from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from database import get_session
from identity import get_current_breeder_id
from snake_registry.schemas import SnakeCreate, SnakeRead
from snake_registry.service import DuplicateSnakeId, find_snake, register_snake

router = APIRouter(prefix="/snakes", tags=["snakes"])
DatabaseSession = Annotated[Session, Depends(get_session)]
CurrentBreeder = Annotated[str, Depends(get_current_breeder_id)]


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
        snake = find_snake(session, snake_id)
    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database unavailable") from None
    if snake is None:
        raise HTTPException(status_code=404, detail="Snake not found")
    return snake
