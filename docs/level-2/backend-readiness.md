# Level 2 - Backend and Database Readiness

## Approved Contract

Workflow: Day 1 setup, before the minimal Streamlit page. The human approved a
database-inclusive HTTP check, implemented separately from process liveness.

- Input: GET `/ready`, no body, query parameters, or database password in HTTP.
- Success: HTTP 200, `{"status":"ok","database":"ok"}`.
- Missing database password or failed database check: HTTP 503,
  `{"status":"unavailable","database":"unavailable"}`.
- `/health` remains the existing backend-only response; blockchain readiness is
  outside this task. Operational paths are explicit exceptions to business
  routes under `/api/v1`.

Reuse `backend.database.check_database_connection` for a fresh SELECT 1 on each
request. Use the local demo settings 127.0.0.1:5433, ballpython_demo, ballpython,
and read DEMO_DB_PASSWORD from the backend process environment at request time.
The startup command must load `.env` with `uv run --env-file .env`. Do not return
raw connection exceptions, passwords, or connection strings in HTTP responses.

Provide handler/import changes and tests in chat for human insertion. Test the
HTTP success, database-failure, and missing-password cases with a mocked checker;
the existing database integration test covers the real connection. Manually
request `/ready` on the running backend for end-to-end verification afterwards.
This task requires no new dependency and does not alter the database schema.

Status: the human inserted the code, reported nine passing backend tests, and
confirmed the live `/ready` response matches the success contract. The readiness
endpoint is ready for the approved minimal Streamlit integration.
