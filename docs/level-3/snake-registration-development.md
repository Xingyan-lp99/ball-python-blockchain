# Snake Registration Development Record

Date: 2026-11-12 (Europe/Berlin)

Status: **Database stage complete**, including automated checks and manual browser
acceptance performed by the user. This document preserves that stage's historical
record. The subsequent local-chain stage is documented in
`snake-registration-chain-development.md`; real authentication and certificates remain pending.

## Existing project and decisions

- Streamlit: `frontend/main.py`, separate uv environment.
- FastAPI: `backend/main.py`; SQLAlchemy engine: `backend/database.py`.
- PostgreSQL: existing Compose `db` service and `postgres_data` named volume.
- Solidity/Hardhat: `contracts/`, currently Counter sample contracts and tests.
- No login or migration mechanism existed; Level 2 and Level 3 feature files were empty.
- Retain `/api/v1`, the modular monolith and all existing contract functionality.
- Use the current explicit request for fields and supplied IDs. Document differences
  from the earlier Level 1 proposal; do not silently rewrite the high-level design.
- Use SQL migrations with version tracking and transactions, built on the existing
  SQLAlchemy/psycopg stack. Add only pytest/httpx development dependencies.

## Implemented

Database-only snake creation and lookup, server-assigned demo identity and timestamp,
unique IDs, request/database validation, explicit error statuses, Streamlit forms,
saved-profile display and clear trust labels. Docker starts migrations before FastAPI.
No chain transaction or laboratory verification is submitted or inferred.

## Executed checks

| Check | Result |
|---|---|
| `.venv/Scripts/python.exe -m pytest -q -ra` from backend | 26 passed, no skips |
| `.venv/Scripts/python.exe -m unittest discover -s tests -v` from frontend | 5 passed |
| PostgreSQL committed-row and constraints checks | Passed in isolated test schema |
| HTTP persistence across actual Uvicorn process restart | Passed; exact saved JSON retrieved after restart |
| Repeat SQL migration | Passed; test profile retained |
| `.venv/Scripts/python.exe migrate.py` from backend | Applied successfully to existing development database |
| `docker compose config --quiet` | Passed |
| `docker compose build backend frontend` | Both images built successfully |
| `docker compose up -d backend frontend` | Both application containers started; existing database healthy |
| Container HTTP smoke checks | API and database health 200; unknown snake 404; blank-ID registration 422; Streamlit health 200 |
| `just --list` | Passed; new recipes listed |
| Manual browser acceptance performed by the user (2026-11-12) | Registration, lookup, duplicate-ID rejection, original-record preservation, missing-ID feedback and status explanations all met expectations |

The manual acceptance result above was reported by the user; it was not performed
by the coding agent. The automated results are from the implementation run. This
acceptance/documentation update does not change application code or rerun those tests.

The backend suite emits one upstream Starlette warning about its httpx TestClient
integration. Streamlit AppTest emits missing ScriptRunContext notices in bare test
mode. Neither caused test failures. No dependencies were changed to suppress warnings.

Initially Docker was stopped and PostgreSQL unavailable. The installed Docker Desktop
was started, the existing PostgreSQL container became healthy, and database tests then
executed successfully. No replacement database or credentials were invented.

Tests create their own random PostgreSQL schema and remove only that schema. The
development migration adds tables; it does not remove or reset existing data.

## Running locally

Reuse the existing root `.env` and uv environments. Required local backend variable:
`DATABASE_URL` with a valid PostgreSQL SQLAlchemy psycopg URL. Compose uses the existing
`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`; do not print or commit their values.
Frontend `API_BASE_URL` defaults to `http://127.0.0.1:8000` for local runs and is already
set to the backend service by Compose.

From the repository root:

```powershell
docker compose up -d db
just migrate
just backend
```

In another terminal:

```powershell
just frontend
```

Open `http://localhost:8501` and API docs at `http://localhost:8000/docs`.
Alternatively, `docker compose up -d --build` builds and runs the existing services;
the backend container applies pending migrations automatically.

```powershell
just test-backend
just test-frontend
```

Backend tests use PostgreSQL and create-schema permission. Set `TEST_DATABASE_URL` to
an explicitly configured test database if desired. An unavailable database yields
explicit skips, not successful database validation. Do not use `docker compose down -v`
because it removes the data volume.

Example registration body for `POST /api/v1/snakes`:

```json
{
  "snake_id": "S001",
  "name": "Amber",
  "sex": "female",
  "date_of_birth": "2025-06-15",
  "morph_description": "Breeder-reported Pastel; not laboratory certified"
}
```

Retrieve it with `GET /api/v1/snakes/S001`. A second registration of S001 returns 409.
The server sets breeder and initial manager to demo BR001; this is not real login.

## Not yet implemented or checked at the database-stage handoff

- Real authentication, chain registration, signing, transaction reconciliation,
  certificates and confirmed keeper state are not implemented in this iteration.
- Existing Solidity tests have not been rerun: no contract files were changed and
  this database slice does not use the chain.
- No durability claim is made for database-volume deletion or host disaster recovery;
  the tested guarantee is committed data surviving application-process restart.

See the Level 2 deferred-work list before connecting blockchain registration.

## Local commit scope after acceptance

The user authorized a local commit with message
`feat: implement database-backed snake registration` and explicitly excluded remote
push. Include the registration implementation, tests, migration, feature documents
and the existing app/runtime/dependency files needed to run this database slice.
Exclude the pre-existing Level 1 data-model edit, contract project and IDE settings.
Do not stage environment secrets, private keys, virtual environments or database files.
