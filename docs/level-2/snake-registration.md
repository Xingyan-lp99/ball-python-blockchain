# Level 2 - Snake Registration

## Scope and approved iteration

The completed database stage implements PostgreSQL registration and lookup, requested
on 2026-11-12. The subsequent local-chain stage below adds explicit blockchain submission
to the existing Streamlit/FastAPI/SQLAlchemy/PostgreSQL flow. Creating a database profile
still does not submit a transaction automatically.

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
`certificate_status: "not_verified"`. `registration_status` initially remains
`not_submitted`; it is now derived from checked local-chain evidence when an attempt
exists. `chain_registration` is null until there is an attempt, then contains the
status/evidence structure defined below. Certificates remain unverified throughout.

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

## Local Hardhat registration stage

### Scope and contract

Local chain ID 31337 only; no public testnet deployment. Preserve Counter and its
deployment module. Add SnakeRegistry with `register(string snakeId)`,
`managerOf(string)` and immutable `instanceId`. Registration rejects empty/ASCII
whitespace-only IDs and exact duplicate IDs. The manager is always `msg.sender`;
there is no manager parameter to impersonate. `SnakeRegistered(string snakeId,
address indexed manager)` records both values. Detailed profiles remain off-chain.
Certificate hashes, certificate checks and manager transfers are excluded.

Use the existing Hardhat 3 / Ignition stack. The local deployment script generates
a random instance ID and an ignored `.local/snake-registry.json` manifest containing
ABI, chain ID, contract address, instance ID, runtime code hash, deployment block
anchor and the public development wallet address. It neither exports nor logs keys.
Do not redeploy on every app restart; reuse this manifest with the same running chain.

### Demo identity and signing

Only server-side BR001 maps to the manifest's development wallet. The backend uses
web3.py `eth_sendTransaction` through Hardhat's unlocked local account; Hardhat holds
the key and signs on the server's behalf. This is **server-mediated signing for a
local demo, not real authentication**. No private key is required in application
configuration, source code, database, frontend, API response or Git. The UI cannot
choose a signer or override the mapped address. The adapter restricts the RPC to
loopback/localhost or Docker Desktop's host gateway, validates Hardhat client type,
and requires chain ID 31337. Do not expose this RPC or use these accounts with real funds.

### Additional API routes

| Operation | Route | Body |
|---|---|---|
| Submit/retry registration | `POST /api/v1/snakes/{snake_id}/registration` | `{}`; extra fields forbidden |
| Reconcile/query transaction result | `GET /api/v1/snakes/{snake_id}/registration` | None |

POST requires an existing database profile whose breeder and current manager are
the current BR001 context. Missing profiles return 404; unauthorized profiles return
403; identity/transaction/deployment conflicts and concurrent signer operations
return 409. Configuration/RPC failure before creating an intent returns 503. Database
errors return sanitized 503 messages and ask the caller to query before retrying.
Successful submissions and reconciliation return 200 with the status below; 200
alone never means the transaction succeeded.

Existing `GET /api/v1/snakes/{snake_id}` also reconciles profiles with an attempt;
an unavailable chain never makes an existing database profile disappear. Profiles
without an attempt remain readable and writable without chain configuration.

### Status and evidence

| `status` | Meaning |
|---|---|
| `not_submitted` | No local transaction intent recorded |
| `processing` | Prepared/submitted/pending, uncertain broadcast, or historical confirmation cannot currently be checked |
| `confirmed` | Scope valid, canonical receipt status 1, sender/calldata/event and current manager all match |
| `failed` | Receipt status 0, or current check detects stale/conflicting evidence; profile retained |

One successful mined receipt is sufficient for this local demo; this is not a
production finality policy. A timeout is not a failed transaction. A hash alone is
not success. RPC failure never produces `confirmed`.

