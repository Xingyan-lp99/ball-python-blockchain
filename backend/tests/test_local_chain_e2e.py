"""Opt-in real HTTP/Streamlit/PostgreSQL/Hardhat checks. Never reset the chain."""

import os
import socket
import subprocess
import sys
import time
from pathlib import Path
from uuid import uuid4

import httpx
import pytest
from sqlalchemy import text

from snake_registry.local_chain import ChainStale, LocalChain

pytestmark = pytest.mark.skipif(
    os.getenv("RUN_LOCAL_CHAIN_TESTS") != "1",
    reason="Real Hardhat checks require RUN_LOCAL_CHAIN_TESTS=1 and an existing local deployment",
)


@pytest.fixture
def live_client(registry_engine):
    with registry_engine.connect() as connection:
        schema = connection.scalar(text("SELECT current_schema()"))
    environment = os.environ.copy()
    environment["DATABASE_URL"] = registry_engine.url.update_query_dict(
        {"options": f"-csearch_path={schema}"}
    ).render_as_string(hide_password=False)
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        port = listener.getsockname()[1]
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", str(port)],
        env=environment, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    try:
        with httpx.Client(base_url=f"http://127.0.0.1:{port}", timeout=15, trust_env=False) as client:
            for _ in range(100):
                assert process.poll() is None, "Test API exited during startup"
                try:
                    if client.get("/api/v1/health").status_code == 200:
                        break
                except httpx.TransportError:
                    pass
                time.sleep(0.1)
            else:
                pytest.fail("Test API startup timed out")
            yield client, f"http://127.0.0.1:{port}"
    finally:
        process.terminate()
        process.wait(timeout=10)


def test_streamlit_to_actual_contract(live_client):
    client, base_url = live_client
    chain = LocalChain()
    chain.validate_scope()
    root = Path(__file__).resolve().parents[2]
    frontend_python = root / "frontend/.venv/Scripts/python.exe"
    if not frontend_python.exists():
        frontend_python = root / "frontend/.venv/bin/python"
    assert frontend_python.exists(), "Existing frontend uv environment is required for the full UI test"
    snake_id = "E2E-" + uuid4().hex
    environment = os.environ.copy()
    environment.update(API_BASE_URL=base_url, E2E_SNAKE_ID=snake_id, E2E_APP=str(root / "frontend/main.py"))
    result = subprocess.run([str(frontend_python), "-c", """
import os
from streamlit.testing.v1 import AppTest
app = AppTest.from_file(os.environ['E2E_APP'], default_timeout=20).run()
app.text_input[0].set_value(os.environ['E2E_SNAKE_ID'])
app.button[1].click().run()
assert not app.exception and app.success
next(button for button in app.button if button.label == 'Submit local-chain registration').click().run()
assert not app.exception
assert any('Confirmed on the current local Hardhat chain' in item.value for item in app.success)
"""], env=environment, capture_output=True, timeout=45,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    assert result.returncode == 0, "Live Streamlit registration flow failed"
    profile = client.get(f"/api/v1/snakes/{snake_id}").json()
    state = profile["chain_registration"]
    assert state["status"] == "confirmed"
    assert state["chain_check"] == "verified"
    receipt = chain.web3.eth.get_transaction_receipt(state["transaction_hash"])
    assert receipt["status"] == 1
    assert chain.contract.functions.managerOf(snake_id).call() == chain.manager
    events = chain.contract.events.SnakeRegistered().process_receipt(receipt)
    assert events[0]["args"]["snakeId"] == snake_id
    assert events[0]["args"]["manager"] == chain.manager
    assert client.post(f"/api/v1/snakes/{snake_id}/registration", json={}).json()["transaction_hash"] == state["transaction_hash"]
    evidence = {"snake_id": snake_id, **state}
    # Evidence contains public chain metadata only. Do not print environment variables.
    print("LIVE_CHAIN_EVIDENCE", evidence)


def test_real_pending_transaction_and_poll(live_client, registry_engine):
    client, _ = live_client
    chain = LocalChain()
    snake_id = "PENDING-" + uuid4().hex
    assert client.post("/api/v1/snakes", json={"snake_id": snake_id, "sex": "unknown"}).status_code == 201
    endpoint = f"/api/v1/snakes/{snake_id}/registration"
    chain.web3.provider.make_request("evm_setAutomine", [False])
    try:
        response = client.post(endpoint, json={})
        assert response.status_code == 200
        state = response.json()
        assert state["status"] == "processing"
        assert state["transaction_hash"]
        # Simulate losing the hash write while the real transaction is pending.
        # Only this test's row in its isolated schema is changed.
        with registry_engine.begin() as connection:
            connection.execute(text("""
                UPDATE snake_registration_attempts
                SET transaction_hash = NULL, status = 'prepared'
                WHERE transaction_hash = :hash
            """), {"hash": state["transaction_hash"]})
        recovered = client.get(endpoint).json()
        assert recovered["status"] == "processing"
        assert recovered["transaction_hash"] == state["transaction_hash"]
        assert client.post(endpoint, json={}).json()["transaction_hash"] == state["transaction_hash"]
        chain.web3.provider.make_request("evm_mine", [])
        assert client.get(endpoint).json()["status"] == "confirmed"
        assert chain.manager_of(snake_id) == chain.manager
    finally:
        chain.web3.provider.make_request("evm_setAutomine", [True])


def test_real_conflicting_manager(live_client):
    client, _ = live_client
    chain = LocalChain()
    snake_id = "CONFLICT-" + uuid4().hex
    other = chain.web3.eth.accounts[1]
    transaction_hash = chain.contract.functions.register(snake_id).transact({"from": other})
    assert chain.web3.eth.wait_for_transaction_receipt(transaction_hash)["status"] == 1
    assert client.post("/api/v1/snakes", json={"snake_id": snake_id, "sex": "unknown"}).status_code == 201
    assert client.post(f"/api/v1/snakes/{snake_id}/registration", json={}).status_code == 409
    assert chain.manager_of(snake_id) == other
    assert client.get(f"/api/v1/snakes/{snake_id}").status_code == 200


@pytest.mark.parametrize("mismatch", ["instance", "code", "block"])
def test_real_chain_rejects_wrong_deployment_evidence(mismatch):
    chain = LocalChain()
    if mismatch == "instance":
        chain.instance_id = "0x" + "ff" * 32
    elif mismatch == "code":
        chain.deployment["runtime_code_hash"] = "0x" + "ff" * 32
    else:
        chain.deployment["deployment_block_hash"] = "0x" + "ff" * 32
    with pytest.raises(ChainStale):
        chain.validate_scope()
