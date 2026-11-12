import hashlib
from uuid import uuid4

import pytest
from sqlalchemy import select
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from certificates.local_chain import CertificateChain, CertificateSubject, CertificatePreflightError
from certificates.models import Certificate, CertificateVersion, IssuanceAttempt, StoredFile
from certificates.storage import original_path
from snake_registry.local_chain import ChainUnavailable, ChainStale, ChainConflict
from pdf_fixtures import test_pdf as make_pdf


class FakeCertificateChain:
    chain_id = 31337
    address = "0x" + "71" * 20
    manager = "0x" + "72" * 20
    lab_name = "TEST ONLY Laboratory LAB001"

    def __init__(self):
        self.instance_id = "0x" + uuid4().hex * 2
        self.records, self.hashes, self.receipts = {}, {}, {}
        self.send_calls = []
        self.pending = self.revert = self.unavailable = self.stale = self.lost_response = False
        self.authorized = self.snake_registered = True

    def validate_scope(self):
        if self.unavailable:
            raise ChainUnavailable
        if self.stale:
            raise ChainStale

    def assert_can_issue(self, subject):
        if subject.issuer_address != self.manager:
            raise CertificatePreflightError("issuer_wallet_mismatch", "V1 issuer differs from the LAB001 signing wallet")
        if not self.authorized:
            raise CertificatePreflightError("laboratory_not_authorized", "LAB001 signing wallet is not authorized")
        if not self.snake_registered:
            raise CertificatePreflightError("snake_not_registered", f"Snake {subject.snake_id} is not registered in the referenced SnakeRegistry; complete Breeder registration first")

    def record(self, certificate_id):
        self.validate_scope()
        return self.records.get(certificate_id)

    assert_record = CertificateChain.assert_record

    def transaction_parameters(self):
        return len(self.send_calls), 1_000_000_000, 1

    def send(self, subject, nonce, gas_price):
        self.send_calls.append((subject, nonce, gas_price))
        tx_hash = "0x" + f"{nonce + 1:064x}"
        self.hashes[subject.certificate_id] = tx_hash
        if not self.pending:
            self.receipts[tx_hash] = {"status": 0 if self.revert else 1, "blockNumber": nonce + 2,
                                      "blockHash": bytes([nonce + 1]) * 32}
            if not self.revert:
                self.records[subject.certificate_id] = {"certificate_id": subject.certificate_id,
                    "snake_id": subject.snake_id, "issuer_address": subject.issuer_address,
                    "version": 1, "file_hash": subject.file_hash}
        if self.lost_response:
            raise ChainUnavailable
        return tx_hash

    def registration_hash(self, subject):
        return self.hashes.get(subject.certificate_id)

    def recover_hash(self, nonce, start_block, subject):
        return self.hashes.get(subject.certificate_id)

    def receipt(self, tx_hash):
        self.validate_scope()
        return self.receipts.get(tx_hash)

    def verify_success(self, subject, tx_hash, receipt):
        self.assert_record(subject, self.records[subject.certificate_id])


@pytest.fixture
def certificate_chain(monkeypatch, tmp_path):
    chain = FakeCertificateChain()
    monkeypatch.setattr("certificates.routes.get_certificate_chain", lambda: chain)
    monkeypatch.setenv("CERTIFICATE_STORAGE_DIR", str(tmp_path / "certificate-files"))
    return chain


def upload(client, certificate_id, snake_id, content=None, filename="fixture.pdf", **fields):
    return client.post("/api/v1/certificates", data={"certificate_id": certificate_id, "snake_id": snake_id, **fields},
                       files={"file": (filename, content if content is not None else make_pdf(), "application/pdf")})


def draft(client):
    snake_id, certificate_id = "TEST-S-" + uuid4().hex, "TEST-C-" + uuid4().hex
    assert client.post("/api/v1/snakes", json={"snake_id": snake_id, "sex": "unknown"}).status_code == 201
    response = upload(client, certificate_id, snake_id)
    assert response.status_code == 201, response.json()
    return snake_id, certificate_id, f"/api/v1/certificates/{certificate_id}/versions/1"


def verify(client, endpoint, content=None, filename="candidate.pdf"):
    return client.post(endpoint + "/verification", files={"file": (filename, content or make_pdf(), "application/pdf")})


