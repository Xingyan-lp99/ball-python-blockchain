from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from snake_registry.models import Snake
from snake_registry.schemas import SnakeCreate


class DuplicateSnakeId(Exception):
    pass


def register_snake(session: Session, data: SnakeCreate, breeder_id: str) -> Snake:
    snake = Snake(
        **data.model_dump(),
        breeder_id=breeder_id,
        current_manager_id=breeder_id,
    )
    session.add(snake)
    try:
        session.commit()
    except IntegrityError as error:
        session.rollback()
        # Let PostgreSQL arbitrate duplicates, including concurrent requests.
        if (
            getattr(error.orig, "sqlstate", None) == "23505"
            and error.orig.diag.constraint_name == "uq_snakes_snake_id"
        ):
            raise DuplicateSnakeId from error
        raise
    session.refresh(snake)
    return snake


def find_snake(session: Session, snake_id: str) -> Snake | None:
    return session.scalar(select(Snake).where(Snake.snake_id == snake_id.strip()))
