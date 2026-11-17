import psycopg
from psycopg.rows import dict_row

from backend.keeper_transfers import get_keeper_state


# Purpose: translate an on-chain address into the existing public account identity.
# Without this lookup, the profile could only show a wallet rather than its manager.
def _participant_for_address(
    connection: psycopg.Connection, *, wallet_address: str
) -> dict:
    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            """
            SELECT participants.participant_id, participants.display_name,
                   accounts.username, participants.wallet_address
            FROM participants
            LEFT JOIN user_accounts AS accounts USING (participant_id)
            WHERE LOWER(participants.wallet_address) = LOWER(%s)
            """,
            (wallet_address,),
        )
        participant = cursor.fetchone()

    return participant if participant is not None else {
        "participant_id": None,
        "display_name": None,
        "username": None,
        "wallet_address": wallet_address,
    }


# Purpose: combine live keeper authority with the latest recorded transfer outcome.
# Without this query, a cleared pending flag cannot distinguish acceptance or refusal.
def get_keeper_transfer_status(
    connection: psycopg.Connection, *, snake_id: str
) -> dict:
    if connection.execute(
        "SELECT 1 FROM snakes WHERE snake_id = %s", (snake_id,)
    ).fetchone() is None:
        raise LookupError("Snake profile not found.")

    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(
            """
            SELECT transfer.transfer_id, transfer.status,
                   transfer.initiated_at, transfer.resolved_at,
                   sender.wallet_address AS from_address,
                   recipient.wallet_address AS recipient_address
            FROM keeper_transfers AS transfer
            JOIN participants AS sender
              ON sender.participant_id = transfer.from_participant_id
            JOIN participants AS recipient
              ON recipient.participant_id = transfer.to_participant_id
            WHERE transfer.snake_id = %s
            ORDER BY (transfer.status IS NULL) DESC,
                     (transfer.status = 'pending') DESC NULLS LAST,
                     COALESCE(transfer.resolved_at, transfer.initiated_at) DESC NULLS LAST,
                     transfer.transfer_id
            LIMIT 1
            """,
            (snake_id,),
        )
        transfer = cursor.fetchone()

        transaction = None
        if transfer is not None:
            cursor.execute(
                """
                SELECT transaction_hash, operation, status
                FROM blockchain_transactions
                WHERE transfer_id = %s
                ORDER BY transaction_id DESC
                LIMIT 1
                """,
                (transfer["transfer_id"],),
            )
            transaction = cursor.fetchone()

    result = {
        "snake_id": snake_id,
        "current_keeper": None,
        "transfer_status": "unable_to_confirm",
        "transfer_id": transfer["transfer_id"] if transfer is not None else None,
        "from_participant": None,
        "to_participant": None,
        "initiated_at": transfer["initiated_at"] if transfer is not None else None,
        "resolved_at": transfer["resolved_at"] if transfer is not None else None,
        "transaction_hash": (
            transaction["transaction_hash"] if transaction is not None else None
        ),
        "transaction_status": transaction["status"] if transaction is not None else None,
        "chain_block_number": None,
        "detail": None,
    }
    if transfer is not None:
        result["from_participant"] = _participant_for_address(
            connection, wallet_address=transfer["from_address"]
        )
        result["to_participant"] = _participant_for_address(
            connection, wallet_address=transfer["recipient_address"]
        )

    try:
        state = get_keeper_state(snake_id=snake_id)
    except (OSError, LookupError):
        result["detail"] = "Current keeper and transfer status could not be confirmed on-chain."
        return result

    result["chain_block_number"] = state["block_number"]
    result["current_keeper"] = _participant_for_address(
        connection, wallet_address=state["current_keeper_address"]
    )

    if state["pending"]:
        # These parties come from the chain, even if local request data is missing.
        result["from_participant"] = result["current_keeper"]
        result["to_participant"] = _participant_for_address(
            connection, wallet_address=state["recipient_address"]
        )

    if transfer is None:
        if state["pending"]:
            result["detail"] = (
                "A pending proposal exists on-chain without a matching local request."
            )
        else:
            result["transfer_status"] = "no_pending_transfer"
        return result

    if transaction is None:
        result["detail"] = "This local request has no recorded transaction result."
        return result
    if transaction["status"] == "submitted":
        result["detail"] = (
            "A transfer transaction is awaiting confirmation or result recording. "
            "Check its transaction hash before submitting another action."
        )
        return result

    if state["pending"]:
        if (
            transfer["status"] == "pending"
            and transfer["from_address"].lower() == state["from_keeper_address"].lower()
            and transfer["recipient_address"].lower() == state["recipient_address"].lower()
            and (
                (
                    transaction["status"] == "failed"
                    and transaction["operation"] in {
                        "accept_keeper_transfer", "reject_keeper_transfer",
                        "cancel_keeper_transfer",
                    }
                )
                or (
                    transaction["status"] == "confirmed"
                    and transaction["operation"] == "initiate_keeper_transfer"
                )
            )
        ):
            result["transfer_status"] = "pending_acceptance"
            if transaction["status"] == "failed":
                result["detail"] = "The last action failed; this proposal is still pending."
        else:
            result["detail"] = "The recorded request does not match the pending chain state."
        return result

    expected_operations = {
        "accepted": "accept_keeper_transfer",
        "rejected": "reject_keeper_transfer",
        "cancelled": "cancel_keeper_transfer",
    }
    status = transfer["status"]
    expected_keeper = (
        transfer["recipient_address"] if status == "accepted" else transfer["from_address"]
    )
    if (
        status in expected_operations
        and transaction["status"] == "confirmed"
        and transaction["operation"] == expected_operations[status]
        and state["current_keeper_address"].lower() == expected_keeper.lower()
    ):
        result["transfer_status"] = status
    else:
        result["detail"] = (
            "The recorded transfer outcome is not confirmed by the current chain state."
        )

    return result