def test_original_bytes_download_hash_and_repeat_upload(db_client, certificate_chain, registry_engine):
    snake_id, cert_id, endpoint = draft(db_client)
    saved = db_client.get(endpoint).json()
    assert saved["sha256"] == hashlib.sha256(make_pdf()).hexdigest()
    assert saved["lab_id"] == "LAB001" and saved["issuer_address"] == certificate_chain.manager
    assert saved["version"] == 1
    assert not saved["latest_version_checked"] and not saved["revocation_checked"]
    assert db_client.get(endpoint + "/file").content == make_pdf()
    assert upload(db_client, cert_id, snake_id, filename="renamed.pdf").status_code == 200
    assert db_client.get(endpoint).json()["original_filename"] == "fixture.pdf"
    assert upload(db_client, cert_id, snake_id, content=make_pdf("different")).status_code == 409
    assert db_client.get(endpoint + "/file").content == make_pdf()
    assert db_client.get(f"/api/v1/snakes/{snake_id}/certificates").json()[0]["certificate_id"] == cert_id
    with Session(registry_engine) as session:
        version = session.scalar(select(CertificateVersion).join(Certificate).where(Certificate.certificate_id == cert_id))
        stored = session.get(StoredFile, version.file_id)
        assert stored.storage_key.endswith(".pdf") and stored.storage_key != "fixture.pdf"


def test_authorized_issue_and_duplicate_requests(db_client, certificate_chain):
    snake_id, _, endpoint = draft(db_client)
    state = db_client.post(endpoint + "/issuance", json={}).json()
    assert state["status"] == "confirmed"
    assert state["manager_address"] == certificate_chain.manager
    assert db_client.post(endpoint + "/issuance", json={}).json() == state
    assert db_client.get(endpoint + "/issuance").json() == state
    assert len(certificate_chain.send_calls) == 1
    assert db_client.get(f"/api/v1/snakes/{snake_id}").json()["certificate_status"] == "not_verified"


@pytest.mark.parametrize("field", ["issuer_address", "private_key", "version", "sha256", "lab_id"])
def test_upload_cannot_override_server_fields(db_client, certificate_chain, field):
    assert upload(db_client, "TEST-C", "TEST-S", **{field: "untrusted"}).status_code == 422


@pytest.mark.parametrize("field", ["from", "issuer_address", "private_key", "file_hash"])
def test_issuance_cannot_override_signer_or_digest(db_client, certificate_chain, field):
    _, _, endpoint = draft(db_client)
    assert db_client.post(endpoint + "/issuance", json={field: "untrusted"}).status_code == 422
    assert certificate_chain.send_calls == []


def test_invalid_input_and_missing_subject(db_client, certificate_chain):
    assert upload(db_client, "TEST-C", "missing").status_code == 404
    assert upload(db_client, " ", "missing").status_code == 422
    assert upload(db_client, "TEST-C", "missing", content=b"not PDF").status_code == 422
    assert upload(db_client, "TEST-C", "missing", content=b"%PDF-" + b"x" * (10 * 1024 * 1024)).status_code == 413
    assert db_client.get("/api/v1/certificates/missing/versions/1").status_code == 404


@pytest.mark.parametrize("allowed,registered", [(False, True), (True, False)])
def test_unauthorized_lab_or_missing_chain_snake_rejected(db_client, certificate_chain, allowed, registered):
    _, _, endpoint = draft(db_client)
    certificate_chain.authorized, certificate_chain.snake_registered = allowed, registered
    assert db_client.post(endpoint + "/issuance", json={}).status_code == 409
    assert db_client.get(endpoint + "/file").content == make_pdf()
    assert certificate_chain.send_calls == []


def test_other_demo_identity_cannot_issue(db_client, certificate_chain):
    from main import app
    from identity import get_current_lab_id
    _, _, endpoint = draft(db_client)
    app.dependency_overrides[get_current_lab_id] = lambda: "BR001"
    assert db_client.post(endpoint + "/issuance", json={}).status_code == 403


