import os
from unittest.mock import patch

import psycopg
import pytest

from backend.database import check_database_connection


# Purpose: verify the real local PostgreSQL connection.
# Workflow: environment setup, Day 1, database validation.
# Removing this test loses coverage of the actual connection path.
def test_database_connection_returns_true() -> None:
    assert check_database_connection(
        host="127.0.0.1",
        port=5433,
        dbname="ballpython_demo",
        user="ballpython",
        password=os.environ["DEMO_DB_PASSWORD"],
    ) is True


# Purpose: verify that connection failures expose only a safe message.
# Workflow: environment setup, Day 1, database failure validation.
# Removing this test loses coverage of the failure message.
def test_database_connection_failure_has_safe_message() -> None:
    with patch(
        "backend.database.psycopg.connect",
        side_effect=psycopg.OperationalError("test-password"),
    ):
        with pytest.raises(RuntimeError) as error:
            check_database_connection(
                host="127.0.0.1",
                port=5433,
                dbname="ballpython_demo",
                user="ballpython",
                password="test-password",
            )

    assert str(error.value) == "Database connection check failed."
    assert error.value.__suppress_context__ is True