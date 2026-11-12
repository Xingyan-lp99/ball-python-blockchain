from datetime import date, datetime, timezone
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, field_validator


class Sex(StrEnum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"


class SnakeCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    snake_id: str
    name: str | None = None
    sex: Sex
    date_of_birth: date | None = None
    breeder_internal_id: str | None = None
    morph_description: str | None = None

    @field_validator("snake_id")
    @classmethod
    def validate_snake_id(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("snake_id must not be blank")
        return value

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, value: date | None) -> date | None:
        if value is not None and value > datetime.now(timezone.utc).date():
            raise ValueError("date_of_birth must not be in the future (UTC)")
        return value


class RegistrationSubmit(BaseModel):
    model_config = ConfigDict(extra="forbid")


class RegistrationRead(BaseModel):
    status: Literal["not_submitted", "processing", "confirmed", "failed"]
    chain_check: Literal["not_checked", "verified", "unavailable", "stale", "conflict"]
    recorded_status: str | None = None
    error: str | None = None
    transaction_hash: str | None = None
    chain_id: int | None = None
    contract_address: str | None = None
    manager_address: str | None = None
    block_number: int | None = None
    block_hash: str | None = None
    instance_id: str | None = None


class SnakeRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    snake_id: str
    name: str | None
    sex: Sex
    date_of_birth: date | None
    breeder_internal_id: str | None
    morph_description: str | None
    breeder_id: str
    current_manager_id: str
    created_at: datetime
    registration_status: Literal["not_submitted", "processing", "confirmed", "failed"] = "not_submitted"
    chain_registration: RegistrationRead | None = None
    certificate_status: Literal["not_verified"] = "not_verified"
