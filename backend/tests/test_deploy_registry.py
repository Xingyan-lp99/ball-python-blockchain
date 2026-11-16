import json
from pathlib import Path
from unittest.mock import Mock

import pytest
from hexbytes import HexBytes
from web3.exceptions import ContractCustomError, TimeExhausted

from backend.deploy_registry import (
    SNAKE_NOT_FOUND,
    deploy_snake_registry,
)


CONTRACT_ADDRESS = "0x1111111111111111111111111111111111111111"


@pytest.fixture
def artifact_path(tmp_path: Path) -> Path:
    path = tmp_path / "SnakeRegistry.json"
    path.write_text(
        json.dumps({"abi": [], "bytecode": "0x6000"}),
        encoding="utf-8",
    )
    return path


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> Mock:
    node = Mock()
    node.is_connected.return_value = True
    node.eth.chain_id = 31337
    node.eth.accounts = [
        "0x2222222222222222222222222222222222222222"
    ]

    contract = node.eth.contract.return_value
    contract.constructor.return_value.transact.return_value = (
        HexBytes("0x1234")
    )

    node.eth.wait_for_transaction_receipt.return_value = {
        "status": 1,
        "contractAddress": CONTRACT_ADDRESS,
    }
    node.eth.get_code.return_value = HexBytes("0x6000")

    contract.functions.getCurrentKeeper.return_value.call.side_effect = (
        ContractCustomError(
            "Expected unregistered snake",
            data=SNAKE_NOT_FOUND,
        )
    )

    monkeypatch.setattr(
        "backend.deploy_registry.Web3",
        Mock(return_value=node),
    )
    return node


def test_success_requires_receipt_code_and_expected_error(
    client: Mock,
    artifact_path: Path,
) -> None:
    result = deploy_snake_registry(
        rpc_url="http://127.0.0.1:8545",
        expected_chain_id=31337,
        artifact_path=artifact_path,
    )

    assert result == {
        "transaction_hash": "0x1234",
        "receipt_status": 1,
        "contract_address": CONTRACT_ADDRESS,
        "verification": "SnakeNotFound",
    }

    client.eth.contract.return_value.constructor.return_value.transact\
        .assert_called_once_with({"from": client.eth.accounts[0]})
    client.eth.get_code.assert_called_once_with(CONTRACT_ADDRESS)
    client.eth.contract.return_value.functions.getCurrentKeeper\
        .assert_called_once_with("SNAKE001")


def test_wrong_chain_does_not_submit_deployment(
    client: Mock,
    artifact_path: Path,
) -> None:
    client.eth.chain_id = 1

    with pytest.raises(ValueError, match="Unexpected chain ID"):
        deploy_snake_registry(
            rpc_url="http://127.0.0.1:8545",
            expected_chain_id=31337,
            artifact_path=artifact_path,
        )

    client.eth.contract.assert_not_called()


def test_failed_receipt_does_not_report_success(
    client: Mock,
    artifact_path: Path,
) -> None:
    client.eth.wait_for_transaction_receipt.return_value = {
        "status": 0,
        "contractAddress": None,
    }

    with pytest.raises(RuntimeError, match="transaction failed"):
        deploy_snake_registry(
            rpc_url="http://127.0.0.1:8545",
            expected_chain_id=31337,
            artifact_path=artifact_path,
        )

    client.eth.get_code.assert_not_called()


def test_missing_code_does_not_report_success(
    client: Mock,
    artifact_path: Path,
) -> None:
    client.eth.get_code.return_value = HexBytes("0x")

    with pytest.raises(RuntimeError, match="no contract code"):
        deploy_snake_registry(
            rpc_url="http://127.0.0.1:8545",
            expected_chain_id=31337,
            artifact_path=artifact_path,
        )


def test_unexpected_custom_error_does_not_report_success(
    client: Mock,
    artifact_path: Path,
) -> None:
    contract = client.eth.contract.return_value
    contract.functions.getCurrentKeeper.return_value.call.side_effect = (
        ContractCustomError(
            "Different error",
            data="0x12345678",
        )
    )

    with pytest.raises(RuntimeError, match="unexpected custom error"):
        deploy_snake_registry(
            rpc_url="http://127.0.0.1:8545",
            expected_chain_id=31337,
            artifact_path=artifact_path,
        )


def test_receipt_timeout_does_not_resubmit(
    client: Mock,
    artifact_path: Path,
) -> None:
    client.eth.wait_for_transaction_receipt.side_effect = (
        TimeExhausted("Simulated timeout")
    )

    with pytest.raises(RuntimeError, match="outcome is unknown"):
        deploy_snake_registry(
            rpc_url="http://127.0.0.1:8545",
            expected_chain_id=31337,
            artifact_path=artifact_path,
        )

    contract = client.eth.contract.return_value
    contract.constructor.return_value.transact.assert_called_once()
    client.eth.get_code.assert_not_called()


def test_real_local_deployment_and_read() -> None:
    result = deploy_snake_registry(
        rpc_url="http://127.0.0.1:8545",
        expected_chain_id=31337,
    )

    assert result["receipt_status"] == 1
    assert result["contract_address"]
    assert result["transaction_hash"].startswith("0x")
    assert result["verification"] == "SnakeNotFound"

    print(f"\nLocal deployment: {result}")