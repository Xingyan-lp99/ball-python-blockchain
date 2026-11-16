from fastapi.testclient import TestClient

from backend.main import app


# Purpose: check the agreed health response.
# Workflow: environment setup, Day 1, step 1 validation.
# Removing this test loses automated coverage of that response.
def test_health_returns_ok() -> None:
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}