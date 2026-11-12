# Certificate V1 - Development and Acceptance Record

Date: 2026-11-12 (Europe/Berlin)

Status: **Certificate V1 stage complete**, including automated checks and manual browser
acceptance performed by the user on 2026-11-12. The user confirmed CERT-LAB001-BP-S001 V1
at block 46, lookup through BP-S001, a matching direct verification, and working PDF
preview/download. A local feature commit was authorized after acceptance; remote push
is excluded. No chain/database reset, original-file replacement or existing-data deletion.

## Baseline and implementation decisions

Baseline commits: database `91998923146d12d44da49f3eeebee0307d6c3596` and local chain
`e1f3c2d57de98d68563a42cbfe1d5853c231d6d3`. Read root/contract AGENTS, Level 0/1 docs,
registration spec/tasks, current contract/deployment, chain adapter/recovery and UI.
Followed project-local Hardhat and ethers toolbox skills. Preserved pre-existing mixed
contract config/README content, Counter files, Level 1 edit and IDE files. Their baseline
content hashes are kept in ignored `.local/certificate-v1-baseline.json` for comparison.

Keep the running SnakeRegistry unchanged. Add a CertificateRegistry referencing that
exact deployment, with administrator authorization and caller-bound issuance. This
avoids losing registered snakes by replacing a non-upgradeable registry. Deployment
through the existing Ignition stack also authorizes LAB001. No public network is used.

LAB001 uses development account 1; BR001 keeps its existing account 0. The deployment
administrator is account 0, and no ordinary API/page exposes authorization. Keys stay
inside the existing Hardhat node. The UI workspace selector changes demonstration
operations only; it is not authentication or a production permission system.

PDF names supplied by users are metadata. Files use exclusively created UUID names,
exact bytes, fsync and a persistent named volume. Certificate/header/version/attempt
tables separate immutable evidence from transaction progress and support future inserts
of another version. Only V1 endpoints exist now. No received PDF is regenerated.

Shared transaction helpers were extracted from the existing snake flow: the same
dedicated-connection advisory lock, status mapping and receipt persistence. Certificate
adapter reuses local scope/receipt/pending sender-nonce lookup. Intent/hash commits,
uncertain responses and chain-success/DB-write recovery are preserved. The old snake
tests and retained live snake profile remain valid after the change.

Primary buyer verification reopens the platform's actual PDF, hashes its current bytes
and reads the current contract V1, receipt and event. No buyer upload is needed. Optional
external-file comparison independently hashes the uploaded bytes. Neither mode trusts
filenames or a DB digest. Tests alter a cache and an isolated stored file to prove both
the live-chain and actual-file boundaries.
Registration status and byte-comparison results are separate, with no aggregate
snake-certified flag or unsupported latest/revocation check.

## Files changed

- `contracts/contracts/CertificateRegistry.sol` and `.t.sol`.
- `contracts/ignition/modules/CertificateRegistry.ts` and
  `contracts/scripts/deploy-certificate-registry.ts`.
- `backend/certificates/`: models, storage, adapter, business service and HTTP routes.
- `backend/blockchain/`: shared transaction mechanics extracted from registration.
- `backend/migrations/003_certificate_v1.sql`.
- Existing backend main/identity, snake adapter/recovery, Dockerfile, dependencies/lock.
- `backend/tests/pdf_fixtures.py`, `test_certificates.py`, `test_certificate_e2e.py`,
  and migration-count assertion in the existing snake test.
- `frontend/certificate_page.py`, main, Dockerfile and certificate page tests.
- Compose document volume/configuration, Just deployment recipe, backend/frontend READMEs.
- Level 2 certificate spec, Level 3 tasks/this record and sample-input instructions.

No Level 0 or Level 1 content is changed by this iteration. Existing Level 1 data-model
work stays outside this feature's edits. Current global public certificate IDs and
demo lab labels are documented simplifications; broader multi-lab design remains open.

## Actual validation

