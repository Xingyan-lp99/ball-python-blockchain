"""Opt-in real HTTP/database/Hardhat version history, without chain resets."""
import hashlib
import os

import pytest
from sqlalchemy import text

from certificates.local_chain import CertificateChain, VersionedCertificateChain
from pdf_fixtures import test_pdf as make_pdf
from test_certificate_e2e import create_draft, document_directory
from test_local_chain_e2e import live_client

pytestmark = pytest.mark.skipif(os.getenv("RUN_LOCAL_CHAIN_TESTS") != "1", reason="Requires existing local deployments")


def test_actual_separate_history_append_pending_recovery_and_verification(live_client, registry_engine):
    client, _ = live_client
    snake, certificate, legacy = create_draft(client)
    old = client.post(legacy + "/issuance", json={}).json()
    assert old["status"] == "confirmed"
    base = f"/api/v1/certificates/{certificate}"
    response = client.post(base + "/histories", json={})
    assert response.status_code == 201, response.text
    history = response.json()["history_id"]
    params = {"history_id": history}
    first = client.post(legacy + "/issuance", json={}, params=params).json()
    assert first["status"] == "confirmed"
    assert first["contract_address"] != old["contract_address"] and first["block_number"] > old["block_number"]
    original = make_pdf("TEST ONLY V2 original")
    modified = original.replace(b"original", b"modified", 1)
    assert modified != original
    response = client.post(base + f"/histories/{history}/versions", files={"file": ("TEST_ONLY_v2.pdf", original, "application/pdf")})
    assert response.status_code == 201, response.text
    chain = VersionedCertificateChain()
    chain.validate_scope()
    chain.web3.provider.make_request("evm_setAutomine", [False])
    try:
        endpoint = base + "/versions/2/issuance"
        pending = client.post(endpoint, json={}, params=params).json()
        assert pending["status"] == "processing" and pending["transaction_hash"]
        assert chain.latest_version(certificate) == 1
        assert client.post(legacy + "/verification/stored", json={}, params=params).json()["version_status"] == "latest"
        with registry_engine.begin() as connection:
            connection.execute(text("UPDATE certificate_issuance_attempts SET transaction_hash=NULL,status='prepared' WHERE transaction_hash=:hash"), {"hash": pending["transaction_hash"]})
        assert client.get(endpoint, params=params).json()["transaction_hash"] == pending["transaction_hash"]
        assert client.post(endpoint, json={}, params=params).json()["transaction_hash"] == pending["transaction_hash"]
        chain.web3.provider.make_request("evm_mine", [])
        assert client.get(endpoint, params=params).json()["status"] == "confirmed"
    finally:
        chain.web3.provider.make_request("evm_setAutomine", [True])
    record = chain.contract.functions.getVersion(certificate, 2).call()
    assert record[0] == snake and record[1] == chain.manager and record[2] == 2
    assert bytes(record[3]) == hashlib.sha256(original).digest()
    assert chain.latest_version(certificate) == 2
    assert CertificateChain().record(certificate)["file_hash"] == hashlib.sha256(make_pdf()).digest()
    first_result = client.post(legacy + "/verification/stored", json={}, params=params).json()
    assert (first_result["file_result"], first_result["version_status"]) == ("match", "superseded")
    endpoint = base + "/versions/2"
    second_result = client.post(endpoint + "/verification/stored", json={}, params=params).json()
    assert (second_result["file_result"], second_result["version_status"]) == ("match", "latest")
    assert client.get(endpoint + "/file", params=params).content == original
    for filename, content, expected in [("renamed.pdf", original, "match"), ("TEST_ONLY_v2.pdf", modified, "mismatch")]:
        result = client.post(endpoint + "/verification", params=params, files={"file": (filename, content, "application/pdf")}).json()
        assert result["file_result"] == expected and result["version_status"] == "latest"
    assert client.get(legacy).json()["issuance"]["transaction_hash"] == old["transaction_hash"]
    assert client.get(base + "/histories").json()["default_version"] == 2
