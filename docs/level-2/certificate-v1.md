# Level 2 - Certificate V1 and Independent File Verification

## Scope and identities

One immutable V1 PDF per globally unique certificate ID, using only local Hardhat
chain 31337. One snake may have multiple distinct certificates. Preserve the running
SnakeRegistry; a separate CertificateRegistry references it. No V2, revocation,
latest-version checks, real login, manager transfer or public deployment.

The deployment administrator alone authorizes laboratory addresses. The contract
requires an authorized caller and a snake registered in its referenced SnakeRegistry;
the issuer is always `msg.sender`, never a supplied argument. It stores certificate ID,
snake ID, issuer, version 1 and SHA-256 digest, and emits matching issuance evidence.
Duplicate V1 cannot overwrite a record. Version-indexed contract storage and separate
database certificate/version rows allow future append-only versions.

BR001 remains the server breeder context. LAB001 is a separate server laboratory
context mapped to a different unlocked development wallet by the deployment manifest.
Hardhat holds/signs with the keys; no key enters app source, database, UI or response.
The existing node wrapper suppresses its default private-key output. The UI's Breeder,
Laboratory and Buyer workspaces are **not authentication**. No normal page/API exposes
arbitrary lab authorization. PostgreSQL lab labels do not grant contract permission.

## API and immutable storage

All paths below have `/api/v1` prefix and explicit version 1:

| Operation | Route | Request |
|---|---|---|
| Save original V1 | `POST /certificates` | Multipart certificate_id, snake_id, file |
| Read selected V1/evidence | `GET /certificates/{id}/versions/1` | None |
| Submit/retry issuance | `POST /certificates/{id}/versions/1/issuance` | `{}` |
| Poll/reconcile | `GET /certificates/{id}/versions/1/issuance` | None |
| Download original | `GET /certificates/{id}/versions/1/file` | None |
| Verify platform original (primary) | `POST /certificates/{id}/versions/1/verification/stored` | `{}`; no file/hash/path |
| Compare external file (optional) | `POST /certificates/{id}/versions/1/verification` | Multipart file only |
| Snake's certificates | `GET /snakes/{snake_id}/certificates` | None |

Certificate ID and existing database snake ID are the required supplied metadata.
The server assigns LAB001/name/wallet, version 1, SHA-256 and creation timestamps.
Trim IDs and reject blanks. Extra/repeated form fields and extra issuance JSON fields
are rejected, including user hashes, signer, lab identity or version. A draft upload
does not broadcast; submission checks current chain snake registration and lab permission.

New upload returns 201. Same ID/snake/lab/bytes returns 200 without replacing the
original file/name; changed subject or content returns 409. Missing object: 404;
wrong server demo identity: 403; invalid input: 422; oversized file: 413; conflict,
busy transaction or stale deployment: 409; unavailable DB/config/storage: 503.

First-issuance preflight is also performed on metadata/status refresh, even when no
attempt exists. A missing chain snake keeps status not_submitted and hash null, but
returns error_code snake_not_registered with the exact snake/registry and required
Breeder step. Other codes distinguish laboratory_not_authorized, issuer_wallet_mismatch
and certificate_record_conflict. POST returns structured detail `{code, message}` and
logs the safe code/identifiers. The page displays the actual cause and disables Issue
until preflight clears; it does not auto-register or authorize. After the proper
prerequisite is completed, refresh allows first issuance. Matching already-issued chain
records can recover local evidence on refresh without another transaction.

Operational upload limit is 10 MiB. Check PDF header and EOF marker, which is basic
format screening, not semantic/malware validation. Preserve every uploaded byte;
never rewrite, compress or regenerate received PDFs. Save with a random internal UUID
name opened exclusively, flush/fsync original bytes, then commit metadata. Uploaded
filenames are metadata only, not paths or comparison keys. Downloads use safe names.

Migration 003 creates laboratories, files, certificates, certificate_versions and
certificate_issuance_attempts with explicit foreign keys and unique certificate/version
constraints. Earlier migrations and profiles are retained. Labels and global public IDs
are this demo slice; broader Level 1 multi-lab design remains to be reconciled, unchanged.
V1 has no replacement/update endpoint; future versions must insert new rows.

Compose stores PDFs in named volume `certificate_files` at `/app/certificate-files`.
Local Python defaults to ignored `.local/certificate-files`; override via
`CERTIFICATE_STORAGE_DIR`. Back up documents and database together. If file writing
succeeds but DB commit fails, retain the unreferenced file rather than deleting data;
explicit orphan cleanup is deferred. Buyer verification uploads are not persisted.

## Transactions and recovery

Reuse the existing local adapter's scope, receipt and pending/mined sender/nonce lookup.
Shared in-process helpers now provide both features with dedicated-connection advisory
locking across commits, status reporting and receipt persistence. No worker/service
or architecture change is introduced.

