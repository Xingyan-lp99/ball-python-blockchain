# Keeper Transfers Contract

## Approved Scope

The human approved adapting the transfer logic from teammate commit
`b527c1c73a424b3edb65bd30481ee4599abb6225` into a separate KeeperTransfers
contract. The source is `contracts/contracts/KeeperTransfers.sol`.

This is selective reuse, not a merge of feature/keeper-transfer. The teammate's
HusbandryEvidenceRegistry, its tests, and its changes to husbandry on-chain
boundaries are not adopted. Husbandry records remain entirely in PostgreSQL.
Buyer-uploaded certificate verification has also been removed from this demo.

The existing SnakeRegistry and CertificateRegistry are retained. Recompiling
Solidity does not change deployed code; no proxy, code replacement, forced
transfer, or data replay is introduced.

## Keeper Authority and Existing Data

KeeperTransfers has an immutable snakeRegistry reference. Its constructor
rejects zero addresses and addresses without contract code. The deployment
step must additionally verify this is the intended existing SnakeRegistry.

For a snake with no accepted transfer in KeeperTransfers, getCurrentKeeper
reads the initial keeper from the existing registry. Once a transfer is
accepted, the accepted address in KeeperTransfers takes precedence. Unknown
identifiers fail through the original registry's SnakeNotFound error.

The registering keeper value in the original SnakeRegistry is not updated.
After activation, backend permission checks must use KeeperTransfers, including
all husbandry writes and transfer actions. They must not fall back to the
original registration keeper if the transfer contract is unavailable.

Snake registration continues through the original SnakeRegistry. Its original
keeper remains a suitable initial value for later registered snakes. Existing
CertificateRegistry uses that registry only to confirm snake existence when
issuing a report; it does not grant keeper rights. Certificate history, PDFs,
laboratory permissions, and breeder attribution are unchanged.

Deploy this contract once against the intended registry and retain its address.
Deploying another instance creates independent transfer state, not a copy of
existing accepted transfers.

## Contract Interface

| Operation | Input | Output and rules |
|---|---|---|
| constructor | existing snake registry address | Immutable dependency; no snake re-registration |
| snakeRegistry | none | Address of the original registry |
| getCurrentKeeper | exact snake ID | Accepted keeper, or initial keeper before any accepted transfer |
| initiateKeeperTransfer | snake ID, recipient address | Current keeper only; recipient must be nonzero and different; at most one pending proposal |
| acceptKeeperTransfer | snake ID | Designated recipient only; updates keeper and clears pending state |
| rejectKeeperTransfer | snake ID | Designated recipient only; clears proposal without changing keeper |
| cancelKeeperTransfer | snake ID | Current keeper who initiated the proposal only; clears proposal without changing keeper |
| getPendingKeeperTransfer | snake ID | fromKeeper, recipient, pending; unknown snake reverts |

Write functions have no Solidity return value. Inputs retain the exact snake ID
semantics of the existing registry, including case and whitespace. There are
no new laboratory permissions, administrative transfer privileges, payments,
transfer expiry, account registration, or husbandry evidence operations.

An existing snake without a pending transfer returns zero fromKeeper and
recipient addresses with pending=false. Initiation leaves the current keeper
unchanged. Rejection and cancellation also leave the current keeper unchanged.
Acceptance changes keeper only when the current keeper still matches the
proposal sender. A later accepted keeper may initiate another transfer.

## Events and History

All four events have the same argument layout:

```solidity
event KeeperTransferInitiated(
    string indexed snakeId,
    address indexed fromKeeper,
    address indexed recipient
);
```

KeeperTransferAccepted, KeeperTransferRejected, and KeeperTransferCancelled
use the same three fields. Event topics contain the signature, Keccak hash of
the exact snake ID, and the two indexed addresses. The indexed string is not
decoded as the original readable snake ID.

Pending state is removed when resolved; events retain the history. There is no
on-chain transfer ID or unbounded history array. The later backend step will
associate local transfer IDs with confirmed transaction hashes and events.
An initiation transaction awaiting confirmation and a confirmed proposal
awaiting buyer acceptance are different states.

## Authorization and Off-Chain Effects

