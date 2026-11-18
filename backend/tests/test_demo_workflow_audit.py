"""Opt-in acceptance audit using a disposable database, chain, and upload store.

Run with RUN_DEMO_WORKFLOW_AUDIT=1 and the existing database credential loaded.
No existing account credentials, session tokens, or business rows are inspected.
"""

import hashlib
import json
import os
from io import BytesIO
from pathlib import Path
import shutil
import socket
import subprocess
import time
from uuid import uuid4

from fastapi.testclient import TestClient
from PIL import Image
import psycopg
from psycopg import sql
import pytest
from web3 import Web3


ROOT = Path(__file__).resolve().parents[2]
pytestmark = pytest.mark.skipif(
    os.environ.get("RUN_DEMO_WORKFLOW_AUDIT") != "1",
    reason="Opt in to the isolated local workflow audit explicitly.",
)


@pytest.fixture
def isolated_demo(monkeypatch, tmp_path):
    from backend import certificate_files, photos
    from backend.deploy_registry import deploy_snake_registry
    from backend.main import app
    from backend.seed_participants import seed_demo_participants
    from backend.setup_certificates import setup_certificates

    node = shutil.which("node")
    if not node:
        pytest.fail("Node.js is required for the isolated Hardhat chain.")
    with socket.socket() as available:
        available.bind(("127.0.0.1", 0))
        port = available.getsockname()[1]
    process = subprocess.Popen(
        [node, str(ROOT / "contracts/node_modules/hardhat/dist/src/cli.js"),
         "node", "--hostname", "127.0.0.1", "--port", str(port)],
        cwd=ROOT / "contracts", stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    connect = psycopg.connect
    provider = Web3.HTTPProvider
    password = os.environ["DEMO_DB_PASSWORD"]
    database = "workflow_audit_" + uuid4().hex
    maintenance = None
    created = False
    try:
        chain = Web3(provider(f"http://127.0.0.1:{port}"))
        for _ in range(100):
            if chain.is_connected():
                break
            if process.poll() is not None:
                pytest.fail("Isolated Hardhat process exited during startup.")
            time.sleep(0.1)
        assert chain.is_connected(), "Isolated Hardhat node did not become ready."
        maintenance = connect(
            host="127.0.0.1", port=5433, dbname="postgres",
            user="ballpython", password=password, autocommit=True,
        )
        maintenance.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database)))
        created = True

        def audit_connect(*args, **kwargs):
            if kwargs.get("dbname") == "ballpython_demo":
                kwargs["dbname"] = database
            return connect(*args, **kwargs)

        def audit_provider(endpoint_uri=None, *args, **kwargs):
            if endpoint_uri == "http://127.0.0.1:8545":
                endpoint_uri = f"http://127.0.0.1:{port}"
            return provider(endpoint_uri, *args, **kwargs)

        monkeypatch.setattr(psycopg, "connect", audit_connect)
        monkeypatch.setattr(Web3, "HTTPProvider", audit_provider)
        monkeypatch.setattr(photos, "STORAGE_DIRECTORY", tmp_path / "uploads")
        monkeypatch.setattr(certificate_files, "STORAGE_DIRECTORY", tmp_path / "uploads")
        with audit_connect(host="127.0.0.1", port=5433, dbname="ballpython_demo",
                           user="ballpython", password=password) as connection:
            for migration in sorted((ROOT / "backend/migrations").glob("*.sql")):
                connection.execute(migration.read_text(encoding="utf-8"))
        seed_demo_participants(password=password)
        snake = deploy_snake_registry(
            rpc_url="http://127.0.0.1:8545", expected_chain_id=31337,
        )["contract_address"]
        monkeypatch.setenv("DEMO_REGISTRY_ADDRESS", snake)
        certificate = setup_certificates(password=password, snake_registry_address=snake)
        monkeypatch.setenv("DEMO_CERTIFICATE_REGISTRY_ADDRESS", certificate)
        artifact = json.loads((ROOT / "contracts/artifacts/contracts/KeeperTransfers.sol/KeeperTransfers.json").read_text())
        factory = chain.eth.contract(abi=artifact["abi"], bytecode=artifact["bytecode"])
        receipt = chain.eth.wait_for_transaction_receipt(
            factory.constructor(snake).transact({"from": chain.eth.accounts[0]})
        )
        assert receipt.status == 1
        monkeypatch.setenv("DEMO_KEEPER_TRANSFERS_ADDRESS", receipt.contractAddress)
        with TestClient(app) as client:
            yield client, chain, audit_connect
    finally:
        if maintenance is not None:
            if created:
                maintenance.execute(
                    sql.SQL("DROP DATABASE {} WITH (FORCE)").format(sql.Identifier(database))
                )
            maintenance.close()
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)


