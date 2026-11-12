"""Apply ordered SQL migrations transactionally, without resetting existing data."""

from pathlib import Path

from sqlalchemy import text
from sqlalchemy.engine import Engine

from database import engine


def migrate(database_engine: Engine = engine) -> None:
    with database_engine.begin() as connection:
        # Serialize concurrent migration runners in this database/schema.
        connection.execute(text("SELECT pg_advisory_xact_lock(724801001)"))
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version text PRIMARY KEY,
                applied_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """))
        applied = set(connection.execute(text("SELECT version FROM schema_migrations")).scalars())
        for path in sorted((Path(__file__).parent / "migrations").glob("*.sql")):
            if path.name in applied:
                continue
            connection.exec_driver_sql(path.read_text(encoding="utf-8"))
            connection.execute(
                text("INSERT INTO schema_migrations (version) VALUES (:version)"),
                {"version": path.name},
            )


if __name__ == "__main__":
    try:
        migrate()
    except Exception:
        # Avoid printing connection strings, credentials, or SQL parameter values.
        raise SystemExit("Migration failed. Check database availability and schema compatibility.") from None
    print("Database migrations applied.")
