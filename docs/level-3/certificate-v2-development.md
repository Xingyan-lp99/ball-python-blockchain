# Certificate V2 Development Record

Date: 2026-11-13. Baseline V1 commit:
`07c2895c18ec2c8989cafa618a82d8f04da65965`.

## Deployment decision and retained evidence

Inspected AGENTS, documentation hierarchy, V1 spec/development record, contract,
adapter, recovery and Streamlit before changes. Applied the repository Hardhat and
toolbox skills for contract tests/deployment. Existing README/config/Level 1 and
agent/IDE/sample changes remain untouched. Baseline byte hashes were retained under
ignored `.local/certificate-v2-baseline.json` and rechecked after implementation.

The current legacy contract has only issueV1 and immutable code. Added a separate
VersionedCertificateRegistry rather than pretending edited Solidity upgrades it.
The new deployment references the existing SnakeRegistry and uses the same separate
LAB001 development signer. No reset, public chain, key handling or authorization bypass.

| Deployment | Address | Evidence |
|---|---|---|
| Existing SnakeRegistry | `0x5FbDB2315678afecb367f032d93F642f64180aa3` | Retained unchanged |
| Legacy CertificateRegistry | `0xA51c1fc2f0D1a1b8494Ed1FE312d7C3a78Ed91C0` | Existing formal V1 block 46 |
| New VersionedCertificateRegistry | `0x67d269191c92Caf3cD7723F116c85e6E9bf55933` | Separate manifest/history |
| LAB001 actual signer | `0x70997970C51812dc3A010C7d01b50e0d17dc79C8` | Authorized; different from BR001 |

For CERT-LAB001-BP-S001, both histories use the same series header and unchanged
original V1 bytes, but their V1 version/transaction records are separate:

- Legacy V1: block **46**, transaction
  `0x06b9c78e9789f4fab31480b34f9b69765e810502175ed209419a37eee7b4f885`.
- New-deployment V1: block **62**, transaction
  `0xc92a7edc99f03aa81a02cd24f33741a2cfb19d912b2418162ac9c76745a62865`.
- New formal history: `04a23d32-c007-401c-9637-9b0e15f5e0bf`.
- Original stays 45,064 bytes, SHA-256
  `e5cb1de883ca64ab75a68e70f58f8f5d83fe9d06696d6ecbd03b086e796281a5`.

Block 62 is explicitly a new signature/transaction, not the old block 46 migrated.
The old route without history_id continues to retrieve block 46 and its exact PDF.
No old V1/new V2 history is spliced. Original V1 first-issuance conflict root cause,
normal registration repair and regressions remain in `certificate-v1-development.md`.

## Implementation

New contract requires the next integer version, original issuer still authorized and
unchanged snake. It preserves each version hash and event. Administrator lab access
changes are separate from unimplemented certificate revocation.

Migration 004 was applied through the existing runner to the existing DB and to
isolated test schemas. It backfills legacy history scope from issuance evidence,
retains all version/file/attempt IDs, and changes uniqueness to history/version.
Repeat application by the runner is safe; container startup also reruns the runner.
PDF storage remains the persistent certificate_files volume with immutable UUID names.

Added history initialization and next-version upload APIs, plus selected version and
history parameters for existing metadata/issue/poll/download/verification endpoints.
New-history V1 initialization only prepares metadata with the verified original file;
issuing it is a separate visible transaction. V2 files cannot replace V1 or existing V2.

Reuse global advisory locking, early durable intent/hash, canonical receipt/call/event
and record validation. A LAB001 prepared nonce reservation now spans both deployments:
the same wallet must not independently reserve one nonce in two contracts. A regression
asserts refusal before broadcast. Fake test wallets are isolated so deliberately pending
transactions from one test do not reserve another test's independent wallet.

Buyer reads actual stored bytes and corresponding live version hash. Version status
is separately read from chain latestVersion. Pending or failed V2 leaves V1 latest;
confirmed V2 makes matching V1 superseded. A failure of just latest lookup leaves
file comparison available but version status unknown; missing/stale/RPC evidence never
means tampering or success. Optional external comparisons do not persist/sign anything.

## Actual local-chain demonstration

Formal V2 and V2_MODIFIED files were absent. To avoid occupying formal V2 with test
content, used visibly TEST ONLY series **TEST-ONLY-V2-7db29809** associated with BP-S001.
Its own new-deployment V1 and V2 are in history
`e47a2c05-5457-443d-b722-a3282dea8698`:

| Version | Block | Transaction |
|---|---|---|
| New-history TEST ONLY V1 | 64 | `0xbb179214e3023629f552602817c615ef096a466a6e2844fabd88aef49dcc8b1c` |
| TEST ONLY V2 | 65 | `0x8452153269ab912f047550f186f5ef9e0feff1fad7b409d92e49ee53892ba4bb` |

Actual API uploads and signatures completed; direct contract reads confirmed snake,
issuer, V2 hash and latest version 2. V1 direct verification matched/superseded; V2
matched/latest; a modification derived from this TEST ONLY V2 mismatched/latest.
Same-byte downloads were verified. After rebuilding/recreating backend and frontend
containers, the PDFs remained byte-identical and both live version statuses persisted.
Legacy block 46 and its PDF were checked again and remained unchanged.