@pytest.mark.parametrize("filename,modified,expected", [
    ("fixture.pdf", False, "match"), ("renamed.pdf", False, "match"),
    ("fixture.pdf", True, "mismatch"), ("different.pdf", True, "mismatch"),
])
def test_independent_file_comparison(db_client, certificate_chain, filename, modified, expected):
    _, _, endpoint = draft(db_client)
    assert db_client.post(endpoint + "/issuance", json={}).json()["status"] == "confirmed"
    content = make_pdf("different findings TEST ONLY") if modified else make_pdf()
    result = verify(db_client, endpoint, content, filename).json()
    assert result["file_result"] == expected
    assert result["uploaded_sha256"] == hashlib.sha256(content).hexdigest()
    assert result["on_chain_sha256"] == hashlib.sha256(make_pdf()).hexdigest()
    assert result["registration"]["status"] == "confirmed"
    assert not result["latest_version_checked"] and not result["revocation_checked"]


def test_verification_reads_chain_hash_not_database_cache(db_client, certificate_chain, registry_engine):
    _, cert_id, endpoint = draft(db_client)
    assert db_client.post(endpoint + "/issuance", json={}).json()["status"] == "confirmed"
    with Session(registry_engine) as session:
        version = session.scalar(select(CertificateVersion).join(Certificate).where(Certificate.certificate_id == cert_id))
        version.file_hash = bytes(32)  # Test-only cache corruption, not an application update endpoint.
        session.commit()
    assert verify(db_client, endpoint).json()["file_result"] == "match"


@pytest.mark.parametrize("failure", ["rpc", "stale", "missing"])
def test_verification_failure_is_unable_not_mismatch(db_client, certificate_chain, failure):
    _, certificate_id, endpoint = draft(db_client)
    assert db_client.post(endpoint + "/issuance", json={}).json()["status"] == "confirmed"
    if failure == "rpc":
        certificate_chain.unavailable = True
    elif failure == "stale":
        certificate_chain.stale = True
    else:
        certificate_chain.records.pop(certificate_id)
    result = verify(db_client, endpoint).json()
    assert result["file_result"] == "unable_to_verify"
    assert result["registration"]["status"] != "confirmed"
    assert result["on_chain_sha256"] is None


def test_pending_polling_and_repeated_submit(db_client, certificate_chain):
    _, _, endpoint = draft(db_client)
    certificate_chain.pending = True
    state = db_client.post(endpoint + "/issuance", json={}).json()
    assert state["status"] == "processing" and state["transaction_hash"]
    assert db_client.post(endpoint + "/issuance", json={}).json() == state
    assert db_client.get(endpoint + "/issuance").json()["status"] == "processing"
    assert len(certificate_chain.send_calls) == 1
    assert verify(db_client, endpoint).json()["file_result"] == "unable_to_verify"


def test_lost_response_recovers_from_live_record(db_client, certificate_chain):
    _, _, endpoint = draft(db_client)
    certificate_chain.lost_response = True
    state = db_client.post(endpoint + "/issuance", json={}).json()
    assert state["status"] == "processing" and state["transaction_hash"] is None
    assert db_client.get(endpoint + "/issuance").json()["status"] == "confirmed"
    assert db_client.post(endpoint + "/issuance", json={}).json()["status"] == "confirmed"
    assert len(certificate_chain.send_calls) == 1


@pytest.mark.parametrize("status", ["submitted", "confirmed"])
def test_chain_success_then_db_write_failure_recovers(db_client, certificate_chain, monkeypatch, status):
    _, _, endpoint = draft(db_client)
    original_commit, injected = Session.commit, False

    def failing_commit(session):
        nonlocal injected
        if not injected and any(isinstance(item, IssuanceAttempt) and item.status == status for item in session.identity_map.values()):
            injected = True
            raise OperationalError("simulated", {}, Exception("unavailable"))
        return original_commit(session)

    monkeypatch.setattr(Session, "commit", failing_commit)
    assert db_client.post(endpoint + "/issuance", json={}).status_code == 503
    assert injected
    assert db_client.get(endpoint + "/issuance").json()["status"] == "confirmed"
    assert db_client.get(endpoint + "/file").content == make_pdf()
    assert len(certificate_chain.send_calls) == 1


