import hashlib
import os
import subprocess
from pathlib import Path
from uuid import uuid4

import pytest
from sqlalchemy import text
from web3.exceptions import ContractLogicError

from certificates.local_chain import CertificateChain, CertificateSubject
from pdf_fixtures import test_pdf as make_pdf
from test_local_chain_e2e import live_client

pytestmark = pytest.mark.skipif(os.getenv("RUN_LOCAL_CHAIN_TESTS") != "1",
                              reason="Certificate real-chain tests require an existing local certificate deployment and RUN_LOCAL_CHAIN_TESTS=1")


@pytest.fixture(autouse=True)
def document_directory(monkeypatch, tmp_path):
    monkeypatch.setenv("CERTIFICATE_STORAGE_DIR", str(tmp_path / "certificate-files"))


def create_draft(client):
    snake_id, certificate_id = "TEST-CERT-S-" + uuid4().hex, "TEST-V1-" + uuid4().hex
    assert client.post("/api/v1/snakes", json={"snake_id": snake_id, "sex": "unknown"}).status_code == 201
    state = client.post(f"/api/v1/snakes/{snake_id}/registration", json={})
    assert state.status_code == 200 and state.json()["status"] == "confirmed"
    response = client.post("/api/v1/certificates", data={"certificate_id": certificate_id, "snake_id": snake_id},
                           files={"file": ("TEST_ONLY_original_v1.pdf", make_pdf(), "application/pdf")})
    assert response.status_code == 201, response.json()
    return snake_id, certificate_id, f"/api/v1/certificates/{certificate_id}/versions/1"


