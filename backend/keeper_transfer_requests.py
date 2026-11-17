from uuid import uuid4

import psycopg
from psycopg.rows import dict_row

from backend.keeper_transfers import (
    KeeperTransferTransactionError,
    TransferAction,
    get_keeper_state,
    initiate_keeper_transfer_on_chain,
    resolve_keeper_transfer_on_chain,
)


class KeeperTransferConflictError(RuntimeError):
    """Identify an existing request that must be resolved before another one."""

    def __init__(self, message: str, *, transfer_id: str | None = None) -> None:
        super().__init__(message)
        self.transfer_id = transfer_id


class KeeperTransferRequestError(RuntimeError):
    """Retain request and transaction identities after an incomplete write."""

    def __init__(
        self, message: str, *, transfer_id: str,
        transaction_hash: str | None, outcome: str,
    ) -> None:
        super().__init__(message)
        self.transfer_id = transfer_id
        self.transaction_hash = transaction_hash
        self.outcome = outcome


# Purpose: link submitted and confirmed transactions to their transfer request.
# Without this link, the application cannot explain an uncertain submission.
def _record_transfer_transaction(
    connection: psycopg.Connection,
    *,
    transfer_id: str,
    snake_id: str,
    transaction_hash: str,
    status: str,
    operation: str = "initiate_keeper_transfer",
) -> None:
    connection.execute(
        """
        INSERT INTO blockchain_transactions (
            transaction_hash, operation, status, snake_id, transfer_id
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (transaction_hash) DO UPDATE SET status = EXCLUDED.status
        """,
        (transaction_hash, operation, status, snake_id, transfer_id),
    )


# Purpose: turn the signed-in keeper's request into a confirmed pending proposal.
# Without this service, buyer lookup, SQL records, and chain submission are separate.
def initiate_keeper_transfer(
    connection: psycopg.Connection,
    *,
    snake_id: str,
    participant_id: str,
    recipient_username: str,
) -> dict:
    if connection.execute(
        "SELECT 1 FROM snakes WHERE snake_id = %s", (snake_id,)
    ).fetchone() is None:
        raise LookupError("Snake profile not found.")

    sender = connection.execute(
        "SELECT wallet_address FROM participants WHERE participant_id = %s",
        (participant_id,),
    ).fetchone()
    if sender is None:
        raise LookupError("The signed-in participant is not configured.")

    recipient = connection.execute(
        """
        SELECT accounts.participant_id, accounts.username, participants.wallet_address
        FROM user_accounts AS accounts
        JOIN participants USING (participant_id)
        WHERE LOWER(accounts.username) = LOWER(%s) AND accounts.role = 'buyer'
        """,
        (recipient_username.strip(),),
    ).fetchone()
    if recipient is None:
        raise LookupError("Registered buyer account not found.")

    recipient_id, recipient_name, recipient_address = recipient
    sender_address = sender[0]
    if recipient_id == participant_id or recipient_address.lower() == sender_address.lower():
        raise ValueError("The recipient must be different from the current keeper.")

    state = get_keeper_state(snake_id=snake_id)
    if state["current_keeper_address"].lower() != sender_address.lower():
        raise PermissionError("Only the current keeper may initiate a transfer.")
    if state["pending"]:
        raise KeeperTransferConflictError("This snake already has a pending transfer.")

    unresolved = connection.execute(
        """
        SELECT transfer_id FROM keeper_transfers
        WHERE snake_id = %s AND (status IS NULL OR status = 'pending')
        LIMIT 1
        """,
        (snake_id,),
    ).fetchone()
    if unresolved is not None:
        raise KeeperTransferConflictError(
            "An unresolved local request already exists. "
            "Check its transaction before submitting another request.",
            transfer_id=unresolved[0],
        )

    transfer_id = f"TRANSFER-{uuid4().hex}"
    with connection.transaction():
        connection.execute(
            """
            INSERT INTO keeper_transfers (
                transfer_id, snake_id, from_participant_id, to_participant_id
            )
            VALUES (%s, %s, %s, %s)
            """,
            (transfer_id, snake_id, participant_id, recipient_id),
        )

    def remember_submission(transaction_hash: str) -> None:
        with connection.transaction():
            _record_transfer_transaction(
                connection, transfer_id=transfer_id, snake_id=snake_id,
                transaction_hash=transaction_hash, status="submitted",
            )

    try:
        result = initiate_keeper_transfer_on_chain(
            snake_id=snake_id,
            sender_address=sender_address,
            recipient_address=recipient_address,
            on_submitted=remember_submission,
        )
    except KeeperTransferTransactionError as error:
        outcome = error.outcome
        if error.transaction_hash is not None:
            transaction_status = {
                "failed": "failed", "unverified": "confirmed",
            }.get(outcome, "submitted")
            try:
                with connection.transaction():
                    _record_transfer_transaction(
                        connection, transfer_id=transfer_id, snake_id=snake_id,
                        transaction_hash=error.transaction_hash,
                        status=transaction_status,
                    )
            except psycopg.Error:
                outcome = "storage_error"
        raise KeeperTransferRequestError(
            str(error), transfer_id=transfer_id,
            transaction_hash=error.transaction_hash, outcome=outcome,
        ) from None

    try:
        with connection.transaction():
            updated = connection.execute(
                """
                UPDATE keeper_transfers SET status = 'pending', initiated_at = %s
                WHERE transfer_id = %s AND status IS NULL
                """,
                (result["initiated_at"], transfer_id),
            )
            if updated.rowcount != 1:
                raise RuntimeError("The local transfer state changed.")
            _record_transfer_transaction(
                connection, transfer_id=transfer_id, snake_id=snake_id,
                transaction_hash=result["transaction_hash"], status="confirmed",
            )
    except (psycopg.Error, RuntimeError):
        raise KeeperTransferRequestError(
            "Initiation was confirmed on-chain, but its database result could "
            "not be fully saved. Do not submit again.",
            transfer_id=transfer_id,
            transaction_hash=result["transaction_hash"], outcome="storage_error",
        ) from None

    return {
        **result,
        "transfer_id": transfer_id,
        "snake_id": snake_id,
        "from_participant_id": participant_id,
        "to_participant_id": recipient_id,
        "recipient_username": recipient_name,
        "status": "pending",
        "resolved_at": None,
    }


