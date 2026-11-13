"""Deployment isolation and immutable V2 workflow through the real database API."""
import hashlib
from concurrent.futures import ThreadPoolExecutor

import pytest
from sqlalchemy import select
from sqlalchemy.orm import Session

from certificates.local_chain import CertificatePreflightError
from certificates.models import CertificateVersion, IssuanceAttempt
from pdf_fixtures import test_pdf as make_pdf
from test_certificates import FakeCertificateChain, certificate_chain, draft


class FakeVersionedChain(FakeCertificateChain):
    address = "0x" + "81" * 20

    def record(self, certificate_id, version_number=1):
        self.validate_scope()
        return self.records.get((certificate_id, version_number))

    def latest_version(self, certificate_id):
        self.validate_scope()
        return max([v for c, v in self.records if c == certificate_id], default=0)

    def assert_can_issue(self, subject):
        super().assert_can_issue(subject)
        first = self.record(subject.certificate_id)
        if first and (first["issuer_address"] != self.manager or first["snake_id"] != subject.snake_id):
            raise CertificatePreflightError("series_immutable", "Original laboratory and snake cannot change")
        if subject.version != self.latest_version(subject.certificate_id) + 1:
            raise CertificatePreflightError("non_contiguous_version", "Only the next version is permitted")

    def send(self, subject, nonce, gas_price):
        self.send_calls.append((subject, nonce, gas_price))
        key = (subject.certificate_id, subject.version)
        tx_hash = "0x" + f"{nonce + 100:064x}"
        self.hashes[key] = tx_hash
        if not self.pending:
            self.receipts[tx_hash] = {"status": 0 if self.revert else 1, "blockNumber": nonce + 100,
                                      "blockHash": bytes([nonce + 1]) * 32}
            if not self.revert:
                self.records[key] = {"certificate_id": subject.certificate_id, "snake_id": subject.snake_id,
                                     "issuer_address": subject.issuer_address, "version": subject.version,
                                     "file_hash": subject.file_hash}
        if self.lost_response:
            from snake_registry.local_chain import ChainUnavailable
            raise ChainUnavailable
        return tx_hash

    def registration_hash(self, subject):
        return self.hashes.get((subject.certificate_id, subject.version))

    def recover_hash(self, nonce, start_block, subject):
        return self.registration_hash(subject)

    def verify_success(self, subject, tx_hash, receipt):
        self.assert_record(subject, self.record(subject.certificate_id, subject.version))


@pytest.fixture
def version_chain(monkeypatch, certificate_chain):
    chain = FakeVersionedChain()
    chain.manager = certificate_chain.manager
    monkeypatch.setattr("certificates.routes.get_versioned_certificate_chain", lambda: chain)
    return chain


def prepared(client):
    snake, certificate, legacy = draft(client)
    old = client.post(legacy + "/issuance", json={}).json()
    assert old["status"] == "confirmed"
    base = f"/api/v1/certificates/{certificate}"
    response = client.post(base + "/histories", json={})
    assert response.status_code == 201, response.json()
    history = response.json()["history_id"]
    params = {"history_id": history}
    assert client.post(legacy + "/issuance", json={}, params=params).json()["status"] == "confirmed"
    return snake, certificate, base, history, old


def append(client, base, history, content=None):
    return client.post(base + f"/histories/{history}/versions",
                       files={"file": ("TEST_ONLY_v2.pdf", content or make_pdf("V2 TEST ONLY"), "application/pdf")})


def stored(client, base, number, history):
    return client.post(base + f"/versions/{number}/verification/stored", json={}, params={"history_id": history}).json()


