# Level 3 - Implementation Tasks

## Snake registration: database iteration (2026-11-12)

Status: **Complete** for the database stage. Automated checks passed, and the user
completed manual browser acceptance on 2026-11-12. Local-chain registration is now
implemented in the follow-up section below; real authentication and certificates remain pending.

### Implemented

- [x] Inspect existing docs, dependencies, code, services and API conventions.
- [x] Add a focused Snake Registry module with separate routes, schemas and service.
- [x] Add an ordered, transactional SQL migration and database unique/check constraints.
- [x] Implement `POST /api/v1/snakes` and `GET /api/v1/snakes/{snake_id}`.
- [x] Assign explicit server-side demo identity BR001 and initial manager.
- [x] Reject user-supplied server fields, invalid sex, blank ID and future birth dates.
- [x] Return 409 for duplicate IDs and 404 for missing IDs.
- [x] Add Streamlit registration/query forms with saved-profile display.
- [x] Label morph descriptions as breeder-provided and not laboratory certified.
- [x] Clearly distinguish database storage from blockchain/certificate verification.
- [x] Package new modules and migrations in the backend container.
- [x] Add Just commands and local run instructions.
- [x] Record the requested differences from Level 1 without editing higher-level docs.

### Tested

- [x] Backend: 26 tests passed against PostgreSQL, including direct database checks.
- [x] Real HTTP registration, Uvicorn process stop/start, and persistent lookup.
- [x] Repeat migration without losing the saved test profile.
- [x] Frontend: 5 Streamlit AppTest tests passed using mocked HTTP.
- [x] Apply migration to the existing development PostgreSQL database.
- [x] Validate Docker Compose configuration.
- [x] Build and start both application containers against the existing database volume.
- [x] Container HTTP smoke checks: API/database health, 404, 422 and Streamlit health.
- [x] Validate Just command listing.
- [x] Manual browser acceptance performed by the user: registration, lookup,
  duplicate-ID rejection, preservation of the original record, missing-ID feedback
  and status explanations all met expectations.

Container build/start results and remaining checks are recorded in
`snake-registration-development.md`.

### Pending

- [ ] Review and reconcile the broader Level 1 design with this requested database slice.
- [ ] Replace demo identity with real login and authorization.
- [x] Implement local-chain registration in the follow-up stage below.
- [x] Implement V1 issuance and independent file comparison in the stage below.

No existing contracts are changed. The user authorized a local feature commit after
acceptance; remote push and existing-data deletion are outside this iteration.

## Snake registration: local-chain iteration (2026-11-12)

Status: **Complete** for the local-chain registration stage. Automated checks passed,
and manual browser acceptance was performed by the user on 2026-11-12. The earlier
database-stage acceptance is unchanged. Historical-profile recovery after chain reset
remains pending.

### Implemented

- [x] Inspect and retain pre-existing Level 1, IDE and contract contents.
- [x] Follow project-local Hardhat and ethers toolbox skills.
- [x] Preserve Counter; add caller-bound SnakeRegistry and Ignition deployment module/script.
- [x] Reject empty/duplicate IDs; emit snake ID and manager evidence.
- [x] Map BR001 on the server to a local unlocked Hardhat development wallet.
- [x] Suppress node private-key output; keep runtime deployment metadata out of Git.
- [x] Add non-destructive versioned transaction-attempt migration.
- [x] Add explicit submit/retry and read/reconcile routes under `/api/v1`.
- [x] Enforce existing-profile/current-demo-manager restrictions and forbid signer overrides.
- [x] Persist intent before broadcast and hash before receipt checks; serialize demo signer.
- [x] Recover uncertain/hashless broadcasts and chain-success/database-failure cases.
- [x] Expose not-submitted, processing, confirmed and failed states with public evidence.
- [x] Revalidate scope/receipt/event/manager before reporting confirmation.
- [x] Preserve historical evidence and refuse silent rebinding after reset/redeployment.
- [x] Add UI submission/status refresh while retaining uncertified-description notices.
- [x] Connect existing Compose backend to the host's local chain using a read-only manifest.

### Tested

- [x] Hardhat build and TypeScript typecheck.
- [x] Contract tests: 10 passed (8 Solidity, 2 existing Mocha).
- [x] Backend: 53 tests passed with actual local-chain checks enabled, no skips.
- [x] Frontend tests: 10 passed, covering confirmation, pending, stale and timeout displays.
- [x] Actual Streamlit -> HTTP API -> PostgreSQL/web3.py -> Hardhat registration.
- [x] Independent direct contract manager, receipt and event reads.
- [x] Actual pending transaction, repeat request and conflicting wallet checks.
- [x] Real chain rejects mismatched instance, code hash and block-anchor evidence.
- [x] Simulated RPC failures, transaction revert, lost response and DB-write recovery.
- [x] Compose configuration, image build/start and container-to-host RPC access.
- [x] Manual browser acceptance performed by the user: correct lookup, new-profile
  submission to the local chain, transaction evidence after confirmation, consistent
  results after refresh, and certificates remaining unverified.

### Pending / outside this stage

- [ ] Real authentication and signing outside the local demo.
- [ ] Certificate V2/revocation lifecycle and manager transfers; V1 is implemented below.
- [ ] Explicit recovery/rebinding policy for profiles belonging to a reset local chain.
- [ ] Background reconciliation and production confirmation/reorg policy.

