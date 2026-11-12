# Level 2 - Snake Registration

## Scope and approved iteration

This iteration implements a PostgreSQL-only registration and lookup workflow, requested
on 2026-11-12. It uses the existing Streamlit frontend, FastAPI modular monolith,
SQLAlchemy connection and PostgreSQL service. It does not submit blockchain transactions.

The current request explicitly differs from the earlier Level 1 data-model proposal:
callers supply `snake_id`; `name`, `date_of_birth`, `breeder_internal_id` and
`morph_description` are optional; the initial database manager is the registering
breeder. Level 1's generated `public_snake_id`, required genetic description,
wallet-selected initial keeper, photo and parent relationships belong to the broader
design and are not claimed as implemented here. Level 0 and Level 1 remain unchanged.
Reconcile that design with this iteration before expanding the schema or chain workflow.

Database profile creation is complete when committed to PostgreSQL. This is separate
from successful blockchain registration, which still requires confirmed execution.
`current_manager_id` is an application identity, not an Ethereum address or confirmed
on-chain keeper. This iteration does not grant transfer or husbandry permissions.

## API contract

Use the existing `/api/v1` prefix:

| Operation | Route | Success |
|---|---|---|
| Register database profile | `POST /api/v1/snakes` | 201, saved profile |
| Look up public identifier | `GET /api/v1/snakes/{snake_id}` | 200, saved profile |

| Request field | Required | Validation |
|---|---|---|
| `snake_id` | Yes | String; trim surrounding whitespace; reject blank; case-sensitive unique ID |
| `name` | No | String or null |
| `sex` | Yes | `male`, `female`, `unknown` |
| `date_of_birth` | No | Calendar date (`YYYY-MM-DD`) or null; no later than today in UTC |
| `breeder_internal_id` | No | String or null; breeder's own reference, not identity |
| `morph_description` | No | String or null; breeder-provided, not laboratory certified |

Unknown request fields are rejected. In particular, callers cannot set `breeder_id`,
`current_manager_id`, `created_at` or verification statuses. Optional omitted fields
are saved as null. The UI also converts empty optional text fields to null.

The response contains these six profile fields plus server-controlled `breeder_id`,
`current_manager_id`, UTC `created_at`, `registration_status: "not_submitted"` and
`certificate_status: "not_verified"`. These statuses are fixed descriptions of this
database-only implementation; no chain or certificate evidence exists yet.

| Failure | HTTP status |
|---|---|
| Invalid request, blank ID, future birth date, forbidden extra field | 422 |
| Duplicate snake ID, including competing inserts | 409 |
| Unknown snake ID | 404 |
| Database operation unavailable | 503, sanitized message |

## Identity and trust

There is no existing login implementation. `backend/identity.py` explicitly supplies
server-side demo identity `BR001` through a FastAPI dependency. The service derives
both `breeder_id` and initial `current_manager_id` from this dependency. It does not
read identity from the request body or an untrusted header. This is a demonstration
mechanism, **not authentication or authorization**. The page displays this limitation.
Replace the dependency with a real authenticated user context in a later iteration.

Morph descriptions are breeder reports and are never represented as laboratory
certificates. The page displays this qualification beside the field and saved profile.

## Storage and migration

There was no existing migration runner or application schema. Add a small ordered SQL
migration runner using the existing SQLAlchemy and psycopg dependencies, without adding
another framework. `backend/migrations/001_create_snakes.sql` creates only `snakes`.
An internal UUID `id` remains distinct from public `snake_id`; its unique constraint is
`uq_snakes_snake_id`. Other constraints enforce nonempty normalized IDs, allowed sex and
nonfuture birth dates. `created_at` uses the PostgreSQL timestamp default.

`python migrate.py` applies pending versions and records them in `schema_migrations`.
Migrations run in one transaction with an advisory lock; rerunning does not recreate
tables or erase data. An incompatible existing table fails instead of being replaced.
There is no automatic downgrade or destructive reset. Run migration explicitly before
local Uvicorn; the backend container runs it before starting Uvicorn.

Streamlit only calls FastAPI over HTTP. It never accesses the database. Registration
success displays the returned committed profile; lookup displays the saved profile.
A lost registration response asks the user to query the ID before retrying.

## Verification and acceptance

Backend tests use a newly generated `test_snakes_<uuid>` PostgreSQL schema, apply the
real SQL migration, and remove only that test schema afterward. `TEST_DATABASE_URL`
may select a separate PostgreSQL database; otherwise the existing `DATABASE_URL` is
used with an isolated schema. Schema creation requires database permission.
Unavailable PostgreSQL explicitly skips database checks; a skip is not a pass.

Coverage includes registration, optional fields, all sex values, lookup, duplicates,
invalid input, forbidden server fields, server identity dependency, 404, sanitized
database errors, actual saved rows, database constraints and repeatable migration.
A real HTTP test starts Uvicorn, registers a profile, terminates the process, starts
Uvicorn again and verifies the same committed profile through HTTP.

Streamlit AppTest checks registration/query via mocked HTTP, saved profile display,
duplicate and missing-ID messages, and network failure handling. It is not a manual
browser test. See the development record for checks actually executed and limitations.

## Deferred chain integration

- Reconcile the Level 1 identifier, field and keeper design before extending this slice.
- Implement real breeder authentication and identity-to-wallet mapping.
- Add and test a snake registry Solidity contract; retain the existing Counter sample.
- Configure chain ID, deployed contract/ABI, RPC and an authorized signing mechanism.
- Add transaction-attempt migrations and web3.py submission independent of profile creation.
- Define confirmation policy, uncertain submissions, retries, receipt verification,
  database/chain reconciliation and local-chain reset handling.
- Populate confirmed keeper information only from confirmed chain evidence; do not
  translate the demo manager into a wallet address.
- Add genuine certificate issuance and verification before displaying verified status.
