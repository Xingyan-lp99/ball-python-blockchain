# Level 1 - Logical Data Model

## 1. Purpose and Demonstration

This is the logical model for a one-week learning project. It describes entities,
primary keys (PK), foreign keys (FK), and relationships, not executable schemas.
PostgreSQL types, indexes, API shapes, hash algorithm, and Solidity storage layout
will be discussed when the corresponding small coding task is approved.

The [editable combined diagram](../diagram/data-model.drawio) uses blue for
off-chain records, green for blockchain state/evidence, and yellow for boundary
and permission notes. Blockchain boxes are logical state, not additional SQL
tables or a requirement for separate contracts.

| Step | Actor and action | Acceptance result |
|---|---|---|
| 1 | Breeder registers one fictional snake | Profile is stored off-chain; the registering address becomes the confirmed initial keeper. |
| 2 | LAB001 and LAB002 each issue one report | Two independent certificate series reference the same snake, each with V1. |
| 3 | LAB001 corrects its report | Its series gains V2; V1 and its original file remain available. |
| 4 | Buyer verifies the official V2 file | Its bytes match the selected on-chain V2 hash; version status is shown separately. |
| 5 | Buyer verifies a modified copy against V2 | Hash mismatch is shown; verification does not register a version. |
| 6 | Breeder initiates a transfer after the offline sale; buyer accepts | Only confirmed acceptance changes the current keeper. No payment is processed here. |
| 7 | Buyer adds, edits, and deletes their own husbandry rows | Own rows are writable; breeder-authored rows remain read-only. |

Use local Hardhat accounts for breeder, buyer, LAB001, LAB002, and administrative
setup. Roles do not require separate account types or a login system. Laboratory
testing directions are descriptive metadata, not different program structures.
The PDFs are opaque documents: no extracted genetics, pathogens, or test-result
tables are required. Example files are reference material, not final schemas.

## 2. Off-Chain Entities and Relationships

Field lists are logical proposals within the approved model. Names are English
and snake_case. A nullable relationship is identified explicitly below; complete
column constraints remain a later implementation discussion.

| Entity | Key and main fields | Relationship / purpose |
|---|---|---|
| participants | PK participant_id; display_name; wallet_address | One participant has one local demonstration address. The address identifies the signer, not a stored private key. A participant can be breeder, keeper, or record author. |
| laboratories | PK laboratory_id; FK participant_id; name; testing_direction | Each laboratory profile belongs to one participant, with one profile per lab participant. LAB001 and LAB002 have different addresses. |
| snakes | PK snake_id; FK breeder_id -> participants; FK current_keeper_id -> participants (confirmed cache, initially unset until registration confirms); breeder_internal_id; nickname; species; sex; date_of_birth; introduction; genetic_description; sire_description; dam_description; photo_reference; created_at; updated_at | One breeder can register many snakes. The on-chain snake identifier corresponds to snake_id. The breeder remains unchanged by transfer. Photo reference points to off-chain file storage; image bytes are not SQL fields. |
| certificate_series | PK series_id; FK snake_id; FK laboratory_id; title | One snake and one laboratory can each have many series. A new independent test creates a new series, even for the same snake and laboratory. |
| certificate_versions | PK version_id; FK series_id; version_number; optional FK previous_version_id -> certificate_versions; file_reference; file_hash; issuer_address; status; issued_at | One series has many versions. The first version has no predecessor; corrections refer to a predecessor in the same series. Version number is unique within a series. File references point to preserved original PDFs. Hash, issuer, and lifecycle status mirror confirmed on-chain evidence. |
| keeper_transfers | PK transfer_id; FK snake_id; FK from_participant_id -> participants; FK to_participant_id -> participants; status; initiated_at; resolved_at | One snake has many historical transfers; each has a sender and recipient. Resolved time is absent while pending. Status reflects confirmed transfer state, not transaction submission. |
| blockchain_transactions | PK transaction_id; transaction_hash; operation; status; optional FK snake_id; optional FK version_id; optional FK transfer_id | Each row tracks one submitted transaction and its submitted/confirmed/failed outcome. Link the relevant business object: registration to snake, issuance/revision to version, and transfer actions to transfer. One transfer can have multiple transaction rows. |

The model is deliberately small: no structured genetic results, specimen entity,
parent-snake relationships, marketplace, payment records, verification history,
or general-purpose audit system. Verification uploads are processed temporarily,
not added to the certificate archive. File paths and private keys must not be
exposed as user-facing evidence or included in API responses.

