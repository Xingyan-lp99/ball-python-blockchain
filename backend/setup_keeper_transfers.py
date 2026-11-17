import json
import os
from pathlib import Path

from requests.exceptions import RequestException
from web3 import Web3
from web3.contract import Contract
from web3.exceptions import ContractLogicError, Web3Exception

from backend.deploy_registry import ARTIFACT_PATH as SNAKE_ARTIFACT_PATH


KEEPER_ARTIFACT_PATH = (
    Path(__file__).resolve().parents[1]
    / "contracts"
    / "artifacts"
    / "contracts"
    / "KeeperTransfers.sol"
    / "KeeperTransfers.json"
)
DEMO_SNAKE_ID = "SNAKE001"
ZERO_ADDRESS = "0x" + "0" * 40


# Purpose: check the dependency and read a consistent keeper/pending snapshot.
# Without this check, setup could accept another registry or inconsistent state.
def _read_keeper_state(
    client: Web3,
    registry: Contract,
    *,
    snake_registry_address: str,
) -> tuple[str, str, str, bool]:
    if not client.eth.get_code(registry.address):
        raise RuntimeError("KeeperTransfers code is unavailable at that address.")

    block_number = client.eth.block_number
    linked_registry = registry.functions.snakeRegistry().call(
        block_identifier=block_number
    )
    if linked_registry.lower() != snake_registry_address.lower():
        raise RuntimeError("KeeperTransfers references a different SnakeRegistry.")

    keeper = registry.functions.getCurrentKeeper(DEMO_SNAKE_ID).call(
        block_identifier=block_number
    )
    from_keeper, recipient, pending = registry.functions.getPendingKeeperTransfer(
        DEMO_SNAKE_ID
    ).call(block_identifier=block_number)

    if not Web3.is_address(keeper) or keeper.lower() == ZERO_ADDRESS:
        raise RuntimeError("KeeperTransfers returned an invalid current keeper.")

    if pending:
        if (
            from_keeper.lower() != keeper.lower()
            or recipient.lower() in {ZERO_ADDRESS, keeper.lower()}
        ):
            raise RuntimeError("KeeperTransfers returned an invalid pending transfer.")
    elif from_keeper.lower() != ZERO_ADDRESS or recipient.lower() != ZERO_ADDRESS:
        raise RuntimeError("KeeperTransfers returned unexpected pending parties.")

    return keeper, from_keeper, recipient, pending


# Purpose: deploy once or reuse the specified transfer contract on the local chain.
# Without this setup, later backend keeper checks have no transfer-contract address.
def setup_keeper_transfers(
    *,
    snake_registry_address: str,
    keeper_transfers_address: str | None = None,
) -> str:
    if not Web3.is_address(snake_registry_address):
        raise RuntimeError("Set a valid DEMO_REGISTRY_ADDRESS before running setup.")
    if keeper_transfers_address and not Web3.is_address(keeper_transfers_address):
        raise RuntimeError("DEMO_KEEPER_TRANSFERS_ADDRESS is not a valid address.")

    client = Web3(
        Web3.HTTPProvider(
            "http://127.0.0.1:8545",
            request_kwargs={"timeout": 5},
            exception_retry_configuration=None,
        )
    )
    if not client.is_connected():
        raise RuntimeError("Cannot connect to the local blockchain.")
    if client.eth.chain_id != 31337:
        raise RuntimeError("Expected local chain ID 31337.")

    snake_address = Web3.to_checksum_address(snake_registry_address)
    if not client.eth.get_code(snake_address):
        raise RuntimeError("The existing SnakeRegistry code is unavailable.")

    try:
        artifact = json.loads(KEEPER_ARTIFACT_PATH.read_text(encoding="utf-8"))
        snake_artifact = json.loads(SNAKE_ARTIFACT_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        raise RuntimeError("Compiled contract artifacts are unavailable. Compile first.") from None

    if not artifact.get("abi") or artifact.get("bytecode", "0x") == "0x":
        raise RuntimeError("The KeeperTransfers artifact has no ABI or bytecode.")

    original_registry = client.eth.contract(address=snake_address, abi=snake_artifact["abi"])
    initial_keeper = original_registry.functions.getCurrentKeeper(DEMO_SNAKE_ID).call()
    if not Web3.is_address(initial_keeper) or initial_keeper.lower() == ZERO_ADDRESS:
        raise RuntimeError("The original registry returned an invalid keeper.")

    created = not keeper_transfers_address
    if keeper_transfers_address:
        address = Web3.to_checksum_address(keeper_transfers_address)
        print("Reusing the configured KeeperTransfers contract.", flush=True)
    else:
        accounts = client.eth.accounts
        if not accounts:
            raise RuntimeError("No local deployment account is available.")

        factory = client.eth.contract(abi=artifact["abi"], bytecode=artifact["bytecode"])
        try:
            transaction_hash = factory.constructor(snake_address).transact(
                {"from": accounts[0]}
            )
        except ContractLogicError:
            raise RuntimeError("The deployment request was rejected; no transaction was submitted.") from None
        except (RequestException, Web3Exception):
            raise RuntimeError(
                "Deployment submission outcome is unknown. Check the local chain "
                "before running setup again; do not deploy another instance automatically."
            ) from None

        transaction_hex = transaction_hash.to_0x_hex()
        print("Deployment transaction:", transaction_hex, flush=True)
        try:
            receipt = client.eth.wait_for_transaction_receipt(transaction_hash, timeout=30)
        except (RequestException, Web3Exception):
            raise RuntimeError(
                "Deployment confirmation is unavailable. "
                f"Check {transaction_hex} before running setup again."
            ) from None

        if receipt["status"] != 1:
            raise RuntimeError(f"Deployment transaction failed: {transaction_hex}")
        address = receipt["contractAddress"]
        if not address:
            raise RuntimeError(
                f"Deployment receipt has no contract address. Check {transaction_hex}."
            )

    # Print the address before later reads so it remains recoverable if they fail.
    print("KeeperTransfers address:", address, flush=True)
    print(f'$env:DEMO_KEEPER_TRANSFERS_ADDRESS = "{address}"', flush=True)
    registry = client.eth.contract(address=address, abi=artifact["abi"])
    keeper, from_keeper, recipient, pending = _read_keeper_state(
        client, registry, snake_registry_address=snake_address
    )
    if created and (keeper.lower() != initial_keeper.lower() or pending):
        raise RuntimeError(
            "The new contract does not match the expected initial state. "
            "Retain its printed address and inspect it before running setup again."
        )

    print("SnakeRegistry:", snake_address)
    print(f"{DEMO_SNAKE_ID} registration keeper:", initial_keeper)
    print(f"{DEMO_SNAKE_ID} current keeper:", keeper)
    print("Pending transfer:", pending)
    if pending:
        print("From keeper:", from_keeper)
        print("Recipient:", recipient)
    print("KeeperTransfers setup completed successfully.")
    return str(address)


if __name__ == "__main__":
    try:
        setup_keeper_transfers(
            snake_registry_address=os.environ.get("DEMO_REGISTRY_ADDRESS", "").strip(),
            keeper_transfers_address=(
                os.environ.get("DEMO_KEEPER_TRANSFERS_ADDRESS", "").strip() or None
            ),
        )
    except (RequestException, Web3Exception):
        raise SystemExit(
            "A blockchain request failed. Retain any printed contract address "
            "and check any deployment transaction hash before running setup again."
        ) from None
    except (RuntimeError, ValueError, OSError) as error:
        raise SystemExit(str(error)) from None
