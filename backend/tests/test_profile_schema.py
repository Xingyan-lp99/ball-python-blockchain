import os
from collections.abc import Iterator
from datetime import date
from pathlib import Path
from uuid import uuid4
from backend.snake_profiles import save_snake_profile, get_snake_profile

import psycopg
import pytest
from psycopg import sql

from unittest.mock import Mock

from backend import snake_registration as workflow
from backend.register_snake import RegistrationTransactionError


MIGRATIONS_DIRECTORY = (
    Path(__file__).resolve().parents[1] / "migrations"
)

MIGRATION_PATHS = [
    MIGRATIONS_DIRECTORY / "001_create_participants_and_snakes.sql",
    MIGRATIONS_DIRECTORY / "002_require_snake_sex.sql",
    MIGRATIONS_DIRECTORY / "003_create_blockchain_transactions.sql",
    MIGRATIONS_DIRECTORY / "009_remove_breeder_internal_id.sql",
]


@pytest.fixture
def connection() -> Iterator[psycopg.Connection]:
    with psycopg.connect(
        host="127.0.0.1",
        port=5433,
        dbname="ballpython_demo",
        user="ballpython",
        password=os.environ["DEMO_DB_PASSWORD"],
        connect_timeout=5,
    ) as database:
        try:
            schema = sql.Identifier(f"test_profiles_{uuid4().hex}")

            database.execute(
                sql.SQL("CREATE SCHEMA {}").format(schema)
            )
            database.execute(
                sql.SQL("SET LOCAL search_path TO {}").format(schema)
            )
            for migration_path in MIGRATION_PATHS:
                database.execute(
                    migration_path.read_text(encoding="utf-8")
                )
            database.execute(
                """
                INSERT INTO participants (
                    participant_id, display_name, wallet_address
                )
                VALUES (%s, %s, %s)
                """,
                (
                    "BREEDER001",
                    "Demo Breeder",
                    "0x" + "a" * 40,
                ),
            )

            yield database
        finally:
            database.rollback()


@pytest.fixture
def profile() -> dict[str, object]:
    return {
        "snake_id": "SNAKE001",
        "breeder_id": "BREEDER001",
        "species": "Python regius",
        "sex": "Female",
        "date_of_birth": date(2025, 6, 1),
        "genetic_description": "Fictional demonstration description",
        "photo_reference": "photos/snake001.jpg",
    }


def insert_profile(
    connection: psycopg.Connection,
    profile: dict[str, object],
) -> str:
    return save_snake_profile(connection, **profile)


def test_profile_is_stored_with_unconfirmed_keeper(
    connection: psycopg.Connection,
    profile: dict[str, object],
) -> None:
    assert insert_profile(connection, profile) == "SNAKE001"

    row = connection.execute(
        """
        SELECT snake_id, breeder_id, current_keeper_id, date_of_birth,
               photo_reference, created_at, updated_at, sex
        FROM snakes
        WHERE snake_id = %s
        """,
        ("SNAKE001",),
    ).fetchone()

    assert row[:5] == (
        "SNAKE001",
        "BREEDER001",
        None,
        date(2025, 6, 1),
        "photos/snake001.jpg",
    )
    assert row[5] is not None
    assert row[6] is not None
    assert row[7] == "Female"
    assert "breeder_internal_id" not in get_snake_profile(connection, snake_id="SNAKE001")


@pytest.mark.parametrize(
    "field",
    [
        "species",
        "date_of_birth",
        "genetic_description",
        "photo_reference",
        "sex"
    ],
)
def test_required_fields_reject_null(
    connection: psycopg.Connection,
    profile: dict[str, object],
    field: str,
) -> None:
    profile[field] = None

    with pytest.raises(psycopg.errors.NotNullViolation):
        insert_profile(connection, profile)


@pytest.mark.parametrize(
    "field",
    [
        "species",
        "genetic_description",
        "photo_reference",
        "sex"
    ],
)
def test_required_text_rejects_whitespace(
    connection: psycopg.Connection,
    profile: dict[str, object],
    field: str,
) -> None:
    profile[field] = " \t\n"

    with pytest.raises(psycopg.errors.CheckViolation):
        insert_profile(connection, profile)


def test_wallet_address_is_unique_ignoring_case(
    connection: psycopg.Connection,
) -> None:
    with pytest.raises(psycopg.errors.UniqueViolation):
        connection.execute(
            """
            INSERT INTO participants (
                participant_id, display_name, wallet_address
            )
            VALUES (%s, %s, %s)
            """,
            ("OTHER001", "Other Participant", "0x" + "A" * 40),
        )


def test_duplicate_snake_identifier_is_rejected(
    connection: psycopg.Connection,
    profile: dict[str, object],
) -> None:
    insert_profile(connection, profile)

    with pytest.raises(psycopg.errors.UniqueViolation):
        insert_profile(connection, profile)


def test_unknown_breeder_is_rejected(
    connection: psycopg.Connection,
    profile: dict[str, object],
) -> None:
    profile["breeder_id"] = "UNKNOWN"

    with pytest.raises(psycopg.errors.ForeignKeyViolation):
        insert_profile(connection, profile)


def test_unknown_keeper_is_rejected(
    connection: psycopg.Connection,
    profile: dict[str, object],
) -> None:
    insert_profile(connection, profile)

    with pytest.raises(psycopg.errors.ForeignKeyViolation):
        connection.execute(
            """
            UPDATE snakes
            SET current_keeper_id = %s
            WHERE snake_id = %s
            """,
            ("UNKNOWN", "SNAKE001"),
        )


def test_snake_identifier_keeps_original_whitespace_rule(
    connection: psycopg.Connection,
    profile: dict[str, object],
) -> None:
    profile["snake_id"] = " "
    insert_profile(connection, profile)

    profile["snake_id"] = ""

    with pytest.raises(psycopg.errors.CheckViolation):
        insert_profile(connection, profile)
