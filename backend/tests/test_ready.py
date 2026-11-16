from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from backend.main import app


# Purpose: verify the successful readiness response.
# Workflow: Day 1, readiness response validation.
# Removing this test loses coverage of the successful HTTP contract.
def test_ready_returns_ok(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DEMO_DB_PASSWORD", "test-password")

    with patch(
        "backend.main.check_database_connection",
        return_value=True,
    ) as database_check:
        with TestClient(app) as client:
            response = client.get("/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "ok"}
    database_check.assert_called_once()


# Purpose: verify that database failure returns a safe 503 response.
# Workflow: Day 1, readiness failure validation.
# Removing this test loses coverage of database-unavailable handling.
def test_ready_returns_503_on_database_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("DEMO_DB_PASSWORD", "test-password")

    with patch(
        "backend.main.check_database_connection",
        side_effect=RuntimeError("Sensitive database detail"),
    ):
        with TestClient(app) as client:
            response = client.get("/ready")

    assert response.status_code == 503
    assert response.json() == {
        "status": "unavailable",
        "database": "unavailable",
    }


# Purpose: verify that missing configuration cannot report readiness.
# Workflow: Day 1, readiness configuration validation.
# Removing this test loses coverage of missing-password handling.
def test_ready_returns_503_without_password(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("DEMO_DB_PASSWORD", raising=False)

    with patch("backend.main.check_database_connection") as database_check:
        with TestClient(app) as client:
            response = client.get("/ready")

    assert response.status_code == 503
    assert response.json() == {
        "status": "unavailable",
        "database": "unavailable",
    }
    database_check.assert_not_called()