def test_append_confirmation_and_separate_legacy_history(db_client, version_chain):
    snake, certificate, base, history, old = prepared(db_client)
    assert append(db_client, base, history).status_code == 201
    assert stored(db_client, base, 1, history)["version_status"] == "latest"
    state = db_client.post(base + "/versions/2/issuance", json={}, params={"history_id": history}).json()
    assert state["status"] == "confirmed"
    first, second = stored(db_client, base, 1, history), stored(db_client, base, 2, history)
    assert (first["file_result"], first["version_status"]) == ("match", "superseded")
    assert (second["file_result"], second["version_status"]) == ("match", "latest")
    assert second["latest_version"] == 2 and not second["revocation_checked"]
    legacy = db_client.get(base + "/versions/1").json()
    assert legacy["issuance"]["transaction_hash"] == old["transaction_hash"]
    assert legacy["version_status"] == "latest"  # Only within the OLD deployment.
    assert db_client.get(base + "/versions/2").status_code == 404
    catalog = db_client.get(base + "/histories").json()
    assert catalog["default_history_id"] == history and catalog["default_version"] == 2
    assert db_client.get(f"/api/v1/snakes/{snake}/certificates").json()[0]["version"] == 2
    assert db_client.post(base + "/histories", json={}).status_code == 200
    assert db_client.get(base + "/versions/1/file").content == make_pdf()


@pytest.mark.parametrize("pending,revert", [(True, False), (False, True)])
def test_pending_or_failed_v2_keeps_v1_latest(db_client, version_chain, pending, revert):
    _, _, base, history, _ = prepared(db_client)
    append(db_client, base, history)
    version_chain.pending, version_chain.revert = pending, revert
    params = {"history_id": history}
    endpoint = base + "/versions/2/issuance"
    state = db_client.post(endpoint, json={}, params=params).json()
    assert state["status"] == ("processing" if pending else "failed")
    assert stored(db_client, base, 1, history)["version_status"] == "latest"
    assert db_client.get(base + "/histories").json()["default_version"] == 1
    if pending:
        assert db_client.post(endpoint, json={}, params=params).json()["transaction_hash"] == state["transaction_hash"]
        assert len(version_chain.send_calls) == 2  # New V1 and one V2.


def test_duplicate_concurrent_uploads_and_immutable_bytes(db_client, version_chain, registry_engine):
    _, _, base, history, _ = prepared(db_client)
    with ThreadPoolExecutor(max_workers=2) as pool:
        statuses = list(pool.map(lambda _: append(db_client, base, history).status_code, range(2)))
    assert 201 in statuses and set(statuses) <= {200, 201, 409}
    assert append(db_client, base, history).status_code == 200
    assert append(db_client, base, history, make_pdf("different")).status_code == 409
    with Session(registry_engine) as session:
        assert len(session.scalars(select(CertificateVersion).where(CertificateVersion.history_id == history)).all()) == 2
    params = {"history_id": history}
    with ThreadPoolExecutor(max_workers=2) as pool:
        responses = list(pool.map(lambda _: db_client.post(base + "/versions/2/issuance", json={}, params=params), range(2)))
    assert all(r.status_code in {200, 409} for r in responses)
    assert len(version_chain.send_calls) == 2


@pytest.mark.parametrize("identity", ["LAB002", "BR001", "Buyer"])
def test_other_demo_roles_cannot_append(db_client, version_chain, identity):
    from main import app
    from identity import get_current_lab_id
    _, _, base, history, _ = prepared(db_client)
    app.dependency_overrides[get_current_lab_id] = lambda: identity
    assert append(db_client, base, history).status_code == 403
    assert db_client.post(base + "/histories", json={}).status_code == 403


def test_deauthorized_or_wrong_wallet_cannot_append(db_client, version_chain):
    _, _, base, history, _ = prepared(db_client)
    version_chain.authorized = False
    assert append(db_client, base, history).status_code == 409
    version_chain.authorized = True
    version_chain.manager = "0x" + "99" * 20
    assert append(db_client, base, history).status_code == 403
    assert len(version_chain.send_calls) == 1


