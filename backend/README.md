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
