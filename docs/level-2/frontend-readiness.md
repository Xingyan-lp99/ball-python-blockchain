# Level 2 - Minimal Streamlit Readiness Page

## Approved Workflow and Contract

Day 1, frontend-to-backend-to-database verification. Display a title and one
check button. On click, the Streamlit Python process requests
GET http://127.0.0.1:8001/ready with a five-second request timeout.

- HTTP 200 with the exact agreed ready payload: show backend/database success.
- HTTP 503 with the exact agreed unavailable payload: show database not ready.
- Request connection failure or timeout: show backend unavailable or timed out.
- Other status/payload or invalid JSON: show unexpected backend response.
- After any failure the page remains usable and the button can be clicked again.

Use frontend/api.py for HTTP classification and frontend/app.py for display.
The helper takes the readiness URL and returns a small status label; it never
returns raw errors or credentials. The page needs no database password and makes
no direct SQL or blockchain calls. Do not cache readiness results.

Run Streamlit locally on 127.0.0.1:8502 from the repository root. Declare Streamlit
and Requests as project dependencies. Provide all code, dependency edits, and
AppTest tests in chat for human insertion under AGENTS.md.

Acceptance: AppTest exercises the button with mocked HTTP success, database
failure, unexpected payload, connection error, timeout, and invalid JSON. Then
manually click the real page button with the backend and database running.

Status: contract approved; snippets provided; human insertion, automated tests,
and real-page verification pending. No frontend test result is claimed yet.
