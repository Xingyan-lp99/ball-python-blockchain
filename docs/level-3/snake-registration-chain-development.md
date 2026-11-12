# Snake Registration - Local Chain Development Record

Date: 2026-11-12 (Europe/Berlin)

Status: **Local-chain registration stage complete**, including automated checks and
manual browser acceptance performed by the user on 2026-11-12. Database-stage
acceptance and commit `91998923146d12d44da49f3eeebee0307d6c3596` remain the baseline.
Historical-profile recovery after chain reset remains pending. Following acceptance,
the user authorized the local feature commit described below; remote push is excluded.

## Scope and preserved work

Inspected root and contract AGENTS instructions, Level 0/1 architecture/data model,
registration spec/tasks, database module, frontend and existing Hardhat scripts.
Applied the project-local `hardhat` and `hardhat-toolbox-mocha-ethers` skills.

The pre-existing Level 1 change, IDE settings, Counter sources/tests, original
deployment module and original script contents were preserved. Before implementation,
content hashes of existing files were saved under ignored `.local/`; comparison after
implementation found only the intended localhost config addition and contract README
usage instructions.
New contract, Solidity tests, Ignition module and deployment script were added alongside
the examples. No reset, clean, data-volume removal or public network deployment occurred.

The broader Level 1 model still proposes generated IDs and a breeder-selected wallet.
This requested slice retains the already accepted caller-supplied database ID and
binds chain manager to the actual transaction sender. Differences are documented at
Level 2; no Level 0 or Level 1 content was rewritten.

## Implementation

- SnakeRegistry stores the exact snake ID -> caller address mapping, rejects empty
  and duplicate IDs, emits ID/manager events and exposes a random deployment instance ID.
- BR001 maps to the deployment manifest's public dev wallet. web3.py asks Hardhat to
  sign through its unlocked account. This is server-mediated local demo signing, not
  real authentication; the application receives/stores no private key.
- `backend/dev_chain.py` runs the existing node with stdout/stderr discarded, avoiding
  Hardhat's default private-key banner. It refuses to replace an existing RPC server.
- SQL migration 002 adds attempts with foreign keys and receipt evidence without
  changing existing profiles. The original 001 migration was not edited.
- Dedicated-connection advisory locking serializes the demo signer across workers,
  including intent/hash commits. Nonces reserved by unresolved intents cannot be
  consumed by another profile through this application.
- Intents and nonce/gas parameters are durable before broadcast; hashes are committed
  immediately after broadcast returns. Pending/mined transactions and registration
  events allow recovery after a lost response or database-write failure.
- Confirmation requires successful canonical receipt, expected call/sender/event,
  current contract manager and valid deployment scope. Historical database confirmation
  alone is insufficient. A timeout/RPC loss produces uncertainty, not fabricated success.
- POST/GET registration routes supplement the existing create/read routes. Request
  bodies cannot select an address, sender or key. Profiles owned by another manager
  cannot be submitted. No certificate or transfer operation was added.
- Streamlit adds submission and status refresh, current confirmation checks, evidence
  display and stale/unavailable warnings. It retains the uncertified morph notice.
- Compose reuses PostgreSQL and mounts ignored public deployment configuration read-only;
  the backend reaches the host node through `host.docker.internal`.

## Executed validation

| Check | Actual result |
|---|---|
| `npx.cmd hardhat build` from contracts | Passed; compiled 2 new Solidity files with existing solc 0.8.34 |
| `npx.cmd tsc --noEmit` after build | Passed |
| `npx.cmd hardhat test` | 10 passed: 8 Solidity (Counter + SnakeRegistry), 2 existing Mocha |
| `$env:RUN_LOCAL_CHAIN_TESTS='1'; .venv/Scripts/python.exe -m pytest -q -ra` from backend | **53 passed, no skips** |
| `.venv/Scripts/python.exe -m unittest discover -s tests -v` from frontend | **10 passed** |
| Real local chain UI/HTTP integration | Streamlit AppTest made actual HTTP calls to Uvicorn, PostgreSQL and web3.py; contract state, receipt and event verified independently |
| Actual pending transaction | Disabled automining temporarily, recovered an erased test-row hash from the real pending transaction, observed stable repeated hash, mined and observed confirmed; automining restored in finally |
| Actual conflicting wallet | Another local wallet registered the same ID; backend returned 409 and preserved the profile |
| Actual deployment-evidence validation | Wrong instance ID, code hash and block anchor rejected against the running chain, without resetting it |
| Simulated workflow failures against real PostgreSQL | RPC failure, revert, pending receipt, lost send response, nonce reservation and hash/confirmation DB-write recovery passed |
| Simulated reset/redeployment | Prior evidence retained; effective state stale/failed and submission refused |
| `docker compose config --quiet` | Passed |
| `docker compose up -d --build backend frontend` | Images built, migration applied, both apps started against existing database volume |
| Backend-container `LocalChain.validate_scope()` | Passed through host gateway with read-only manifest |
| Current container-app demo through Streamlit | Completed and retained in development database; details below |
| `git diff --check` and preserved-file hash comparison | Passed; pre-existing unrelated contents preserved |
| Manual browser acceptance performed by the user (2026-11-12) | Correct lookup, successful new-profile local-chain registration, transaction evidence after confirmation, consistent results after refresh, and certificates remaining unverified |

The browser acceptance result was reported by the user, not performed by the coding
agent. Automated results above are from the implementation run. This acceptance and
commit-preparation update does not change application logic or rerun those tests.

The backend still emits the upstream Starlette/httpx TestClient deprecation warning;
AppTest emits bare-mode ScriptRunContext notices. Tests passed with these warnings.