def test_complete_demo_workflow(isolated_demo, monkeypatch):
    client, chain, connect = isolated_demo
    checks = []

    def request(method, path, expected, token=None, **kwargs):
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        response = client.request(method, "/api/v1" + path, headers=headers, **kwargs)
        assert response.status_code == expected, (
            f"{method} {path}: expected {expected}, got {response.status_code}"
        )
        return response

    assert client.get("/health").status_code == 200
    assert client.get("/ready").status_code == 200
    request("GET", "/snakes/SNAKE001", 401)
    request("POST", "/accounts", 422, json={})
    sessions = {}
    for role, lab in [("breeder", None), ("buyer", None), ("lab", "LAB001"), ("lab", "LAB002")]:
        name = lab or role
        data = {
            "username": "audit_" + name, "email": name + "@audit.invalid",
            "password": "isolated-test-only", "role": role,
            "display_name": "Audit " + name, "country_or_region": "Demo",
            "demo_consent": True,
        }
        if lab:
            data["laboratory_id"] = lab
        if role == "breeder":
            data["breeder_name"] = "Audit Breeder"
        request("POST", "/accounts", 201, json=data)
        request("POST", "/accounts", 409, json=data)
        request("POST", "/sessions", 401, json={"username": data["username"], "password": "wrong"})
        sessions[name] = request("POST", "/sessions", 200,
                                 json={"username": data["username"], "password": data["password"]}).json()
        request("GET", "/sessions/current", 200, sessions[name]["access_token"])
    checks.append("account registration, conflicts, login, invalid credentials, authenticated identity")
    breeder, buyer, lab1, lab2 = [sessions[k]["access_token"] for k in ("breeder", "buyer", "LAB001", "LAB002")]
    image = BytesIO()
    Image.new("RGB", (32, 32), "gold").save(image, format="PNG")
    profile = {
        "snake_id": "SNAKE001", "breeder_internal_id": "AUDIT-001",
        "species": "Ball Python", "sex": "Female", "date_of_birth": "2025-01-01",
        "genetic_description": "Fictional isolated test", "nickname": "Audit snake",
    }
    upload = {"data": {"profile_json": json.dumps(profile)},
              "files": {"photo": ("audit.png", image.getvalue(), "image/png")}}
    request("POST", "/snakes", 403, buyer, **upload)
    request("POST", "/snakes", 201, breeder, **upload)
    request("POST", "/snakes", 409, breeder, **upload)
    request("GET", "/snakes/SNAKE001", 200, buyer)
    request("GET", "/snakes/MISSING", 404, buyer)
    request("GET", "/snakes/SNAKE001/photo", 200, buyer)
    request("GET", "/snakes/random-profiles", 200, buyer)
    request("GET", "/snakes/showcase-images", 200)
    checks.append("snake registration, duplicate guard, profile, photo, random previews, missing profile")
    pdf1, pdf2 = b"%PDF-1.4\nAudit original\n%%EOF", b"%PDF-1.4\nAudit revision\n%%EOF"

    def report(token, content=pdf1):
        return request("POST", "/certificate-series", 201, token,
                       data={"snake_id": "SNAKE001", "title": "Audit report"},
                       files={"pdf": ("audit.pdf", content, "application/pdf")}).json()

    request("POST", "/certificate-series", 403, buyer,
            data={"snake_id": "SNAKE001", "title": "Denied"}, files={"pdf": ("audit.pdf", pdf1)})
    request("POST", "/certificate-series", 422, lab1,
            data={"snake_id": "SNAKE001", "title": "Invalid"}, files={"pdf": ("bad.pdf", b"not a PDF")})
    first, second = report(lab1), report(lab2)
    revision_path = f"/certificate-series/{first['series_id']}/versions"
    request("POST", revision_path, 403, lab2, files={"pdf": ("revision.pdf", pdf2)})
    revised = request("POST", revision_path, 201, lab1,
                      files={"pdf": ("revision.pdf", pdf2)}).json()
    assert revised["version_number"] == 2
    history = request("GET", "/snakes/SNAKE001/certificate-series", 200, buyer).json()
    versions = [v for series in history["series"] for v in series["versions"]]
    assert len(versions) == 3
    assert all(v["evidence_status"] == "confirmed" for v in versions)
    assert sorted(v["status"] for v in versions) == ["current", "current", "superseded"]
    for version in versions:
        response = request("GET", f"/certificate-versions/{version['version_id']}/file", 200, buyer)
        assert hashlib.sha256(response.content).hexdigest() == version["file_hash"]
    checks.append("both laboratories issue, issuer-only revision, confirmed version history, original PDF hashes")
    inputs = {
        "growth": {"weight_g": 150, "length_cm": 30, "notes": "Audit"},
        "shedding": {"outcome": "Complete", "follow_up": "Audit"},
        "feeding": {"food": "Mouse", "feeding_outcome": "Accepted", "notes": "Audit"},
        "health": {"event": "Observation", "status": "Normal", "follow_up": "Audit"},
    }
    retained = {}
    for kind, values in inputs.items():
        path = f"/snakes/SNAKE001/husbandry/{kind}"
        body = {"data": {"record_date": "2026-11-19", **values}}
        request("POST", path, 403, buyer, json=body)
        request("POST", path, 403, lab1, json=body)
        row = request("POST", path, 201, breeder, json=body).json()
        request("PUT", path + f"/{row['record_id']}", 200, breeder, json=body)
        request("DELETE", path + f"/{row['record_id']}", 204, breeder)
        retained[kind] = request("POST", path, 201, breeder, json=body).json()["record_id"]
    checks.append("four husbandry types: breeder add/edit/delete, buyer and laboratory permission denial")

    def transfer():
        return request("POST", "/snakes/SNAKE001/keeper-transfers", 201, breeder,
                       json={"recipient_username": "audit_buyer"}).json()["transfer_id"]

    request("GET", "/snakes/SNAKE001/keeper", 200, buyer)
    tid = transfer()
    request("POST", f"/keeper-transfers/{tid}/accept", 403, breeder)
    request("POST", f"/keeper-transfers/{tid}/reject", 200, buyer)
    tid = transfer()
    request("POST", f"/keeper-transfers/{tid}/cancel", 200, breeder)
    tid = transfer()
    request("POST", "/snakes/SNAKE001/keeper-transfers", 409, breeder,
            json={"recipient_username": "audit_buyer"})
    request("POST", f"/keeper-transfers/{tid}/accept", 200, buyer)
    state = request("GET", "/snakes/SNAKE001/keeper", 200, buyer).json()
    assert state["current_keeper"]["participant_id"] == "BUYER001"
    checks.append("keeper status, recipient-only accept/reject, cancellation, duplicate pending guard, accepted transfer")
    for kind, values in inputs.items():
        path = f"/snakes/SNAKE001/husbandry/{kind}"
        body = {"data": {"record_date": "2026-11-19", **values}}
        request("POST", path, 403, breeder, json=body)
        request("DELETE", path + f"/{retained[kind]}", 403, buyer)
        request("PUT", path + f"/{retained[kind]}", 403, buyer, json=body)
        row = request("POST", path, 201, buyer, json=body).json()
        request("PUT", path + f"/{row['record_id']}", 200, buyer, json=body)
        request("DELETE", path + f"/{row['record_id']}", 204, buyer)
        assert len(request("GET", path, 200, buyer).json()) == 1
    checks.append("post-transfer rights, buyer CRUD, retained original-author protection")

    from streamlit.testing.v1 import AppTest
    import requests
    from urllib.parse import urlsplit

    methods = []

    def transport(method, url, **kwargs):
        methods.append(method.upper())
        kwargs.pop("timeout", None)
        parsed = urlsplit(url)
        return client.request(method, parsed.path + ("?" + parsed.query if parsed.query else ""), **kwargs)

    with monkeypatch.context() as ui:
        ui.setattr(requests, "request", transport)
        for method in ("get", "post", "put", "delete"):
            ui.setattr(requests, method, lambda url, _method=method, **kwargs: transport(_method, url, **kwargs))
        login = AppTest.from_file(str(ROOT / "frontend/app.py"), default_timeout=30).run()
        assert not login.exception
        for name in ("breeder", "buyer", "LAB001", "LAB002"):
            at = AppTest.from_file(str(ROOT / "frontend/app.py"), default_timeout=30)
            at.session_state["auth_session"] = sessions[name]
            at.run()
            assert not at.exception, f"{name} workspace crashed"
            if name in ("buyer", "breeder"):
                assert not any(s.value == "Husbandry Records" for s in at.subheader)
                at.button(key="view_profile").click().run()
                assert not at.exception, f"{name} profile crashed"
                assert [tab.label for tab in at.tabs][:3] == ["Certificate History", "Keeper Management", "Husbandry Records"]
                if name == "buyer":
                    at.session_state["husbandry_section_SNAKE001"]["blocked"].add("growth")
                    at.run()
                    assert any(b.label == "Add Record" and b.disabled for b in at.button)
                    at.button(key="refresh_husbandry_SNAKE001").click().run()
                    assert not at.exception
                    assert not at.session_state["husbandry_section_SNAKE001"]["blocked"]
                    assert all(not b.disabled for b in at.button if b.label == "Add Record")
            else:
                assert [tab.label for tab in at.tabs] == ["New Report", "Revise Report"]
            at.run()
            assert not at.exception
        assert not any(method != "GET" for method in methods), "A render or lookup triggered a write."
    checks.append("real frontend/backend role rendering and profile tabs; reruns and lookups issue no writes")
    checks.append("husbandry uncertain-write lock persists until an explicit successful refresh")
    block_before = chain.eth.block_number
    with monkeypatch.context() as missing:
        missing.setenv("DEMO_REGISTRY_ADDRESS", "")
        response = request("POST", "/snakes", 503, breeder, **upload)
        assert response.json()["outcome"] == "not_submitted"
    with monkeypatch.context() as missing:
        missing.setenv("DEMO_CERTIFICATE_REGISTRY_ADDRESS", "")
        response = request("POST", "/certificate-series", 503, lab1,
                           data={"snake_id": "SNAKE001", "title": "Unavailable"},
                           files={"pdf": ("audit.pdf", pdf1)})
        assert response.json()["outcome"] == "not_submitted"
        history = request("GET", "/snakes/SNAKE001/certificate-series", 200, buyer).json()
        unavailable = [v for series in history["series"] for v in series["versions"]]
        assert history["warnings"]
        assert all(v["status"] is None and v["evidence_status"] == "unavailable" for v in unavailable)
        request("GET", f"/certificate-versions/{first['version_id']}/file", 200, buyer)
    with monkeypatch.context() as missing:
        missing.setenv("DEMO_KEEPER_TRANSFERS_ADDRESS", "")
        request("POST", "/snakes/SNAKE001/husbandry/growth", 503, buyer,
                json={"data": {"record_date": "2026-11-19", **inputs["growth"]}})
        state = request("GET", "/snakes/SNAKE001/keeper", 200, buyer).json()
        assert state["transfer_status"] == "unable_to_confirm"
    assert chain.eth.block_number == block_before
    checks.append("missing contract configurations fail safely without transactions or false success; archived PDFs remain downloadable")
    request("DELETE", "/sessions/current", 204, buyer)
    request("GET", "/sessions/current", 401, buyer)
    with connect(host="127.0.0.1", port=5433, dbname="ballpython_demo", user="ballpython",
                 password=os.environ["DEMO_DB_PASSWORD"], autocommit=True) as connection:
        connection.execute("UPDATE login_sessions SET expires_at=CURRENT_TIMESTAMP - INTERVAL '1 second' WHERE account_id=(SELECT account_id FROM user_accounts WHERE username='audit_LAB002')")
    request("GET", "/sessions/current", 401, lab2)
    checks.append("logout revocation and expired session rejection")
    for check in checks:
        print("PASS:", check)
