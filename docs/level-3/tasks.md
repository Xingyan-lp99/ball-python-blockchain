# Level 3 - One-Week Implementation Roadmap

## Current State and Reading Order

### Latest Approved Checkpoint

The human has now confirmed successful website handover and the post-transfer
husbandry acceptance workflow: the buyer maintains their own records, prior
breeder-authored rows remain protected, and the former keeper no longer has
write rights. The core approved feature implementation is complete. These are
human-reported manual results, not newly executed automated tests. Unit tests
remain paused. The detailed implementation checkpoints below retain what the
agent actually checked at each earlier step.

Current collaboration task: commit and push the complete code, migrations, and
updated documentation to GitHub on the human's explicit request. Local settings,
uploaded files, PostgreSQL data, and Hardhat state are not part of Git sharing.
See the updated README for collaborator setup from migration 003 onward.

The original day-by-day entries below are historical and are not the current
feature status. The human has confirmed snake registration/query, account
registration/login, husbandry pages, V1 issuance by both laboratories, and
LAB001 V2 issuance. Certificate history and original PDF downloads are
implemented. Buyer-uploaded file verification and its match/mismatch cases
were explicitly removed from this iteration.

The keeper-transfer branch b527c1c was fetched and reviewed without switching
branches or merging. Its husbandry evidence contract and architecture changes
are not adopted. The approved small task adapts only its transfer logic into
the standalone [KeeperTransfers contract](../level-2/keeper-transfers.md),
preserving the existing SnakeRegistry and CertificateRegistry deployments.
The adapted contract compiled successfully; no unit tests were run.

The human approved preparation of backend/setup_keeper_transfers.py. Its syntax,
import, and required compilation artifacts were checked. The script deploys
against the existing registry or reuses an explicitly configured transfer
address. The human confirmed successful execution of this deployment script.

The authoritative keeper reader is implemented in backend/keeper_transfers.py,
and husbandry add/edit/delete checks now use it while retaining original-author
checks. Syntax, imports, and one read-only query of SNAKE001 succeeded; the chain
still showed the breeder as keeper and no pending proposal. FastAPI activation
requires the new contract address in its startup environment. No database write
or keeper transfer has been performed by the agent, and unit tests remain paused.

The human also approved breeder submission after an offline sale, buyer
accept/reject actions, current-keeper cancellation, and current-manager/transfer
status display in the profile. Migration 007 is prepared with transfer records,
confirmed-state timestamp constraints, one confirmed pending request per snake,
and a nullable transaction-to-transfer link. The agent has not applied it;
human execution is pending. Transfer submission APIs and the page follow in
separately approved steps.

The separately approved initiation backend is now implemented as POST
/api/v1/snakes/{snake_id}/keeper-transfers. It resolves a buyer username,
authorizes the signed-in current keeper, tracks submission, and stores Pending
only after verifying receipt/event/state evidence. Syntax, imports, OpenAPI,
and a read-only keeper query were checked. The agent has not executed migration
007 or submitted a transfer; full initiation remains unverified manually.
Recipient acceptance/rejection and initiating-keeper cancellation APIs are also
implemented. Their shared logic verifies receipt events and resolved chain
state; only acceptance updates the SQL current_keeper_id cache. Syntax,
imports, and authenticated OpenAPI declarations passed inspection. No write
routes were invoked, no chain transfers were submitted, and no unit tests ran.
The current-manager/transfer-status query is implemented as authenticated GET
/api/v1/snakes/{snake_id}/keeper. It combines live keeper/pending state with
the latest SQL request and transaction, exposing manager names/usernames and
explicit unconfirmed results. Syntax, imports, and OpenAPI checks succeeded;
the SQL-backed endpoint has not been manually exercised by the agent.
Streamlit Keeper Management is connected below profile fields for Buyer/Breeder,
with manager/username/status display and identity-dependent initiate, accept,
reject, and cancel controls. Writes refresh the keeper snapshot; uncertain
outcomes retain identifiers and lock repeat actions. Frontend syntax/imports
and the local required API declarations were checked without unit tests or
actual transfers. The running backend still required a restart at this check.
The human subsequently confirmed the website handover and post-transfer husbandry
workflow as recorded in the latest checkpoint above. The agent did not perform
those write actions or run the paused unit suite.

### Earlier Roadmap Notes

The design documents and logical diagram are prepared. The first backend health
endpoint and its test have been inserted by the human and verified. The human
also inserted Python database and blockchain connection checks and reported six
passing backend tests. Streamlit integration remains pending. The day numbers
below are a suggested sequence; completion is reported explicitly below.

New collaborators should read:
1. [AGENTS.md](../../AGENTS.md): scope and mandatory human-AI learning rules.
2. [Architecture](../level-0/architecture.md): stack and storage boundaries.
3. [Logical data model](../level-1/data-model.md): approved demonstration and permissions.
4. [Combined diagram](../diagram/data-model.drawio): editable overview.
5. [Backend modules](../level-1/modules.md): responsibilities inside FastAPI.

