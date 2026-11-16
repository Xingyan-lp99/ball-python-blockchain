import json

from requests.exceptions import RequestException
from web3 import Web3
from web3.exceptions import ContractCustomError, Web3Exception

from backend.deploy_registry import ARTIFACT_PATH
from collections.abc import Callable


SNAKE_ALREADY_REGISTERED = Web3.to_hex(
    Web3.keccak(text="SnakeAlreadyRegistered()")[:4]
)


class SnakeAlreadyRegisteredError(ValueError):
    """Identify duplicate registration without matching error-message text."""


class RegistrationTransactionError(RuntimeError):
    """Preserve transaction identity when registration cannot report success."""

    def __init__(
        self,
        message: str,
        transaction_hash: str,
        outcome: str,
    ) -> None:
        super().__init__(message)
        self.transaction_hash = transaction_hash
        self.outcome = outcome


# Purpose: submit registration and verify its confirmed event.
# Workflow: demo step 1, Python-to-contract snake registration.
# Without this operation, Python cannot register a snake through the contract.
def register_snake(
    *,
    rpc_url: str,
    expected_chain_id: int,
    contract_address: str,
    snake_id: str,
    sender_address: str,
    on_submitted: Callable[[str], None] | None = None,
) -> dict[str, str | int]:
    if snake_id == "":
        raise ValueError("Snake identifier must not be empty.")

    client = Web3(
        Web3.HTTPProvider(
            rpc_url,
            request_kwargs={"timeout": 5},
            exception_retry_configuration=None,
        )
    )

    if not client.is_connected():
        raise ConnectionError("Cannot connect to the blockchain node.")

    if client.eth.chain_id != expected_chain_id:
        raise ValueError("Unexpected chain ID; registration was not submitted.")

    address = Web3.to_checksum_address(contract_address)
    sender = Web3.to_checksum_address(sender_address)

    if not client.eth.get_code(address):
        raise RuntimeError("No contract code exists at the supplied address.")

    artifact = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    registry = client.eth.contract(
        address=address,
        abi=artifact["abi"],
    )

    try:
        transaction_hash = registry.functions.registerSnake(
            snake_id
        ).transact({"from": sender})
    except ContractCustomError as error:
        if error.data == SNAKE_ALREADY_REGISTERED:
            raise SnakeAlreadyRegisteredError(
                "Snake identifier is already registered."
            ) from None
        raise

    transaction_hex = transaction_hash.to_0x_hex()
    if on_submitted is not None:
        try:
            on_submitted(transaction_hex)
        except Exception:
            raise RegistrationTransactionError(
                "Transaction was submitted, but its hash could not be recorded. "
                "Check the transaction before submitting again.",
                transaction_hex,
                "unknown",
            ) from None

    try:
        receipt = client.eth.wait_for_transaction_receipt(
            transaction_hash,
            timeout=30,
        )
    except (RequestException, Web3Exception):
        raise RegistrationTransactionError(
            "Registration outcome is unknown. "
            "Check the transaction before submitting again.",
            transaction_hex,
            "unknown",
        ) from None

    if receipt["status"] != 1:
        raise RegistrationTransactionError(
            "Registration transaction failed.",
            transaction_hex,
            "failed",
        )

    try:
        events = registry.events.SnakeRegistered().process_receipt(receipt)
    except (Web3Exception, ValueError):
        raise RegistrationTransactionError(
            "Transaction succeeded, but registration event decoding failed.",
            transaction_hex,
            "unverified",
        ) from None

    if len(events) != 1:
        raise RegistrationTransactionError(
            "Transaction succeeded, but registration event verification failed.",
            transaction_hex,
            "unverified",
        )

    event = events[0]

    if (
        event["address"] != address
        or event["args"]["snakeId"] != snake_id
        or event["args"]["keeper"] != sender
    ):
        raise RegistrationTransactionError(
            "Transaction succeeded, but registration event data was unexpected.",
            transaction_hex,
            "unverified",
        )

    return {
        "transaction_hash": transaction_hex,
        "receipt_status": receipt["status"],
        "snake_id": event["args"]["snakeId"],
        "initial_keeper": event["args"]["keeper"],
    }