# Purpose: resolve the existing request and update the keeper cache on acceptance.
# Without this service, pending proposals cannot complete or retain their outcome.
def resolve_keeper_transfer(
    connection: psycopg.Connection,
    *,
    transfer_id: str,
    participant_id: str,
    action: TransferAction,
) -> dict:
    statuses = {"accept": "accepted", "reject": "rejected", "cancel": "cancelled"}
    if action not in statuses:
        raise ValueError("Unsupported transfer action.")

    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            """
            SELECT transfer.snake_id, transfer.from_participant_id,
                   transfer.to_participant_id, transfer.status, transfer.initiated_at,
                   sender.wallet_address AS from_address,
                   recipient.wallet_address AS recipient_address,
                   recipient_account.username AS recipient_username
            FROM keeper_transfers AS transfer
            JOIN participants AS sender
              ON sender.participant_id = transfer.from_participant_id
            JOIN participants AS recipient
              ON recipient.participant_id = transfer.to_participant_id
            JOIN user_accounts AS recipient_account
              ON recipient_account.participant_id = transfer.to_participant_id
            WHERE transfer.transfer_id = %s
            """,
            (transfer_id,),
        )
        transfer = cursor.fetchone()

    if transfer is None:
        raise LookupError("Transfer request not found.")

    expected_actor = (
        transfer["from_participant_id"] if action == "cancel"
        else transfer["to_participant_id"]
    )
    if participant_id != expected_actor:
        raise PermissionError(
            "Only the initiating current keeper may cancel this request."
            if action == "cancel"
            else "Only the designated recipient may accept or reject this request."
        )
    if transfer["status"] != "pending":
        raise KeeperTransferConflictError(
            "This request is not a confirmed pending transfer.", transfer_id=transfer_id
        )

    unresolved = connection.execute(
        """
        SELECT 1 FROM blockchain_transactions
        WHERE transfer_id = %s
          AND operation IN (
              'accept_keeper_transfer', 'reject_keeper_transfer', 'cancel_keeper_transfer'
          )
          AND status IN ('submitted', 'confirmed')
        LIMIT 1
        """,
        (transfer_id,),
    ).fetchone()
    if unresolved is not None:
        raise KeeperTransferConflictError(
            "A resolution transaction already exists. Check its result before retrying.",
            transfer_id=transfer_id,
        )

    snake_id = transfer["snake_id"]
    state = get_keeper_state(snake_id=snake_id)
    if not (
        state["pending"]
        and state["current_keeper_address"].lower() == transfer["from_address"].lower()
        and state["from_keeper_address"].lower() == transfer["from_address"].lower()
        and state["recipient_address"].lower() == transfer["recipient_address"].lower()
    ):
        raise KeeperTransferConflictError(
            "The local request does not match the chain's pending transfer. "
            "Check the existing transactions before continuing.",
            transfer_id=transfer_id,
        )

    operation = f"{action}_keeper_transfer"
    actor_address = (
        transfer["from_address"] if action == "cancel" else transfer["recipient_address"]
    )

    def remember_submission(transaction_hash: str) -> None:
        with connection.transaction():
            _record_transfer_transaction(
                connection, transfer_id=transfer_id, snake_id=snake_id,
                transaction_hash=transaction_hash, status="submitted", operation=operation,
            )

    try:
        result = resolve_keeper_transfer_on_chain(
            action=action,
            snake_id=snake_id,
            actor_address=actor_address,
            from_keeper_address=transfer["from_address"],
            recipient_address=transfer["recipient_address"],
            on_submitted=remember_submission,
        )
    except KeeperTransferTransactionError as error:
        outcome = error.outcome
        if error.transaction_hash is not None:
            transaction_status = {
                "failed": "failed", "unverified": "confirmed",
            }.get(outcome, "submitted")
            try:
                with connection.transaction():
                    _record_transfer_transaction(
                        connection, transfer_id=transfer_id, snake_id=snake_id,
                        transaction_hash=error.transaction_hash,
                        status=transaction_status, operation=operation,
                    )
            except psycopg.Error:
                outcome = "storage_error"
        raise KeeperTransferRequestError(
            str(error), transfer_id=transfer_id,
            transaction_hash=error.transaction_hash, outcome=outcome,
        ) from None

    try:
        with connection.transaction():
            updated = connection.execute(
                """
                UPDATE keeper_transfers SET status = %s, resolved_at = %s
                WHERE transfer_id = %s AND status = 'pending'
                """,
                (statuses[action], result["resolved_at"], transfer_id),
            )
            if updated.rowcount != 1:
                raise RuntimeError("The local transfer state changed.")

            if action == "accept":
                updated_snake = connection.execute(
                    """
                    UPDATE snakes
                    SET current_keeper_id = %s, updated_at = CURRENT_TIMESTAMP
                    WHERE snake_id = %s
                    """,
                    (transfer["to_participant_id"], snake_id),
                )
                if updated_snake.rowcount != 1:
                    raise RuntimeError("The snake profile could not be updated.")

            _record_transfer_transaction(
                connection, transfer_id=transfer_id, snake_id=snake_id,
                transaction_hash=result["transaction_hash"], status="confirmed",
                operation=operation,
            )
    except (psycopg.Error, RuntimeError):
        raise KeeperTransferRequestError(
            "The transfer action was confirmed on-chain, but its database result "
            "could not be fully saved. Do not submit again.",
            transfer_id=transfer_id,
            transaction_hash=result["transaction_hash"], outcome="storage_error",
        ) from None

    return {
        **result,
        "transfer_id": transfer_id,
        "snake_id": snake_id,
        "from_participant_id": transfer["from_participant_id"],
        "to_participant_id": transfer["to_participant_id"],
        "recipient_username": transfer["recipient_username"],
        "status": statuses[action],
        "initiated_at": transfer["initiated_at"],
    }