After confirmed acceptance, the backend updates its current_keeper_id cache
and keeps the original breeder_id and all historical authors unchanged.
Husbandry writes still require both live keeper authority and, for edits or
deletions, original authorship. Transfer acceptance does not give the buyer
permission to edit breeder-authored rows.

SQL and blockchain updates are not atomic together. The later integration must
record submitted transaction hashes, distinguish failed/unknown/confirmed
outcomes, and avoid automatic write retries. A successful receipt must be
checked against the expected event and keeper/pending state before a completed
transfer is shown.

## Build and Current Status

On 2026-11-17, from contracts/:

```powershell
npx.cmd --no-install hardhat compile
```

Result: one Solidity file compiled successfully with solc 0.8.28, EVM target
Cancun. The generated ABI and bytecode are under
`contracts/artifacts/contracts/KeeperTransfers.sol/KeeperTransfers.json`.

No unit tests were created or run, following the human's instruction. The
teammate's reported 28 passing tests do not verify this adapted contract.
At that build checkpoint the contract was not deployed. The human subsequently
confirmed successful setup execution. Backend activation and transfer writes
are tracked in the later integration notes below.

## Deployment Setup Script

`backend/setup_keeper_transfers.py` is prepared for human execution from the
project root:

```powershell
uv run --locked python -m backend.setup_keeper_transfers
```

Set DEMO_REGISTRY_ADDRESS to the existing SnakeRegistry in the invoking
terminal first. If KeeperTransfers has already been deployed, also set
DEMO_KEEPER_TRANSFERS_ADDRESS to that existing address. The script reads only
these public process-environment settings; it does not read .env, database
passwords, or private keys. PostgreSQL and FastAPI do not need to be restarted.

Setup checks local chain ID 31337, original registry code, compiled artifacts,
and the original registration keeper for SNAKE001 before a deployment. When
no transfer address is configured, it deploys from unlocked local account 0,
prints the transaction hash immediately, and waits up to 30 seconds for a
successful receipt. Account 0 receives no administrative keeper powers.

With an existing address, setup performs reads only and never silently deploys
a replacement. Both paths validate the immutable original-registry reference
and read current keeper and pending parties at one block. A fresh instance
must have the original keeper and no pending transfer. A reused instance may
legitimately have a different accepted keeper or an existing pending proposal;
setup does not reset either state.

The script prints the contract address and a PowerShell assignment:

```powershell
$env:DEMO_KEEPER_TRANSFERS_ADDRESS = "<printed contract address>"
```

The human must execute that assignment in the terminal to retain the address.
Printing it does not set the parent shell's environment. Retain the address
for future reuse and backend configuration. A missing address setting causes
another deployment, not discovery or migration of a prior instance.

If submission or confirmation is uncertain, stop and inspect the transaction
before rerunning. If an address was printed before a later read failed, keep
that address and configure it for reuse; do not deploy another instance.
There are no automatic transaction retries or keeper transfer writes.

Script checks on 2026-11-17: Python syntax and import succeeded; the generated
ABI contains the three read methods used by setup, its constructor accepts
one address, and deployment bytecode is present. The agent did not execute
setup, submit a deployment, or run unit tests. The human subsequently confirmed
deployment. The agent has not performed a keeper transfer.

## Authoritative Keeper Read Integration

`backend/keeper_transfers.py` provides get_keeper_state(snake_id=...). It reads
DEMO_KEEPER_TRANSFERS_ADDRESS and DEMO_REGISTRY_ADDRESS from the backend process
environment. Both addresses must be configured. It checks chain ID 31337,
contract code, and the immutable registry reference, then reads current keeper
and pending parties at one block. The result contains snake_id,
current_keeper_address, pending, optional from_keeper_address and
recipient_address, and block_number.

Husbandry's shared current-keeper permission check now calls this reader for
all add/edit/delete operations. Edits and deletions still separately require
original authorship. Missing configuration, an unavailable node, a wrong
registry reference, or inconsistent state rejects the write with an unavailable
service response. There is no application fallback to the original keeper or
SQL cache. The contract's initial-keeper fallback remains part of its confirmed
on-chain read and is not an application error fallback.

Registration and certificate snake-existence checks continue using the original
registry. The generic original-registry reader in backend/blockchain.py is
retained for those checks; it is no longer used for husbandry authorization.

