from uuid import uuid4

import pytest
from sqlalchemy import select, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from snake_registry.local_chain import ChainConflict, ChainStale, ChainUnavailable
from snake_registry.models import RegistrationAttempt


class FakeChain:
    chain_id = 31337
    address = "0x" + "11" * 20
    manager = "0x" + "22" * 20
    instance_id = "0x" + "33" * 32

    def __init__(self):
        self.instance_id = "0x" + uuid4().hex * 2
        self.owners = {}
        self.hashes = {}
        self.receipts = {}
        self.send_calls = []
        self.pending = False
        self.revert = False
        self.unavailable = False
        self.stale = False
        self.lost_send_response = False

    def validate_scope(self):
        if self.unavailable:
            raise ChainUnavailable
        if self.stale:
            raise ChainStale

    def manager_of(self, snake_id):
        return self.owners.get(snake_id)

    def transaction_parameters(self):
        return len(self.send_calls), 1_000_000_000, 1

    def send(self, snake_id, nonce, gas_price):
        self.send_calls.append((snake_id, nonce, gas_price))
        transaction_hash = "0x" + f"{nonce + 1:064x}"
        self.hashes[snake_id] = transaction_hash
        if not self.pending:
            self.receipts[transaction_hash] = {
                "status": 0 if self.revert else 1,
                "blockNumber": nonce + 2, "blockHash": bytes([nonce + 1]) * 32,
            }
            if not self.revert:
                self.owners[snake_id] = self.manager
        if self.lost_send_response:
            raise ChainUnavailable
        return transaction_hash

    def receipt(self, transaction_hash):
        if self.unavailable:
            raise ChainUnavailable
        return self.receipts.get(transaction_hash)

    def registration_hash(self, snake_id):
        return self.hashes.get(snake_id)

    def recover_hash(self, nonce, start_block, snake_id):
        return self.hashes.get(snake_id)

    def verify_success(self, snake_id, transaction_hash, receipt):
        if self.owners.get(snake_id) != self.manager:
            raise ChainConflict


@pytest.fixture
def chain(monkeypatch):
    chain = FakeChain()
    monkeypatch.setattr("snake_registry.routes.get_local_chain", lambda: chain)
    return chain


def create_profile(client):
    snake_id = "CHAIN-" + uuid4().hex
    assert client.post("/api/v1/snakes", json={"snake_id": snake_id, "sex": "unknown"}).status_code == 201
    return snake_id, f"/api/v1/snakes/{snake_id}/registration"


def test_normal_registration_is_idempotent(db_client, chain, registry_engine):
    snake_id, endpoint = create_profile(db_client)
    response = db_client.post(endpoint, json={})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "confirmed"
    assert data["chain_check"] == "verified"
    assert data["chain_id"] == 31337
    assert data["manager_address"] == chain.manager
    assert data["transaction_hash"]
    assert data["block_number"]
    assert db_client.post(endpoint, json={}).json() == data
    assert db_client.get(endpoint).json() == data
    profile = db_client.get(f"/api/v1/snakes/{snake_id}").json()
    assert profile["registration_status"] == "confirmed"
    assert profile["certificate_status"] == "not_verified"
    assert len(chain.send_calls) == 1
    with Session(registry_engine) as session:
        assert session.scalar(select(RegistrationAttempt).where(RegistrationAttempt.transaction_hash == data["transaction_hash"])) is not None


@pytest.mark.parametrize("field", ["from", "manager_address", "private_key", "chain_id"])
def test_sender_cannot_be_overridden(db_client, chain, field):
    _, endpoint = create_profile(db_client)
    assert db_client.post(endpoint, json={field: "untrusted"}).status_code == 422
    assert chain.send_calls == []


def test_missing_database_profile(db_client, chain):
    endpoint = f"/api/v1/snakes/missing-{uuid4().hex}/registration"
    assert db_client.post(endpoint, json={}).status_code == 404
    assert db_client.get(endpoint).status_code == 404
    assert chain.send_calls == []


