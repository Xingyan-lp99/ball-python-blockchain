from datetime import date
from decimal import Decimal
from typing import Annotated

import psycopg
from psycopg import sql
from psycopg.rows import dict_row
from pydantic import BaseModel, ConfigDict, Field

from backend.keeper_transfers import get_keeper_state


NonBlankText = Annotated[str, Field(strict=True, pattern=r"\S")]


class RecordData(BaseModel):
    model_config = ConfigDict(extra="forbid")

    record_date: date


class GrowthData(RecordData):
    weight_g: Decimal
    length_cm: Decimal | None = None
    notes: str | None = None


class SheddingData(RecordData):
    outcome: NonBlankText
    follow_up: str | None = None


class FeedingData(RecordData):
    food: NonBlankText
    feeding_outcome: NonBlankText
    notes: str | None = None


class HealthData(RecordData):
    event: NonBlankText
    follow_up: str | None = None
    status: NonBlankText


RECORD_DEFINITIONS: dict[str, tuple[str, type[RecordData]]] = {
    "growth": ("growth_records", GrowthData),
    "shedding": ("shedding_records", SheddingData),
    "feeding": ("feeding_records", FeedingData),
    "health": ("health_records", HealthData),
}


def _definition(record_type: str) -> tuple[str, type[RecordData]]:
    if record_type not in RECORD_DEFINITIONS:
        raise ValueError("Unknown husbandry record type.")

    return RECORD_DEFINITIONS[record_type]


def _require_existing_snake(
    connection: psycopg.Connection,
    snake_id: str,
) -> None:
    snake = connection.execute(
        "SELECT 1 FROM snakes WHERE snake_id = %s",
        (snake_id,),
    ).fetchone()

    if snake is None:
        raise LookupError("Snake profile not found.")


# Purpose: authorize writes using the acting participant and live keeper state.
# Without this check, a former keeper could continue writing after a transfer.
def _require_current_keeper(
    connection: psycopg.Connection,
    *,
    snake_id: str,
    participant_id: str,
) -> None:
    _require_existing_snake(connection, snake_id)

    participant = connection.execute(
        """
        SELECT wallet_address
        FROM participants
        WHERE participant_id = %s
        """,
        (participant_id,),
    ).fetchone()

    if participant is None:
        raise LookupError("Participant not found.")

    keeper = get_keeper_state(snake_id=snake_id)["current_keeper_address"]

    if participant[0].lower() != keeper.lower():
        raise PermissionError("Only the current keeper may write records.")


# Purpose: require both current keeper status and original authorship.
# Without this check, a new keeper could change a predecessor's records.
def _require_owned_record(
    connection: psycopg.Connection,
    *,
    table: str,
    snake_id: str,
    record_id: int,
    participant_id: str,
) -> None:
    record = connection.execute(
        sql.SQL(
            """
            SELECT created_by
            FROM {}
            WHERE snake_id = %s AND record_id = %s
            FOR UPDATE
            """
        ).format(sql.Identifier(table)),
        (snake_id, record_id),
    ).fetchone()

    if record is None:
        raise LookupError("Husbandry record not found.")

    _require_current_keeper(
        connection,
        snake_id=snake_id,
        participant_id=participant_id,
    )

    if record[0] != participant_id:
        raise PermissionError("Only the original author may change this record.")


# Purpose: retrieve retained records with their original author names.
# Workflow: view husbandry history before and after keeper transfer.
# Without this operation, the page cannot display the stored history.
def list_husbandry_records(
    connection: psycopg.Connection,
    *,
    snake_id: str,
    record_type: str,
) -> list[dict[str, object]]:
    table, _ = _definition(record_type)
    _require_existing_snake(connection, snake_id)

    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            sql.SQL(
                """
                SELECT records.*, author.display_name AS author_name
                FROM {} AS records
                JOIN participants AS author
                    ON author.participant_id = records.created_by
                WHERE records.snake_id = %s
                ORDER BY records.record_date, records.record_id
                """
            ).format(sql.Identifier(table)),
            (snake_id,),
        )
        return cursor.fetchall()


# Purpose: create an off-chain record authored by the acting current keeper.
# Without this operation, keepers cannot add their own husbandry observations.
def add_husbandry_record(
    connection: psycopg.Connection,
    *,
    snake_id: str,
    record_type: str,
    participant_id: str,
    data: dict[str, object],
) -> dict[str, object]:
    table, model = _definition(record_type)
    values = model.model_validate(data).model_dump()

    columns = ["snake_id", "created_by", *values.keys()]
    parameters = [snake_id, participant_id, *values.values()]

    with connection.transaction():
        _require_current_keeper(
            connection,
            snake_id=snake_id,
            participant_id=participant_id,
        )

        with connection.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                sql.SQL(
                    "INSERT INTO {} ({}) VALUES ({}) RETURNING *"
                ).format(
                    sql.Identifier(table),
                    sql.SQL(", ").join(
                        sql.Identifier(column) for column in columns
                    ),
                    sql.SQL(", ").join(
                        sql.Placeholder() for _ in columns
                    ),
                ),
                parameters,
            )
            return cursor.fetchone()


# Purpose: replace editable content while retaining snake and author identity.
# Without this operation, current keepers cannot correct their own records.
def update_husbandry_record(
    connection: psycopg.Connection,
    *,
    snake_id: str,
    record_type: str,
    record_id: int,
    participant_id: str,
    data: dict[str, object],
) -> dict[str, object]:
    table, model = _definition(record_type)
    values = model.model_validate(data).model_dump()

    assignments = sql.SQL(", ").join(
        sql.SQL("{} = %s").format(sql.Identifier(field))
        for field in values
    )

    with connection.transaction():
        _require_owned_record(
            connection,
            table=table,
            snake_id=snake_id,
            record_id=record_id,
            participant_id=participant_id,
        )

        with connection.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                sql.SQL(
                    """
                    UPDATE {}
                    SET {}, updated_at = CURRENT_TIMESTAMP
                    WHERE snake_id = %s AND record_id = %s
                    RETURNING *
                    """
                ).format(
                    sql.Identifier(table),
                    assignments,
                ),
                [*values.values(), snake_id, record_id],
            )
            return cursor.fetchone()


# Purpose: remove only the acting current keeper's own husbandry row.
# Without this operation, keepers cannot delete their own unwanted entries.
# This does not delete snake profiles, certificate files, or project files.
def delete_husbandry_record(
    connection: psycopg.Connection,
    *,
    snake_id: str,
    record_type: str,
    record_id: int,
    participant_id: str,
) -> int:
    table, _ = _definition(record_type)

    with connection.transaction():
        _require_owned_record(
            connection,
            table=table,
            snake_id=snake_id,
            record_id=record_id,
            participant_id=participant_id,
        )

        row = connection.execute(
            sql.SQL(
                """
                DELETE FROM {}
                WHERE snake_id = %s AND record_id = %s
                RETURNING record_id
                """
            ).format(sql.Identifier(table)),
            (snake_id, record_id),
        ).fetchone()

        return row[0]
