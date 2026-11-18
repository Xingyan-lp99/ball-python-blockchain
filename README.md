# Ball Python Blockchain Registry

A small local learning demonstration built with Streamlit, FastAPI,
PostgreSQL, Solidity, Hardhat, and web3.py.

The current code includes account registration/sign-in, role-specific workspaces,
breeder snake registration with photos, two-laboratory PDF issuance, append-only
certificate revisions, version history/downloads, keeper transfer requests and
accept/reject/cancel actions, and four off-chain husbandry record types. Profile
views display the current manager and transfer status. Husbandry edits/deletions
require both current keeper rights and original authorship.

The owner has manually verified the main handover and post-transfer husbandry
workflow. The November 19 audit also passed an isolated end-to-end workflow and
19 focused tests; the historical full suite has not been rerun. Buyer-uploaded
PDF verification is outside the approved demonstration. Husbandry evidence is
not stored on-chain.

Read [AGENTS.md](AGENTS.md) before contributing. The approved demonstration
is in [the logical data model](docs/level-1/data-model.md), and the architecture
is described in [the architecture document](docs/level-0/architecture.md).

## Local environment

For the November 19 frontend update, included Logo/photos/fonts, safe Git sync,
role-page preview, and a ready-to-forward Codex prompt, see the
[collaborator handoff](docs/collaborator-handoff-2026-11-19.md).
Git transfers source/static assets; it does not transfer accounts, uploaded
reports, PostgreSQL data, or a running Hardhat chain. Each collaborator starts
their own services and opens their local `http://127.0.0.1:8502` URL.

These instructions use Windows PowerShell in VS Code and assume Git, uv,
Node.js/npm, and Docker Desktop with Docker Compose are already installed.
Start Docker Desktop before running database commands. A VS Code extension by
itself does not install or start these tools.

Python must satisfy the project's `>=3.12` requirement. The commands below use
Python 3.12 explicitly. The existing development machine uses Node.js 22.16.0;
the installed Hardhat CLI checks for a minimum of 22.13.0. Check the Hardhat
startup output for compatibility messages on your machine.

| Component | Local address | How it runs |
|---|---|---|
| PostgreSQL | `127.0.0.1:5433` | Docker Compose, service `db` |
| Hardhat JSON-RPC | `http://127.0.0.1:8545` | Dedicated terminal; chain ID `31337` |
| FastAPI | `http://127.0.0.1:8001` | Dedicated terminal |
| Streamlit | `http://127.0.0.1:8502` | Dedicated terminal |

The repository's Compose configuration starts only PostgreSQL. Any older backend
or frontend containers on a contributor's computer are separate from this setup.
The current frontend calls port **8001**, even if an older container uses 8000.

Run commands from the repository root unless a step explicitly changes folders.
Stop when a command fails; resolve that error before continuing.

## First-time setup

### 1. Get the shared code and dependencies

Accept the GitHub collaborator invitation. Copy the repository's clone URL from
GitHub's **Code** menu. Replace `REPOSITORY_URL` below with that URL:

```powershell
git clone REPOSITORY_URL
Set-Location ball-python-blockchain
uv sync --locked --python 3.12
Set-Location contracts
npm ci
npx.cmd --no-install hardhat compile
Set-Location ..
```

If the clone has a different folder name, use that name in `Set-Location`.
`uv sync` creates the local Python environment and installs project and default
development dependencies. `npm ci` uses `contracts/package-lock.json`.
Compilation recreates the ignored contract artifacts required by the backend.
Initial dependency installation and compilation may require internet access.

### 2. Create your own local settings

Manually create `.env` in the repository root using the editor. Add this setting,
replacing the example value with your own local database password:

```dotenv
DEMO_DB_PASSWORD=replace_with_your_own_local_demo_password
```

There is currently no `.env.example` file. Do not copy another contributor's
password. `.env` is ignored by Git and must remain local. Use only local Hardhat
test accounts; no real wallet private key is needed.

### 3. Start PostgreSQL

```powershell
docker compose --env-file .env -f infrastructure/compose.yaml up -d db
docker compose --env-file .env -f infrastructure/compose.yaml ps
```