def test_only_current_demo_manager_can_submit(db_client, chain, registry_engine):
    snake_id, endpoint = create_profile(db_client)
    with registry_engine.begin() as connection:
        connection.execute(text("UPDATE snakes SET current_manager_id = 'BR002' WHERE snake_id = :id"), {"id": snake_id})
    assert db_client.post(endpoint, json={}).status_code == 403
    assert db_client.get(f"/api/v1/snakes/{snake_id}").status_code == 200
    assert chain.send_calls == []


def test_other_context_has_no_demo_wallet(db_client, chain):
    from identity import get_current_breeder_id
    from main import app
    snake_id, endpoint = create_profile(db_client)
    app.dependency_overrides[get_current_breeder_id] = lambda: "BR002"
    assert db_client.post(endpoint, json={}).status_code == 403
    assert chain.send_calls == []


def test_rpc_unavailable_does_not_submit(db_client, chain):
    snake_id, endpoint = create_profile(db_client)
    chain.unavailable = True
    assert db_client.post(endpoint, json={}).status_code == 503
    assert db_client.get(endpoint).json()["status"] == "not_submitted"
    assert db_client.get(f"/api/v1/snakes/{snake_id}").status_code == 200
    assert chain.send_calls == []


def test_pending_and_polling_never_duplicate(db_client, chain):
    _, endpoint = create_profile(db_client)
    chain.pending = True
    data = db_client.post(endpoint, json={}).json()
    assert data["status"] == "processing"
    assert data["transaction_hash"]
    assert db_client.get(endpoint).json()["status"] == "processing"
    assert db_client.post(endpoint, json={}).json()["status"] == "processing"
    assert len(chain.send_calls) == 1
    chain.owners[chain.send_calls[0][0]] = chain.manager
    chain.receipts[data["transaction_hash"]] = {"status": 1, "blockNumber": 7, "blockHash": bytes([7]) * 32}
    assert db_client.get(endpoint).json()["status"] == "confirmed"


def test_reverted_transaction_can_retry_with_history(db_client, chain, registry_engine):
    _, endpoint = create_profile(db_client)
    chain.revert = True
    failed = db_client.post(endpoint, json={}).json()
    assert failed["status"] == "failed"
    assert failed["error"] == "transaction_reverted"
    chain.revert = False
    successful = db_client.post(endpoint, json={}).json()
    assert successful["status"] == "confirmed"
    assert successful["transaction_hash"] != failed["transaction_hash"]
    with Session(registry_engine) as session:
        attempt = session.scalar(select(RegistrationAttempt).where(
            RegistrationAttempt.transaction_hash == failed["transaction_hash"],
            RegistrationAttempt.instance_id == chain.instance_id,
        ))
        assert attempt.status == "failed"


def test_lost_send_response_recovers_by_chain_read(db_client, chain):
    _, endpoint = create_profile(db_client)
    chain.lost_send_response = True
    initial = db_client.post(endpoint, json={}).json()
    assert initial["status"] == "processing"
    assert initial["transaction_hash"] is None
    assert db_client.get(endpoint).json()["status"] == "confirmed"
    assert db_client.post(endpoint, json={}).json()["status"] == "confirmed"
    assert len(chain.send_calls) == 1


@pytest.mark.parametrize("failed_status", ["submitted", "confirmed"])
def test_chain_success_database_failure_recovers(db_client, chain, monkeypatch, failed_status):
    _, endpoint = create_profile(db_client)
    original_commit = Session.commit
    injected = False

    def failing_commit(session):
        nonlocal injected
        if not injected and any(
            isinstance(item, RegistrationAttempt) and item.status == failed_status
            for item in session.identity_map.values()
        ):
            injected = True
            raise OperationalError("simulated DB failure", {}, Exception("unavailable"))
        return original_commit(session)

    monkeypatch.setattr(Session, "commit", failing_commit)
    assert db_client.post(endpoint, json={}).status_code == 503
    assert injected
    recovered = db_client.get(endpoint).json()
    assert recovered["status"] == "confirmed"
    assert recovered["transaction_hash"]
    assert db_client.post(endpoint, json={}).json()["status"] == "confirmed"
    assert len(chain.send_calls) == 1


