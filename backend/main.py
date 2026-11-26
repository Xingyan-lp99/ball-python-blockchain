import os
import sys

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from backend.sepolia_registry import configure_local_sepolia_signers
from backend.database import check_database_connection
from backend.husbandry_routes import router as husbandry_router
from backend.snake_routes import router as snake_router

from backend.account_routes import router as account_router
from backend.session_routes import router as session_router

from backend.certificate_routes import router as certificate_router
from backend.keeper_transfer_routes import router as keeper_transfer_router
from backend.sepolia_routes import router as sepolia_router

app = FastAPI()
app.include_router(snake_router)
app.include_router(husbandry_router)
app.include_router(account_router)
app.include_router(session_router)
app.include_router(certificate_router)
app.include_router(keeper_transfer_router)
app.include_router(sepolia_router)


if os.environ.get("SEPOLIA_DEMO_SIGNING") == "1":
    @app.on_event("startup")
    def load_local_sepolia_signers() -> None:
        if not sys.stdin.isatty():
            raise RuntimeError("Sepolia demo signing requires a local interactive terminal.")
        configure_local_sepolia_signers()

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