def test_revert_and_retry_keep_original_v1(db_client, certificate_chain):
    _, _, endpoint = draft(db_client)
    certificate_chain.revert = True
    failed = db_client.post(endpoint + "/issuance", json={}).json()
    assert failed["status"] == "failed" and failed["error"] == "transaction_reverted"
    certificate_chain.revert = False
    confirmed = db_client.post(endpoint + "/issuance", json={}).json()
    assert confirmed["status"] == "confirmed"
    assert confirmed["transaction_hash"] != failed["transaction_hash"]
    assert db_client.get(endpoint + "/file").content == make_pdf()


def test_rpc_failure_before_send_never_confirms(db_client, certificate_chain):
    _, _, endpoint = draft(db_client)
    certificate_chain.unavailable = True
    assert db_client.post(endpoint + "/issuance", json={}).status_code == 503
    assert certificate_chain.send_calls == []


def test_same_filename_different_certificates_never_overwrite_files(db_client, certificate_chain):
    snake_id, _, first = draft(db_client)
    certificate_id = "TEST-C-" + uuid4().hex
    different = make_pdf("another certificate TEST ONLY")
    assert upload(db_client, certificate_id, snake_id, different, "fixture.pdf").status_code == 201
    second = f"/api/v1/certificates/{certificate_id}/versions/1"
    assert db_client.get(first + "/file").content == make_pdf()
    assert db_client.get(second + "/file").content == different
    assert db_client.post(first + "/issuance", json={}).json()["status"] == "confirmed"
    assert db_client.post(second + "/issuance", json={}).json()["status"] == "confirmed"


def test_stored_verification_reads_file_and_ignores_cached_hash(db_client, certificate_chain, registry_engine):
    _, cert_id, endpoint = draft(db_client)
    assert db_client.post(endpoint + "/issuance", json={}).json()["status"] == "confirmed"
    with Session(registry_engine) as session:
        version = session.scalar(select(CertificateVersion).join(Certificate).where(Certificate.certificate_id == cert_id))
        version.file_hash = bytes(32)  # Make the cache wrong, not the actual file.
        session.commit()
    response = db_client.post(endpoint + "/verification/stored", json={})
    assert response.status_code == 200
    result = response.json()
    assert result["file_source"] == "platform" and result["file_result"] == "match"
    assert result["file_sha256"] == hashlib.sha256(make_pdf()).hexdigest()
    assert result["file_sha256"] == result["on_chain_sha256"]
    assert len(certificate_chain.send_calls) == 1


def test_stored_verification_detects_changed_platform_bytes(db_client, certificate_chain, registry_engine):
    _, cert_id, endpoint = draft(db_client)
    assert db_client.post(endpoint + "/issuance", json={}).json()["status"] == "confirmed"
    with Session(registry_engine) as session:
        version = session.scalar(select(CertificateVersion).join(Certificate).where(Certificate.certificate_id == cert_id))
        stored = session.get(StoredFile, version.file_id)
        path = original_path(stored.storage_key)
    changed = make_pdf().replace(b"fixture", b"changed", 1)
    path.write_bytes(changed)  # Only the isolated test's temporary file, never application originals.
    result = db_client.post(endpoint + "/verification/stored", json={}).json()
    assert result["file_result"] == "mismatch"
    assert result["file_sha256"] == hashlib.sha256(changed).hexdigest()
    assert result["on_chain_sha256"] == hashlib.sha256(make_pdf()).hexdigest()
    assert result["registration"]["status"] == "confirmed"


def test_stored_file_unavailable_is_not_mismatch(db_client, certificate_chain, monkeypatch, tmp_path):
    _, _, endpoint = draft(db_client)
    assert db_client.post(endpoint + "/issuance", json={}).json()["status"] == "confirmed"
    monkeypatch.setattr("certificates.service.original_path", lambda key: tmp_path / "absent.pdf")
    result = db_client.post(endpoint + "/verification/stored", json={}).json()
    assert result["file_result"] == "unable_to_verify"
    assert result["file_sha256"] is None
    assert result["registration"]["status"] == "confirmed"
    assert len(certificate_chain.send_calls) == 1


