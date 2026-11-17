# Level 2 - Certificate Contract Integration

## Scope and Source

The contract and existing Solidity tests were integrated from
`origin/feature/certificate-registry`, commit
`92ef9f7035f0d6796d3b85e16869a406b730a42b`, by fast-forwarding the local branch.
Existing uncommitted backend, frontend, and documentation work was retained.

Sources:
- `contracts/contracts/CertificateRegistry.sol`
- `contracts/contracts/CertificateRegistry.t.sol`

Local integration changes make the deploying administrator immutable and add
comments describing the file hash convention and indexed events. Public function
and event signatures remain unchanged. The contributor's tests are retained
without changes. They are not executed under the current instruction to pause
unit tests.

This contract supports laboratory authorization, initial issuance, append-only
revision, and evidence/history reads. It does not implement revocation,
laboratory deauthorization, PDF storage, file comparison, or keeper transfers.

## Deployment

- Solidity compiler: `0.8.28`, using the existing Hardhat 3 project.
- Local RPC: `http://127.0.0.1:8545`; expected chain ID: `31337`.
- Constructor: `constructor(address snakeRegistryAddress)`.
- The constructor rejects the zero address and fixes the administrator as
  `msg.sender`. The deployer must also verify that the supplied address contains
  the intended, already-deployed SnakeRegistry code; the constructor does not
  perform that code check.
- `snakeRegistry()` returns the configured registry address; it is immutable.
- `administrator()` returns the deploying administrator address; it is immutable.

Use the main project's existing SnakeRegistry. Do not replace it or copy a
contract address from another developer's local chain.

Local account indexes, starting at zero:

| Index | Responsibility |
|---|---|
| 0 | Deploy CertificateRegistry and authorize laboratories |
| 1 | BREEDER001 |
| 2 | LAB001 |
| 3 | LAB002 |
| 4 | BUYER001 |

Creating a laboratory website account does not authorize its address on-chain.

## Identifiers and File Hashes

- Snake, series, and version identifiers are case-sensitive Solidity strings.
  Preserve the exact snake identifier already stored in the project.
- Series identifiers are globally unique within this CertificateRegistry.
- Version identifiers are globally unique across all series in this contract.
- Series and version identifiers must be nonempty. The contract does not trim
  whitespace or normalize case.
- The first version has number `1` and an empty `previousVersionId` string.
- The application convention is SHA-256 over the exact original PDF bytes.
  Python supplies `hashlib.sha256(pdf_bytes).digest()` as the 32-byte value.
  A hexadecimal display has 64 hex digits, optionally prefixed by `0x`.
  Do not pass the UTF-8 bytes of that hexadecimal text as the digest.
- The Solidity `bytes32` value does not identify or enforce a hash algorithm.
  The contributor's tests use Keccak-generated fixture values; those are not
  PDF hashing instructions. Preserve them as contract fixtures.
- File hashes use SHA-256; indexed event topics use Ethereum Keccak-256.
  These are separate operations and must not be substituted for each other.
- Verification reads evidence and compares bytes off-chain. It sends no
  transaction and creates no certificate version.

## Public Functions

| Function | Result | Rule |
|---|---|---|
| `administrator()` | `address` | Fixed deployment administrator |
| `snakeRegistry()` | `address` | Fixed SnakeRegistry dependency |
| `authorizeLaboratory(address laboratory)` | No Solidity return value | Administrator only; reject zero or already-authorized address |
| `isAuthorizedLaboratory(address laboratory)` | `bool authorized` | Unauthorized addresses return false |
| `issueCertificate(string snakeId, string seriesId, string versionId, bytes32 fileHash)` | No Solidity return value | Authorized sender; new series and version; registered snake; creates V1 |
| `appendRevision(string seriesId, string versionId, bytes32 fileHash)` | No Solidity return value | Original series issuer; fresh version ID; appends to current version |
| `getVersion(string versionId)` | One `VersionEvidence` tuple | Unknown version reverts |
| `getSeries(string seriesId)` | One `SeriesSummary` tuple | Unknown series reverts |
| `getSeriesVersionIdAt(string seriesId, uint256 index)` | `string versionId` | Zero-based history; unknown series or invalid index reverts |

The issuer is always the transaction sender. Keeper status does not grant
certificate issuance or revision rights. Snake existence is checked by calling
the existing `getCurrentKeeper(string)` function on the configured registry.

`appendRevision` accepts no predecessor argument. It selects the current version,
marks that predecessor Superseded, creates the next numbered version as Current,
and retains the old evidence. There is no deauthorization operation in this
contract, so a series issuer remains an authorized laboratory.

