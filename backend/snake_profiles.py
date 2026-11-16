from datetime import date
from psycopg.rows import dict_row

import psycopg


# Purpose: store the snake's off-chain profile before chain confirmation.
# Workflow: demo step 1, profile persistence.
# Without this function, registration cannot retain the detailed profile.
# The caller owns the transaction and commits only when appropriate.
def save_snake_profile(
    connection: psycopg.Connection,
    *,
    snake_id: str,
    breeder_id: str,
    breeder_internal_id: str,
    species: str,
    sex: str,
    date_of_birth: date,
    genetic_description: str,
    photo_reference: str,
    nickname: str | None = None,
    introduction: str | None = None,
    sire_description: str | None = None,
    dam_description: str | None = None,
) -> str:
    connection.execute(
        """
        INSERT INTO snakes (
            snake_id,
            breeder_id,
            breeder_internal_id,
            species,
            sex,
            date_of_birth,
            genetic_description,
            photo_reference,
            nickname,
            introduction,
            sire_description,
            dam_description
        )
        VALUES (
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s
        )
        """,
        (
            snake_id,
            breeder_id,
            breeder_internal_id,
            species,
            sex,
            date_of_birth,
            genetic_description,
            photo_reference,
            nickname,
            introduction,
            sire_description,
            dam_description,
        ),
    )

    return snake_id

# Purpose: retrieve the stored profile independently of the page session.
# Workflow: demo step 1, viewing a previously registered snake.
# Without this query, the page can only show the latest submitted form.
def get_snake_profile(
    connection: psycopg.Connection,
    *,
    snake_id: str,
) -> dict[str, object] | None:
    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            """
            SELECT
                snakes.snake_id,
                snakes.breeder_id,
                breeder.display_name AS breeder_name,
                snakes.breeder_internal_id,
                snakes.nickname,
                snakes.species,
                snakes.sex,
                snakes.date_of_birth,
                snakes.introduction,
                snakes.genetic_description,
                snakes.sire_description,
                snakes.dam_description,
                snakes.photo_reference
            FROM snakes
            JOIN participants AS breeder
                ON breeder.participant_id = snakes.breeder_id
            WHERE snakes.snake_id = %s
            """,
            (snake_id,),
        )
        return cursor.fetchone()