During development, the old migration-count assertion needed updating for migration
002; fake-chain instances initially shared IDs across tests and were isolated; a
frontend mock reused a mutable response and was corrected; real HTTP AppTest needed
an explicit 20-second script timeout instead of its default 3 seconds. These failures
were corrected and the final checks above passed. No skipped check is counted as passed.

## Retained actual chain evidence

The following profile remains in the development database for page lookup. It was
created and submitted through Streamlit AppTest using the current container API, then
verified using a separate web3.py contract/receipt/event read. Automated tests use
separate schemas; their database rows are removed with those schemas, while their
unique IDs remain on the ephemeral development chain.

| Item | Observed value |
|---|---|
| Snake ID | `LOCAL-b4c680626bc3` |
| Chain ID | `31337` |
| Registry | `0x5FbDB2315678afecb367f032d93F642f64180aa3` |
| Manager (BR001 dev wallet) | `0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266` |
| Registration transaction | `0xaa02f6f40733754b45b319652e1f73f629d0a1770d9415b5eaaff5a04db84ad6` |
| Confirmation block | `11` |
| Receipt status | `1` |
| Block hash | `0x1423ed7f5eb7279d16adc69196c8b396f121eed3d719644ba5f1f03eccf9c50c` |
| Instance ID | `0xe90121857296a82d7748f0d135388a7fa8b5ce70e3d9419242943354e5a6ac93` |

These are observations on the current local instance, not permanent validity claims.
The page rechecks evidence; after reset/redeployment it must show stale/unavailable.
Only public identifiers and hashes are recorded here; no keys are included.

## Run and operate

Keep the existing PostgreSQL environment and uv/npm installations. No environment
reinitialization or new runtime dependency was needed. From the repository root:

```powershell
# First terminal: keep running. Skip if this local node is already running.
just chain
```

```powershell
# Another terminal: run once for this new chain, not on every app restart.
just deploy-registry
docker compose up -d --build backend frontend
```

Open `http://localhost:8501`. Create a database profile or query an existing BR001
profile, then choose Submit local-chain registration. Refresh chain status for pending
transactions. Query `LOCAL-b4c680626bc3` to inspect the retained demo on this instance.
The server controls the wallet; there is no key/address input.

For local Python application runs instead of containers:

```powershell
just migrate
just backend
# Separate terminal
just frontend
```

Defaults: RPC `http://127.0.0.1:8545`, manifest `.local/snake-registry.json`.
`LOCAL_CHAIN_RPC_URL` and `LOCAL_CHAIN_DEPLOYMENT` may select supported local paths;
the manifest is produced by deployment and includes the public BR001 wallet mapping.
Compose supplies its host-gateway URL and `/app/local-chain/snake-registry.json` path.
No signing-key variable is required. Root `.env` remains unchanged and uncommitted.

```powershell
just test-contracts
just test-frontend
cd backend
$env:RUN_LOCAL_CHAIN_TESTS = '1'
uv run pytest -q -ra
```

Without `RUN_LOCAL_CHAIN_TESTS=1`, the six real-chain checks are explicitly skipped;
this is not equivalent to the full validation above. PostgreSQL unavailability also
produces explicit integration-test skips. Full UI integration needs the existing
frontend uv environment. Tests never call `hardhat_reset` or remove the data volume.

## Reset limitations and remaining work

Hardhat chain state is ephemeral. A node reset/restart can erase deployments,
transactions and registrations; the same chain ID or reused address is insufficient
evidence. Scope validation checks code hash, immutable instance and block anchor;
recorded scope is compared on every reconciliation. Historical confirmation becomes
stale or unavailable rather than current success. Historical attempts and database
profiles remain intact.

A destructive reset of the user's running chain was **not performed**. Reset handling
was tested with simulated reset/redeployment and real mismatched deployment evidence.
After a deliberate reset, deploy a new instance with a new manifest. Old profiles are
not silently rebound or automatically resubmitted; an explicit historical-data recovery
policy remains to be designed. Do not delete profile/history rows to hide this state.

Still pending: real authentication and secure
non-demo signing, certificate/hash/verification features, manager transfers, background
reconciliation, public-network finality/reorg policy and Level 1 design reconciliation.
The local policy accepts one successful mined receipt. Polling is initiated by API/page
requests. Public testnet deployment and remote Git push are outside this iteration.

## Local commit after acceptance

The user authorized the local message `feat: implement local-chain snake registration`.
Stage the local-chain implementation, migration, UI changes, tests and documentation,
plus the contract dependencies/build configuration required to run them. Keep unrelated
pre-existing Level 1 edits, IDE settings, Counter example sources/tests/deployment and
the sample OP transaction script outside the commit. Where a previously untracked
contract configuration or README mixes local-chain additions with unrelated sample
content, stage only the relevant content and preserve the complete working file.
Exclude environment files, keys, databases, runtime manifests/journals, logs, generated
artifacts and dependency directories. No remote push is authorized.

## References used

- Project-local skills: `contracts/.agents/skills/hardhat/SKILL.md` and
  `contracts/.agents/skills/hardhat-toolbox-mocha-ethers/SKILL.md`.
- [web3.py transaction methods](https://web3py.readthedocs.io/en/stable/transactions.html)
  for node-signed contract transactions.
- [Hardhat Ignition deployment guide](https://hardhat.org/ignition/docs/guides/deploy)
  for deployment parameters and separate local deployment journals.
- [Hardhat configuration](https://hardhat.org/docs/reference/configuration)
  and the installed Hardhat 3 package/types for local network and script APIs.
