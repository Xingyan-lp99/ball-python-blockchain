from datetime import date, datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Snake(Base):
    __tablename__ = "snakes"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    snake_id: Mapped[str] = mapped_column(Text, unique=True)
    name: Mapped[str | None] = mapped_column(Text)
    sex: Mapped[str] = mapped_column(Text)
    date_of_birth: Mapped[date | None]
    breeder_internal_id: Mapped[str | None] = mapped_column(Text)
    morph_description: Mapped[str | None] = mapped_column(Text)
    breeder_id: Mapped[str] = mapped_column(Text)
    current_manager_id: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
