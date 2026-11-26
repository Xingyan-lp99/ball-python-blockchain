from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from backend.main import app


@pytest.mark.parametrize("laboratory_id", ["LAB001", "LAB002"])
def test_public_lab_registration_is_denied_before_database_access(laboratory_id):
    data = {
        "username": "lab-test", "email": "lab@example.test", "password": "test-only",
        "role": "lab", "laboratory_id": laboratory_id, "display_name": "Test Lab",
        "country_or_region": "Demo", "demo_consent": True,
    }
    with patch("backend.account_routes.psycopg.connect") as connect:
        response = TestClient(app).post("/api/v1/accounts", json=data)
    assert response.status_code == 403
    assert "Public laboratory registration is disabled" in response.json()["detail"]
    connect.assert_not_called()
