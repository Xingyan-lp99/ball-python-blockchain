# Level 2 - Backend Health Response

## Approved Small Task

Workflow: development environment setup, Day 1, step 1. Confirm that FastAPI can
start and respond before introducing database, blockchain, or frontend integration.

- Input: HTTP GET `/health`, with no required query parameters or request body.
- Output: HTTP 200 and JSON `{"status": "ok"}`.
- This is a process-liveness response only; it does not check PostgreSQL or Hardhat.
- `/health` is the explicitly approved operational endpoint. Future business API
  endpoints still follow the `/api/v1` convention.

## Implementation Proposal for Human Insertion

Use a root `pyproject.toml` for uv dependencies, `backend/main.py` for the minimal
FastAPI application, and `backend/tests/test_health.py` for its response-contract
test. Use Python 3.12 or newer, consistent with the existing local Python 3.12
environment. FastAPI and Uvicorn are runtime dependencies; pytest and HTTPX are
development dependencies. Resolve exact versions with the human-run uv sync and
share the resulting lockfile through the normal reviewed Git workflow.

The health handler has no arguments and returns a string-key/string-value mapping.
The test sends a GET request through FastAPI TestClient and checks HTTP 200 and
the exact JSON body. It does not depend on a running external server.

## Acceptance and Current Status

Acceptance requires both a successful automated response-contract test and a
manual request to the running Uvicorn server at `/health`. Start from the project
root so the backend module can be imported consistently on Windows and macOS.

Inputs and outputs were explicitly approved in chat. Code and dependency
configuration are to be supplied in chat for human insertion, per AGENTS.md.
The human inserted the application, test, and dependency configuration. The AI
did not write these program files. Validation completed on 2026-11-14:

- Response-contract test: 1 passed. The local run also reported a TestClient
  dependency deprecation and a sandbox cache-permission warning; neither failed
  the response test.
- Port 8000 was already listening under `com.docker.backend`; it was not stopped.
- A temporary Uvicorn process on 127.0.0.1:8001 returned HTTP 200 and the exact
  agreed JSON from `/health`. Only that temporary process was stopped afterwards.
- For interactive use, run from the project root with
  `uv run python -m uvicorn backend.main:app --reload --port 8001`, then open
  `http://127.0.0.1:8001/health`. Reload mode has not been separately verified.