## Tuple Order and Status Mapping

`VersionEvidence`, returned by `getVersion`, has this exact order:

| Position | Field | ABI type |
|---|---|---|
| 0 | snakeId | string |
| 1 | seriesId | string |
| 2 | versionId | string |
| 3 | versionNumber | uint256 |
| 4 | previousVersionId | string |
| 5 | issuer | address |
| 6 | fileHash | bytes32 |
| 7 | status | uint8 |

`SeriesSummary`, returned by `getSeries`, has this exact order:

| Position | Field | ABI type |
|---|---|---|
| 0 | snakeId | string |
| 1 | issuer | address |
| 2 | currentVersionId | string |
| 3 | currentVersionNumber | uint256 |
| 4 | versionCount | uint256 |

| Enum value | Solidity status | Display meaning |
|---|---|---|
| 0 | None | Internal default; not a pending transaction or confirmed version |
| 1 | Current | Current version in its series |
| 2 | Superseded | Retained earlier version |

Unknown version queries revert rather than returning status None. There is no
Revoked enum value in this implementation. Do not invent a numeric value for it.
Transaction submitted/confirmed/failed states remain separate from version
lifecycle status.

## Events and Receipt Validation

Exact declarations:

```solidity
event LaboratoryAuthorized(address laboratory);

event CertificateIssued(
    string indexed seriesId,
    string indexed versionId,
    string snakeId,
    address indexed issuer,
    uint256 versionNumber,
    bytes32 fileHash
);

event CertificateRevised(
    string indexed seriesId,
    string indexed previousVersionId,
    string indexed versionId,
    address issuer,
    uint256 versionNumber,
    bytes32 fileHash
);
```

Indexed strings are stored as Keccak topics, not reversible strings. For these
string values, compare each topic with `Web3.keccak(text=known_identifier)`.
Do not compare a decoded indexed string field directly with its original text.

- Issued topics after the event signature: series ID hash, version ID hash,
  padded issuer address.
- Revised topics after the event signature: series ID hash, predecessor ID hash,
  new version ID hash. The issuer is in the non-indexed data.
- Keep submitted IDs and the known predecessor in backend records. Retrieve
  readable IDs and full evidence with `getVersion(versionId)`.
- Validate a successful receipt, emitting contract address, expected event,
  identifiers/topics, sender, version number, and file hash.
- When checking state produced by a transaction, read at the receipt's block.
  Use fresh reads for user-facing current lifecycle status.