| Check | Executed result |
|---|---|
| `npx.cmd hardhat build` from contracts | Passed; new contract/test compiled using existing solc 0.8.34 |
| `npx.cmd tsc --noEmit` after compilation | Passed |
| `npx.cmd hardhat test` | **18 passed**: 16 Solidity, 2 existing Mocha; 8 new certificate tests |
| `$env:RUN_LOCAL_CHAIN_TESTS='1'; .venv/Scripts/python.exe -m pytest -q -ra` from backend | **99 passed, no skips**, including the first-issuance conflict repair |
| `.venv/Scripts/python.exe -m unittest discover -s tests -v` from frontend | **22 passed**, including 12 certificate tests |
| Current-chain deployment and lab authorization | Passed; original snake deployment retained, separate lab wallet authorized |
| Actual HTTP multipart upload/issue/verify | Passed against real Uvicorn, PostgreSQL and Hardhat |
| Direct contract storage/receipt/event checks | Passed; V1 subject, issuer, version and SHA-256 agree |
| Actual unauthorized wallet/missing chain snake | Rejected by contract calls |
| Actual pending issuance/lost hash | Removed only the isolated test row's hash, recovered it from the real pending transaction, repeated request retained it, mined/confirmed; automining restored |
| Original/renamed bytes versus modified bytes | Match/match/mismatch, including different bytes with the same filename |
| Original download after image rebuild/container recreation | **Byte-for-byte identical**, then fresh chain comparison matched |
| RPC/absent/stale evidence and hash-cache independence | Passed with isolated DB/mock failures; unable never misreported as mismatch/pass |
| Revert and chain success followed by DB-write failures | Passed; new attempt/recovery retained original V1 and avoided duplicate send |
| Compose configuration and image build/start | Passed; migration 003 applied without deleting existing data |
| Earlier retained snake `LOCAL-b4c680626bc3` | Still confirmed on current chain after deployment/rebuild |
| Live buyer primary flow with actual HTTP | Queried the snake profile/list, selected V1 and clicked 核验证书 without uploading; matched actual stored bytes/live chain; lab transaction nonce unchanged |
| Stored-file integrity failure checks | Wrong DB cache ignored; changed temporary stored bytes detected; missing file and unavailable RPC yield unable |
| Both verification routes are non-signing | No new certificates, files, versions or issuance attempts; lab original retained and send count unchanged |
| Manual browser acceptance performed by the user (2026-11-12) | CERT-LAB001-BP-S001 V1 confirmed at block 46; Buyer lookup through BP-S001, matching direct verification, PDF preview/download all accepted |

The full backend run includes 42 certificate workflow tests, 4 real-chain
certificate tests and the prior 53 tests. Real checks are opt-in; without
RUN_LOCAL_CHAIN_TESTS=1 the ten real-chain checks are explicitly skipped. An unavailable
PostgreSQL also skips DB checks. Those skips are not equivalent to the full result above.
The frontend unit suite uses mocked HTTP; additional live page reads and real multipart
API checks are separate. The actual buyer page automation now also clicks the direct
stored-file verification action. Browser
file-picker/download interaction was subsequently accepted by the user, not performed
by the coding agent. This acceptance/documentation update does not rerun the automated
suites; the recorded 99 backend, 22 frontend and earlier contract results remain the
actual implementation-run evidence.

An initial Solidity duplicate test placed sha256 computation after expectRevert; its
precompile consumed the next-call expectation. Moving the digest calculation before
the expectation fixed the test; final contract results above passed. Starlette's
httpx deprecation warning and AppTest bare-mode notices remain, without test failures.

## Retained test-only live evidence

This example is not the missing BP-S001 formal certificate. Its PDF visibly says TEST
ONLY and includes the test certificate/snake IDs. Both records remain in the current
development database and chain for manual inspection.

| Item | Observed value |
|---|---|
| Certificate | `CERT-V1-TEST-b59407` |
| Snake | `SNAKE-TEST-b59407` |
| Lab | `LAB001` / `Demo Laboratory LAB001` |
| Lab wallet | `0x70997970C51812dc3A010C7d01b50e0d17dc79C8` |
| Breeder wallet | `0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266` |
| CertificateRegistry | `0xA51c1fc2f0D1a1b8494Ed1FE312d7C3a78Ed91C0` |
| Referenced SnakeRegistry | `0x5FbDB2315678afecb367f032d93F642f64180aa3` |
| Chain / version | `31337` / `1` |
| Transaction | `0x06a3393d05b49a51207dda77399a60ba0f5698d5bbfb81d7e07302b442d2fa46` |
| Confirmed block | `28`, receipt status `1` |
| SHA-256 of original 647 bytes | `b37599ecd08eb4cb52e71f9747e49dcff67e44abf3d91278513fc958e6a4764d` |

Ignored local originals: `.local/certificate-v1-test-original.pdf` and
`.local/certificate-v1-test-modified.pdf`. The modified file was derived from this
original by replacing equal-length ORIGINAL/MODIFIED text; no V2_MODIFIED input was
used. `.local/certificate-v1-demo.json` stores public evidence and the completed
container-rebuild check. No key is included. Evidence is an observation of this local
instance, not a guarantee after reset.

## Run and manual browser acceptance

The current node and both apps are running. Open `http://localhost:8501`.
For application restart/build, reuse the current manifests and named volumes:

```powershell
docker compose up -d --build backend frontend
```

Deploy the certificate extension only if it has not been deployed for this verified
snake instance: `just deploy-certificates`. Do not rerun `just deploy-registry` for this
feature or redeploy either contract on every application restart. If a node is not
running, `just chain` starts the existing wrapper without logging keys; an erased
previous instance still needs an explicit historical recovery policy, not silent reuse.

