import psycopg

from backend.register_snake import (
    RegistrationTransactionError,
    register_snake,
)
from backend.snake_profiles import save_snake_profile


class UnknownParticipantError(ValueError):
    """The sending account has no configured participant."""


class SnakeProfileExistsError(ValueError):
    """The identifier already has a stored profile."""


def _record_transaction(
    connection: psycopg.Connection,
    transaction_hash: str,
    snake_id: str,
    status: str,
) -> None:
    connection.execute(
        """
        INSERT INTO blockchain_transactions (
            transaction_hash, operation, status, snake_id
        )
        VALUES (%s, 'register_snake', %s, %s)
        ON CONFLICT (transaction_hash)
        DO UPDATE SET status = EXCLUDED.status
        """,
        (transaction_hash, status, snake_id),
    )


# Purpose: coordinate off-chain profile storage and confirmed registration.
# Workflow: demo step 1, complete backend registration.
# Without this operation, chain registration and profile storage remain separate.
# The API supplies an autocommit connection; each transaction block commits
# one phase so later chain failures do not erase the stored profile.
def register_snake_profile(
    connection: psycopg.Connection,
    *,
    rpc_url: str,
    expected_chain_id: int,
    contract_address: str,
    sender_address: str,
    profile: dict[str, object],
) -> dict[str, str | int]:
    try:
        with connection.transaction():
            participant = connection.execute(
                """
                SELECT participant_id
                FROM participants
                WHERE LOWER(wallet_address) = LOWER(%s)
                """,
                (sender_address,),
            ).fetchone()

            if participant is None:
                raise UnknownParticipantError(
                    "The sending account is not configured as a participant."
                )

            breeder_id = participant[0]
            profile_data = {**profile, "breeder_id": breeder_id}
            snake_id = save_snake_profile(connection, **profile_data)
    except psycopg.errors.UniqueViolation:
        raise SnakeProfileExistsError(
            "Snake identifier already has a stored profile."
        ) from None

    def remember_submission(transaction_hash: str) -> None:
        with connection.transaction():
            _record_transaction(
                connection,
                transaction_hash,
                snake_id,
                "submitted",
            )

    try:
        result = register_snake(
            rpc_url=rpc_url,
            expected_chain_id=expected_chain_id,
            contract_address=contract_address,
            snake_id=snake_id,
            sender_address=sender_address,
            on_submitted=remember_submission,
        )
    except RegistrationTransactionError as error:
        status = {
            "unknown": "submitted",
            "failed": "failed",
            "unverified": "confirmed",
        }[error.outcome]

        try:
            with connection.transaction():
                _record_transaction(
                    connection,
                    error.transaction_hash,
                    snake_id,
                    status,
                )
        except psycopg.Error:
            raise RegistrationTransactionError(
                "The transaction result could not be saved.",
                error.transaction_hash,
                "storage_error",
            ) from None

        raise

    try:
        with connection.transaction():
            connection.execute(
                """
                UPDATE snakes
                SET current_keeper_id = %s,
                    updated_at = CURRENT_TIMESTAMP
                WHERE snake_id = %s
                """,
                (breeder_id, snake_id),
            )
            _record_transaction(
                connection,
                result["transaction_hash"],
                snake_id,
                "confirmed",
            )
    except psycopg.Error:
        raise RegistrationTransactionError(
            "Chain registration succeeded, but database completion failed.",
            result["transaction_hash"],
            "storage_error",
        ) from None

    return result