### Parallel Husbandry Entities

All four entities independently reference a snake and their original author.
They are not child records of one another and require no shared husbandry parent
table. Each has PK record_id; FK snake_id; FK created_by -> participants;
record_date; created_at; updated_at, plus the fields below.

| Entity / page table | Fixed visible content columns after date |
|---|---|
| growth_records | weight_g; length_cm (optional); notes |
| shedding_records | outcome; follow_up |
| feeding_records | food; feeding_outcome; notes |
| health_records | event; follow_up; status |

Show author information so that the human can distinguish writable and historical
rows. Each page table supports adding rows. These tables remain simple support
features; implementation should not add extra care-management workflows.

## 3. Blockchain Evidence and Authority

| Logical on-chain object | Evidence / state | Link to PostgreSQL |
|---|---|---|
| Snake management rights | snake_id; current_keeper_address; registration/transfer events | snakes.snake_id; address maps to participants.wallet_address |
| Laboratory issuance permission | laboratory account address and issuance permission | laboratories -> participants.wallet_address; provision the two demo laboratories during setup |
| Certificate evidence | series/version references; snake identifier; issuer address; file hash; version number; predecessor; lifecycle status | certificate_series and certificate_versions identifiers; do not put the PDF or testing results on-chain |
| Transfer state and events | transfer reference; snake identifier; from/to addresses; pending/accepted/rejected/cancelled outcome | keeper_transfers and its related blockchain_transactions |

Registration and certificate submission may have local records before confirmation.
Those records must not be displayed as completed or confirmed chain facts.
For a confirmed correction, show the earlier version as superseded and the new
version as current. Revocation targets one version, preserves its evidence, and
does not reactivate an older superseded version. A revocation page and laboratory
deauthorization workflow are outside this iteration; their full implementation
must not block the demonstration.

Transfer rules remain: only the current keeper initiates; only the designated
recipient accepts or rejects; only the current keeper cancels; at most one
pending transfer per snake. No expiry is required. Pending recipient acceptance
and a transaction awaiting confirmation are different conditions. The transfer
does not change breeder attribution, certificate issuers, or historical authors.

PostgreSQL caches do not grant chain rights. Check confirmed chain state for
authorization; if that check cannot complete, do not grant a write based only
on a cached keeper. Solidity enforces certificate and transfer permissions.
FastAPI enforces off-chain husbandry permissions using current keeper state.
This is a demonstration of shared evidence and signing authority, not a claim
that chain and SQL updates are automatically atomic or tamper-proof together.

## 4. Record Permissions and Verification

| Action | Current keeper, own row | Current keeper, predecessor's row | Former keeper |
|---|---|---|---|
| Add husbandry row | Allowed, author set to acting participant | Not applicable | Denied |
| Edit husbandry row | Allowed | Denied | Denied, including their own old rows |
| Delete husbandry row | Allowed | Denied | Denied, including their own old rows |
| View retained history | Allowed | Allowed | Demo view permitted; no write rights |

Editing keeps only the latest content; deletion removes the permitted husbandry
row without adding soft-deletion or revision history requirements. Record author
and snake association are not editable. Husbandry deletion never deletes a snake,
certificate, certificate file, or transfer history. Buyer editing of basic profile
fields and photographs is outside the demonstration workflow.

Verification takes a selected registered certificate version and supplied PDF
bytes. It compares their calculated hash with the on-chain hash and separately
reports issuer and lifecycle status. An old or revoked file may still match its
own recorded hash. An unavailable chain read is an incomplete check, not a hash
mismatch. Matching bytes do not prove biological truth, specimen identity, or
the correctness of a laboratory conclusion.

Use the local original V2 and modified V2 to exercise the match/mismatch cases;
do not copy the complete local reference documents into tracked documentation.

## 5. Implementation and Validation Boundaries

The human-AI workflow in AGENTS.md applies to every coding step: explain inputs,
outputs, reasons, and examples; obtain agreement; provide code in chat; the human
inserts it. No application code, migrations, tests, or executable configuration
are introduced by this document or diagram.

Implement the seven demonstration steps in order, one small task at a time.
Provide relevant test code under the same agreement-and-copy workflow. Include
negative cases for non-issuer certificate changes, unauthorized transfer actions,
former keeper writes, and a current keeper editing/deleting a predecessor's row.
Run tests only after the human inserts the corresponding code and report actual
results. Confirmation details, hash choice, file handling, and API/function
inputs and outputs are decisions for those tasks, not extra platform features.
