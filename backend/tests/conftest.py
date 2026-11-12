import os
import sys
from pathlib import Path
from uuid import uuid4

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from database import DATABASE_URL, get_session
from main import app
from migrate import migrate


@pytest.fixture(scope="session")
def registry_engine():
    """Use only a new isolated schema; never reset application tables."""
    url = os.getenv("TEST_DATABASE_URL", DATABASE_URL)
    admin = create_engine(url, connect_args={"connect_timeout": 3})
    schema = f"test_snakes_{uuid4().hex}"
    try:
        with admin.begin() as connection:
            connection.execute(text(f'CREATE SCHEMA "{schema}"'))
    except OperationalError:
        admin.dispose()
        pytest.skip("PostgreSQL unavailable; database integration checks not executed")
    test_engine = create_engine(
        url, connect_args={"connect_timeout": 3, "options": f"-csearch_path={schema}"}
    )
    try:
        migrate(test_engine)
        yield test_engine
    finally:
        test_engine.dispose()
        # Only remove the randomly named schema created by this test run.
        with admin.begin() as connection:
            connection.execute(text(f'DROP SCHEMA "{schema}" CASCADE'))
        admin.dispose()


@pytest.fixture
def db_client(registry_engine):
    from fastapi.testclient import TestClient

    def test_session():
        with Session(registry_engine) as session:
            yield session

    app.dependency_overrides[get_session] = test_session
    try:
        with TestClient(app) as client:
            yield client
    finally:
        app.dependency_overrides.clear()
