# Backend

Use the existing root `.env` with `DATABASE_URL`. From this directory:

```powershell
uv run python migrate.py
uv run uvicorn main:app --reload
uv run pytest -q -ra
```

Routes: `POST /api/v1/snakes`, `GET /api/v1/snakes/{snake_id}`.
The server currently uses demo breeder BR001; real authentication is not implemented.
Records are saved only to PostgreSQL, with no chain registration or certificate verification.

Tests use an isolated random PostgreSQL schema and remove only their own schema.
Optional `TEST_DATABASE_URL` selects a separate database. Database checks are explicitly
skipped if PostgreSQL is unavailable. See `../docs/level-3/snake-registration-development.md`.