Activation requires restarting FastAPI from a terminal with the retained
DEMO_KEEPER_TRANSFERS_ADDRESS set. Setting it in a different terminal does not
change the running backend process. This step adds no SQL schema, transfer
submission routes, manager display, or action buttons.

Verification on 2026-11-17: the new reader, husbandry module, and original
registry module parsed and imported successfully with FastAPI. One read-only
call against the human-deployed KeeperTransfers returned SNAKE001's breeder
address 0x70997970C51812dc3A010C7d01b50e0d17dc79C8, pending=false, and no pending
parties at block 15. No database writes, keeper transfers, or unit tests were
performed. Husbandry authorization after an actual transfer still requires
the later end-to-end manual demonstration.

## Approved Transfer Page Requirements

The human clarified the remaining workflow: after an offline sale, the breeder
submits a transfer request on the platform, and the designated buyer accepts
or rejects it. The current keeper may cancel a pending request. No payment or
sale transaction is processed by this application.

The snake profile must display Current Keeper (display name and username),
Transfer Status, and pending From/To parties when present. Pending acceptance
leaves keeper authority with the breeder. Only confirmed acceptance changes
the manager to the buyer. Breeder attribution and historical record authors
remain unchanged.

The later backend/database step must distinguish No Pending Transfer,
Pending Acceptance, Accepted, Rejected, and Cancelled. A cleared on-chain
pending flag alone cannot distinguish the three resolved outcomes; show the
latest confirmed transfer history result. Transaction submission awaiting
confirmation must not be shown as a completed transfer or a confirmed pending
proposal. These page and history requirements are approved but not implemented
by the keeper-read step.

## Transfer Records Migration

Migration `backend/migrations/007_create_keeper_transfers.sql` creates
keeper_transfers with transfer_id, snake_id, from_participant_id,
to_participant_id, status, initiated_at, and resolved_at. Snake and participant
references use the existing tables; sender and recipient must differ.

Status is NULL until initiation is confirmed. Both timestamps are NULL in that
state. Confirmed pending rows require initiated_at and no resolved_at. Accepted,
rejected, and cancelled rows require both timestamps, with resolution at or
after initiation. These are confirmed lifecycle states; submitted/confirmed/
failed transaction progress remains in blockchain_transactions.

A partial unique index allows at most one status=pending row per snake. It
does not treat unconfirmed local rows as confirmed proposals. The contract
independently enforces its one-pending-transfer rule. Each local transfer ID
is application metadata and is not an additional contract input.

The migration adds a nullable transfer_id foreign key to blockchain_transactions
so one request can retain its initiation and resolution transactions. Existing
snake-registration and certificate transaction rows remain valid with NULL
transfer_id. No existing profiles, certificate records, authors, or keeper
values are updated by the migration.

The human approved creation of migration 007. The agent reviewed its schema
against existing migrations but did not connect to PostgreSQL, apply the SQL,
or run unit tests. Human migration execution remains pending. Backend request
handling and the transfer page remain separate tasks.

## Initiation API

POST `/api/v1/snakes/{snake_id}/keeper-transfers` is implemented with a JSON
body containing only recipient_username. It requires a valid buyer or breeder
session. The actor's participant ID comes from that session, not request data.
The recipient is resolved case-insensitively to a registered buyer account and
its existing participant wallet. The current keeper check still determines
whether the authenticated actor may initiate.

The service checks snake existence, a different recipient, live keeper
authority, and the absence of both a chain pending proposal and an unresolved
local request. It creates a local transfer ID with NULL lifecycle status and
timestamps, submits initiateKeeperTransfer, and saves the transaction hash
before waiting. Migration 007 must already have been applied by the human.

A successful receipt alone is insufficient: the backend checks the emitted
contract address, indexed snake-ID hash, sender, recipient, unchanged keeper,
and pending parties at the receipt block. It then saves status=pending,
initiated_at from the mined block, and the confirmed transaction in one SQL
transaction. The current_keeper_id cache and historical authors are not
changed by initiation. Transaction operation is initiate_keeper_transfer.

