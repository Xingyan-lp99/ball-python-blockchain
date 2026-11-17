import json

from requests.exceptions import RequestException
from web3 import Web3
from web3.exceptions import ContractCustomError, Web3Exception

from backend.deploy_registry import ARTIFACT_PATH, SNAKE_NOT_FOUND


# Purpose: verify the expected blockchain and read its account addresses.
# Workflow: environment setup, Day 1, Python-to-blockchain connection.
# Removing this function removes this connection and network identity check.
def check_blockchain_connection(
    *,
    rpc_url: str,
    expected_chain_id: int,
) -> dict[str, int | list[str]]:
    try:
        client = Web3(
            Web3.HTTPProvider(
                rpc_url,
                request_kwargs={"timeout": 5},
                exception_retry_configuration=None,
            )
        )

        if not client.is_connected():
            raise ConnectionError("Cannot connect to the blockchain node.")

        chain_id = client.eth.chain_id

        if chain_id != expected_chain_id:
            raise ValueError(
                f"Unexpected chain ID: expected {expected_chain_id}, "
                f"received {chain_id}."
            )

        accounts = [str(address) for address in client.eth.accounts]

    except (RequestException, Web3Exception):
        raise ConnectionError("Blockchain RPC request failed.") from None

    return {
        "chain_id": chain_id,
        "accounts": accounts,
    }


# Purpose: read the original registry's keeper for registration/existence checks.
# Certificate preflight uses this read to confirm the registered snake exists.
# Management rights must use backend.keeper_transfers.get_keeper_state instead.
def get_current_keeper(
    *,
    rpc_url: str,
    expected_chain_id: int,
    contract_address: str,
    snake_id: str,
) -> str:
    try:
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
            raise ConnectionError("Unexpected blockchain chain ID.")

        address = Web3.to_checksum_address(contract_address)

        if not client.eth.get_code(address):
            raise ConnectionError("Registry contract code is unavailable.")

        artifact = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
        registry = client.eth.contract(
            address=address,
            abi=artifact["abi"],
        )

        keeper = registry.functions.getCurrentKeeper(snake_id).call()

        if (
            not Web3.is_address(keeper)
            or keeper.lower() == "0x" + "0" * 40
        ):
            raise ConnectionError("Registry returned an invalid keeper.")

        return keeper

    except ContractCustomError as error:
        if error.data == SNAKE_NOT_FOUND:
            raise LookupError(
                "Snake is not registered in the configured registry."
            ) from None
        raise ConnectionError("Keeper lookup failed.") from None
    except (RequestException, Web3Exception, OSError, ValueError):
        raise ConnectionError("Keeper lookup is unavailable.") from None


if __name__ == "__main__":
    result = check_blockchain_connection(
        rpc_url="http://127.0.0.1:8545",
        expected_chain_id=31337,
    )

    print(f"Chain ID: {result['chain_id']}")
    print(f"Accounts: {result['accounts']}")