For local Python, run `just migrate`, `just backend` and `just frontend` in separate
terminals. Local manifest defaults are `.local/snake-registry.json` and
`.local/certificate-registry.json`. Compose sets CERTIFICATE_CHAIN_DEPLOYMENT to its
read-only public manifest mount and CERTIFICATE_STORAGE_DIR to the document volume.
Root .env and existing installations remain in use. Only python-multipart was added.

Priority manual acceptance: Laboratory uploads and issues, then Buyer queries the
snake profile, selects its listed certificate and directly clicks 核验证书. A second
PDF upload is not part of this primary acceptance path.

Manual checks using the retained TEST ONLY example:

1. Choose Breeder and query SNAKE-TEST-b59407; profile/uncertified morph labels remain.
2. Choose Laboratory. Confirm the demo/代签 limitations, select CERT-V1-TEST-b59407,
   and inspect snake ID, LAB001/name, wallet, version 1 and transaction/block evidence.
3. Use 下载证书 PDF or 预览证书 PDF for the selected platform original. Compare downloaded
   bytes/hash with `.local/certificate-v1-test-original.pdf`; content visibly says TEST ONLY.
   Embedded preview depends on browser PDF support; direct download remains available.
4. For new issuance, create/register a new test snake through existing Breeder actions,
   then in Laboratory save a test PDF under a new certificate ID and explicitly issue V1.
5. Choose Buyer, enter SNAKE-TEST-b59407 in 球蟒编号 and click 查询球蟒档案. Inspect the
   profile and certificate list, select CERT-V1-TEST-b59407 and click 核验证书. Expect a
   platform-source match without any file upload. Check selected snake/lab/version,
   file hash and chain transaction basis; no whole-snake certification claim is made.
6. Optionally expand 上传外部文件核验（可选）. Original/renamed original matches; a
   modified PDF differs, even with the same filename. This comparison does not create
   a certificate, replace the original or issue a transaction. Registration status is
   separate; latest-version and revocation checks remain unimplemented.
7. Repeat/save the identical V1: it should retain original content and avoid another
   issuance transaction. Different bytes under that certificate ID must be refused.
8. Refresh/reselect and confirm current evidence. Recheck with the direct button if a
   fresh comparison is desired; a prior result is not reused as a new check.

The primary-flow adjustment changes no Solidity or schema. Contract build/test results
above are from the initial V1 implementation; contracts were not redeployed or retested
for this interaction-only refinement. Rebuilt and restarted application containers
reuse the current chain, database and file volume. Actual reads against the retained
demo match its original digest, and the original bytes/issuance transaction stay unchanged.

Do not stop/reset the user's chain merely to perform fault tests. Automated failure
checks cover unavailable/stale conditions; history and PDFs must stay intact.

## Initial formal-input gap and later update

No BP-S001_Certificate_V1.pdf was found. Expected path:
`docs/samples/certificates/BP-S001_Certificate_V1.pdf`. At the actual precondition check,
BP-S001 returned database **404** and had **no current chain registration**. Neither
profile nor formal certificate was invented. Before formal acceptance, inspect the
file's actual certificate ID, lab name and snake ID, reconcile its lab mapping, and
create/register BP-S001 on the current deployment. Use that exact original V1 for any
derived modification test; never substitute a pre-existing V2_MODIFIED file.

The later user reproduction supplied the original through platform upload and created
the BP-S001 database profile. The missing chain prerequisite was repaired below; file
supply and BP-S001 registration are no longer pending. The user subsequently accepted
the formal V1 browser workflow. That technical acceptance and byte matching do not
validate biological findings or unimplemented latest-version/revocation behavior.

Pending: V2/revocation, real identity/signing, transfers, historical
reset recovery, backup/disaster recovery and orphan-file policy. Upload screening is
basic PDF header/EOF detection, not full document security analysis. File fsync followed
by a failed metadata commit may leave an unreferenced file; it is retained for future
explicit reconciliation, without automatic deletion. Named-volume deletion is not a
supported durability scenario. No production latest/revocation/finality claims are made.

## Actual first-issuance conflict: CERT-LAB001-BP-S001

On 2026-11-12 the user reported Issue -> generic 409, followed by Refresh ->
not_submitted/null hash. Reproduced this against the running container API, not a mock.

Evidence before repair:

- Certificate ID CERT-LAB001-BP-S001, version 1, database snake BP-S001; breeder and
  current manager both BR001. No extra version or issuance attempt existed. There was
  no pending/failed issuance transaction or stuck processing marker to clear.
- CertificateRegistry `0xA51c1fc2f0D1a1b8494Ed1FE312d7C3a78Ed91C0` references the current
  SnakeRegistry `0x5FbDB2315678afecb367f032d93F642f64180aa3`; manifests/scope matched.
