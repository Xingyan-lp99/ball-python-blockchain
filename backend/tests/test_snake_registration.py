import os
import subprocess
import sys
import socket
import time
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from uuid import uuid4

import pytest
import httpx
from fastapi.testclient import TestClient
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, OperationalError

from database import get_session
from identity import get_current_breeder_id
from main import app
from migrate import migrate

ENDPOINT = "/api/v1/snakes"


@pytest.fixture
def validation_client():
    def no_database():
        yield None

    app.dependency_overrides[get_session] = no_database
    try:
        with TestClient(app) as client:
            yield client
    finally:
        app.dependency_overrides.clear()


@pytest.mark.parametrize("payload", [
    {"snake_id": "", "sex": "male"},
    {"snake_id": " \t\n", "sex": "male"},
    {"snake_id": "S-invalid", "sex": "invalid"},
    {"snake_id": "S-invalid", "sex": None},
    {"snake_id": "S-invalid"},
    {"sex": "unknown"},
    {"snake_id": None, "sex": "unknown"},
    {"snake_id": "S-invalid", "sex": "female", "date_of_birth": "not-a-date"},
    {"snake_id": "S-invalid", "sex": "female", "date_of_birth":
     (datetime.now(timezone.utc).date() + timedelta(days=1)).isoformat()},
    {"snake_id": "S-invalid", "sex": "male", "breeder_id": "ATTACKER"},
    {"snake_id": "S-invalid", "sex": "male", "current_manager_id": "ATTACKER"},
    {"snake_id": "S-invalid", "sex": "male", "created_at": "2020-01-01T00:00:00Z"},
    {"snake_id": "S-invalid", "sex": "male", "registration_status": "confirmed"},
])
def test_invalid_input(validation_client, payload):
    assert validation_client.post(ENDPOINT, json=payload).status_code == 422


def test_database_error_is_sanitized(validation_client, monkeypatch):
    def fail(*args):
        raise OperationalError("secret SQL", {}, Exception("secret password"))

    monkeypatch.setattr("snake_registry.routes.register_snake", fail)
    response = validation_client.post(ENDPOINT, json={"snake_id": "S1", "sex": "unknown"})
    assert response.status_code == 503
    assert response.json() == {"detail": "Database unavailable"}


def test_register_query_duplicate_and_database(db_client, registry_engine):
    snake_id = f"S-{uuid4().hex}"
    payload = {
        "snake_id": snake_id, "name": "Amber", "sex": "female",
        "date_of_birth": "2025-06-15", "breeder_internal_id": "clutch-17",
        "morph_description": "Breeder-reported Pastel",
    }
    response = db_client.post(ENDPOINT, json=payload)
    assert response.status_code == 201
    profile = response.json()
    assert all(profile[key] == value for key, value in payload.items())
    assert profile["breeder_id"] == profile["current_manager_id"] == "BR001"
    created_at = datetime.fromisoformat(profile["created_at"].replace("Z", "+00:00"))
    assert created_at.tzinfo is not None
    assert abs((datetime.now(timezone.utc) - created_at).total_seconds()) < 60
    assert profile["registration_status"] == "not_submitted"
    assert profile["certificate_status"] == "not_verified"
    assert db_client.get(f"{ENDPOINT}/{snake_id}").json() == profile
    assert db_client.post(ENDPOINT, json=payload).status_code == 409
    assert db_client.get(f"{ENDPOINT}/{snake_id}").json() == profile
    with registry_engine.connect() as connection:
        row = connection.execute(
            text("SELECT * FROM snakes WHERE snake_id = :id"), {"id": snake_id}
        ).mappings().one()
        assert row["name"] == "Amber"
        assert row["breeder_id"] == row["current_manager_id"] == "BR001"


@pytest.mark.parametrize("sex", ["male", "female", "unknown"])
def test_optional_fields_and_trimmed_id(db_client, sex):
    snake_id = f"S-{uuid4().hex}"
    response = db_client.post(ENDPOINT, json={"snake_id": f" {snake_id} ", "sex": sex})
    assert response.status_code == 201
    profile = response.json()
    assert profile["snake_id"] == snake_id
    for key in ["name", "date_of_birth", "breeder_internal_id", "morph_description"]:
        assert profile[key] is None
    assert db_client.post(ENDPOINT, json={"snake_id": snake_id, "sex": sex}).status_code == 409


def test_missing_snake(db_client):
    assert db_client.get(f"{ENDPOINT}/missing-{uuid4().hex}").status_code == 404


def test_identity_comes_from_server_context(db_client):
    app.dependency_overrides[get_current_breeder_id] = lambda: "BR-test-context"
    response = db_client.post(ENDPOINT, json={"snake_id": uuid4().hex, "sex": "unknown"})
    assert response.status_code == 201
    assert response.json()["breeder_id"] == "BR-test-context"
    assert response.json()["current_manager_id"] == "BR-test-context"


@pytest.mark.parametrize("values", [
    {"snake_id": "", "sex": "male", "dob": None},
    {"snake_id": "  ", "sex": "male", "dob": None},
    {"snake_id": "DB-invalid", "sex": "invalid", "dob": None},
    {"snake_id": "DB-invalid", "sex": "male", "dob":
     datetime.now(timezone.utc).date() + timedelta(days=1)},
])
def test_database_constraints(registry_engine, values):
    with pytest.raises(IntegrityError):
        with registry_engine.begin() as connection:
            connection.execute(text("""
                INSERT INTO snakes (id, snake_id, sex, date_of_birth, breeder_id, current_manager_id)
                VALUES (:id, :snake_id, :sex, :dob, 'BR001', 'BR001')
            """), {"id": uuid4(), **values})


def test_migration_is_repeatable(db_client, registry_engine):
    snake_id = uuid4().hex
    assert db_client.post(ENDPOINT, json={"snake_id": snake_id, "sex": "unknown"}).status_code == 201
    migrate(registry_engine)
    assert db_client.get(f"{ENDPOINT}/{snake_id}").status_code == 200
    with registry_engine.connect() as connection:
        assert connection.scalar(text("SELECT count(*) FROM schema_migrations")) == 2


def test_persistence_after_http_application_restart(registry_engine):
    snake_id = uuid4().hex
    with registry_engine.connect() as connection:
        schema = connection.scalar(text("SELECT current_schema()"))
    registry_engine.dispose()
    environment = os.environ.copy()
    environment["DATABASE_URL"] = registry_engine.url.update_query_dict(
        {"options": f"-csearch_path={schema}"}
    ).render_as_string(hide_password=False)
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        port = listener.getsockname()[1]

    @contextmanager
    def running_app():
        process = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", str(port)],
            env=environment, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        try:
            with httpx.Client(base_url=f"http://127.0.0.1:{port}", timeout=3, trust_env=False) as client:
                deadline = time.monotonic() + 15
                while True:
                    assert process.poll() is None, "HTTP application exited before becoming ready"
                    try:
                        if client.get("/api/v1/health").status_code == 200:
                            break
                    except httpx.TransportError:
                        pass
                    assert time.monotonic() < deadline, "HTTP application startup timed out"
                    time.sleep(0.1)
                yield client
        finally:
            process.terminate()
            process.wait(timeout=10)

    with running_app() as client:
        response = client.post(ENDPOINT, json={"snake_id": snake_id, "sex": "unknown"})
        assert response.status_code == 201
        expected = response.json()
    # Start Uvicorn again on the same database, after the original process exited.
    with running_app() as client:
        response = client.get(f"{ENDPOINT}/{snake_id}")
        assert response.status_code == 200
        assert response.json() == expected
