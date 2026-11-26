import json
from unittest.mock import MagicMock, Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.auth import require_breeder
from backend.session_routes import CurrentAccountResponse
from backend.snake_routes import router


SELLER_ADDRESS = "0x53c31f84Ea3F2b0A1c856a30ab519b8c8Dc55a57"
CONTRACT_ADDRESS = "0x1111111111111111111111111111111111111111"
PROFILE = {
    "snake_id": "NETWORK-ROUTE-TEST",
    "species": "Dog",
    "sex": "Female",
    "date_of_birth": "2025-03-04",
}
ANVIL_RESULT = {
    "transaction_hash": "0x" + "1" * 64,
    "receipt_status": 1,
    "snake_id": PROFILE["snake_id"],
    "initial_keeper": SELLER_ADDRESS,
}
SEPOLIA_RESULT = {
    **ANVIL_RESULT,
    "contract_address": CONTRACT_ADDRESS,
    "etherscan_url": "https://sepolia.etherscan.io/tx/0x" + "1" * 64,
    "chain_id": 11155111,
    "estimated_gas": 100_000,
    "gas_limit": 120_000,
    "max_fee_per_gas": 1,
    "max_cost_wei": 120_000,
}


@pytest.fixture
def client() -> TestClient:
    app = FastAPI()
    app.include_router(router)
    account = CurrentAccountResponse(
        account_id=1,
        username="seller",
        display_name="Seller",
        role="breeder",
        participant_id="BREEDER001",
    )
    app.dependency_overrides[require_breeder] = lambda: account
    with TestClient(app, client=("127.0.0.1", 51000)) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def database(monkeypatch: pytest.MonkeyPatch) -> Mock:
    connection = Mock()
    statements: list[str] = []

    def execute(statement: str, *_args, **_kwargs) -> Mock:
        statements.append(statement)
        result = Mock()
        if "FROM participants" in statement:
            result.fetchone.return_value = (SELLER_ADDRESS,)
        elif "FROM snakes" in statement:
            result.fetchone.return_value = None
        return result

    connection.execute.side_effect = execute
    context = MagicMock()
    context.__enter__.return_value = connection
    monkeypatch.setattr("backend.snake_routes.psycopg.connect", Mock(return_value=context))
    monkeypatch.setenv("DEMO_DB_PASSWORD", "test-password")
    monkeypatch.setenv("DEMO_REGISTRY_ADDRESS", CONTRACT_ADDRESS)
    connection.statements = statements
    return connection


def post_registration(client: TestClient, network: str | None = None):
    data = {"profile_json": json.dumps(PROFILE)}
    if network is not None:
        data["network"] = network
    return client.post(
        "/api/v1/snakes",
        data=data,
        files={"photo": ("pet.jpg", b"photo-bytes", "image/jpeg")},
    )


def test_sepolia_network_uses_only_sepolia_handler(
    client: TestClient, database: Mock, monkeypatch: pytest.MonkeyPatch,
) -> None:
    sepolia = Mock(return_value=SEPOLIA_RESULT)
    anvil = Mock(return_value=ANVIL_RESULT)
    monkeypatch.setattr("backend.snake_routes.register_pet_on_sepolia", sepolia)
    monkeypatch.setattr("backend.snake_routes.register_snake_profile", anvil)

    response = post_registration(client, "sepolia")

    assert response.status_code == 201
    sepolia.assert_called_once()
    anvil.assert_not_called()
    assert not any("FROM snakes" in sql for sql in database.statements)


def test_anvil_network_uses_only_anvil_handler(
    client: TestClient, database: Mock, monkeypatch: pytest.MonkeyPatch,
) -> None:
    sepolia = Mock(return_value=SEPOLIA_RESULT)
    anvil = Mock(return_value=ANVIL_RESULT)
    monkeypatch.setattr("backend.snake_routes.register_pet_on_sepolia", sepolia)
    monkeypatch.setattr("backend.snake_routes.register_snake_profile", anvil)
    monkeypatch.setattr("backend.snake_routes.save_snake_photo", Mock(return_value="photos/test.jpg"))

    response = post_registration(client, "anvil")

    assert response.status_code == 201
    anvil.assert_called_once()
    sepolia.assert_not_called()
    assert any("FROM snakes" in sql for sql in database.statements)


@pytest.mark.parametrize("network", [None, "invalid"])
def test_missing_or_invalid_network_is_rejected_without_registration(
    client: TestClient, monkeypatch: pytest.MonkeyPatch, network: str | None,
) -> None:
    connect = Mock()
    sepolia = Mock(return_value=SEPOLIA_RESULT)
    anvil = Mock(return_value=ANVIL_RESULT)
    monkeypatch.setattr("backend.snake_routes.psycopg.connect", connect)
    monkeypatch.setattr("backend.snake_routes.register_pet_on_sepolia", sepolia)
    monkeypatch.setattr("backend.snake_routes.register_snake_profile", anvil)

    response = post_registration(client, network)

    assert response.status_code == 422
    connect.assert_not_called()
    sepolia.assert_not_called()
    anvil.assert_not_called()
