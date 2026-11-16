from datetime import date
from unittest.mock import ANY, MagicMock, Mock

from backend.snake_registration import (
    SnakeProfileExistsError,
    UnknownParticipantError,
)

import pytest
from fastapi.testclient import TestClient
from requests.exceptions import ConnectionError as RequestConnectionError

from backend.main import app
from backend.register_snake import (
    RegistrationTransactionError,
    SnakeAlreadyRegisteredError,
)


CONTRACT_ADDRESS = "0x1111111111111111111111111111111111111111"
SENDER_ADDRESS = "0x2222222222222222222222222222222222222222"

PAYLOAD = {
    "snake_id": "SNAKE001",
    "sender_address": SENDER_ADDRESS,
    "breeder_internal_id": "BP001",
    "species": "Python regius",
    "sex": "Female",
    "date_of_birth": "2025-06-01",
    "genetic_description": "Fictional demonstration description",
    "photo_reference": "photos/snake001.jpg",
}

RESULT = {
    "transaction_hash": "0x1234",
    "receipt_status": 1,
    "snake_id": "SNAKE001",
    "initial_keeper": SENDER_ADDRESS,
}


@pytest.fixture
def registration(monkeypatch: pytest.MonkeyPatch) -> Mock:
    monkeypatch.setenv("DEMO_REGISTRY_ADDRESS", CONTRACT_ADDRESS)
    monkeypatch.setenv("DEMO_DB_PASSWORD", "test-password")

    monkeypatch.setattr(
        "backend.snake_routes.psycopg.connect",
        MagicMock(),
    )

    operation = Mock(return_value=RESULT.copy())
    monkeypatch.setattr(
        "backend.snake_routes.register_snake_profile",
        operation,
    )
    return operation


def test_registration_returns_201(registration: Mock) -> None:
    with TestClient(app) as client:
        response = client.post("/api/v1/snakes", json=PAYLOAD)

    assert response.status_code == 201
    assert response.json() == RESULT

        expected_profile = {
        key: value
        for key, value in PAYLOAD.items()
        if key != "sender_address"
    }
    expected_profile.update({
        "date_of_birth": date(2025, 6, 1),
        "nickname": None,
        "introduction": None,
        "sire_description": None,
        "dam_description": None,
    })

    registration.assert_called_once_with(
        ANY,
        rpc_url="http://127.0.0.1:8545",
        expected_chain_id=31337,
        contract_address=CONTRACT_ADDRESS,
        sender_address=SENDER_ADDRESS,
        profile=expected_profile,
    )


@pytest.mark.parametrize(
    "payload",
    [
        {**PAYLOAD, "snake_id": ""},
        {**PAYLOAD, "sender_address": "invalid"},
        {
            key: value
            for key, value in PAYLOAD.items()
            if key != "sender_address"
        },
    ],
)
def test_invalid_request_returns_422(
    registration: Mock,
    payload: dict,
) -> None:
    with TestClient(app) as client:
        response = client.post("/api/v1/snakes", json=payload)

    assert response.status_code == 422
    registration.assert_not_called()


def test_whitespace_identifier_is_preserved(registration: Mock) -> None:
    registration.return_value = {**RESULT, "snake_id": " "}

    with TestClient(app) as client:
        response = client.post(
            "/api/v1/snakes",
            json={**PAYLOAD, "snake_id": " "},
        )

    assert response.status_code == 201
    assert response.json()["snake_id"] == " "
    assert registration.call_args.kwargs["profile"]["snake_id"] == " "


def test_duplicate_returns_409(registration: Mock) -> None:
    registration.side_effect = SnakeAlreadyRegisteredError("Duplicate")

    with TestClient(app) as client:
        response = client.post("/api/v1/snakes", json=PAYLOAD)

    assert response.status_code == 409
    assert response.json() == {
        "detail": "Snake identifier is already registered."
    }


@pytest.mark.parametrize("address", [None, "invalid"])
def test_missing_or_invalid_configuration_does_not_submit(
    registration: Mock,
    monkeypatch: pytest.MonkeyPatch,
    address: str | None,
) -> None:
    if address is None:
        monkeypatch.delenv("DEMO_REGISTRY_ADDRESS", raising=False)
    else:
        monkeypatch.setenv("DEMO_REGISTRY_ADDRESS", address)

    with TestClient(app) as client:
        response = client.post("/api/v1/snakes", json=PAYLOAD)

    assert response.status_code == 503
    assert response.json()["outcome"] == "not_submitted"
    registration.assert_not_called()


@pytest.mark.parametrize(
    ("outcome", "status_code"),
    [
        ("unknown", 503),
        ("failed", 502),
        ("unverified", 502),
        ("storage_error", 503),
    ],
)
def test_transaction_problem_preserves_hash(
    registration: Mock,
    outcome: str,
    status_code: int,
) -> None:
    registration.side_effect = RegistrationTransactionError(
        "Internal diagnostic detail",
        "0x1234",
        outcome,
    )

    with TestClient(app) as client:
        response = client.post("/api/v1/snakes", json=PAYLOAD)

    assert response.status_code == status_code
    assert response.json()["outcome"] == outcome
    assert response.json()["transaction_hash"] == "0x1234"
    assert "Internal diagnostic detail" not in response.text


def test_node_failure_returns_safe_response(registration: Mock) -> None:
    registration.side_effect = RequestConnectionError(
        "Private internal connection detail"
    )

    with TestClient(app) as client:
        response = client.post("/api/v1/snakes", json=PAYLOAD)

    assert response.status_code == 503
    assert response.json()["outcome"] == "unknown"
    assert "Private internal connection detail" not in response.text

@pytest.mark.parametrize(
    ("error", "status_code"),
    [
        (UnknownParticipantError("Not configured"), 422),
        (SnakeProfileExistsError("Existing profile"), 409),
    ],
)
def test_participant_and_profile_errors(
    registration: Mock,
    error: Exception,
    status_code: int,
) -> None:
    registration.side_effect = error

    with TestClient(app) as client:
        response = client.post("/api/v1/snakes", json=PAYLOAD)

    assert response.status_code == status_code


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("breeder_internal_id", " "),
        ("species", ""),
        ("sex", None),
        ("date_of_birth", "not-a-date"),
        ("genetic_description", "\t"),
        ("photo_reference", " "),
    ],
)
def test_invalid_profile_does_not_call_registration(
    registration: Mock,
    field: str,
    value: object,
) -> None:
    with TestClient(app) as client:
        response = client.post(
            "/api/v1/snakes",
            json={**PAYLOAD, field: value},
        )

    assert response.status_code == 422
    registration.assert_not_called()