from unittest.mock import patch

import pytest

from backend.blockchain import check_blockchain_connection


# Purpose: verify the actual local blockchain connection.
# Workflow: environment setup, Day 1, blockchain validation.
# Removing this test loses coverage of the real RPC connection.
def test_blockchain_connection_returns_chain_and_accounts() -> None:
    result = check_blockchain_connection(
        rpc_url="http://127.0.0.1:8545",
        expected_chain_id=31337,
    )

    assert result["chain_id"] == 31337
    assert isinstance(result["accounts"], list)
    assert len(result["accounts"]) > 0


# Purpose: verify that an unreachable node produces a clear failure.
# Workflow: environment setup, Day 1, blockchain failure validation.
# Removing this test loses coverage of unavailable-node handling.
def test_blockchain_connection_rejects_unavailable_node() -> None:
    with patch("backend.blockchain.Web3") as web3_class:
        client = web3_class.return_value
        client.is_connected.return_value = False

        with pytest.raises(ConnectionError, match="Cannot connect"):
            check_blockchain_connection(
                rpc_url="http://127.0.0.1:8545",
                expected_chain_id=31337,
            )


# Purpose: prevent accepting a connection to the wrong chain.
# Workflow: environment setup, Day 1, network identity validation.
# Removing this test loses coverage of chain-ID mismatch handling.
def test_blockchain_connection_rejects_wrong_chain() -> None:
    with patch("backend.blockchain.Web3") as web3_class:
        client = web3_class.return_value
        client.is_connected.return_value = True
        client.eth.chain_id = 1

        with pytest.raises(ValueError, match="Unexpected chain ID"):
            check_blockchain_connection(
                rpc_url="http://127.0.0.1:8545",
                expected_chain_id=31337,
            )