Wait until `db` is healthy. For diagnosis, view its recent logs:

```powershell
docker compose --env-file .env -f infrastructure/compose.yaml logs --tail 50 db
```

The database is `ballpython_demo`, the user is `ballpython`, and the host port is
5433. Its data is kept in a Docker named volume. Changing `.env` later does not
change the password of an already initialized PostgreSQL volume.

### 4. Initialize the database tables once

For a fresh database, apply the existing migration files in this exact order.
Run each command separately and check that it succeeds before running the next:

```powershell
Get-Content -Raw backend/migrations/001_create_participants_and_snakes.sql | docker compose --env-file .env -f infrastructure/compose.yaml exec -T db psql -U ballpython -d ballpython_demo -v ON_ERROR_STOP=1 --single-transaction
```

```powershell
Get-Content -Raw backend/migrations/002_require_snake_sex.sql | docker compose --env-file .env -f infrastructure/compose.yaml exec -T db psql -U ballpython -d ballpython_demo -v ON_ERROR_STOP=1 --single-transaction
```

```powershell
Get-Content -Raw backend/migrations/003_create_blockchain_transactions.sql | docker compose --env-file .env -f infrastructure/compose.yaml exec -T db psql -U ballpython -d ballpython_demo -v ON_ERROR_STOP=1 --single-transaction
```

```powershell
Get-Content -Raw backend/migrations/004_create_husbandry_records.sql | docker compose --env-file .env -f infrastructure/compose.yaml exec -T db psql -U ballpython -d ballpython_demo -v ON_ERROR_STOP=1 --single-transaction
```

```powershell
Get-Content -Raw backend/migrations/005_create_accounts_and_sessions.sql | docker compose --env-file .env -f infrastructure/compose.yaml exec -T db psql -U ballpython -d ballpython_demo -v ON_ERROR_STOP=1 --single-transaction
```

```powershell
Get-Content -Raw backend/migrations/006_create_certificate_records.sql | docker compose --env-file .env -f infrastructure/compose.yaml exec -T db psql -U ballpython -d ballpython_demo -v ON_ERROR_STOP=1 --single-transaction
```

```powershell
Get-Content -Raw backend/migrations/007_create_keeper_transfers.sql | docker compose --env-file .env -f infrastructure/compose.yaml exec -T db psql -U ballpython -d ballpython_demo -v ON_ERROR_STOP=1 --single-transaction
```

An existing clone initialized through migration 003 needs only 004 through 007,
in order, after confirming they have not already been applied. These add
husbandry, accounts/sessions, laboratory/certificate, and transfer records.
The migrations are not automatically tracked by a
migration runner and are not safe to rerun blindly. If tables already exist,
first check which migrations have been applied. Do not delete the database to
work around an error without agreeing how to preserve any existing data.

### 5. Start the local blockchain

Open a dedicated terminal at the repository root, then run:

```powershell
Set-Location contracts
npx.cmd --no-install hardhat node --network localDemo --hostname 127.0.0.1 --port 8545
```

Leave this terminal running and rename it `Hardhat` in VS Code. The configured
chain ID is 31337. Hardhat displays public development accounts and keys; these
are for this local demonstration only.

### 6. Deploy the contract and initialize participants

In another terminal at the repository root:

```powershell
uv run --locked python -m backend.blockchain
uv run --locked python -m backend.deploy_registry
```

The connection check should show chain ID 31337. Successful deployment prints
`receipt_status: 1`, a `contract_address`, and `verification: SnakeNotFound`.
Here, `SnakeNotFound` is the expected verification result for a fresh contract
before any snake is registered.

Copy the printed contract address into your local `.env` as a second setting:

```dotenv
DEMO_REGISTRY_ADDRESS=0x_replace_with_the_address_printed_by_your_deployment
```

Replace the entire example value with the actual address. Then initialize the
demo participants and check the database connection:

```powershell
uv run --locked --env-file .env python -m backend.seed_participants
uv run --locked --env-file .env python -m backend.database
```

