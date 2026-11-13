# Level 2 - Certificate V2 and Historical Verification

This extends `certificate-v1.md`; the latter remains the record of the completed
V1 stage. Local Hardhat chain 31337 only. No certificate revocation, real login,
manager transfer or public deployment is included.

## Series, deployment histories and compatibility

A certificate series has one immutable certificate ID, snake and original laboratory.
Versions belong to an explicit deployment history within that series. Never join
versions across deployments into one contract's history.

The existing CertificateRegistry is immutable and supports only V1. Its Solidity,
deployment script and `.local/certificate-registry.json` are preserved. A separate
VersionedCertificateRegistry is deployed without resetting the running node or
SnakeRegistry. Its manifest is `.local/certificate-versioned-registry.json`, plus an
instance-named archive. The deployment script refuses to overwrite an existing current
versioned manifest. Compose exposes both configurations read-only.

For an existing series, an explicit LAB001 action prepares a separate new-deployment
V1 referencing the unchanged original PDF. A separate NEW issuance transaction is
required; this is not migration of the old transaction. In particular, old
CERT-LAB001-BP-S001 block 46 remains legacy evidence. The new history's V1 and V2 must
both be issued to the new contract. UI history selectors show deployment addresses
and explain this distinction. Omitting `history_id` retains legacy V1 behavior.

Migration 004 backfills a legacy history for every existing series, retaining file,
version and transaction IDs. Existing attempt scope is used when present; a never
submitted legacy draft is bound on its first intent/recovery commit. The unique key
becomes `(history_id, version_number)`. Run through the existing ordered migration
runner, whose ledger makes repeat runs safe. Do not drop or reset application data.

## Authorization and append-only transactions

The contract requires current laboratory authorization on every issuance. The first
issuer is `msg.sender`; only that same still-authorized wallet can append. Snake ID
cannot change. Versions must equal `latestVersion + 1`; history cannot be overwritten
or skipped. Each version records its own SHA-256 and emits CertificateIssued with
certificate ID, snake ID, actual caller and version. Administrator-only laboratory
authorization is not exposed through ordinary pages and is not certificate revocation.

The application exposes V2 only. Server LAB001 uses its existing separate development
wallet; no request selects a wallet, hash, lab, version or private key. Demo workspace
selection is not authentication. LAB002/breeder/buyer server contexts cannot append.

Uploading creates an immutable UUID-named PDF and a version draft; it does not change
the chain's latest version. Exact repeat uploads return the same row without replacing
the filename/file; changed bytes return 409. V1 and V2 retain independent file/version
and attempt records. A database advisory lock serializes uploads/signing, and unique
constraints prevent duplicate version rows. Wallet nonce reservations span both old
and new contracts. Persist intent before broadcast and hash immediately after response.

Reuse existing prepared/submitted/confirmed/failed reconciliation. Pending timeouts
remain processing. Confirmation requires canonical receipt, matching calldata/caller,
event and selected chain record. Retry first checks chain state and recovers matching
successful evidence instead of broadcasting again, including after a DB write failure.
Conflicts and stale deployments are explicit; originals remain intact.

## API

All routes use `/api/v1`. Existing version endpoints accept version 1 or 2 and optional
UUID query `history_id`: metadata, issuance POST/GET, file, verification/stored and
external verification. Version 2 without its selected history returns 404.

| Operation | Route | Request |
|---|---|---|
| List deployment/version histories | GET /certificates/{id}/histories | None |
| Prepare independent new-deployment V1 | POST /certificates/{id}/histories | `{}` |
| Upload immutable next V2 | POST /certificates/{id}/histories/{history_id}/versions | Multipart file only |

History creation verifies existing legacy V1, actual original file bytes and original
signer. Uploading V2 requires this new deployment's V1 already on chain and current
authorization. Series metadata is never supplied by the update request. Existing
403/404/409/413/422/503 conventions apply. Specific preflight reasons remain visible.

## Buyer verification and version status

After a snake query, default to the latest verified confirmed version in the most
recent applicable deployment history. Allow explicit deployment and historical version
selection, preview/download of every saved original, and direct stored-file verification.
V2 drafts, pending or failed attempts leave V1 as chain latest; only successful V2
confirmation advances it. RPC/stale evidence never establishes a latest-version claim.

On every verification read the selected actual PDF bytes and independently compute
SHA-256. Compare to that deployment's selected version hash, with live receipt/event
evidence. External upload is a separate optional read-only comparison using the same
selected history/version; it neither stores a certificate nor signs a transaction.

Return separate file_result (`match`, `mismatch`, `unable_to_verify`) and version_status
(`latest`, `superseded`, `unknown`). Read latestVersion from the chain; legacy's verified
immutable V1-only deployment reads its existing V1 record. A matching historical V1
is superseded after its own deployment confirms V2, not mismatched because V2 differs.
If latest lookup alone fails, file evidence may still match while version status is
unknown. If record/RPC/scope evidence fails, file verification is unable, not mismatch.
`revocation_checked` remains false. Matching proves consistency with the selected
registered version, not biological truth, attribution of edits or whole-snake validation.

## Materials and limitations

Formal V2 and V2_MODIFIED PDFs were absent. Use generated visibly TEST ONLY materials
in a separate test series, leaving formal CERT-LAB001-BP-S001 V2 unoccupied. Supply
`docs/samples/certificates/BP-S001_Certificate_V2.pdf` and
`BP-S001_Certificate_V2_MODIFIED.pdf` for formal acceptance. Inspect certificate ID,
LAB001 name and BP-S001 association before use; MODIFIED is external comparison only.
No V3 application workflow or certificate revocation is provided. Deployment-reset
historical recovery, orphan cleanup and backup policies remain follow-up work.
