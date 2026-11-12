FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY main.py database.py ./
COPY identity.py migrate.py ./
COPY snake_registry ./snake_registry
COPY blockchain ./blockchain
COPY certificates ./certificates
COPY migrations ./migrations

EXPOSE 8000

CMD ["sh", "-c", "uv run --no-sync python migrate.py && exec uv run --no-sync uvicorn main:app --host 0.0.0.0 --port 8000"]
