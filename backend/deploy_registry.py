import json
from pathlib import Path

from web3 import Web3
from web3.exceptions import ContractCustomError, TimeExhausted


ARTIFACT_PATH = (
    Path(__file__).resolve().parents[1]
    / "contracts"
    / "artifacts"
    / "contracts"
    / "SnakeRegistry.sol"
    / "SnakeRegistry.json"
)

SNAKE_NOT_FOUND = Web3.to_hex(
    Web3.keccak(text="SnakeNotFound()")[:4]
)


# Purpose: deploy and verify the registry on the local demonstration chain.
# Workflow: demo step 1, before snake registration and backend integration.
# Without this operation, later calls have no deployed registry address.
def deploy_snake_registry(
    *,
    rpc_url: str,
    expected_chain_id: int,
    artifact_path: Path = ARTIFACT_PATH,
) -> dict[str, str | int]:
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
        raise ValueError("Unexpected chain ID; deployment was not submitted.")

    accounts = client.eth.accounts

    if not accounts:
        raise RuntimeError("No local deployment account is available.")

    artifact = json.loads(artifact_path.read_text(encoding="utf-8"))

    factory = client.eth.contract(
        abi=artifact["abi"],
        bytecode=artifact["bytecode"],
    )

    transaction_hash = factory.constructor().transact(
        {"from": accounts[0]}
    )

    try:
        receipt = client.eth.wait_for_transaction_receipt(
            transaction_hash,
            timeout=30,
        )
    except TimeExhausted:
        raise RuntimeError(
            "Receipt wait timed out. Deployment outcome is unknown. "
            f"Check transaction {transaction_hash.to_0x_hex()} "
            "before deploying again."
        ) from None

    if receipt["status"] != 1:
        raise RuntimeError("Deployment transaction failed.")

    contract_address = receipt["contractAddress"]

    if not contract_address or not client.eth.get_code(contract_address):
        raise RuntimeError("Deployment verification found no contract code.")

    registry = client.eth.contract(
        address=contract_address,
        abi=artifact["abi"],
    )

    try:
        registry.functions.getCurrentKeeper("SNAKE001").call()
    except ContractCustomError as error:
        if error.data != SNAKE_NOT_FOUND:
            raise RuntimeError(
                "Registry verification returned an unexpected custom error."
            ) from None
    else:
        raise RuntimeError(
            "Registry verification expected an unregistered identifier."
        )

    return {
        "transaction_hash": transaction_hash.to_0x_hex(),
        "receipt_status": receipt["status"],
        "contract_address": contract_address,
        "verification": "SnakeNotFound",
    }


if __name__ == "__main__":
    result = deploy_snake_registry(
        rpc_url="http://127.0.0.1:8545",
        expected_chain_id=31337,
    )

    for name, value in result.items():
        print(f"{name}: {value}")