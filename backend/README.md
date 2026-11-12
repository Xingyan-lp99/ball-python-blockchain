# Backend

Use the existing root `.env` with `DATABASE_URL`. From this directory:

```powershell
uv run python migrate.py
uv run uvicorn main:app --reload
uv run pytest -q -ra
```

Routes: `POST /api/v1/snakes`, `GET /api/v1/snakes/{snake_id}`.
The server currently uses demo breeder BR001; real authentication is not implemented.
Creating a profile saves only to PostgreSQL. Explicit local-chain submission uses
`POST /api/v1/snakes/{snake_id}/registration` with `{}`; query/reconcile with GET at
the same path. Certificates remain unverified. BR001 uses a server-controlled,
unlocked Hardhat wallet for local demo signing; the app never needs private keys.

From the root, start `just chain`, then (in another terminal) `just deploy-registry`.
Keep the chain running; apply migrations before starting the local API. Deployment
metadata is generated under ignored `.local/`; no chain configuration is necessary
for database-only profiles. See the chain development record for reset limitations.

For real-chain tests, from this directory:

```powershell
$env:RUN_LOCAL_CHAIN_TESTS = "1"
uv run pytest -q -ra
```

Tests use an isolated random PostgreSQL schema and remove only their own schema.
Optional `TEST_DATABASE_URL` selects a separate database. Database checks are explicitly
skipped if PostgreSQL is unavailable. See `../docs/level-3/snake-registration-development.md`
and `../docs/level-3/snake-registration-chain-development.md`.

Certificate V1 uses a separate contract, deployed once with `just deploy-certificates`
from the root while the current snake chain/deployment runs. Do not redeploy the snake
registry. Multipart `POST /api/v1/certificates` accepts certificate_id, snake_id and file.
Version-specific issue/poll/verify/download routes are in `../docs/level-2/certificate-v1.md`.
LAB001 is a server demo context with a separate node-held wallet, not real login.

Compose persists original PDFs in `certificate_files`; local Python defaults to ignored
`.local/certificate-files` unless CERTIFICATE_STORAGE_DIR is set. Preserve document storage
with PostgreSQL. Only python-multipart was added to runtime dependencies. See
`../docs/level-3/certificate-v1-development.md` for actual checks and manual steps.

Primary verification is `POST /api/v1/certificates/{id}/versions/1/verification/stored`
with `{}`. It reads actual stored bytes and freshly hashes them against current chain
evidence. The existing multipart `/verification` route is optional external-file
comparison. Neither route creates/overwrites certificates or broadcasts transactions.