HTTP 201 returns transfer_id, snake_id, from_participant_id,
to_participant_id, recipient_username, pending status, initiated_at,
resolved_at=NULL, current_keeper_address, transaction_hash, and receipt_status=1.
Unknown buyer/snake gives 404, lack of keeper authority gives 403, an existing
proposal gives 409, and invalid input gives 422. Incomplete writes return known
transfer/transaction identifiers and an outcome such as unknown, unverified,
failed, storage_error, or not_submitted. They do not claim a confirmed proposal.

There is no automatic retry or general reconciliation. An unresolved local
request blocks another request until its transaction/state is inspected,
including a local draft whose initiation could not complete. This is a
sequential local demonstration, not a concurrent transfer-processing service.

Implementation checks: the five changed Python modules parsed/imported, and
OpenAPI declared the authenticated POST with only recipient_username in the
body and pending as the successful response status. A read-only keeper query
still returned the breeder and pending=false. The agent did not call the POST,
apply migration 007, change database rows, submit a transfer, or run unit tests.
Acceptance, rejection, and cancellation APIs are described below. Profile
state reads are described below; Streamlit transfer controls remain a later step.

## Accept, Reject, and Cancel APIs

The following POST endpoints require a valid buyer/breeder session and have no
JSON body. The actor is derived exclusively from the authenticated account.

| Endpoint | Allowed actor | Confirmed result |
|---|---|---|
| `/api/v1/keeper-transfers/{transfer_id}/accept` | Designated recipient | accepted; keeper changes to recipient |
| `/api/v1/keeper-transfers/{transfer_id}/reject` | Designated recipient | rejected; keeper unchanged |
| `/api/v1/keeper-transfers/{transfer_id}/cancel` | Initiating current keeper | cancelled; keeper unchanged |

The service looks up the stored request and its participants' wallet addresses,
requires a confirmed pending request, and checks the corresponding live keeper
and pending parties. It rejects a request that is already resolved, mismatches
chain state, or has an existing submitted/confirmed resolution transaction
requiring inspection. Known failed transactions do not count as confirmed
resolutions. The contract independently enforces sender/recipient authority.

Submission immediately records the transaction hash with operation
accept_keeper_transfer, reject_keeper_transfer, or cancel_keeper_transfer.
Successful confirmation requires the matching event from the intended contract,
the expected indexed snake ID and both parties, no remaining pending transfer,
and the expected current keeper at the receipt block. Acceptance expects the
recipient as keeper; rejection and cancellation expect the original sender.

The resolved status and mined-block resolution time are saved together with the
confirmed transaction. Acceptance also updates snakes.current_keeper_id and
updated_at in that same SQL transaction. Rejection and cancellation do not
update the snake cache. No breeder_id, husbandry author, certificate, or PDF
reference is modified. A successful response is HTTP 200 with the transfer
identifiers, parties, resolved lifecycle status, timestamps, current keeper
address, and transaction hash.

The same incomplete-result handling as initiation preserves known identifiers
and avoids automatically repeating writes. If chain confirmation succeeds but
SQL cannot be saved, the API reports storage_error rather than falsely claiming
that all application records were updated. There is no automatic recovery worker.

Implementation checks: all three changed Python modules parsed/imported;
OpenAPI retained authenticated initiation and declared three authenticated,
body-free resolution endpoints with accepted/rejected/cancelled response states.
No unit tests were created or run. The agent did not invoke the write routes,
change SQL rows, or submit any chain transaction. Actual acceptance/rejection/
cancellation and post-transfer husbandry rights remain for manual verification
after the website controls are connected.

## Current Manager and Transfer Status Query

GET `/api/v1/snakes/{snake_id}/keeper` requires a valid demonstration account
session. It returns current_keeper (participant ID, display name, username,
wallet address), transfer_status, request ID, From/To identities, initiation
and resolution times, the latest transaction hash/status, the chain snapshot
block, and an optional explanatory detail. It exposes no email, password,
token, or filesystem reference. An address with no matching participant keeps
its wallet value and has NULL local identity fields.

| API transfer_status | Intended page label |
|---|---|
| no_pending_transfer | No Pending Transfer |
| pending_acceptance | Pending Acceptance |
| accepted | Accepted |
| rejected | Rejected |
| cancelled | Cancelled |
| unable_to_confirm | Unable to Confirm |