def test_conflicting_on_chain_owner_is_rejected(db_client, chain):
    snake_id, endpoint = create_profile(db_client)
    chain.owners[snake_id] = "0x" + "44" * 20
    assert db_client.post(endpoint, json={}).status_code == 409
    assert db_client.get(f"/api/v1/snakes/{snake_id}").status_code == 200
    assert chain.send_calls == []


def test_old_success_is_not_current_success_after_reset(db_client, chain):
    snake_id, endpoint = create_profile(db_client)
    assert db_client.post(endpoint, json={}).json()["status"] == "confirmed"
    chain.stale = True
    state = db_client.get(endpoint).json()
    assert state["status"] == "failed"
    assert state["recorded_status"] == "confirmed"
    assert state["chain_check"] == "stale"
    assert db_client.get(f"/api/v1/snakes/{snake_id}").json()["registration_status"] == "failed"
    assert db_client.post(endpoint, json={}).status_code == 409
    assert len(chain.send_calls) == 1


def test_rpc_loss_clears_current_confirmation_but_keeps_history(db_client, chain):
    _, endpoint = create_profile(db_client)
    saved = db_client.post(endpoint, json={}).json()
    chain.unavailable = True
    state = db_client.get(endpoint).json()
    assert state["status"] == "processing"
    assert state["recorded_status"] == "confirmed"
    assert state["chain_check"] == "unavailable"
    assert state["transaction_hash"] == saved["transaction_hash"]


def test_redeployment_does_not_relabel_old_confirmation(db_client, chain):
    _, endpoint = create_profile(db_client)
    previous = db_client.post(endpoint, json={}).json()
    chain.instance_id = "0x" + uuid4().hex * 2
    state = db_client.get(endpoint).json()
    assert state["status"] == "failed"
    assert state["chain_check"] == "stale"
    assert state["instance_id"] == previous["instance_id"]
    assert db_client.post(endpoint, json={}).status_code == 409


def test_global_signer_lock_blocks_competing_request(db_client, chain, registry_engine):
    _, endpoint = create_profile(db_client)
    with registry_engine.connect() as connection:
        connection.execute(text("SELECT pg_advisory_lock(724801002)"))
        try:
            assert db_client.post(endpoint, json={}).status_code == 409
            assert chain.send_calls == []
        finally:
            connection.execute(text("SELECT pg_advisory_unlock(724801002)"))


def test_receipt_without_matching_evidence_is_not_confirmation(db_client, chain, monkeypatch):
    _, endpoint = create_profile(db_client)

    def mismatch(*args):
        raise ChainConflict

    monkeypatch.setattr(chain, "verify_success", mismatch)
    assert db_client.post(endpoint, json={}).status_code == 409
    state = db_client.get(endpoint).json()
    assert state["status"] == "failed"
    assert state["chain_check"] == "conflict"
    assert state["recorded_status"] == "submitted"


def test_unbroadcast_intent_retries_same_transaction_parameters(db_client, chain, monkeypatch):
    _, endpoint = create_profile(db_client)
    original_send = chain.send

    def before_broadcast(*args):
        raise ChainUnavailable

    monkeypatch.setattr(chain, "send", before_broadcast)
    initial = db_client.post(endpoint, json={}).json()
    assert initial["status"] == "processing"
    assert initial["transaction_hash"] is None
    other_id, other_endpoint = create_profile(db_client)
    assert db_client.post(other_endpoint, json={}).status_code == 409
    monkeypatch.setattr(chain, "send", original_send)
    assert db_client.post(endpoint, json={}).json()["status"] == "confirmed"
    assert chain.send_calls[0][1:] == (0, 1_000_000_000)
    assert db_client.get(f"/api/v1/snakes/{other_id}").status_code == 200