- LAB001 actually signs as `0x70997970C51812dc3A010C7d01b50e0d17dc79C8`, and that wallet
  was already authorized. No lab authorization change was needed.
- The referenced registry returned no manager for BP-S001. Its DB snake registration
  history was empty. The certificate contract returned no V1 record for this ID.
- Original filename BP-S001_Certificate_V1.pdf, 45,064 bytes; actual download SHA-256
  agreed with both stored file/version digests. No upload replacement was needed.

The exact failing branch was CertificateChain.assert_can_issue checking the missing
snake, before intent creation or broadcast. The old handler combined that branch with
unauthorized lab/content conflict; the frontend replaced HTTP detail with another generic
409 message. Refresh returned immediately when no attempt existed, hiding the same
missing prerequisite. Thus not_submitted/null was accurate transaction state, not a revert.

Fix:

- Distinct preflight codes/messages for missing chain snake, unauthorized lab, issuer
  wallet mismatch and actual certificate-record conflict. Do not bypass any check.
- Return structured HTTP detail and safe diagnostic log. Metadata/status refresh checks
  preflight even with no attempt, showing the reason without manufacturing a failed tx.
- Show exact backend error on the page, retain its code/reason on Refresh and disable
  Issue while blocked. Completing the normal prerequisite then refreshing clears it.
- Preserve recovery for matching chain success and preserve immutable conflicting V1.

Observed log after fix:

```text
certificate_issue_blocked code=snake_not_registered certificate_id='CERT-LAB001-BP-S001' snake_id='BP-S001'
```

Actual data repair used the existing authorized workflows: POST the BP-S001 registration
as server BR001, then POST this existing V1 issuance as LAB001. No synthetic profile,
replacement file, manual DB status edit, contract redeployment/reset or new lab grant.

| Item | Verified result |
|---|---|
| Snake registration | Block 45, confirmed under BR001 wallet |
| Snake transaction | `0x409ddc9508514ea96404be070fcb559688b5028d47c35c5b6126a0f8ab1839dd` |
| Certificate issuance | Block 46, receipt status 1, confirmed under LAB001 |
| Certificate transaction | `0x06b9c78e9789f4fab31480b34f9b69765e810502175ed209419a37eee7b4f885` |
| Original SHA-256 before/after | `e5cb1de883ca64ab75a68e70f58f8f5d83fe9d06696d6ecbd03b086e796281a5` |
| Original size | 45,064 bytes, exact byte equality before/after |
| Database history | Exactly one confirmed issuance attempt; version remains 1 |
| Chain evidence | Actual caller/calldata, canonical receipt, event and V1 record agree |
| Direct platform-file verification | match, using freshly read file bytes and live chain hash |

Public repair evidence is saved in ignored `.local/certificate-issue-repair.json`.
The lab nonce increased by exactly one for issuance; no duplicate signature/transaction
was sent. Original PDF and all prior records remain intact. Tests include the real
missing-snake first-issue case, zero nonce change on refusal, refresh reason, normal
breeder registration, one successful issuance and unchanged bytes. UI tests exercise
specific HTTP errors and the disabled Issue button clearing after refresh. Current full
results are 99 backend and 22 frontend passes; no Solidity/schema change was needed.

Manual follow-up: refresh Laboratory's selected CERT-LAB001-BP-S001 to see confirmed
evidence, or choose Buyer, query BP-S001, select its V1 and click 核验证书 without upload.
The corresponding post-repair live AppTest flow was executed against the current
container API: Laboratory displayed confirmed evidence with no stale preflight error;
Buyer queried BP-S001, selected this certificate and directly obtained a stored-file
match. The PDF digest was checked again afterward and remained unchanged.
These automated checks are distinct from the subsequent user-performed browser
acceptance below. The root cause, repair steps and regression results above are retained.

## User acceptance and local commit scope

On 2026-11-12 the user reported manual browser acceptance: CERT-LAB001-BP-S001 V1
displayed confirmed with block 46, Buyer found the certificate through BP-S001, direct
verification matched, and PDF preview/download worked. This completes the implemented
V1 stage. It does not claim V2, revocation, real authentication, transfers or biological
validation. Those unimplemented features and reset/orphan/backup policies remain pending.

The user authorized the local commit message
`feat: implement certificate v1 issuance and verification`, with no remote push. Include
only V1 contract/deployment/test files, backend/storage/transaction recovery and error
fixes, buyer/laboratory UI, runtime configuration/dependency changes and related docs.
Keep pre-existing contract README/config sample additions, Counter files/scripts,
agent/IDE files and the Level 1 edit outside the commit. Exclude environment files,
keys, databases, runtime logs, original PDFs, local test/demo products, generated build
artifacts and deployment manifests/journals. Preserve all original working contents.