def test_live_hash_external_filename_and_rpc_independence(db_client, version_chain):
    _, _, base, history, _ = prepared(db_client)
    original = make_pdf("V2 TEST ONLY")
    append(db_client, base, history, original)
    params = {"history_id": history}
    db_client.post(base + "/versions/2/issuance", json={}, params=params)
    for name, content, expected in [("renamed.pdf", original, "match"), ("TEST_ONLY_v2.pdf", make_pdf("modified"), "mismatch")]:
        result = db_client.post(base + "/versions/2/verification", params=params,
            files={"file": (name, content, "application/pdf")}).json()
        assert result["file_result"] == expected and result["version_status"] == "latest"
    version_chain.unavailable = True
    result = stored(db_client, base, 2, history)
    assert result["file_result"] == "unable_to_verify" and result["version_status"] == "unknown"
    assert not result["latest_version_checked"]
    assert len(version_chain.send_calls) == 2


def test_lost_response_restores_v2_without_second_transaction(db_client, version_chain, registry_engine):
    _, _, base, history, _ = prepared(db_client)
    append(db_client, base, history)
    version_chain.lost_response = True
    params = {"history_id": history}
    endpoint = base + "/versions/2/issuance"
    db_client.post(endpoint, json={}, params=params)
    assert db_client.get(endpoint, params=params).json()["status"] == "confirmed"
    # Model successful broadcast followed by loss of all local transaction evidence.
    with Session(registry_engine) as session:
        version = session.scalar(select(CertificateVersion).where(CertificateVersion.history_id == history, CertificateVersion.version_number == 2))
        attempt = session.scalar(select(IssuanceAttempt).where(IssuanceAttempt.version_id == version.id))
        attempt.transaction_hash, attempt.status = None, "prepared"
        session.commit()
    assert db_client.post(endpoint, json={}, params=params).json()["status"] == "confirmed"
    assert len(version_chain.send_calls) == 2


def test_latest_rpc_failure_does_not_claim_latest(db_client, version_chain, monkeypatch):
    from snake_registry.local_chain import ChainUnavailable
    _, _, base, history, _ = prepared(db_client)
    def fail(_):
        raise ChainUnavailable
    monkeypatch.setattr(version_chain, "latest_version", fail)
    result = stored(db_client, base, 1, history)
    assert result["file_result"] == "match" and result["version_status"] == "unknown"
    assert not result["latest_version_checked"]


@pytest.mark.parametrize("status", ["submitted", "confirmed"])
def test_v2_chain_success_database_failure_recovers(db_client, version_chain, monkeypatch, status):
    from sqlalchemy.exc import OperationalError
    _, _, base, history, _ = prepared(db_client)
    append(db_client, base, history)
    original_commit, injected = Session.commit, False
    def fail_once(session):
        nonlocal injected
        if not injected and any(isinstance(item, IssuanceAttempt) and item.status == status for item in session.identity_map.values()):
            injected = True
            raise OperationalError("simulated", {}, Exception("unavailable"))
        return original_commit(session)
    monkeypatch.setattr(Session, "commit", fail_once)
    params = {"history_id": history}
    endpoint = base + "/versions/2/issuance"
    assert db_client.post(endpoint, json={}, params=params).status_code == 503
    assert injected
    assert db_client.get(endpoint, params=params).json()["status"] == "confirmed"
    assert len(version_chain.send_calls) == 2
    assert stored(db_client, base, 1, history)["version_status"] == "superseded"


def test_nonce_reservation_is_shared_across_deployments(db_client, version_chain, registry_engine):
    _, _, base, history, _ = prepared(db_client)
    append(db_client, base, history)
    # A legacy prepared intent must reserve this same LAB001 wallet's nonce too.
    with Session(registry_engine) as session:
        old = session.scalar(select(IssuanceAttempt).where(IssuanceAttempt.contract_address == FakeCertificateChain.address,
                                                         IssuanceAttempt.manager_address == version_chain.manager))
        old_id, previous_status, previous_nonce = old.id, old.status, old.nonce
        old.status, old.nonce = "prepared", 1
        session.commit()
    try:
        result = db_client.post(base + "/versions/2/issuance", json={}, params={"history_id": history})
    finally:
        with Session(registry_engine) as session:
            old = session.get(IssuanceAttempt, old_id)
            old.status, old.nonce = previous_status, previous_nonce
            session.commit()
    assert result.status_code == 409 and "reserves" in result.json()["detail"]
    assert len(version_chain.send_calls) == 1