The service prioritizes unresolved local requests, then pending requests,
then the most recently resolved history entry. It reads the latest associated
transaction. Current keeper and pending parties always come from KeeperTransfers
at a single block; identity labels are looked up by those wallet addresses.
It does not use snakes.current_keeper_id as a keeper authority.

Pending Acceptance requires matching confirmed local and on-chain parties.
A known failed accept/reject/cancel leaves the original proposal pending.
Resolved labels require no pending proposal, a matching confirmed resolution
operation, and the expected keeper (recipient for accepted, sender otherwise).
A cleared pending flag alone does not imply acceptance.

Unconfirmed drafts, submitted transactions, missing local requests, and
conflicting local/chain evidence produce Unable to Confirm with details and
available identifiers. On a chain lookup failure, current_keeper and block are
NULL; no SQL keeper fallback is displayed. When the chain keeper can be read
but transfer history disagrees, the actual keeper can still be returned while
the transfer result remains unconfirmed. Database unavailability gives 503;
an unknown off-chain snake gives 404.

This endpoint performs SELECTs and chain reads only. It does not reconcile,
repair, or submit transfers. It depends on migration 007 and the backend's
configured original and transfer-contract addresses.

Implementation checks: both changed modules parsed/imported, and OpenAPI
declared the authenticated GET, public manager identity fields, and all six
status values while retaining the four transfer write endpoints. No unit
tests ran. The agent did not connect to PostgreSQL, call the query endpoint,
modify SQL rows, or submit transactions. Full SQL-backed status behavior and
page labels remain for the later manual website demonstration.

## Streamlit Transfer Workspace

The Buyer and Breeder snake-profile view now includes Keeper Management between
the profile fields and Certificate History. It displays Current Keeper using
the public display name and username, the mapped Transfer Status label, and
From/To identities for the latest request. Transfer Details retains the request
ID, times, and transaction hash/status. Status snapshots identify their chain
block and can be reloaded with Refresh Transfer Status.

The current keeper can enter a registered Buyer Username and submit Initiate
Transfer when the status is confirmed and no request is pending. With Pending
Acceptance, only the designated buyer sees Accept Transfer and Reject Transfer;
the initiating current keeper sees Cancel Transfer. Other participants see
status without those controls. Backend identity and live-chain checks remain
the authority even if a displayed snapshot becomes stale.

After each action, Streamlit retains the response and invalidates its cached
keeper snapshot. A rerun reads current manager/state again. Initiation leaves
the original keeper in place. Acceptance changes the displayed manager only
after confirmed backend evidence; rejection/cancellation retain the original
keeper. All UI labels are English.

The frontend sends only a buyer username for initiation and the existing request
ID/action for resolution. Bearer credentials are included in the HTTP header,
not in public result displays. Session expiry uses the existing sign-in reset.
Lost/unreadable responses and unknown, unverified, or incompletely saved results
retain available transaction IDs and lock further transfer actions in that
Streamlit session; refreshing status does not automatically retry or repair a
write. Existing sign-out clears account-specific cached state. Known denied or
not-submitted requests can be corrected subject to the freshly read state.

Required runtime setup remains migration 007 and the original database/session
configuration plus DEMO_REGISTRY_ADDRESS and DEMO_KEEPER_TRANSFERS_ADDRESS in
the FastAPI startup terminal. Existing certificate configuration is retained.
Restart FastAPI and Streamlit to load the new routes and imported UI modules.
No chain reset, re-registration, or new deployment is required.

Implementation checks: frontend/api.py, frontend/keeper_transfers.py, and
frontend/workspace.py parsed/imported successfully, as did backend/main.py.
Local OpenAPI contains the authenticated status GET and all four transfer POSTs.
The running FastAPI instance was inspected and still needed a restart. No unit
tests were created or run; no authenticated write calls, database changes,
actual transfer, or browser end-to-end verification were performed by the agent.
The human can now verify breeder initiation, buyer acceptance, manager/status
changes, and buyer authorship/keeper permissions through the website.

The human subsequently reported successful website handover and completion of
post-transfer husbandry verification. This records the human's manual acceptance;
it is not a claim that the agent submitted transactions or ran automated tests.
