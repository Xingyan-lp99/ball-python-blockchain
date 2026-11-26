# Collaborator handoff - 2026-11-26

Repository: https://github.com/Xingyan-lp99/ball-python-blockchain

Use the current `main` branch. This handoff supersedes the November 19 UI and
setup notes where they differ. Read [AGENTS.md](../AGENTS.md) before editing.

## Included in the source handoff

- Streamlit frontend, current logo/photos/fonts and font licenses.
- FastAPI backend, account and husbandry modules, certificate V1/V2 workflows,
  and Anvil/Sepolia registration and Keeper Transfer integration.
- Solidity sources and tests, Hardhat configuration, pinned Python and npm
  dependency lockfiles, PostgreSQL migrations 001 through 012, and task commands.
- Persistent local Anvil management and local backup/readiness tools.
- Sepolia acceptance JSON fixes, read-only verification, idempotent database
  recovery, and frontend reconciliation of an uncertain submission.
- Architecture, data-model, design-reference and historical audit documents.

No new transactions were sent for this handoff. BP-S004/BP-S008 business data
and existing checkpoints were not changed by the acceptance repair or packaging.

## What GitHub does not transfer

The repository is public. Local `.env`/`.env.sepolia`, RPC credentials, private
keys, login credentials, PostgreSQL contents, uploaded reports/photos, backups,
logs, and local chain/deployment checkpoints are not part of this source package.
The `exports/` directory contains old snapshots and conversation exports and is
also excluded. Rebuild dependencies and artifacts locally.

Cloning the source does not reproduce the owner's running database or registered
pets. A matching runtime/data handoff is a separate task; never mix another
chain's checkpoint with an unrelated database. Do not publish such a backup in
this public repository.

## Get the code

For a new Windows PowerShell checkout:

```powershell
git clone https://github.com/Xingyan-lp99/ball-python-blockchain.git
Set-Location ball-python-blockchain
uv sync --locked --python 3.12
Set-Location contracts
npm ci
npx.cmd --no-install hardhat compile
Set-Location ..
```

For an existing clean checkout, inspect `git status`, then use
`git pull --ff-only origin main`. Preserve local changes and resolve divergence
without resetting or force-pushing another collaborator's work.

Prerequisites are Git, Python/uv, compatible Node.js/npm, Docker Desktop, and
PowerShell. `just` is optional for the provided Windows task recipes. The local
chain manager installs its checked Anvil binary on first use; Hardhat is still
used to compile contracts. Installation can require network access.

## Initialize a separate local demonstration

