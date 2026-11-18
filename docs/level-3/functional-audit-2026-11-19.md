# Functional audit — 2026-11-19

## Scope and authorization

The human authorized checking all existing website functions and directly
repairing failures or missing contract configuration. Existing business data,
credentials, uncertain-write protections, and role permissions must remain intact.
No production feature, schema, contract logic, or business API was added.

## Automated acceptance audit

`backend/tests/test_demo_workflow_audit.py` creates a separate PostgreSQL database,
starts an independent Hardhat node on an available loopback port, deploys the
existing compiled contracts, and redirects uploaded files to a temporary directory.
The database and node are removed/stopped in fixture teardown. The running demo
database, chain, accounts, sessions, and stored uploads are not used for writes.
Test credentials and tokens are generated only in the isolated workflow and are
not printed. Hardhat account output is discarded rather than logged.

The audit passed after correcting an expiry-test query that referenced a
nonexistent test column. It covers:

- Account registration for breeder, buyer, and both labs; duplicate account
  rejection; sign-in, wrong passwords, authenticated identity, logout, and expiry.
- Snake registration, breeder-only authorization, duplicate prevention, profile
  retrieval, missing IDs, photographs, random profiles, and public photo previews.
- Both laboratories issuing V1, issuer-only V2 revision, version history and
  superseded status, original PDF download, and SHA-256 consistency.
- Growth, shedding, feeding, and health record creation, editing, and deletion.
- Keeper initiation, recipient-only acceptance/rejection, sender cancellation,
  duplicate-pending prevention, and confirmed keeper status after acceptance.
- Former-keeper write rejection and protection of records authored by others.
- Actual Streamlit login and all role workspaces through AppTest, connected to
  the isolated real backend. Profile panels and normal reruns issue no writes.
- Husbandry uncertain-write locks and explicit successful refresh before unlock.
- Missing registration, certificate, and keeper configuration: no transaction or
  false success; retained PDF download works without available chain evidence.

Run from the repository root in PowerShell:

```powershell
$env:RUN_DEMO_WORKFLOW_AUDIT = "1"
uv --no-cache run --no-sync --env-file .env python -m pytest backend/tests/test_demo_workflow_audit.py -q -s --tb=short -p no:cacheprovider
```

Prerequisites: PostgreSQL on port 5433, the local database credential loaded by
`uv`, permission to create a temporary database, Node.js/Hardhat installed, and
the three existing contract artifacts compiled. The test does not require or
modify the running demonstration chain. Without explicit opt-in it is skipped.

An additional focused run passed 19 existing tests in `test_health.py`,
`test_ready.py`, `test_database.py`, `test_blockchain.py`, and
`test_register_snake.py`. The historical full repository suite was not run;
older readiness-page tests do not describe the current frontend. Dependency
deprecation warnings remain; they did not fail these checks.

## Running demonstration: read-only verification

- Backend health and database readiness return HTTP 200.
- SnakeRegistry, CertificateRegistry, and KeeperTransfers are configured and
  have deployed code on the current local chain, ID 31337.
- BP-S001 is registered on this chain. Its four stored certificate versions
  have matching confirmed evidence. Its keeper state is available.
- All three stored profile photos are present.
- All eight original PDFs are present, downloadable, and match stored SHA-256.
- Profile, photo, history, keeper-status, and four husbandry-read routes respond
  for all stored snakes. Existing-data route checks substitute a read-only
  account identity only inside the local test process; they do not create or
  read real login tokens. Authentication itself is tested in the isolated audit.

## Preserved limitation: records from the previous local chain

SNAKE001 and SNAKE002 remain in PostgreSQL, but are not registered in the current
SnakeRegistry. Their four old certificate versions have no confirmable evidence
on this chain. Their photos, PDFs, and off-chain husbandry history remain readable.
Keeper-dependent writes and revisions of the old certificate series cannot be
considered usable until the matching old chain state is recovered.

These are not missing current contract configuration. Re-registering the IDs,
reissuing reports, changing stored transaction hashes, or assigning a keeper
would create different evidence and must not masquerade as historical recovery.
No such operation was performed. Genuine recovery requires the corresponding
old Hardhat state/snapshot or a separately defined migration that preserves
the distinction between old and new evidence.

Hardhat's ordinary development node is ephemeral. Restarting it can remove
deployments while PostgreSQL and uploaded files remain. A healthy `/ready`
response confirms database connectivity only, not contract deployment or
historical chain evidence.

AppTest establishes widget behavior and API flows, not browser CSS rendering.
No commit or push was performed for this audit.