def test_stored_rpc_unavailable_cannot_pass(db_client, certificate_chain):
    _, _, endpoint = draft(db_client)
    assert db_client.post(endpoint + "/issuance", json={}).json()["status"] == "confirmed"
    certificate_chain.unavailable = True
    result = db_client.post(endpoint + "/verification/stored", json={}).json()
    assert result["file_result"] == "unable_to_verify"
    assert result["registration"]["status"] != "confirmed"
    assert result["file_sha256"] == hashlib.sha256(make_pdf()).hexdigest()


@pytest.mark.parametrize("field", ["file_path", "sha256", "issuer_address"])
def test_stored_verification_rejects_supplied_file_or_hash(db_client, certificate_chain, field):
    _, _, endpoint = draft(db_client)
    assert db_client.post(endpoint + "/verification/stored", json={field: "untrusted"}).status_code == 422


def test_both_verification_routes_are_read_only(db_client, certificate_chain, registry_engine):
    from sqlalchemy import func
    _, _, endpoint = draft(db_client)
    assert db_client.post(endpoint + "/issuance", json={}).json()["status"] == "confirmed"
    models = [Certificate, CertificateVersion, StoredFile, IssuanceAttempt]
    with Session(registry_engine) as session:
        before = [session.scalar(select(func.count()).select_from(model)) for model in models]
    original = db_client.get(endpoint + "/file").content
    assert db_client.post(endpoint + "/verification/stored", json={}).json()["file_result"] == "match"
    assert verify(db_client, endpoint, make_pdf("external different")).json()["file_result"] == "mismatch"
    assert db_client.get(endpoint + "/file").content == original
    with Session(registry_engine) as session:
        assert before == [session.scalar(select(func.count()).select_from(model)) for model in models]
    assert len(certificate_chain.send_calls) == 1


def test_first_issue_missing_snake_explains_refresh_and_recovers_after_registration(db_client, certificate_chain, registry_engine):
    from sqlalchemy import func
    _, _, endpoint = draft(db_client)
    certificate_chain.snake_registered = False
    original = db_client.get(endpoint + "/file").content
    response = db_client.post(endpoint + "/issuance", json={})
    assert response.status_code == 409
    assert response.json()["detail"]["code"] == "snake_not_registered"
    state = db_client.get(endpoint + "/issuance").json()
    assert state["status"] == "not_submitted" and state["transaction_hash"] is None
    assert state["error_code"] == "snake_not_registered"
    assert "Breeder" in state["error"]
    metadata = db_client.get(endpoint).json()
    assert metadata["issuance"]["error_code"] == "snake_not_registered"
    with Session(registry_engine) as session:
        assert session.scalar(select(func.count()).select_from(IssuanceAttempt).where(IssuanceAttempt.instance_id == certificate_chain.instance_id)) == 0
    assert certificate_chain.send_calls == []
    certificate_chain.snake_registered = True
    assert db_client.get(endpoint + "/issuance").json()["error_code"] is None
    state = db_client.post(endpoint + "/issuance", json={}).json()
    assert state["status"] == "confirmed"
    assert db_client.post(endpoint + "/issuance", json={}).json()["transaction_hash"] == state["transaction_hash"]
    assert len(certificate_chain.send_calls) == 1
    assert db_client.get(endpoint + "/file").content == original


@pytest.mark.parametrize("issuer_matches,authorized,registered,code", [
    (False, True, True, "issuer_wallet_mismatch"),
    (True, False, True, "laboratory_not_authorized"),
    (True, True, False, "snake_not_registered"),
])
def test_actual_adapter_identifies_each_preflight_branch(issuer_matches, authorized, registered, code):
    from unittest.mock import Mock
    chain = object.__new__(CertificateChain)
    chain.manager, chain.address = "0x" + "72" * 20, "0x" + "71" * 20
    chain.contract = Mock()
    chain.contract.functions.authorizedLaboratories.return_value.call.return_value = authorized
    chain.snakes = Mock()
    chain.snakes.address = "0x" + "73" * 20
    chain.snakes.manager_of.return_value = "0x" + "74" * 20 if registered else None
    subject = CertificateSubject("TEST-C", "BP-S001", chain.manager if issuer_matches else "0x" + "75" * 20, bytes(32))
    with pytest.raises(CertificatePreflightError) as caught:
        chain.assert_can_issue(subject)
    assert caught.value.code == code