Live Streamlit AppTest against the running API selected Buyer/BP-S001/test series,
defaulted to V2, verified V2 and historical V1, and previewed the historical PDF.
Laboratory's formal series selected new V1 and offered the empty V2 upload slot.
These are automated checks, **not user-performed manual browser acceptance**.
Public runtime evidence is in ignored `.local/certificate-v2-demo.json`; TEST ONLY
PDFs and logs remain ignored and are not source artifacts.

## Validation commands and observations

- `cd contracts; npx.cmd hardhat build`
- `cd contracts; npx.cmd tsc --noEmit`
- `cd contracts; npx.cmd hardhat test`
- `cd backend; $env:RUN_LOCAL_CHAIN_TESTS='1'; .venv/Scripts/python.exe -m pytest -q -ra`
- `cd frontend; .venv/Scripts/python.exe -m unittest discover -s tests -q`
- `docker compose up -d --build backend frontend`

Contract build/typecheck passed; 25 contract tests passed (23 Solidity, 2 Mocha).
Frontend: 24 tests passed. Final backend run: **114 passed, no skips**, with
RUN_LOCAL_CHAIN_TESTS=1 (11 actual local-chain tests). The existing Starlette/httpx
deprecation warning remains; it is not a failing test. The final runner reported
11459.57 seconds of wall time, including the long environment execution interval.
Two earlier full runs reached 110/113 passes respectively but the pre-existing process
restart check hit its 15-second startup deadline. An isolated rerun passed. The test
readiness budget is now 30 seconds for loaded Windows process startup, still requiring
a real healthy HTTP response; no persistence assertion is skipped or weakened.

## Changed source/documentation files

Pre-existing unrelated edits are excluded from this list and remain unchanged.

| Area | Files |
|---|---|
| Contracts | `contracts/contracts/VersionedCertificateRegistry.sol`, `contracts/contracts/VersionedCertificateRegistry.t.sol` |
| Deployment | `contracts/ignition/modules/VersionedCertificateRegistry.ts`, `contracts/scripts/deploy-versioned-certificate-registry.ts` |
| Backend | `backend/certificates/local_chain.py`, `models.py`, `routes.py`, `service.py`, new `histories.py` in that directory |
| Migration | `backend/migrations/004_certificate_histories.sql` |
| Backend tests | `backend/tests/test_certificate_versions.py`, `test_certificate_versions_e2e.py`, `test_certificates.py`, `test_snake_registration.py` |
| Frontend | `frontend/certificate_page.py`, `frontend/tests/test_certificates.py` |
| Runtime recipes | `compose.yaml`, `justfile` |
| Documentation | `docs/level-2/certificate-versions.md`, `certificate-v1.md` in that directory; `docs/level-3/tasks.md`, `certificate-v2-development.md`; `docs/samples/certificates/README.md` |

## Manual acceptance and remaining work

Open http://localhost:8501. Current services are already rebuilt; preserve the running
node. On this existing chain do not run reset/redeploy commands. For a fresh compatible
environment only: start the established node, deploy SnakeRegistry/legacy certificates
through existing recipes, then `just deploy-versioned-certificates`, `just migrate`
and `docker compose up -d --build backend frontend`. The new recipe refuses to
overwrite an existing versioned manifest. Manifest/instance/code/block anchors detect
chain resets; historical rows are retained without falsely confirming current validity.

1. Buyer: query BP-S001, choose TEST-ONLY-V2-7db29809, select the new contract history.
   V2 is the default confirmed version. Click 核验证书: match and latest. Preview/download.
2. Choose V1 in that same history. Click 核验证书: match and superseded. Select legacy
   history separately to inspect its independent V1 transaction; do not combine histories.
3. External comparison: select new V2 and use ignored
   `.local/certificate-v2-TEST-ONLY-MODIFIED.pdf`: mismatch, version still latest.
   Same original content renamed must match. External input never issues a version.
4. Formal acceptance: supply `docs/samples/certificates/BP-S001_Certificate_V2.pdf`
   and `BP-S001_Certificate_V2_MODIFIED.pdf`. Inspect series CERT-LAB001-BP-S001,
   laboratory and BP-S001 association first. Formal V2 is currently empty.
5. Laboratory: select CERT-LAB001-BP-S001, new versioned history; check V1 block 62.
   Upload only the formal original V2, inspect target series/snake/version, then Issue
   selected V2. While pending, Buyer V1 remains latest. Refresh until actual confirmation.
6. Buyer: repeat V1/V2 direct checks and optional MODIFIED V2 external comparison.
   Old formal V1 block 46 remains accessible in its separate legacy history.

Pending: formal V2 materials/issuance and user browser acceptance; certificate
revocation, production identity/signing, keeper transfers, application V3+ flow,
historical recovery after chain reset and file backup/orphan policies.
No staging, local commit, push, chain reset, database reset or original file replacement.
