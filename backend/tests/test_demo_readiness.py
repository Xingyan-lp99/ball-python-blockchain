from unittest.mock import Mock, patch

from web3 import Web3

from backend.check_demo_readiness import check_demo_readiness


def test_restarted_chain_cannot_pass_readiness(monkeypatch):
    monkeypatch.setenv("DEMO_DB_PASSWORD", "test-only")
    for key in ("DEMO_REGISTRY_ADDRESS", "DEMO_CERTIFICATE_REGISTRY_ADDRESS", "DEMO_KEEPER_TRANSFERS_ADDRESS"):
        monkeypatch.setenv(key, "0x" + "1" * 40)
    client = Mock()
    client.is_connected.return_value = True
    client.eth.chain_id = 31337
    client.eth.block_number = 0
    client.eth.get_code.return_value = b""
    with patch("backend.check_demo_readiness.Web3", wraps=Web3) as web3:
        web3.return_value = client
        with patch("backend.check_demo_readiness.check_database_connection"):
            errors = check_demo_readiness()
    assert any("block 0" in error for error in errors)
    assert sum("no deployed code" in error for error in errors) == 3
    client.eth.send_transaction.assert_not_called()


def test_wrong_chain_stops_contract_checks(monkeypatch):
    monkeypatch.setenv("DEMO_DB_PASSWORD", "test-only")
    client = Mock()
    client.is_connected.return_value = True
    client.eth.chain_id = 1
    with patch("backend.check_demo_readiness.Web3", return_value=client), patch("backend.check_demo_readiness.check_database_connection"):
        errors = check_demo_readiness()
    assert errors == ["Wrong blockchain: expected local chain ID 31337."]
    client.eth.get_code.assert_not_called()


def test_complete_configuration_can_pass(monkeypatch):
    monkeypatch.setenv("DEMO_DB_PASSWORD", "test-only")
    registry = "0x" + "1" * 40
    for key, digit in (("DEMO_REGISTRY_ADDRESS", "1"), ("DEMO_CERTIFICATE_REGISTRY_ADDRESS", "2"), ("DEMO_KEEPER_TRANSFERS_ADDRESS", "3")):
        monkeypatch.setenv(key, "0x" + digit * 40)
    client = Mock()
    client.is_connected.return_value = True
    client.eth.chain_id = 31337
    client.eth.block_number = 10
    client.eth.get_code.return_value = b"deployed-code"
    client.eth.accounts = ["0x" + str(index) * 40 for index in range(5)]
    contract = client.eth.contract.return_value
    contract.functions.snakeRegistry.return_value.call.return_value = registry
    contract.functions.isAuthorizedLaboratory.return_value.call.return_value = True
    with patch("backend.check_demo_readiness.Web3", wraps=Web3) as web3, patch("backend.check_demo_readiness.check_database_connection"):
        web3.return_value = client
        assert check_demo_readiness() == []
    client.eth.send_transaction.assert_not_called()
