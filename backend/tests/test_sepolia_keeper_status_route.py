from contextlib import contextmanager
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.sepolia_routes import router
from backend.session_routes import CurrentAccountResponse, read_current_account


SELLER = "0x53c31f84Ea3F2b0A1c856a30ab519b8c8Dc55a57"
BUYER = "0x5D30F8dB977193e62502B3bD596C05314e5d19aA"


@pytest.mark.parametrize(
    ("role", "participant_id"),
    [("breeder", "BREEDER001"), ("buyer", "BUYER001")],
)
def test_keeper_status_route_is_readable_by_seller_and_buyer(
    monkeypatch: pytest.MonkeyPatch,
    role: str,
    participant_id: str,
) -> None:
    app = FastAPI()
    app.include_router(router)
    account = CurrentAccountResponse(
        account_id=1,
        username=participant_id.lower(),
        display_name=role.title(),
        role=role,
        participant_id=participant_id,
    )
    app.dependency_overrides[read_current_account] = lambda: account

    connection = Mock()
    connection.execute.side_effect = [
        Mock(fetchone=Mock(return_value=("Seller",))),
        Mock(fetchone=Mock(return_value=("seller",))),
    ]

    @contextmanager
    def fake_database():
        yield connection

    monkeypatch.setattr("backend.sepolia_routes._database", fake_database)
    monkeypatch.setattr(
        "backend.sepolia_routes.sepolia_keeper_state",
        Mock(return_value={
            "snake_id": "BP-S004",
            "current_keeper_address": SELLER,
            "pending": False,
            "from_keeper_address": None,
            "recipient_address": None,
            "transfer": None,
            "transaction_hash": None,
            "transaction_status": None,
            "block_number": 12_212_316,
        }),
    )
    signers = {
        "BREEDER001": SimpleNamespace(address=SELLER),
        "BUYER001": SimpleNamespace(address=BUYER),
        "LAB001": SimpleNamespace(address="0x95D61329A586379C6fB19Ebe60F778821319d0f0"),
        "LAB002": SimpleNamespace(address="0x2f3D117EacB4e0F5edA8c2d33eC6Ad5B59aDB6E3"),
    }
    monkeypatch.setattr(
        "backend.sepolia_routes.get_sepolia_signer",
        lambda identity: signers[identity],
    )

    with TestClient(app, client=("127.0.0.1", 52000)) as client:
        response = client.get("/api/v1/sepolia/snakes/BP-S004/keeper")

    assert response.status_code == 200
    assert response.json()["snake_id"] == "BP-S004"
    assert response.json()["current_keeper"]["participant_id"] == "BREEDER001"
    assert response.json()["current_keeper"]["wallet_address"] == SELLER
    assert response.json()["transfer_status"] == "no_pending_transfer"
    assert response.json()["transaction_status"] is None