Follow [README first-time setup](../README.md#first-time-setup), with these
current requirements:

1. Create your own ignored `.env` with `DEMO_DB_PASSWORD`. Do not reuse the
   owner's credentials. There is no tracked environment file.
2. Start PostgreSQL and apply migrations **001 through 012**, in filename order,
   only to a fresh database. On an existing database, first determine which
   migrations have already been applied. Migration 009 removes an old column;
   preserve existing data before applying schema changes.
3. Compile artifacts, start the persistent Anvil node, deploy your local
   SnakeRegistry, and seed the four participants. Save your local addresses as
   `DEMO_REGISTRY_ADDRESS`, `DEMO_CERTIFICATE_REGISTRY_ADDRESS`, and
   `DEMO_KEEPER_TRANSFERS_ADDRESS` in `.env` as each contract is initialized.
4. Initialize CertificateRegistry and laboratory issuance permissions using the
   existing local setup module. Public registration creates Buyer/Breeder
   accounts only. Laboratory login accounts require separate local provisioning;
   participant seeding and on-chain lab permission setup do not create logins.
5. The existing `backend.setup_keeper_transfers` bootstrap reads `SNAKE001` from
   SnakeRegistry. Register that fictional pet on your own local chain first,
   then run the following once and retain the printed KeeperTransfers address:

   ```powershell
   uv run --locked --env-file .env python -m backend.setup_keeper_transfers
   ```

   Start the backend/frontend manually during bootstrap, as described in README.
   `just up` is for an initialized environment: its readiness checks require all
   three configured contracts. Restart the backend after updating `.env`.
6. Normal Mode login works with your own accounts. Demo Mode additionally requires
   an ignored `storage/frontend-demo.json` with `enabled: true` and credentials
   for `Seller`, `Buyer`, `Lab 1`, and `Lab 2`. Those accounts must already exist
   and bind to BREEDER001, BUYER001, LAB001, and LAB002 respectively. Configure
   this locally; do not commit it. Without it, Enter Demo Mode is disabled.

Local URLs after startup:

- Frontend: http://127.0.0.1:8502
- Backend API documentation: http://127.0.0.1:8001/docs
- PostgreSQL host port: 5433
- Anvil JSON-RPC: http://127.0.0.1:8545 (chain ID 31337)

These URLs refer to the computer opening them. GitHub is the source repository,
not a hosted Streamlit deployment. Fresh-clone setup on a collaborator's computer
has not been executed as part of this packaging step.

## Sepolia configuration is separate

Sepolia code is included, but the owner's operational signing session is not.
The backend expects an ignored `.env.sepolia` containing an HTTPS
`SEPOLIA_RPC_URL` and the public `SEPOLIA_BUYER_ADDRESS`, plus the matching
deployment evidence at `storage/sepolia/sepolia-p0-001/state.json` and compatible
compiled artifacts. Anvil addresses cannot substitute for Sepolia deployments.

Setting `SEPOLIA_DEMO_SIGNING=1` enables an interactive backend startup that
requests the configured demonstration keys through hidden terminal input and
keeps them in memory. Do not use the background `just backend` startup for that
mode, commit private keys, or place them in command-line arguments. Coordinate
the authorized setup separately before operating against the existing demo.

Do not run `scripts/sepolia_demo.py` as a generic startup command: it is a
separate deployment/demo utility with its own configuration and explicit write
mode. A fresh clone should not redeploy or replay existing transactions.

## Acceptance behavior and verification results

The ordinary Accept result includes `recipient_username` and is validated against
the existing response model before the final database confirmation updates.
Read-only `GET /api/v1/sepolia/keeper-acceptance` checks the saved acceptance
identity, canonical Receipt, event, database state and a separate latest Keeper
snapshot. An authenticated `POST /api/v1/sepolia/keeper-acceptance/recover` may
synchronize missing database state using the existing successful transaction;
it has no signing or broadcast path. Repeated recovery of consistent records
does not write them again. Refresh uses verification, not database recovery.

The targeted mock regression completed on November 26: **60 passed, 0 failed**,
with two dependency deprecation warnings. Seven changed Python files also passed
syntax checks. Coverage included 33 new acceptance tests, 5 existing registration
tests, 8 existing keeper tests, 4 Demo Mode tests, and 10 laboratory UI/API tests.
This is not a full-suite or live Sepolia transaction acceptance claim.

Run the same isolated regression without enabling Sepolia signing:

```powershell
$keeperTestTemp = Join-Path 'storage' ('pytest-keeper-' + [guid]::NewGuid().ToString('N'))
uv run python -m pytest backend/tests/test_keeper_acceptance_verification.py backend/tests/test_sepolia_keeper_status_route.py backend/tests/test_registration_network_routing.py frontend/tests/test_keeper_acceptance_frontend.py frontend/tests/test_sepolia_keeper_status.py frontend/tests/test_registration_network.py frontend/tests/test_demo_mode.py frontend/tests/test_demo_account_ids.py frontend/tests/test_report_selection.py -q --basetemp=$keeperTestTemp
```

Do not use the historical full suite as a read-only smoke test: some older tests
deploy contracts or write to a local database/chain. The selected files above use
mocked service/database/chain interactions for this regression.