The Level 2 registration specification is currently empty. Before dependent
coding, discuss and document that small feature's agreed inputs, outputs, and
acceptance cases. Do not treat an empty document as an approved specification.

## Suggested Coding Sequence

Current small task: [backend health response](../level-2/backend-health.md).
The human approved GET `/health` -> HTTP 200 with `{"status": "ok"}`.
The human inserted the code and installed dependencies. On 2026-11-14, the health
test passed and a temporary Uvicorn server on port 8001 returned the exact agreed
HTTP response. Port 8000 is occupied by Docker; use 8001 for the local backend.
Dependency/cache warnings are recorded in the feature document. Other Day 1
services and frontend work progressed as recorded below.

The independent Compose project `ball-python-demo` runs PostgreSQL at local port
5433 with a separate volume; the old environment is retained. The human reported
a healthy database and successful SELECT 1, followed by three passing database/
health tests. Hardhat runs at 127.0.0.1:8545 with chain ID 31337 and 20 accounts;
the AI verified those RPC values. After web3.py integration, the human reported
six passing backend tests. The npm audit warning in the Hardhat dependency tree
remains unresolved; no automatic dependency fix has been applied.

The human inserted [backend/database readiness](../level-2/backend-readiness.md),
reported nine passing backend tests, and confirmed the successful live `/ready`
response. `/health` remains unchanged.

Current approved small task: [minimal Streamlit readiness page](../level-2/frontend-readiness.md).
Provide the HTTP helper, button page, dependency edits, and frontend tests in
chat for human insertion. The page checks both backend and database via `/ready`,
runs on local port 8502, and does not directly access PostgreSQL or blockchain.
Frontend tests and manual browser validation are pending.

| Stage | Tasks | Acceptance target | Status |
|---|---|---|---|
| Day 1: minimal skeleton | Start with a minimal FastAPI response; then connect PostgreSQL, start a local Hardhat chain, and create a simple Streamlit-to-FastAPI view. | The development services run and the page can reach the backend. | In progress: health endpoint verified; remaining integrations pending |
| Day 2: snake registration | Test Solidity registration and keeper queries; connect web3.py and off-chain profile persistence; add a registration view. | Breeder registers one snake and sees its profile and confirmed keeper. | Not started |
| Day 3: laboratory reports | Implement and test laboratory permissions, certificate issuance and correction; connect PDF storage and upload views. | LAB001 and LAB002 each issue V1; LAB001 appends V2 without replacing V1. | Not started |
| Day 4: file verification | Calculate a supplied PDF's hash, compare with chain evidence, and display match separately from version status. | Original V2 matches; modified V2 does not. Verification registers nothing. | Not started |
| Day 5: keeper transfer | Test transfer authorization and state; connect backend and initiate/accept views. | Breeder initiates and buyer accepts; confirmed chain state changes keeper. | Not started |
| Day 6: husbandry records | Add four simple parallel database tables and views; enforce current-keeper and original-author checks for writes. | Buyer can add/edit/delete their own rows; breeder rows remain read-only. | Not started |
| Day 7: rehearsal | Run the complete seven-step workflow, relevant tests, and key permission failures; prepare repeatable demo data and fix issues. | A clear end-to-end demonstration; actual test results recorded. | Not started |

Blockchain setup begins on Day 1 and core Solidity work begins on Day 2. FastAPI
integration runs throughout. Add only the simple frontend controls needed for
each working feature, then improve presentation during rehearsal. Do not spend
the week building separate complete layers before trying them together.

For every small task: explain workflow/step and proposed inputs/outputs, reasons,
and an example; wait for explicit agreement; provide code and relevant tests in
chat; the human inserts them; run appropriate checks and report actual outcomes.
Start with the minimal FastAPI response task, not the entire Day 1 at once.

## Two-Person Collaboration

- Use the shared GitHub repository and separate local clones. Private access is
  sufficient; invite the teammate as a collaborator rather than publishing it.
- Before starting, synchronize the latest shared work. Agree who owns each small
  task and use short-lived feature branches. Prefer different files when working
  at the same time.
- Review changes in a pull request before merging; communicate before changing
  shared interfaces. Human-AI coding restrictions apply to both contributors.
- GitHub synchronizes committed files, not chat sessions or local environments.
  Put agreed decisions and progress in documentation so both people have context.
- `docs/data_example/` is intentionally ignored. Share the fictional DOCX/PDF
  references separately and place them at that local path. Do not commit the
  virtual environment, secrets, or private keys.
- Keep this a one-week local demonstration. Do not add payments, production
  authentication, wallets, report parsing, or a marketplace.
