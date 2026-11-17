import hashlib
import hmac
import secrets
from typing import Annotated, Literal, Self

import psycopg
from psycopg.rows import dict_row
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    SecretStr,
    field_validator,
    model_validator,
)


NonBlankText = Annotated[str, Field(pattern=r"\S")]


class AccountRegistrationData(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    username: NonBlankText
    email: str = Field(
        pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    )
    password: SecretStr = Field(min_length=1, max_length=1024)

    role: Literal["buyer", "breeder", "lab"]
    laboratory_id: Literal["LAB001", "LAB002"] | None = None

    display_name: NonBlankText
    country_or_region: NonBlankText
    contact: str | None = None

    breeder_name: str | None = None
    breeder_region: str | None = None
    breeder_introduction: str | None = None

    demo_consent: Literal[True]

    @field_validator(
        "username",
        "email",
        "display_name",
        "country_or_region",
        "contact",
        "breeder_name",
        "breeder_region",
        "breeder_introduction",
        mode="before",
    )
    @classmethod
    def trim_profile_text(cls, value: object) -> object:
        if isinstance(value, str):
            return value.strip()
        return value

    @field_validator("password")
    @classmethod
    def require_nonblank_password(cls, value: SecretStr) -> SecretStr:
        if not value.get_secret_value().strip():
            raise ValueError("Password must not be blank.")
        return value

    @model_validator(mode="after")
    def validate_role_details(self) -> Self:
        if self.role == "lab" and self.laboratory_id is None:
            raise ValueError("Laboratory selection is required.")

        if self.role != "lab" and self.laboratory_id is not None:
            raise ValueError("Laboratory selection requires the lab role.")

        if self.role == "breeder" and not self.breeder_name:
            raise ValueError("Breeder name is required.")

        return self


class AccountConflictError(ValueError):
    """The username, email, or demo participant is already registered."""


class DemoParticipantUnavailableError(RuntimeError):
    """The selected demonstration participant has not been initialized."""


# Purpose: produce a salted password hash for account storage.
# Workflow: account registration before sign-in.
# Without this function, passwords would lack a safe storage representation.
def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)

    try:
        digest = hashlib.scrypt(
            password.encode("utf-8"),
            salt=salt,
            n=16384,
            r=8,
            p=5,
            maxmem=64 * 1024 * 1024,
            dklen=64,
        )
    except (ValueError, MemoryError):
        raise RuntimeError("Password hashing is unavailable.") from None

    return f"scrypt$16384$8$5${salt.hex()}${digest.hex()}"


# Purpose: verify a password against the existing salted scrypt format.
# Workflow: sign-in after account registration.
# Without this function, stored password hashes cannot validate credentials.
def verify_password(password: str, encoded_hash: str) -> bool:
    try:
        algorithm, n, r, p, salt_hex, digest_hex = encoded_hash.split("$")

        if (algorithm, n, r, p) != ("scrypt", "16384", "8", "5"):
            return False

        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(digest_hex)

        if len(salt) != 16 or len(expected) != 64:
            return False
    except ValueError:
        return False

    try:
        actual = hashlib.scrypt(
            password.encode("utf-8"),
            salt=salt,
            n=16384,
            r=8,
            p=5,
            maxmem=64 * 1024 * 1024,
            dklen=64,
        )
    except (ValueError, MemoryError):
        raise RuntimeError("Password verification is unavailable.") from None

    return hmac.compare_digest(actual, expected)


# Purpose: create an account bound to an existing demonstration participant.
# Workflow: registration before login and role-specific workspaces.
# Without this operation, the registration form cannot create an account.
# Account creation and display-name changes commit together.
def create_account(
    connection: psycopg.Connection,
    *,
    data: AccountRegistrationData,
) -> dict[str, object]:
    participant_id = (
        data.laboratory_id
        if data.role == "lab"
        else {
            "buyer": "BUYER001",
            "breeder": "BREEDER001",
        }[data.role]
    )

    password_hash = hash_password(data.password.get_secret_value())
    is_breeder = data.role == "breeder"

    try:
        with connection.transaction():
            participant = connection.execute(
                """
                SELECT participant_id
                FROM participants
                WHERE participant_id = %s
                FOR UPDATE
                """,
                (participant_id,),
            ).fetchone()

            if participant is None:
                raise DemoParticipantUnavailableError(
                    "The selected demo participant is not initialized."
                )

            with connection.cursor(row_factory=dict_row) as cursor:
                cursor.execute(
                    """
                    INSERT INTO user_accounts (
                        username,
                        email,
                        password_hash,
                        role,
                        participant_id,
                        country_or_region,
                        contact,
                        breeder_name,
                        breeder_region,
                        breeder_introduction
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING account_id, username, role, participant_id
                    """,
                    (
                        data.username,
                        data.email,
                        password_hash,
                        data.role,
                        participant_id,
                        data.country_or_region,
                        data.contact or None,
                        data.breeder_name if is_breeder else None,
                        (data.breeder_region or None)
                        if is_breeder else None,
                        (data.breeder_introduction or None)
                        if is_breeder else None,
                    ),
                )
                account = cursor.fetchone()

            connection.execute(
                """
                UPDATE participants
                SET display_name = %s
                WHERE participant_id = %s
                """,
                (data.display_name, participant_id),
            )

    except psycopg.errors.UniqueViolation as error:
        messages = {
            "user_accounts_username_unique": "Username is already registered.",
            "user_accounts_email_unique": "Email is already registered.",
            "user_accounts_participant_id_key": (
                "The selected demo participant already has an account."
            ),
        }
        raise AccountConflictError(
            messages.get(
                error.diag.constraint_name,
                "Account is already registered.",
            )
        ) from None

    return account
