from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError

from database import check_database_connection
from snake_registry.routes import router as snake_router
from certificates.routes import router as certificate_router

app = FastAPI(title="Ball Python Blockchain API")
app.include_router(certificate_router, prefix="/api/v1")
app.include_router(snake_router, prefix="/api/v1")


@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/v1/health/db")
def database_health_check():
    try:
        database_name = check_database_connection()

        return {
            "status": "ok",
            "database": database_name,
        }

    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable",
        )