After manual acceptance, the user authorized a local commit with message
`feat: implement local-chain snake registration`. Remote push remains excluded. See
`snake-registration-chain-development.md` for evidence, commands and limitations.

## Laboratory certificate V1 and file verification (2026-11-12)

Status: **Complete** for certificate V1 issuance and verification. Automated checks
passed, and manual browser acceptance was performed by the user on 2026-11-12 for
CERT-LAB001-BP-S001 V1. Acceptance covers the implemented registration and byte-consistency
workflow; it does not establish biological truth or unimplemented lifecycle checks.

### Implemented

- [x] Preserve pre-existing working changes and current SnakeRegistry deployment.
- [x] Add caller-bound CertificateRegistry with administrator-controlled lab authorization.
- [x] Map LAB001 to a development wallet separate from BR001; no UI authorization controls.
- [x] Add version-ready SQL migration 003, immutable V1 uploads and typed issuance history.
- [x] Save exact original bytes with exclusive UUID names on a persistent document volume.
- [x] Compute SHA-256 on the server; reject supplied hash, issuer, wallet, lab and version fields.
- [x] Add upload, metadata/list, issuance/poll, original download and verification routes.
- [x] Share lock/status/receipt mechanics with snake registration and preserve recovery.
- [x] Primarily compare actual stored bytes against fresh on-chain V1; external upload is optional.
- [x] Distinguish match/mismatch/unable and separate registration status from file comparison.
- [x] Add Breeder/Laboratory/Buyer demo workspaces and explicit identity/trust limitations.
- [x] Keep latest-version/revocation flags false and avoid whole-snake certification claims.
- [x] Document missing formal input and BP-S001 preconditions.
- [x] User supplied BP-S001_Certificate_V1.pdf through LAB001 upload; original bytes preserved.
- [x] BP-S001 database profile exists; normal BR001 chain registration completed during conflict repair.

### Tested

- [x] Contract build/typecheck; 18 contract tests passed, including 8 new certificate tests.
- [x] Backend: 99 passed with actual local-chain checks enabled, no skips (including issuance-conflict regression).
- [x] Frontend: 22 passed, including 12 certificate tests.
- [x] Actual HTTP upload, issuance and independent contract/receipt/event verification.
- [x] Actual unauthorized-wallet/missing-chain-snake rejection and lost pending-hash recovery.
- [x] Exact-byte download, filename independence, modified bytes and immutable repeat requests.
- [x] RPC/absent/stale evidence, cache independence, revert and DB-write failure recovery.
- [x] Image rebuild/container recreation followed by byte-identical PDF download and matching check.
- [x] Earlier retained snake registration remains confirmed after new deployment/rebuild.
- [x] Manual browser acceptance performed by the user: CERT-LAB001-BP-S001 V1 is
  confirmed at block 46; Buyer finds it through BP-S001, direct verification matches,
  and PDF preview/download work normally.

### Pending / excluded

- [ ] V2, revocation, real authentication/signing and manager transfers.
- [ ] Explicit historical recovery after reset and orphan-file/backup policies.

After acceptance, the user authorized a local commit with message
`feat: implement certificate v1 issuance and verification`. Remote push remains excluded.
See `certificate-v1-development.md`.

### Primary verification flow refinement

- [x] Buyer queries a snake profile and selects from that snake's certificate list.
- [x] Provide original PDF preview/download and primary 核验证书 action without re-upload.
- [x] Re-read stored original bytes and SHA-256 each time; ignore cached DB digests.
- [x] Keep external upload comparison in a separate optional collapsed entry.
- [x] Verify both modes cannot create certificates, overwrite originals or sign issuance.
- [x] Test wrong cached digest, changed stored bytes, absent file and unavailable RPC.
- [x] Real-chain page automation: lab uploads/issues, buyer queries the profile/list and
  clicks 核验证书; chain nonce unchanged by verification.
- [x] User performed browser acceptance of lab issuance -> buyer snake query -> direct verification,
  including preview/download, on CERT-LAB001-BP-S001 V1 confirmed at block 46.

### CERT-LAB001-BP-S001 first-issuance conflict repair

- [x] Reproduce HTTP 409 and inspect backend logs, current referenced contracts and database history.
- [x] Establish actual cause: BP-S001 existed only in PostgreSQL; LAB001 was authorized;
  no on-chain V1, no issuance attempt, no pending transaction/processing marker.
- [x] Split preflight reasons, expose structured errors and show them on Refresh before any attempt.
- [x] Disable Issue while blocked, retaining the normal registration/authorization/immutability checks.
- [x] Register BP-S001 through BR001 at block 45, then issue existing V1 once through LAB001 at block 46.
- [x] Independently verify receipt, event, chain record, exactly one confirmed DB attempt and unchanged PDF.
- [x] Add real-chain missing-prerequisite -> normal registration -> successful first issue regression.
- [x] Add adapter error-branch and UI error/disabled-button/refresh regression coverage.

No chain reset, PDF replacement, record overwrite or authorization bypass. Local commit
was authorized only after the subsequent user acceptance; no remote push is authorized.
