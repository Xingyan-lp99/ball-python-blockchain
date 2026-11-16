import json
from unittest.mock import Mock

import pytest
from hexbytes import HexBytes
from web3 import Web3
from web3.exceptions import ContractCustomError, TimeExhausted

from backend.deploy_registry import (
    ARTIFACT_PATH,
    SNAKE_NOT_FOUND,
    deploy_snake_registry,
)
from backend.register_snake import (
    SNAKE_ALREADY_REGISTERED,
    register_snake,
)


RPC_URL = "http://127.0.0.1:8545"
CONTRACT_ADDRESS = "0x1111111111111111111111111111111111111111"
SENDER_ADDRESS = "0x2222222222222222222222222222222222222222"


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> Mock:
    node = Mock()
    node.is_connected.return_value = True
    node.eth.chain_id = 31337
    node.eth.get_code.return_value = HexBytes("0x6000")
    node.eth.wait_for_transaction_receipt.return_value = {"status": 1}

    registry = node.eth.contract.return_value
    registry.functions.registerSnake.return_value.transact.return_value = (
        HexBytes("0x1234")
    )
    registry.events.SnakeRegistered.return_value.process_receipt.return_value = [
        {
            "address": CONTRACT_ADDRESS,
            "args": {
                "snakeId": "SNAKE001",
                "keeper": SENDER_ADDRESS,
            },
        }
    ]

    monkeypatch.setattr(
        "backend.register_snake.Web3",
        Mock(wraps=Web3, return_value=node),
    )
    return node


@pytest.fixture
def inputs() -> dict[str, str | int]:
    return {
        "rpc_url": RPC_URL,
        "expected_chain_id": 31337,
        "contract_address": CONTRACT_ADDRESS,
        "snake_id": "SNAKE001",
        "sender_address": SENDER_ADDRESS,
    }


def test_success_returns_confirmed_registration(
    client: Mock,
    inputs: dict,
) -> None:
    result = register_snake(**inputs)

    assert result == {
        "transaction_hash": "0x1234",
        "receipt_status": 1,
        "snake_id": "SNAKE001",
        "initial_keeper": SENDER_ADDRESS,
    }

    registry = client.eth.contract.return_value
    registry.functions.registerSnake.assert_called_once_with("SNAKE001")
    registry.functions.registerSnake.return_value.transact\
        .assert_called_once_with({"from": SENDER_ADDRESS})

    registry.events.SnakeRegistered.return_value.process_receipt\
        .assert_called_once_with({"status": 1})


def test_empty_identifier_is_rejected(
    client: Mock,
    inputs: dict,
) -> None:
    inputs["snake_id"] = ""

    with pytest.raises(ValueError, match="must not be empty"):
        register_snake(**inputs)

    client.eth.contract.assert_not_called()


def test_wrong_chain_does_not_submit(
    client: Mock,
    inputs: dict,
) -> None:
    client.eth.chain_id = 1

    with pytest.raises(ValueError, match="Unexpected chain ID"):
        register_snake(**inputs)

    client.eth.contract.assert_not_called()


def test_duplicate_identifier_is_reported(
    client: Mock,
    inputs: dict,
) -> None:
    registry = client.eth.contract.return_value
    registry.functions.registerSnake.return_value.transact.side_effect = (
        ContractCustomError(
            "Duplicate snake",
            data=SNAKE_ALREADY_REGISTERED,
        )
    )

    with pytest.raises(ValueError, match="already registered"):
        register_snake(**inputs)

    client.eth.wait_for_transaction_receipt.assert_not_called()


def test_failed_receipt_does_not_report_success(
    client: Mock,
    inputs: dict,
) -> None:
    client.eth.wait_for_transaction_receipt.return_value = {"status": 0}

    with pytest.raises(RuntimeError, match="transaction failed"):
        register_snake(**inputs)

    registry = client.eth.contract.return_value
    registry.events.SnakeRegistered.assert_not_called()


def test_timeout_does_not_resubmit(
    client: Mock,
    inputs: dict,
) -> None:
    client.eth.wait_for_transaction_receipt.side_effect = (
        TimeExhausted("Simulated timeout")
    )

    with pytest.raises(RuntimeError, match="outcome is unknown"):
        register_snake(**inputs)

    registry = client.eth.contract.return_value
    registry.functions.registerSnake.return_value.transact.assert_called_once()


def test_missing_event_does_not_report_success(
    client: Mock,
    inputs: dict,
) -> None:
    registry = client.eth.contract.return_value
    registry.events.SnakeRegistered.return_value.process_receipt.return_value = []

    with pytest.raises(RuntimeError, match="event verification failed"):
        register_snake(**inputs)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("snakeId", "DIFFERENT"),
        ("keeper", CONTRACT_ADDRESS),
    ],
)
def test_unexpected_event_data_does_not_report_success(
    client: Mock,
    inputs: dict,
    field: str,
    value: str,
) -> None:
    registry = client.eth.contract.return_value
    events = (
        registry.events.SnakeRegistered.return_value
        .process_receipt.return_value
    )
    events[0]["args"][field] = value

    with pytest.raises(RuntimeError, match="event data was unexpected"):
        register_snake(**inputs)


def test_real_registration_and_keeper_verification() -> None:
    deployment = deploy_snake_registry(
        rpc_url=RPC_URL,
        expected_chain_id=31337,
    )
    address = deployment["contract_address"]

    client = Web3(
        Web3.HTTPProvider(
            RPC_URL,
            request_kwargs={"timeout": 5},
            exception_retry_configuration=None,
        )
    )

    sender = client.eth.accounts[1]
    artifact = json.loads(ARTIFACT_PATH.read_text(encoding="utf-8"))
    registry = client.eth.contract(
        address=address,
        abi=artifact["abi"],
    )

    result = register_snake(
        rpc_url=RPC_URL,
        expected_chain_id=31337,
        contract_address=address,
        snake_id="SNAKE001",
        sender_address=sender,
    )

    assert result["receipt_status"] == 1
    assert result["snake_id"] == "SNAKE001"
    assert result["initial_keeper"] == sender
    assert registry.functions.getCurrentKeeper("SNAKE001").call() == sender

    with pytest.raises(ValueError, match="already registered"):
        register_snake(
            rpc_url=RPC_URL,
            expected_chain_id=31337,
            contract_address=address,
            snake_id="SNAKE001",
            sender_address=sender,
        )

    assert registry.functions.getCurrentKeeper("SNAKE001").call() == sender

    with pytest.raises(ContractCustomError) as error:
        registry.functions.getCurrentKeeper("SNAKE999").call()

    assert error.value.data == SNAKE_NOT_FOUND

    print(f"\nTest registry: {address}")
    print(f"Confirmed registration: {result}")