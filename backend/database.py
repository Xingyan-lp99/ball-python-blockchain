import os

import psycopg


# Purpose: verify that Python can connect to PostgreSQL and execute SELECT 1.
# Workflow: environment setup, Day 1, database connection check.
# Removing this function removes the Python-to-database connection check.
def check_database_connection(
    *,
    host: str,
    port: int,
    dbname: str,
    user: str,
    password: str,
) -> bool:
    try:
        with psycopg.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password,
            connect_timeout=5,
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
    except psycopg.Error:
        raise RuntimeError("Database connection check failed.") from None

    if result != (1,):
        raise RuntimeError("Database returned an unexpected check result.")

    return True


if __name__ == "__main__":
    password = os.environ.get("DEMO_DB_PASSWORD")

    if not password:
        raise RuntimeError("DEMO_DB_PASSWORD is not set.")

    success = check_database_connection(
        host="127.0.0.1",
        port=5433,
        dbname="ballpython_demo",
        user="ballpython",
        password=password,
    )

    print(f"Database connection successful: {success}")