def test_actual_upload_issuance_independent_verification_and_download(live_client):
    client, _ = live_client
    snake_id, certificate_id, endpoint = create_draft(client)
    original = make_pdf()
    modified = original.replace(b"fixture", b"changed", 1)  # Derive from THIS V1; keep PDF offsets intact.
    assert modified != original
    state = client.post(endpoint + "/issuance", json={})
    assert state.status_code == 200, state.json()
    state = state.json()
    assert state["status"] == "confirmed"
    assert client.post(endpoint + "/issuance", json={}).json()["transaction_hash"] == state["transaction_hash"]
    chain = CertificateChain()
    chain.validate_scope()
    assert chain.manager.lower() != chain.snakes.manager.lower()
    record = chain.contract.functions.getVersion(certificate_id, 1).call()
    assert record[0] == snake_id and record[1] == chain.manager and record[2] == 1
    assert bytes(record[3]) == hashlib.sha256(original).digest()
    receipt = chain.receipt(state["transaction_hash"])
    assert receipt["status"] == 1
    chain.verify_success(CertificateSubject(certificate_id, snake_id, chain.manager, record[3]), state["transaction_hash"], receipt)
    for filename, content, expected in [
        ("TEST_ONLY_original_v1.pdf", original, "match"), ("renamed.pdf", original, "match"),
        ("TEST_ONLY_original_v1.pdf", modified, "mismatch"), ("renamed.pdf", modified, "mismatch"),
    ]:
        result = client.post(endpoint + "/verification", files={"file": (filename, content, "application/pdf")})
        assert result.status_code == 200
        assert result.json()["file_result"] == expected
        assert result.json()["registration"]["status"] == "confirmed"
        assert result.json()["on_chain_sha256"] == hashlib.sha256(original).hexdigest()
    assert client.get(endpoint + "/file").content == original
    stored_result = client.post(endpoint + "/verification/stored", json={})
    assert stored_result.status_code == 200
    assert stored_result.json()["file_source"] == "platform"
    assert stored_result.json()["file_result"] == "match"
    assert stored_result.json()["file_sha256"] == hashlib.sha256(original).hexdigest()
    # Exercise the primary buyer page against the actual HTTP API, without file upload.
    root = Path(__file__).resolve().parents[2]
    frontend_python = root / "frontend/.venv/Scripts/python.exe"
    if not frontend_python.exists():
        frontend_python = root / "frontend/.venv/bin/python"
    environment = os.environ.copy()
    environment.update(API_BASE_URL=live_client[1], E2E_BUYER_SNAKE_ID=snake_id, E2E_BUYER_CERTIFICATE_ID=certificate_id)
    nonce_before = chain.web3.eth.get_transaction_count(chain.manager)
    result = subprocess.run([str(frontend_python), "-c", """
import os
from streamlit.testing.v1 import AppTest
app = AppTest.from_file('main.py', default_timeout=20).run()
app.radio[0].set_value('Buyer').run()
app.text_input[0].set_value(os.environ['E2E_BUYER_SNAKE_ID'])
next(button for button in app.button if button.label == '查询球蟒档案').click().run()
assert not app.exception
assert app.selectbox[0].value == os.environ['E2E_BUYER_CERTIFICATE_ID']
next(button for button in app.button if button.label == '核验证书').click().run()
assert not app.exception
assert any('平台保存的 PDF' in item.value and 'matches this registered V1' in item.value for item in app.success)
"""], cwd=root / "frontend", env=environment, capture_output=True, timeout=60,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    assert result.returncode == 0, "Real buyer profile/list/direct-verification page flow failed"
    assert chain.web3.eth.get_transaction_count(chain.manager) == nonce_before
    repeat = client.post("/api/v1/certificates", data={"certificate_id": certificate_id, "snake_id": snake_id},
                         files={"file": ("renamed.pdf", original, "application/pdf")})
    assert repeat.status_code == 200 and repeat.json()["issuance"]["status"] == "confirmed"
    with pytest.raises(ContractLogicError):
        chain.contract.functions.issueV1(certificate_id, snake_id, hashlib.sha256(modified).digest()).call({"from": chain.manager})


def test_actual_pending_issuance_recovers_missing_hash(live_client, registry_engine):
    client, _ = live_client
    snake_id, certificate_id, endpoint = create_draft(client)
    chain = CertificateChain()
    chain.web3.provider.make_request("evm_setAutomine", [False])
    try:
        state = client.post(endpoint + "/issuance", json={}).json()
        assert state["status"] == "processing" and state["transaction_hash"]
        with registry_engine.begin() as connection:
            connection.execute(text("UPDATE certificate_issuance_attempts SET transaction_hash=NULL,status='prepared' WHERE transaction_hash=:hash"),
                               {"hash": state["transaction_hash"]})
        recovered = client.get(endpoint + "/issuance").json()
        assert recovered["status"] == "processing" and recovered["transaction_hash"] == state["transaction_hash"]
        assert client.post(endpoint + "/issuance", json={}).json()["transaction_hash"] == state["transaction_hash"]
        result = client.post(endpoint + "/verification", files={"file": ("fixture.pdf", make_pdf(), "application/pdf")}).json()
        assert result["file_result"] == "unable_to_verify"
        chain.web3.provider.make_request("evm_mine", [])
        assert client.get(endpoint + "/issuance").json()["status"] == "confirmed"
        assert chain.record(certificate_id)["snake_id"] == snake_id
    finally:
        chain.web3.provider.make_request("evm_setAutomine", [True])


def test_actual_unauthorized_wallet_and_unregistered_snake_are_rejected():
    chain = CertificateChain()
    digest = hashlib.sha256(make_pdf()).digest()
    with pytest.raises(ContractLogicError):
        chain.contract.functions.issueV1("TEST-UNAUTHORIZED-" + uuid4().hex, "TEST-S", digest).call({"from": chain.snakes.manager})
    with pytest.raises(ContractLogicError):
        chain.contract.functions.issueV1("TEST-MISSING-" + uuid4().hex, "MISSING-" + uuid4().hex, digest).call({"from": chain.manager})


def test_first_issuance_reports_missing_snake_then_normal_registration_unblocks(live_client, registry_engine):
    client, _ = live_client
    snake_id, certificate_id = "TEST-PREREQ-" + uuid4().hex, "TEST-PREREQ-C-" + uuid4().hex
    assert client.post("/api/v1/snakes", json={"snake_id": snake_id, "sex": "unknown"}).status_code == 201
    response = client.post("/api/v1/certificates", data={"certificate_id": certificate_id, "snake_id": snake_id},
                           files={"file": ("TEST_ONLY.pdf", make_pdf(), "application/pdf")})
    assert response.status_code == 201
    assert response.json()["issuance"]["error_code"] == "snake_not_registered"
    endpoint = f"/api/v1/certificates/{certificate_id}/versions/1"
    chain = CertificateChain()
    nonce = chain.web3.eth.get_transaction_count(chain.manager)
    assert chain.contract.functions.authorizedLaboratories(chain.manager).call()
    assert chain.snakes.manager_of(snake_id) is None
    refused = client.post(endpoint + "/issuance", json={})
    assert refused.status_code == 409 and refused.json()["detail"]["code"] == "snake_not_registered"
    state = client.get(endpoint + "/issuance").json()
    assert state["status"] == "not_submitted" and state["transaction_hash"] is None
    assert state["error_code"] == "snake_not_registered"
    assert chain.web3.eth.get_transaction_count(chain.manager) == nonce
    registered = client.post(f"/api/v1/snakes/{snake_id}/registration", json={})
    assert registered.status_code == 200 and registered.json()["status"] == "confirmed"
    assert client.get(endpoint + "/issuance").json()["error_code"] is None
    issued = client.post(endpoint + "/issuance", json={})
    assert issued.status_code == 200 and issued.json()["status"] == "confirmed"
    assert chain.record(certificate_id)["snake_id"] == snake_id
    assert client.post(endpoint + "/issuance", json={}).json()["transaction_hash"] == issued.json()["transaction_hash"]
    assert chain.web3.eth.get_transaction_count(chain.manager) == nonce + 1
    assert client.get(endpoint + "/file").content == make_pdf()