For indexed parameter encoding, see the
[Solidity ABI specification](https://docs.soliditylang.org/en/latest/abi-spec.html#events).

## Custom Errors

| Error | Condition |
|---|---|
| `ZeroAddress()` | Zero registry constructor input or zero laboratory address |
| `Unauthorized()` | Non-administrator authorization or unauthorized issuance |
| `LaboratoryAlreadyAuthorized(address laboratory)` | Duplicate authorization |
| `EmptySeriesId()` | Empty series ID during issuance |
| `EmptyVersionId()` | Empty version ID during issuance or revision |
| `SeriesAlreadyExists(string seriesId)` | Reused series ID |
| `VersionAlreadyExists(string versionId)` | Reused version ID |
| `SeriesNotFound(string seriesId)` | Unknown series |
| `VersionNotFound(string versionId)` | Unknown version |
| `VersionIndexOutOfBounds(string seriesId, uint256 index)` | Invalid history position |
| `NotSeriesIssuer(string seriesId, address caller)` | Another account attempts revision |
| `InvalidCurrentVersion(string seriesId, string versionId)` | Predecessor status or number is inconsistent |

The configured SnakeRegistry's `SnakeNotFound()` can bubble up during issuance.
It is an external dependency error, not a separately declared certificate error.

## Demonstration Call Sequence

These are intended calls, not a claim that deployment or issuance has occurred:

1. Deploy from account 0 with the existing SnakeRegistry address.
2. Account 0 authorizes accounts 2 and 3.
3. LAB001 calls `issueCertificate("SNAKE001", "SERIES-LAB001-001",
   "VERSION-LAB001-001-V1", lab001_v1_sha256)`.
4. LAB002 calls `issueCertificate("SNAKE001", "SERIES-LAB002-001",
   "VERSION-LAB002-001-V1", lab002_v1_sha256)`.
5. LAB001 calls `appendRevision("SERIES-LAB001-001",
   "VERSION-LAB001-001-V2", lab001_v2_sha256)`.
6. Read all three versions: LAB001 V1 is Superseded, LAB001 V2 is Current,
   and LAB002 V1 is Current. LAB001 history indexes 0 and 1 return V1 and V2.
7. Compare the original and modified V2 files with the selected V2 hash
   off-chain. Neither comparison changes versionCount.

Replace SNAKE001 with the actual existing identifier if the demonstration uses
a different value. The contributor's test identifier SNAKE-001 is a fixture,
not a reason to rename existing application data.

## Off-Chain Certificate Records

Migration `backend/migrations/006_create_certificate_records.sql` creates:
- `laboratories`: laboratory ID, unique participant reference, name, and optional
  descriptive testing direction. A laboratory profile is not a staff login or
  proof of on-chain authorization.
- `certificate_series`: series ID, snake, issuing laboratory, and report title.
  Independent reports create independent series.
- `certificate_versions`: version ID, series, version number, predecessor,
  preserved PDF reference, SHA-256 file hash, issuer address, confirmed lifecycle
  status, and issuance time.
- Nullable `blockchain_transactions.version_id` to associate a transaction with
  its certificate version while retaining existing registration transactions.

Database file hashes use 64 lowercase hexadecimal characters without `0x`.
Convert the digest to 32 bytes for contract calls. Database status 1 means Current
and 2 means Superseded, matching the actual ABI. Status and issued_at remain NULL
until the corresponding evidence is confirmed; contract enum None is not used
as a pending status. Submitted/confirmed/failed remains a separate transaction
state.

Version numbers are positive and unique within a series. V1 has a NULL
predecessor in PostgreSQL, corresponding to the contract's empty predecessor
string. Later versions require a predecessor reference. The backend must also
verify that this predecessor belongs to the same series and matches the
contract-selected current version; a self-referencing foreign key alone does
not enforce that rule.

Derive the issuer from the signed-in laboratory's participant address and verify
it against chain evidence. Derive confirmed version numbers and predecessor IDs
from the contract; obtain issuance time from the mined block timestamp. Preserve
all earlier PDFs and version rows when appending a revision.

At this step the migration is prepared, not applied by the agent. Laboratory
profile initialization and PDF/contract coordination remain subsequent tasks.

## Local Setup Script

`backend/setup_certificates.py` prepares database laboratory profiles and the
certificate contract without replacing SnakeRegistry or registering another
snake. Run it from the project root after migration 006 and contract compilation:

```powershell
uv run --locked python -m backend.setup_certificates
```

The invoking terminal must already have DEMO_DB_PASSWORD and
DEMO_REGISTRY_ADDRESS configured. The script reads process environment variables,
not .env files. The registry address must be the existing main-project snake
contract used by FastAPI.

The script checks local chain ID 31337, the account list, and existing registry
code. It confirms that LAB001 and LAB002 participants match local accounts 2 and
3, then creates their laboratory profiles in one database transaction. New
profile names are the laboratory IDs, with testing_direction left NULL. Existing
matching profiles and their metadata are retained; conflicts abort the database
transaction.

Without DEMO_CERTIFICATE_REGISTRY_ADDRESS, setup deploys CertificateRegistry from
account 0. With that variable set, it reuses the supplied contract after checking
its code, SnakeRegistry reference, and administrator. It prints a PowerShell
assignment containing the certificate address; the human must execute that
assignment to retain the address in the invoking terminal for reuse.

Account 0 authorizes LAB001 and LAB002, skipping addresses already authorized.
Each new transaction hash is printed before waiting for a successful receipt.
Each new authorization is also read back before overall success is reported.

Database initialization, deployment, and the two grants are separate operations.
A later failure does not undo earlier successful phases. If setup stops after
printing a certificate address, retain and configure that address before
continuing; do not rerun without it and accidentally deploy another contract.
If confirmation fails before the deployment address is known, inspect the
printed transaction hash before resubmitting. There are no automatic write
retries.

The script has been added for human execution. Its creation is not a claim that
deployment, authorization, or database initialization has been performed.

## Build and Integration Status

From `contracts/` on Windows:

```powershell
npx.cmd --no-install hardhat compile
```

The standard generated artifact is
`contracts/artifacts/contracts/CertificateRegistry.sol/CertificateRegistry.json`.
It contains the ABI and deployment bytecode and remains ignored by Git under
the existing project conventions. Do not copy another computer's deployment
address or private keys.

Validation on 2026-11-17:
- `npx.cmd --no-install hardhat compile` completed successfully: two Solidity
  files compiled with solc 0.8.28, EVM target Cancun.
- The generated artifact contains deployment bytecode. Its nine function
  signatures, tuple component orders, and three event declarations were
  inspected against this document.
- All 20 pre-existing modified or untracked files captured before the merge
  retained their SHA-256 contents afterward. The contributor's test file is
  unchanged from the shared commit.
- No unit tests were run and no contract was deployed. Compilation is not a
  claim that functional tests or manual integration have passed.

The compilation notes above describe the earlier build checkpoint, not the
latest local demonstration state. The human subsequently confirmed migration
006, certificate setup, and successful V1 issuance from both LAB001 and LAB002
through the website. The agent did not submit these issuance transactions.

## Website Issuance and Revision Integration

The laboratory workspace provides New Report and Revise Report tabs. Original
PDFs have a 10 MiB upload limit and a basic PDF-header check; no report results
are parsed. SHA-256 is calculated over the original uploaded bytes.

POST `/api/v1/certificate-series` accepts snake_id, title, and pdf. It creates an
independent series and its first version. POST
`/api/v1/certificate-series/{series_id}/versions` accepts a revised pdf and
appends to the specified series. Both routes require a laboratory login session;
the participant and sending address are derived by the backend.

Before revision, the backend checks original laboratory ownership and compares
the database predecessor with the current series and version read from one
chain block. An unresolved local version blocks another revision. Version IDs
are generated by the backend; the next version number and predecessor are
derived from the contract's current series. The contract independently checks
the issuer and selects the actual predecessor when the transaction executes.

After submission, the transaction hash is retained before waiting for the
receipt. Successful revision requires a matching CertificateRevised event and
matching new/current and predecessor/superseded evidence at the receipt block.
Only then are the predecessor status, new version status and issuance time, and
confirmed transaction state saved in one database transaction. Earlier PDF
references, hashes, and issuance times are not replaced. Transactions for
revisions use operation revise_certificate; initial issuance retains
issue_certificate.

A revision response includes the series, new version, version number,
previous_version_id, previous_version_status, SHA-256, issuer, issuance time,
and transaction hash. Status is current for the new version and superseded for
the predecessor. Other laboratories' series are not changed.

There is no automatic write retry or reconciliation worker. Unknown,
unverified, or incompletely saved outcomes retain available identifiers and
must be inspected before another submission. The website locks a revision
after success or an uncertain outcome to prevent accidental resubmission.

Revision implementation checks on 2026-11-17: the five changed Python files
parsed successfully; backend/frontend imports and authenticated multipart
OpenAPI declarations for both endpoints loaded successfully. No unit tests
were created or run, following the human's instruction. The human subsequently
confirmed successful V2 issuance through the website. This is a manual report,
not an agent-run end-to-end test.

## Certificate History and Original PDF Downloads

GET `/api/v1/snakes/{snake_id}/certificate-series` returns the snake's report
series, laboratory names, and all preserved versions. GET
`/api/v1/certificate-versions/{version_id}/file` downloads the selected version's
original PDF. Both routes require a valid login session. The fixed demonstration
allows signed-in participants to read this history and its files; issuance and
revision remain restricted to laboratory accounts and original issuers.

The Buyer and Breeder workspaces display Certificate History below a loaded
snake profile. Each series has a version/status table and a version selector
with Download Original PDF. The latest stored version is selected initially;
selecting V1 after a revision still downloads the preserved V1 file. Local
filesystem references are never included in the API response. The download
resolver accepts only existing PDFs under storage/certificates.

History reads validate the configured local chain and the contract's snake
registry reference, then read version evidence at one block. Identity, series,
version number, predecessor, issuer, and stored SHA-256 must match that evidence
before the page labels a version Current or Superseded. SQL's cached lifecycle
status is not a fallback when chain evidence is unavailable. Unconfirmed,
unavailable, and mismatching evidence have distinct labels. The same status
checks apply independently to both laboratories' series.

Refresh Certificates reads status again; the page identifies the block used for
its displayed snapshot. Reopening a profile refreshes its history. Immutable
downloaded PDF bytes are held only in the signed-in Streamlit session and are
cleared by the existing sign-out/session-reset flow. This history/download step
does not implement uploaded-file verification or submit blockchain transactions.

Implementation checks: all seven changed Python files parsed successfully,
backend/frontend imports loaded, and OpenAPI declared both new authenticated
GET routes while retaining the existing issuance/revision endpoints. No unit
tests were created or run. Browser history display and original-file downloads
remain pending manual verification.