The response additionally exposes `chain_check` (`not_checked`, `verified`,
`unavailable`, `stale`, `conflict`), `recorded_status`, sanitized `error`, transaction
hash, chain ID, contract address, manager wallet, block number, block hash and instance
ID. `chain_check: verified` means the checks completed; it may accompany a pending or
reverted transaction. Only `status: confirmed` plus `chain_check: verified` represents
current confirmation. `recorded_status` describes retained historical database state.

The page shows the state and public evidence, explains server signing, preserves the
uncertified breeder-description notice, and requires explicit submission. It stores
the selected profile in session state across reruns, but rechecks cached confirmations
before displaying them as current. Refreshing chain status never broadcasts. Prepared
intents with no hash may be safely retried after a successful chain check; known pending
transactions only offer status refresh.

### Persistence, retries and recovery

Migration `002_snake_registration_attempts.sql` adds an append-only attempt history
referencing `snakes.id`, without altering/removing existing profiles. Each attempt
records deployment scope, expected wallet, nonce, gas price, starting block, transaction
hash when available, lifecycle, receipt block evidence and sanitized failure code.
Confirmed attempts require hash and block evidence. Existing migrations remain unchanged.

A PostgreSQL advisory lock on a dedicated connection serializes the one demo signer
across commits and Uvicorn workers. The backend commits intent and fixed nonce/gas
parameters before broadcasting, then commits the returned hash immediately before
polling. Another profile cannot consume a nonce reserved by an unresolved intent.

Before retrying, check current chain scope, registered manager and registration events.
If state matches, obtain the successful receipt, validate sender, destination, calldata,
canonical block and event, then recover local evidence without another registration.
If the hash was lost, inspect pending/mined transactions for the stored sender/nonce,
verify the payload and recover the hash, including reverted transactions without events.
An unbroadcast intent can resend exactly the saved transaction parameters and nonce;
it cannot select a new sender or silently allocate a new transaction. A definitive
revert may create a new attempt after checking that the snake is still unregistered.
Earlier failed attempts remain available. Conflicts require explicit resolution.

This covers a lost RPC response, failure to save a returned hash, and successful chain
execution followed by failure to save confirmation. A database failure before intent
commit prevents broadcasting. Never delete the profile to resolve a chain error.

### Local chain reset and redeployment

Hardhat state is ephemeral. Restart/reset may erase deployed bytecode, receipts and
registrations even when chain ID and a subsequently reused contract address look the
same. Validate runtime bytecode hash, immutable random instance ID and the manifest's
block anchor; compare each attempt's original scope with the active manifest. Missing
historical receipts or missing registrations invalidate current confirmation.

Return stale/failed current state, retain historical hashes and `recorded_status`,
and refuse automatic submission against a replacement deployment. RPC unavailability
is reported separately from proven stale scope. No reset, history deletion or automatic
rebinding is implemented. After a deliberate reset, create a new deployment manifest;
reconciling old profiles into a new instance needs a later explicit recovery/migration
policy. Do not edit historical attempt rows just to make the page green.

### Tests and remaining work

Run contract tests, backend tests against isolated PostgreSQL schemas, Streamlit AppTest
checks and opt-in real-chain tests with `RUN_LOCAL_CHAIN_TESTS=1`. Real-chain tests start
a real HTTP API, exercise Streamlit with real HTTP, verify contract storage/receipts/events,
exercise pending mining and a conflicting wallet, and reject wrong deployment evidence.
They do not reset the chain. Development records distinguish actual reads from simulated
RPC/DB failures and reset conditions.

Pending: real authentication and secure non-demo signing; broader Level 1 reconciliation;
certificate V2/revocation lifecycle and transfers; background polling/reconciliation; production chain
finality/reorg policy; explicit historical-profile recovery after a local reset. Public
testnet deployment is outside this iteration.

The subsequent V1 issuance and independent file-comparison slice is specified in
`certificate-v1.md`; it does not change this snake profile's aggregate trust status.
