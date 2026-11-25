import json
import os
from collections.abc import Callable
from datetime import datetime, timezone
from typing import Literal

from requests.exceptions import RequestException
from web3 import Web3
from web3.contract import Contract
from web3.contract.contract import ContractFunction
from web3.exceptions import ContractCustomError, ContractLogicError, Web3Exception
from web3.types import TxReceipt

from backend.deploy_registry import SNAKE_NOT_FOUND
from backend.setup_keeper_transfers import KEEPER_ARTIFACT_PATH, ZERO_ADDRESS


TransferAction = Literal["accept", "reject", "cancel"]


class KeeperTransferTransactionError(RuntimeError):
    """Keep the transaction hash and uncertainty attached to a transfer write."""

    def __init__(
        self, message: str, *, transaction_hash: str | None, outcome: str
    ) -> None:
        super().__init__(message)
        self.transaction_hash = transaction_hash
        self.outcome = outcome


# Purpose: share the expected chain and immutable registry checks for reads/writes.
# Without these checks, a transfer request could reach an unrelated contract.
def _connect_keeper_registry() -> tuple[Web3, Contract]:
    transfer_address = os.environ.get("DEMO_KEEPER_TRANSFERS_ADDRESS", "").strip()
    snake_address = os.environ.get("DEMO_REGISTRY_ADDRESS", "").strip()

    if not Web3.is_address(transfer_address) or not Web3.is_address(snake_address):
        raise ConnectionError(
            "Configure DEMO_KEEPER_TRANSFERS_ADDRESS and DEMO_REGISTRY_ADDRESS "
            "before checking keeper permissions."
        )

    client = Web3(
        Web3.HTTPProvider(
            "http://127.0.0.1:8545",
            request_kwargs={"timeout": 5},
            exception_retry_configuration=None,
        )
    )
    if not client.is_connected() or client.eth.chain_id != 31337:
        raise ConnectionError("The expected local blockchain is unavailable.")

    transfer_address = Web3.to_checksum_address(transfer_address)
    snake_address = Web3.to_checksum_address(snake_address)
    if (
        not client.eth.get_code(transfer_address)
        or not client.eth.get_code(snake_address)
    ):
        raise ConnectionError("Keeper or registration contract code is unavailable.")

    artifact = json.loads(KEEPER_ARTIFACT_PATH.read_text(encoding="utf-8"))
    registry = client.eth.contract(address=transfer_address, abi=artifact["abi"])
    if registry.functions.snakeRegistry().call().lower() != snake_address.lower():
        raise ConnectionError("KeeperTransfers references another SnakeRegistry.")
    return client, registry


# Purpose: read the authoritative keeper and pending parties from one chain block.
# Without this query, the old registration keeper could retain rights after transfer.
def get_keeper_state(*, snake_id: str) -> dict:
    try:
        client, registry = _connect_keeper_registry()
        block_number = client.eth.block_number
        keeper = registry.functions.getCurrentKeeper(snake_id).call(
            block_identifier=block_number
        )
        from_keeper, recipient, pending = registry.functions.getPendingKeeperTransfer(
            snake_id
        ).call(block_identifier=block_number)

        if not Web3.is_address(keeper) or keeper.lower() == ZERO_ADDRESS:
            raise ConnectionError("The current keeper address is invalid.")

        if pending:
            if (
                from_keeper.lower() != keeper.lower()
                or recipient.lower() in {ZERO_ADDRESS, keeper.lower()}
            ):
                raise ConnectionError("The pending transfer state is inconsistent.")
        elif from_keeper.lower() != ZERO_ADDRESS or recipient.lower() != ZERO_ADDRESS:
            raise ConnectionError("Unexpected parties exist without a pending transfer.")

        return {
            "snake_id": snake_id,
            "current_keeper_address": keeper,
            "pending": pending,
            "from_keeper_address": from_keeper if pending else None,
            "recipient_address": recipient if pending else None,
            "block_number": block_number,
        }
    except ContractCustomError as error:
        if error.data == SNAKE_NOT_FOUND:
            raise LookupError("Snake is not registered in the configured registry.") from None
        raise ConnectionError("Keeper state lookup failed.") from None
    except (RequestException, Web3Exception, OSError, ValueError, KeyError, TypeError):
        # There is deliberately no fallback to the original registration keeper.
        raise ConnectionError("The current keeper state could not be confirmed.") from None