The seed maps `BREEDER001`, `LAB001`, `LAB002`, and `BUYER001` to Hardhat account
indexes 1 through 4, respectively. Index 0 deploys the contract. Creating lab
participant records does not implement laboratory issuance permissions.

Prepare the certificate contract and both laboratory permissions next:

```powershell
uv run --locked --env-file .env python -m backend.setup_certificates
```

Retain the printed CertificateRegistry address in your own local settings as
DEMO_CERTIFICATE_REGISTRY_ADDRESS. If you already have a certificate deployment
on this same running chain, configure its address before running setup to reuse
it. Never blindly deploy another instance after an uncertain transaction result.

### 7. Start FastAPI and Streamlit

In a dedicated terminal at the repository root, start FastAPI:

```powershell
uv run --locked --env-file .env python -m uvicorn backend.main:app --host 127.0.0.1 --port 8001
```

Rename this terminal `FastAPI` and leave it running. The `--env-file .env` option
loads settings into this backend process. Restart the backend after changing
`.env` so it reads the updated values.

In a separate terminal at the repository root, start Streamlit:

```powershell
uv run --locked python -m streamlit run frontend/app.py --server.address 127.0.0.1 --server.port 8502
```

Rename this terminal `Streamlit` and leave it running.

## Check the running application

1. Open [backend health](http://127.0.0.1:8001/health). Expect
   `{"status":"ok"}`.
2. Open [database readiness](http://127.0.0.1:8001/ready). Expect
   `{"status":"ok","database":"ok"}`. This check does not check the contract,
   database schema, or participant initialization.
3. Open [API documentation](http://127.0.0.1:8001/docs).
4. Open [Streamlit](http://127.0.0.1:8502), register a Breeder account, and sign in.
   Each role binds to its predefined participant; register one Buyer and staff
   accounts for LAB001 and LAB002 as needed. Account registration does not
   authorize laboratories on-chain; the setup script does that separately.
5. For the first registration, use `SNAKE001`, a fictional breeder internal ID,
   `Python regius`, a sex description, a birth date, a fictional genetic
   description, and a JPEG/PNG photo no larger than 5 MiB.
6. After confirmed registration, use **View Profile** to retrieve `SNAKE001`.
   Check again after reopening the page to confirm retrieval from saved data.

After SNAKE001 exists, deploy KeeperTransfers in a separate terminal:

```powershell
uv run --locked --env-file .env python -m backend.setup_keeper_transfers
```

Retain its printed address as DEMO_KEEPER_TRANSFERS_ADDRESS in your own settings,
then restart FastAPI with all four settings: DEMO_DB_PASSWORD,
DEMO_REGISTRY_ADDRESS, DEMO_CERTIFICATE_REGISTRY_ADDRESS, and
DEMO_KEEPER_TRANSFERS_ADDRESS. This ordering is important for a fresh database:
registration can run before KeeperTransfers setup, but husbandry writes require
the deployed transfer contract. Do not run setup against another contributor's
addresses without confirming those deployments exist on your local chain.

The two lab accounts use New Report to issue separate V1 series. LAB001 uses
Revise Report with its original Series ID to append V2. Buyer/Breeder profiles
show Certificate History, selectable original PDFs, and Keeper Management.
The breeder initiates a handover using the buyer's login username. The buyer
can accept/reject, and the initiating keeper can cancel. Only confirmed
acceptance changes the current keeper. After acceptance, the buyer may maintain
their own husbandry records; original-author restrictions remain in force.

Do not register the same ID again. If a transaction result is unknown or storage
failed, inspect the transaction and saved state before retrying. Registration
changes both the local blockchain and database; `/ready` alone cannot confirm
that these two states agree.

## Run existing tests

The November 19 audit passed an opt-in isolated full workflow test and 19
focused existing tests. See the [audit report](docs/level-3/functional-audit-2026-11-19.md)
for exact coverage, commands, and current-chain limitations. The historical full
suite below was not run in that audit; some older tests describe previous API/UI
versions and may need maintenance. The commands are not required startup steps.

After installing dependencies, initializing the database, compiling the contract,
and starting PostgreSQL and Hardhat, run from the repository root:

```powershell
uv run --locked --env-file .env python -m pytest backend/tests frontend/tests
```

For the existing Solidity tests, run from `contracts/` in a separate terminal:

```powershell
npx.cmd --no-install hardhat test
```

Some Python tests use the real local database and blockchain; deployment and
registration tests submit local transactions. Use the dedicated demonstration
environment. Report the actual results from your own run. Writing this guide did
not perform a fresh-clone installation, run these tests, or complete a browser
registration on another computer.

## Daily startup and shutdown

With existing dependencies and database tables, start Docker Desktop and run
the database startup command from step 3. Do not repeat the migrations. If the
same Hardhat process is still running and its contract is intact, reuse its
deployment and `.env` address, then start FastAPI and Streamlit as in step 7.

Stopping Hardhat with Ctrl+C loses its in-memory blockchain state. PostgreSQL
and uploaded photos persist independently. After a Hardhat restart, deploy the
contract again and update `.env`; the same-looking address does not prove that
the old registrations survived. Existing database profiles may refer to lost
chain registrations. Agree how to reconcile the demo state before continuing;
this project currently has no automatic restore or reset workflow. Do not
automatically delete the database volume or files.

Ctrl+C in the FastAPI or Streamlit terminal stops that application. To stop
PostgreSQL while retaining its volume:

```powershell
docker compose --env-file .env -f infrastructure/compose.yaml stop db
```

## Sharing and collaboration

GitHub shares committed and pushed files. Each contributor installs dependencies
and creates their own database, blockchain, contract deployment, and `.env`.
Localhost links always point to the computer opening them.

The following stay outside Git:

- `.env`: local settings and database password.
- `.venv/` and `node_modules/`: recreated from dependency files.
- `contracts/artifacts/` and `contracts/cache/`: recreated by compilation.
- `storage/`: uploaded photos and original certificate PDFs.
- `docs/data_example/`: optional fictional reference documents, shared separately
  if needed. They are not finalized schemas or confirmed feature requirements.
- Docker database volumes and the running Hardhat chain: local runtime data.

A fresh clone will not contain another contributor's registered snake or photo.
Nor will it contain their accounts, sessions, certificate PDFs, or deployed
contract state. Use a separate local demonstration setup. Sharing
an existing demonstration state requires a separate coordinated data handoff.

Before pulling updates, check `git status` and preserve your own work. Coordinate
small tasks and use feature branches and pull requests. Repository AI learning
rules apply to both contributors: humans insert all program and executable
configuration changes, and commit/push actions require explicit approval.

The current main integration selectively adapts transfer logic from commit
b527c1c into the separate KeeperTransfers contract. It does not merge the
HusbandryEvidenceRegistry or the modified SnakeRegistry from feature/keeper-transfer.
Use main for the approved off-chain husbandry workflow; do not merge that feature
branch's broader storage-boundary changes without a separate scope decision.

## Troubleshooting

| Symptom | Check |
|---|---|
| Compose reports `DEMO_DB_PASSWORD` is missing | Create `.env` at the repository root and keep `--env-file .env` in the command. |
| Database authentication fails after changing the password | The existing volume retains its original database password. Coordinate recovery without deleting it. |
| `/health` works but `/ready` returns 503 | Confirm the database is healthy, uses host port 5433, and the backend loaded the correct password. |
| Readiness succeeds but registration fails | Confirm migrations, participant initialization, Hardhat, compiled artifacts, and the deployed address in `.env`. |
| Frontend cannot reach the backend | The current frontend requires `127.0.0.1:8001`; a server on 8000 does not satisfy it. |
| Port is already occupied | Identify the existing process/container before stopping anything. Do not start a second service on the same port. |
| Contract artifact cannot be found | Run `npx hardhat compile` inside `contracts/`. |
| Frontend reports an import error | Ensure `frontend/app.py` and `frontend/api.py` come from the same shared revision; run from the repository root. |
| Old profiles remain after restarting Hardhat | The database persisted while the local chain reset. Reconcile both states before further registrations. |