Persist intent, expected issuer, nonce, gas price and starting block before broadcasting;
persist the returned hash immediately before receipt checks. Issuance gas is fixed at
500,000. A reserved unresolved lab nonce cannot be reused by another certificate. An
unbroadcast intent retries identical parameters, not a newly allocated transaction.

Before retry, inspect the current V1 record. Matching content recovers its event/hash
and checks actual call/sender, receipt status, canonical block, event and record. Missing
hashes can also be recovered from pending/mined transactions. This preserves recovery
after a lost RPC response or successful chain execution followed by a failed hash or
confirmation DB write. A failed intent commit prevents broadcast. A definite revert
may create a new attempt without altering V1 or prior evidence; conflicts cannot overwrite.

Statuses: not_submitted, processing, confirmed, failed; chain_check and recorded_status
separately describe current checking and historical database state. One successful
mined receipt is sufficient locally. Confirmation also requires matching call/event/live
record. Timeout is uncertainty, not failure. RPC failure cannot establish success.
Attempt evidence includes hash, chain, contract, issuer wallet (shared evidence field
manager_address), deployment instance, receipt block/hash and sanitized failure code.

Validate both certificate and snake deployment instances, runtime code hashes, block
anchors and their linkage. A local reset/redeployment invalidates current evidence even
if chain ID/address is reused. Retain PDF/history, refuse silent rebinding/resubmission,
and distinguish stale scope from unavailable RPC. Recovery is request-driven.

## Verification and display

The primary buyer flow starts at the snake profile: query the snake, inspect its
certificate list, select a V1, preview/download the original and click 核验证书. No
PDF re-upload is required. The stored-verification endpoint opens the selected version's
actual internal file on every request, calculates a fresh SHA-256 and compares with the
current on-chain V1, including issuer/subject, successful receipt and event checks.
Never substitute the PostgreSQL file/version digest for reading the actual bytes.
Changed stored bytes produce mismatch even when cached metadata is unchanged. Missing,
unreadable or oversized stored files produce unable, independently of registration status.
Stored bytes are compared even if their PDF format has been damaged; never regenerate them.

The collapsed 上传外部文件核验（可选） entry independently hashes a PDF received from
a seller or other source and compares with the same selected on-chain V1. It does not
upload a formal certificate, overwrite laboratory files, create versions/attempts or
submit an issuance transaction. Both verification operations are non-signing operations.

Neither mode compares filenames or trusts the database hash cache. Tests corrupt a
test-only cache and alter an isolated stored file to verify both boundaries. Responses
identify file_source (`platform`/`external`) and file_sha256; external mode retains
uploaded_sha256 for compatibility. on_chain_sha256 always comes from a fresh chain read.

| file_result | Meaning |
|---|---|
| match | Actual bytes from the identified source match this registered V1 |
| mismatch | Actual bytes from that source differ from this registered V1 |
| unable_to_verify | Current evidence is unavailable/absent/invalid; no file conclusion |

RPC failure, missing record, stale deployment and conflicting evidence yield unable,
never tampering or a pass. Display the file result separately from registration status,
with selected certificate, snake, lab/name/wallet, version, file source, hashes and transaction basis.
Matching does not prove biological findings or identify who changed a file. No whole-snake
certified flag is set. latest_version_checked and revocation_checked remain false and
the page states these limits. Do not reuse a cached file result as a fresh check.

## Formal PDF gate and remaining work

The original BP-S001_Certificate_V1.pdf was not present. Place it at
`docs/samples/certificates/BP-S001_Certificate_V1.pdf`; inspect its actual certificate ID,
lab name and snake ID before use, resolving mapping discrepancies instead of guessing.
BP-S001 must first exist in PostgreSQL and the current SnakeRegistry. It was initially
absent; the user later supplied its PDF through LAB001 upload. During the issue-conflict
repair, BP-S001's missing chain registration was completed through the normal BR001
operation, and CERT-LAB001-BP-S001 V1 was issued once by LAB001. The original bytes were
preserved and matched on-chain. PDF business-field inspection and human acceptance
remain separate; the repair does not establish biological truth. For synthetic tests,
use only clearly marked TEST ONLY PDFs
and test snake IDs; never substitute an existing V2_MODIFIED file as modified V1.

See the development record for executed automated/real-chain checks. The user completed
manual browser acceptance of CERT-LAB001-BP-S001 V1 at block 46, direct comparison and
PDF preview/download on 2026-11-12. Deferred: V2/revocation, real identity/
signing, transfers, orphan/backup policy and historical recovery after reset. No chain or
database reset is part of this feature workflow. A local feature commit was explicitly authorized
after acceptance; remote push remains excluded.