# Purpose: submit local demo transactions and confirm their receipts.
# Without this helper, resolution could handle uncertain transactions differently.
def _submit_keeper_transaction(
    *,
    client: Web3,
    function: ContractFunction,
    sender_address: str,
    on_submitted: Callable[[str], None],
) -> TxReceipt:
    sender = Web3.to_checksum_address(sender_address)
    try:
        transaction_hash = function.transact({"from": sender})
    except ContractLogicError:
        raise KeeperTransferTransactionError(
            "The contract rejected the transfer request. No transaction was submitted.",
            transaction_hash=None,
            outcome="not_submitted",
        ) from None
    except Exception:
        raise KeeperTransferTransactionError(
            "Transfer submission outcome is unknown. Check the chain before retrying.",
            transaction_hash=None,
            outcome="unknown",
        ) from None

    transaction_hex = transaction_hash.to_0x_hex()
    try:
        on_submitted(transaction_hex)
    except Exception:
        raise KeeperTransferTransactionError(
            "The transaction was submitted, but its hash could not be saved.",
            transaction_hash=transaction_hex,
            outcome="storage_error",
        ) from None

    try:
        receipt = client.eth.wait_for_transaction_receipt(transaction_hash, timeout=30)
    except Exception:
        raise KeeperTransferTransactionError(
            "Transfer confirmation is unavailable. Check the transaction before retrying.",
            transaction_hash=transaction_hex,
            outcome="unknown",
        ) from None

    if receipt["status"] != 1:
        raise KeeperTransferTransactionError(
            "The keeper transfer transaction failed.",
            transaction_hash=transaction_hex,
            outcome="failed",
        )

    return receipt


# Purpose: submit initiation and confirm the exact pending parties at its block.
# Without this operation, an application request cannot become a confirmed proposal.
def initiate_keeper_transfer_on_chain(
    *,
    snake_id: str,
    sender_address: str,
    recipient_address: str,
    on_submitted: Callable[[str], None],
) -> dict:
    try:
        client, registry = _connect_keeper_registry()
        sender = Web3.to_checksum_address(sender_address)
        recipient = Web3.to_checksum_address(recipient_address)
    except (RequestException, Web3Exception, OSError, ValueError, KeyError):
        raise KeeperTransferTransactionError(
            "Transfer configuration or chain lookup is unavailable. "
            "No transaction was submitted.",
            transaction_hash=None,
            outcome="not_submitted",
        ) from None

    receipt = _submit_keeper_transaction(
        client=client,
        function=registry.functions.initiateKeeperTransfer(snake_id, recipient),
        sender_address=sender,
        on_submitted=on_submitted,
    )
    transaction_hex = receipt["transactionHash"].to_0x_hex()

    try:
        signature = Web3.keccak(text="KeeperTransferInitiated(string,address,address)")
        logs = [
            log for log in receipt["logs"]
            if log["address"].lower() == registry.address.lower()
            and len(log["topics"]) == 4
            and bytes(log["topics"][0]) == bytes(signature)
        ]
        if len(logs) != 1:
            raise ValueError("Expected one transfer initiation event.")

        arguments = registry.events.KeeperTransferInitiated().process_log(logs[0])["args"]
        if not (
            bytes(arguments["snakeId"]) == bytes(Web3.keccak(text=snake_id))
            and arguments["fromKeeper"].lower() == sender.lower()
            and arguments["recipient"].lower() == recipient.lower()
        ):
            raise ValueError("The initiation event does not match the request.")

        block_number = receipt["blockNumber"]
        keeper = registry.functions.getCurrentKeeper(snake_id).call(
            block_identifier=block_number
        )
        from_keeper, to_keeper, pending = registry.functions.getPendingKeeperTransfer(
            snake_id
        ).call(block_identifier=block_number)
        if not (
            pending and keeper.lower() == sender.lower()
            and from_keeper.lower() == sender.lower()
            and to_keeper.lower() == recipient.lower()
        ):
            raise ValueError("The pending state does not match the request.")

        block = client.eth.get_block(block_number)
        initiated_at = datetime.fromtimestamp(block["timestamp"], tz=timezone.utc)
    except Exception:
        raise KeeperTransferTransactionError(
            "The transaction succeeded, but its pending transfer evidence "
            "could not be verified. Do not submit again automatically.",
            transaction_hash=transaction_hex,
            outcome="unverified",
        ) from None

    return {
        "transaction_hash": transaction_hex,
        "receipt_status": 1,
        "initiated_at": initiated_at,
        "current_keeper_address": keeper,
        "block_number": receipt["blockNumber"],
        "transaction_index": receipt["transactionIndex"],
    }


