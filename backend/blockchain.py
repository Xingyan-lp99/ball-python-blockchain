from requests.exceptions import RequestException
from web3 import Web3
from web3.exceptions import Web3Exception


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


if __name__ == "__main__":
    result = check_blockchain_connection(
        rpc_url="http://127.0.0.1:8545",
        expected_chain_id=31337,
    )

    print(f"Chain ID: {result['chain_id']}")
    print(f"Accounts: {result['accounts']}")