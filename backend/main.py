import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from backend.database import check_database_connection
from backend.snake_routes import router as snake_router

app = FastAPI()
app.include_router(snake_router)

# Purpose: report that the backend can respond.
# Workflow: environment setup, Day 1, step 1.
# Removing this handler removes the agreed /health check.
@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


# Purpose: report whether the backend can query the demo database.
# Workflow: Day 1, backend/database readiness before frontend integration.
# Removing this handler removes the database-inclusive HTTP check.
@app.get("/ready")
def ready() -> JSONResponse:
    try:
        password = os.environ.get("DEMO_DB_PASSWORD")

        if not password:
            raise RuntimeError("Database password is not configured.")

        check_database_connection(
            host="127.0.0.1",
            port=5433,
            dbname="ballpython_demo",
            user="ballpython",
            password=password,
        )

    except RuntimeError:
        return JSONResponse(
            status_code=503,
            content={
                "status": "unavailable",
                "database": "unavailable",
            },
        )

    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "database": "ok",
        },
    )