# Purpose: confirm a recipient decision or keeper cancellation on-chain.
# Without event and state checks, the application could display a false handover.
def resolve_keeper_transfer_on_chain(
    *,
    action: TransferAction,
    snake_id: str,
    actor_address: str,
    from_keeper_address: str,
    recipient_address: str,
    on_submitted: Callable[[str], None],
) -> dict:
    operations = {
        "accept": ("acceptKeeperTransfer", "KeeperTransferAccepted"),
        "reject": ("rejectKeeperTransfer", "KeeperTransferRejected"),
        "cancel": ("cancelKeeperTransfer", "KeeperTransferCancelled"),
    }
    if action not in operations:
        raise ValueError("Unsupported transfer action.")

    function_name, event_name = operations[action]
    try:
        client, registry = _connect_keeper_registry()
        actor = Web3.to_checksum_address(actor_address)
        from_keeper = Web3.to_checksum_address(from_keeper_address)
        recipient = Web3.to_checksum_address(recipient_address)
    except (RequestException, Web3Exception, OSError, ValueError, KeyError):
        raise KeeperTransferTransactionError(
            "Transfer configuration or chain lookup is unavailable. "
            "No transaction was submitted.",
            transaction_hash=None,
            outcome="not_submitted",
        ) from None

    receipt = _submit_keeper_transaction(
        client=client,
        function=getattr(registry.functions, function_name)(snake_id),
        sender_address=actor,
        on_submitted=on_submitted,
    )
    transaction_hex = receipt["transactionHash"].to_0x_hex()

    try:
        signature = Web3.keccak(text=f"{event_name}(string,address,address)")
        logs = [
            log for log in receipt["logs"]
            if log["address"].lower() == registry.address.lower()
            and len(log["topics"]) == 4
            and bytes(log["topics"][0]) == bytes(signature)
        ]
        if len(logs) != 1:
            raise ValueError("Expected one transfer resolution event.")

        arguments = getattr(registry.events, event_name)().process_log(logs[0])["args"]
        if not (
            bytes(arguments["snakeId"]) == bytes(Web3.keccak(text=snake_id))
            and arguments["fromKeeper"].lower() == from_keeper.lower()
            and arguments["recipient"].lower() == recipient.lower()
        ):
            raise ValueError("The resolution event does not match the request.")

        block_number = receipt["blockNumber"]
        keeper = registry.functions.getCurrentKeeper(snake_id).call(
            block_identifier=block_number
        )
        pending_from, pending_to, pending = registry.functions.getPendingKeeperTransfer(
            snake_id
        ).call(block_identifier=block_number)
        expected_keeper = recipient if action == "accept" else from_keeper
        if not (
            keeper.lower() == expected_keeper.lower()
            and not pending
            and pending_from.lower() == ZERO_ADDRESS
            and pending_to.lower() == ZERO_ADDRESS
        ):
            raise ValueError("The resolved keeper state does not match the action.")

        block = client.eth.get_block(block_number)
        resolved_at = datetime.fromtimestamp(block["timestamp"], tz=timezone.utc)
    except Exception:
        raise KeeperTransferTransactionError(
            "The transaction succeeded, but the resolved transfer evidence "
            "could not be verified. Do not submit again automatically.",
            transaction_hash=transaction_hex,
            outcome="unverified",
        ) from None

    return {
        "transaction_hash": transaction_hex,
        "receipt_status": 1,
        "resolved_at": resolved_at,
        "current_keeper_address": keeper,
        "block_number": receipt["blockNumber"],
        "transaction_index": receipt["transactionIndex"],
    }
