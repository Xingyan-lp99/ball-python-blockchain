# Level 1 - Data Model

## 1. Purpose and Scope

This document defines the initial data model for the Ball Python Blockchain Registry, including the reviewed student MVP simplifications and approved snake registration decisions.

The design supports the six business modules in one FastAPI modular monolith. PostgreSQL stores detailed application data; Solidity maintains shared blockchain state and enforces on-chain authorization. FastAPI coordinates them through web3.py.

The first implementation target is snake registration. Implement `snakes`, `files` for the primary profile photo, and registration tracking in `blockchain_transactions` first. The other tables describe later module designs, not prerequisites for registration.

This is a design document, not SQLAlchemy models, migrations, or Solidity code.

## 2. Data Ownership

### A. PostgreSQL Source Data

PostgreSQL is authoritative for detailed snake profiles, breeder information, genetic descriptions, parent references, file metadata, detailed husbandry records and original authorship, and application requests and submission tracking.

Photos and original certificate PDFs remain in off-chain file storage. PostgreSQL stores their references. Descriptive genetic information is not automatically a laboratory-certified finding.

### B. Blockchain Source Data

The blockchain is authoritative for registered public snake identities, initial and current keepers, laboratory authorization, certificate hashes and versions, certificate statuses, pending transfers and outcomes, relevant historical events, and selected husbandry integrity commitments.

Detailed profiles, photographs, PDFs, and sensitive personal information are not placed on-chain.

### C. PostgreSQL References and Cached Blockchain State

PostgreSQL may hold transaction hashes, chain and contract references, receipt information, and cached confirmed keeper, laboratory, certificate, or transfer state.

These caches support display and queries. They do not override blockchain state or independently grant permission. An intended change is distinct from an observed confirmed change. Unknown state must not be represented as confirmed success.

The MVP does not require common cache provenance columns `state_block_number`, `state_block_hash`, or `state_checked_at` on business tables. Receipt block information belongs in `blockchain_transactions`. More detailed cache provenance may be designed later if needed.

## 3. Shared Conventions

### Identifiers and Types

| Concept | PostgreSQL type | Meaning |
|---|---|---|
| Internal primary key | `uuid` | Database identity; every table uses `id` |
| Public business identifier | `text` | Human-readable identifier such as `S001` |
| Ethereum address | `varchar(42)` | `0x` followed by 40 hexadecimal characters |
| Transaction or block hash | `varchar(66)` | `0x` followed by 64 hexadecimal characters |
| Chain ID | `bigint` | Positive integer suitable for the MVP's Ethereum-compatible chains |
| Block number | `bigint` | Nonnegative block height |
| Timestamp | `timestamptz` | Timezone-aware timestamp, handled consistently in UTC |
| Calendar date | `date` | Date without an assumed time |
| Status | `text` with allowed-value constraints | Explicit lifecycle value |
| Cryptographic digest | `bytea` | Digest bytes interpreted using a named algorithm |

Internal UUIDs, public snake IDs, Ethereum addresses, and transaction hashes are distinct and must not be interchangeable. Validate addresses and store a consistent lowercase form for comparison; display may use checksum notation. Validate chain IDs against the supported positive `bigint` range.

Use explicit foreign keys, plural table names, and snake_case column names. Primary keys and unique constraints provide lookup indexes. Additional indexes below support relationships and common queries.

Do not cascade-delete historical records. Referenced records are retained unless a later approved policy permits removal without losing required history. Never store private keys in PostgreSQL.

### Blockchain Scope

`public_snake_id` is system-generated and unique across this application. A blockchain identity is located by chain ID, registry contract address, and public snake ID.

The MVP has one authoritative blockchain registration per snake database row. Concurrent registration across multiple deployments would need a later mapping design. Transaction rows record the actual target contract; the design does not require one contract per business module.

## 4. Approved Snake Registration Decisions

- Breeders register snakes and specify the initial keeper address. The initial keeper may be the breeder's own wallet.
- The system generates a unique public snake ID, for example `S001`. Users do not supply the identifier.
- Required profile data is sex, breeder information, and genetic description.
- Nickname, hatch date, sire, and dam are optional.
- The first version supports one primary profile photo. The nullable photo reference allows a profile without an uploaded photo.
- Each parent may be a registered snake reference or an external textual reference; an unknown parent may be omitted.
- The MVP guarantees public ID uniqueness. It does not automatically prove that two registrations refer to different physical animals.
- Detailed profiles remain in PostgreSQL. Blockchain registration stores the public snake identity and initial/current keeper state.
- Registration succeeds only after confirmed successful blockchain execution.
- Failed registration attempts do not delete the profile. The breeder may correct the profile and retry registration, retaining its public ID and earlier attempt records.

These decisions resolve the corresponding registration questions previously left open in `modules.md`. That document is not modified as part of this revision. Authentication, signing, and precise confirmation behavior still require Level 2 specification.

## 5. PostgreSQL Tables

### 5.1 snakes

**Purpose:** Store detailed snake profiles and link them to blockchain registration.

**Primary key:** `id`.

| Field | Type | Nullable | Purpose |
|---|---|---|---|
| `id` | `uuid` | No | Internal database identity |
| `public_snake_id` | `text` | No | System-generated public ID, such as S001 |
| `nickname` | `text` | Yes | Optional display name |
| `sex` | `text` | No | `male`, `female`, or `unknown` |
| `hatch_date` | `date` | Yes | Known hatch date |
| `breeder_label` | `text` | No | Required breeder or breeding organization information |
| `breeder_reference` | `text` | Yes | Optional external breeder record reference |
| `genetic_description` | `text` | No | Required descriptive genetics or morph information |
| `sire_id` | `uuid` | Yes | Registered sire |
| `sire_external_reference` | `text` | Yes | External sire reference or description |
| `dam_id` | `uuid` | Yes | Registered dam |
| `dam_external_reference` | `text` | Yes | External dam reference or description |
| `profile_file_id` | `uuid` | Yes | One primary profile photo |
| `profile_status` | `text` | No | `draft`, `active`, or `archived` |
| `requested_initial_keeper_address` | `varchar(42)` | No | Initial keeper specified by the breeder |
| `chain_id` | `bigint` | Yes | Registration chain; required before submission |
| `registry_contract_address` | `varchar(42)` | Yes | Registry address; required before submission |
| `registration_status` | `text` | No | `not_submitted`, `submitted`, `confirmed`, or `failed` |
| `initial_keeper_address_cache` | `varchar(42)` | Yes | Initial keeper from confirmed registration evidence |
| `current_keeper_address_cache` | `varchar(42)` | Yes | Current keeper from confirmed contract state |
| `registration_transaction_id` | `uuid` | Yes | Successful confirmed registration transaction |
| `created_at` | `timestamptz` | No | Profile creation time |
| `updated_at` | `timestamptz` | No | Latest database update |

**Foreign keys:** `sire_id` and `dam_id` reference `snakes.id`; `profile_file_id` references `files.id`; `registration_transaction_id` references `blockchain_transactions.id`.

**Unique constraint:** `public_snake_id`. Its application-wide uniqueness also prevents duplicate IDs within a chain and registry scope.

**Important indexes:** `sire_id`, `dam_id`, `profile_file_id`, `registration_transaction_id`, `(profile_status, created_at)`, and `(chain_id, current_keeper_address_cache)`.

**Relationships:** A snake has many certificates, historical transfers, husbandry records, and registration transaction attempts. The successful registration reference is separate from the attempt history.

**Rules:**

- Required breeder and genetic descriptions must not be blank. Breeder information need not include contact details or other unnecessary personal information.
- For each parent, at most one of the internal reference and external text is populated; both may be null.
- A snake cannot reference itself as a parent. Sire and dam cannot be the same registered snake. Application validation prevents parentage cycles.
- Profile status describes off-chain workflow, not registration success or animal health. A draft is not permission to omit required registration profile fields.
- Chain and contract fields are populated together before submission. A confirmed registration requires matching successful transaction evidence and keeper caches.
- Profile correction after failure preserves the same database ID and public snake ID. Corrections cannot silently change an already-submitted transaction's payload; pending and retry behavior is specified at Level 2.
- Archiving a profile does not erase its blockchain identity or history.

### 5.2 laboratories

**Purpose:** Represent a laboratory authorization identity and its confirmed authorization cache. Implement with the Laboratory Authorization module.

**Primary key:** `id`.

| Field | Type | Nullable | Purpose |
|---|---|---|---|
| `id` | `uuid` | No | Internal identity |
| `display_name` | `text` | Yes | Optional laboratory label |
| `chain_id` | `bigint` | No | Authorization chain |
| `authorization_contract_address` | `varchar(42)` | No | Contract governing authorization |
| `wallet_address` | `varchar(42)` | No | Laboratory issuer address |
| `is_authorized_cache` | `boolean` | Yes | Confirmed authorization; null means unknown |
| `created_at` | `timestamptz` | No | Local creation time |
| `updated_at` | `timestamptz` | No | Latest database update |

**Foreign keys:** None directly; certificates reference this table. Transaction relationships are added with this module.

**Unique constraint:** `(chain_id, authorization_contract_address, wallet_address)`.

**Important index:** `(chain_id, wallet_address)`.

**Relationships:** One laboratory identity may issue many certificates and have many authorization operations. A row does not grant on-chain authorization. Address changes must not rewrite historical issuers; address rotation requires a separate Level 2 policy.

### 5.3 certificates

**Purpose:** Group versions of one certificate for a snake and issuing laboratory. Implement with Certificate Management.

**Primary key:** `id`.

| Field | Type | Nullable | Purpose |
|---|---|---|---|
| `id` | `uuid` | No | Internal certificate identity |
| `snake_id` | `uuid` | No | Subject snake |
| `laboratory_id` | `uuid` | No | Original issuing laboratory identity |
| `certificate_reference` | `text` | No | Stable issuer-scoped business reference |
| `created_at` | `timestamptz` | No | Creation time |

**Foreign keys:** `snake_id` references `snakes.id`; `laboratory_id` references `laboratories.id`.

**Unique constraint:** `(laboratory_id, certificate_reference)`.

**Important index:** `snake_id`; the unique constraint supports laboratory lookup.

**Relationships:** One certificate belongs to one snake and issuer and has many versions. Its issuer chain must agree with the snake's chain and relevant authorization configuration. Do not store one global valid flag; verification evaluates a particular version and its evidence.

### 5.4 certificate_versions

**Purpose:** Preserve append-only certificate revisions and their evidence. Implement with Certificate Management.

**Primary key:** `id`.

| Field | Type | Nullable | Purpose |
|---|---|---|---|
| `id` | `uuid` | No | Internal version identity |
| `certificate_id` | `uuid` | No | Parent certificate |
| `version_number` | `integer` | No | Positive version sequence |
| `version_reference` | `text` | No | Stable version reference used on-chain |
| `file_id` | `uuid` | No | Original certificate document |
| `hash_algorithm` | `text` | No | Certificate hash algorithm |
| `file_hash` | `bytea` | No | Digest of the exact document |
| `issuer_address` | `varchar(42)` | No | Preserved issuer address |
| `genetic_description` | `text` | Yes | Version-specific findings |
| `publication_status` | `text` | No | `not_submitted`, `submitted`, `confirmed`, or `failed` |
| `status_cache` | `text` | Yes | Confirmed lifecycle status, such as active, superseded, or revoked |
| `publication_transaction_id` | `uuid` | Yes | Successful confirmed publication transaction |
| `created_at` | `timestamptz` | No | Version creation time |

**Foreign keys:** `certificate_id` references `certificates.id`; `file_id` references `files.id`; `publication_transaction_id` references `blockchain_transactions.id` when this module is implemented.

**Unique constraints:** `(certificate_id, version_number)` and `(certificate_id, version_reference)`.

**Important indexes:** `file_id`, `publication_transaction_id`, and `(hash_algorithm, file_hash)`.

**Relationships:** Each version belongs to one certificate and references an immutable file. Publication and status-change attempts will use transaction tracking added with this module.

Revision inserts another version. Existing version content, issuer, reference, and hash are not overwritten. Earlier files remain accessible under the agreed access policy. Publication tracking and current status caches may change separately from immutable content; historical statuses remain traceable through blockchain events and transaction references.

A matching file hash does not prove certificate validity or biological truth. A matching file may still be superseded or revoked.

### 5.5 files

**Purpose:** Describe off-chain stored files. The first feature uses this table for one primary snake photo; later features use it for certificate PDFs.

**Primary key:** `id`.

| Field | Type | Nullable | Purpose |
|---|---|---|---|
| `id` | `uuid` | No | Internal file identity |
| `storage_key` | `text` | No | Stable identifier in configured file storage |
| `original_filename` | `text` | Yes | Sanitized original filename |
| `media_type` | `text` | No | Content type |
| `size_bytes` | `bigint` | No | Nonnegative size |
| `hash_algorithm` | `text` | No | Digest algorithm |
| `content_hash` | `bytea` | No | Digest of stored bytes |
| `created_at` | `timestamptz` | No | File registration time |

**Foreign keys:** None.

**Unique constraint:** `storage_key`.

**Important index:** `(hash_algorithm, content_hash)`, not necessarily unique.

**Relationships:** Referenced by a snake's primary photo and, later, certificate versions. File metadata does not imply an on-chain commitment for a profile photo.

Stored certificate bytes are immutable once referenced as evidence. Replacement content receives a new file record and storage key. Storage keys do not grant download permission. Access follows application authorization. Do not expose secrets in filenames or storage references.

### 5.6 keeper_transfers

**Purpose:** Preserve transfer requests, confirmed outcomes, and keeper history. Implement with Keeper Transfers.

**Primary key:** `id`.

| Field | Type | Nullable | Purpose |
|---|---|---|---|
| `id` | `uuid` | No | Internal transfer identity |
| `snake_id` | `uuid` | No | Transferred snake |
| `transfer_reference` | `text` | No | Stable transfer business reference |
| `from_keeper_address` | `varchar(42)` | No | Initiating keeper |
| `recipient_address` | `varchar(42)` | No | Designated recipient |
| `status_cache` | `text` | Yes | Confirmed pending, accepted, rejected, or cancelled state |
| `initiation_transaction_id` | `uuid` | Yes | Confirmed initiation transaction |
| `resolution_transaction_id` | `uuid` | Yes | Confirmed acceptance, rejection, or cancellation |
| `created_at` | `timestamptz` | No | Local request creation |
| `resolved_at` | `timestamptz` | Yes | Confirmed resolution time |

**Foreign keys:** `snake_id` references `snakes.id`; both transaction fields reference `blockchain_transactions.id` when this module is implemented.

**Unique constraints:** `(snake_id, transfer_reference)` and a conditional unique index allowing at most one confirmed pending transfer per snake.

**Important indexes:** `(snake_id, created_at)`, `(recipient_address, status_cache)`, and both transaction foreign keys.

**Relationships:** One snake has many historical transfers. Each transfer may have several initiation or resolution attempts, added to transaction tracking with this module.

A null status cache means confirmed transfer state has not been observed. Submission is distinct from a transfer pending recipient action. A failed acceptance transaction does not mean rejection; the transfer may remain pending.

Solidity independently enforces that only the current keeper initiates or cancels, only the recipient accepts or rejects, and at most one pending transfer exists per snake. Administrators cannot force transfers. Expiration is not required for the MVP.

Initial registration evidence and accepted transfers establish keeper history. Preserve historical rows and relevant events.

### 5.7 husbandry_records

**Purpose:** Store detailed care records with original authorship. Implement with Husbandry Records.

**Primary key:** `id`.

| Field | Type | Nullable | Purpose |
|---|---|---|---|
| `id` | `uuid` | No | Internal record identity |
| `snake_id` | `uuid` | No | Subject snake |
| `author_address` | `varchar(42)` | No | Original authenticated author address |
| `record_type` | `text` | No | Care category; vocabulary defined at Level 2 |
| `occurred_at` | `timestamptz` | No | Time of the recorded care event |
| `details` | `jsonb` | No | Validated structured care details |
| `notes` | `text` | Yes | Optional narrative |
| `created_at` | `timestamptz` | No | Time appended to the registry |

**Foreign key:** `snake_id` references `snakes.id`.

**Unique constraints:** Primary key only.

**Important indexes:** `(snake_id, occurred_at)` and `(author_address, created_at)`.

**Relationships:** One snake has many husbandry records. Original authorship remains unchanged across keeper transfers.

Former keepers cannot append records after transfer completion, even if they enter an earlier event time. Permission is checked when appending. Corrections must preserve original attribution and existing integrity evidence.

**Conceptual integrity support:** Selected records must support on-chain integrity commitments while detailed content stays in PostgreSQL. Level 2 will define selection, data representation, submission, verification, and the relationship to transaction evidence. No commitment columns, proof structures, or grouping strategy are prescribed here before that decision exists.

### 5.8 blockchain_transactions

**Purpose:** Track blockchain attempts, related business operations, and confirmed outcomes. The first implementation tracks only snake registration transactions.

**Primary key:** `id`.

| Field | Type | Nullable | Purpose |
|---|---|---|---|
| `id` | `uuid` | No | Internal attempt identity |
| `request_id` | `uuid` | No | Groups attempts for one application operation |
| `attempt_number` | `integer` | No | Positive attempt sequence |
| `snake_id` | `uuid` | No for registration MVP | Snake being registered |
| `chain_id` | `bigint` | No | Target chain |
| `contract_address` | `varchar(42)` | No | Actual target contract |
| `sender_address` | `varchar(42)` | No | Transaction sender |
| `transaction_hash` | `varchar(66)` | Yes | Hash when available |
| `operation_type` | `text` | No | Initially only `snake_registration` |
| `status` | `text` | No | Prepared, submitted, confirmed, or failed |
| `created_at` | `timestamptz` | No | Attempt creation |
| `submitted_at` | `timestamptz` | Yes | Submission time |
| `confirmed_at` | `timestamptz` | Yes | Successful confirmation time |
| `block_number` | `bigint` | Yes | Receipt block number |
| `block_hash` | `varchar(66)` | Yes | Receipt block hash |
| `receipt_status` | `smallint` | Yes | Receipt success or failure indicator |
| `failed_at` | `timestamptz` | Yes | Time definitive failure was recorded |
| `failure_code` | `text` | Yes | Failure category |
| `failure_message` | `text` | Yes | Sanitized diagnostics |
| `last_checked_at` | `timestamptz` | Yes | Latest outcome check |

**Foreign key:** `snake_id` references `snakes.id`.

**Unique constraints:** `(chain_id, transaction_hash)` when a hash exists, and `(request_id, attempt_number)`.

**Important indexes:** `snake_id`, `(status, last_checked_at)`, and `(chain_id, block_number)`.

**Relationships:** One snake has many registration attempts. Its `registration_transaction_id` identifies the successful confirmed attempt. The application checks that this transaction belongs to that snake and matches its chain and registry.

Do not implement laboratory, certificate, transfer, or husbandry operation relationships in the first version. Add appropriate typed foreign keys or relationships, operation values, and subject constraints when each module is implemented. No generic table-name-plus-UUID relationship is needed for the registration MVP.

### Transaction Lifecycle

| State | Meaning |
|---|---|
| `prepared` | Attempt recorded locally; submission has not yet been established |
| `submitted` | Submitted, but successful confirmation has not been established |
| `confirmed` | Successful execution satisfies the application's confirmation policy |
| `failed` | Definitive submission failure or confirmed execution failure |

- Submitted attempts require a hash and submission timestamp.
- Confirmed attempts require a successful receipt, hash, block information, and confirmation timestamp. Submission alone never establishes success.
- A mined transaction awaiting the agreed confirmation threshold remains submitted; receipt fields may already exist.
- An on-chain failure may have a hash and block information. A failure before broadcast may have neither. Failed attempts have no successful confirmation timestamp.
- Failed attempts require sanitized failure information. Network timeouts alone do not prove failure.
- Retries create new attempt rows rather than overwriting earlier hashes or outcomes.
- Failed registration preserves the off-chain profile and public ID for correction and retry.
- Registration status on `snakes` summarizes its workflow; historical attempts remain in this table. A later failed duplicate attempt must not undo an already-confirmed registration.

## 6. Logical On-Chain Model

This describes information and behavior, not Solidity layouts or contracts.

| Area | Logical blockchain model |
|---|---|
| Snake registration | Stable public snake identifier, existence, and initial keeper |
| Current keeper | Current keeper address for the registered snake |
| Laboratory authorization | Authorized issuer addresses managed by permitted administrators |
| Certificate versions | Snake, certificate and version references, issuer, and exact file hash |
| Certificate status | Current version status with traceable historical changes |
| Pending transfers | Snake and transfer references, initiating keeper, designated recipient, and state |
| Husbandry integrity | Conceptual support for commitments to selected off-chain records; strategy deferred to Level 2 |
| Historical events | Registration, authorization changes, certificate issuance/revision/revocation, transfer initiation/acceptance/rejection/cancellation, and commitment recording |

Certificate version content is append-only. Later status changes do not erase earlier evidence. A matching hash is separate from certificate validity.

Historical events must carry enough identifiers to reconstruct relevant history. Transaction rows are not a complete event archive. A separate local archive may be designed later if needed; it is not required for the first registration feature.

## 7. Integrity and Synchronization

PostgreSQL constraints enforce local relationships. Solidity independently enforces shared state and blockchain permissions. Modules own their records and communicate through internal Python interfaces inside FastAPI.

FastAPI verifies transaction-to-record associations and compatible blockchain scopes. It populates confirmed caches only from verified evidence and must not treat stale keeper caches as sufficient permission for later husbandry writes.

A database update and blockchain submission are not one atomic operation. Record the profile, then transaction attempts referencing it, then link successful evidence after confirmation. Reconcile operations if blockchain execution succeeds but the database update fails.

Omitting common cache provenance columns does not remove the need to check confirmed blockchain state. Confirmation, uncertain submissions, recovery, and development-chain reset behavior require Level 2 rules.

## 8. Example: Snake S001

All values below are illustrative, not actual registry entries.

### PostgreSQL Profile

| Field | Example |
|---|---|
| `id` | `7c0f2ef1-834b-4a79-9c2d-8872cf065abd` |
| `public_snake_id` | `S001`, generated by the system |
| `nickname` | `Amber` |
| `sex` | `female` |
| `hatch_date` | `2025-06-15` |
| `breeder_label` | `Example Breeder`, a nonempty display label |
| `genetic_description` | `Reported Pastel morph; not laboratory verified` |
| `sire_id` | Null |
| `sire_external_reference` | `External breeding record: sire A17` |
| `dam_id` | Null |
| `dam_external_reference` | Null |
| `profile_file_id` | Optional UUID referencing the one primary photo |
| `profile_status` | `active` |

The external sire does not require a fictitious registered snake row. Required breeder and genetic information are present. Profile status alone does not establish successful registration.

### Request and Submission

The breeder specifies the initial keeper, for example `0x1111111111111111111111111111111111111111`. This may be the breeder's own wallet. The application selects the configured chain and registry and creates an attempt linked to S001's internal UUID.

A transaction hash has a different format and purpose, for example `0x` followed by 64 hexadecimal characters. It is not S001's UUID, public ID, or keeper address.

After submission, transaction status and registration status are submitted. The hash is recorded, but registration is not yet successful and confirmed keeper caches remain null.

### Confirmed Registration

The blockchain records public identity S001, its initial keeper, its current keeper, and a registration event. It does not need the database UUID, nickname, hatch date, breeder label, genetic description, parent text, or photograph.

After successful execution satisfies the confirmation policy, the transaction becomes confirmed, receipt block information is saved, S001's registration status becomes confirmed, keeper caches are populated, and the successful transaction is linked to the profile.

If execution fails, the attempt becomes failed without inventing a confirmed keeper. S001's profile remains available for correction and retry with the same public ID and new transaction attempt records.

After a later accepted keeper transfer, current keeper state changes. Initial registration evidence, historical transfers, certificate versions, and original husbandry authors remain traceable.

## 9. Unresolved Level 2 Questions

### Snake Registration Details

1. How is a breeder authenticated and linked to the transaction signing method?
2. What precise validation applies to profile text, sex, dates, parent references, and keeper addresses?
3. What ID format and allocation procedure generate unique IDs safely under concurrent requests? System generation and uniqueness are already settled.
4. Who may correct profile fields, and how are corrections handled while a registration transaction is pending or after confirmation?
5. What API responses and UI states expose pending, failed, and confirmed registration?

Breeder registration, breeder-specified initial keepers, permitted use of the breeder's own wallet, required and optional profile fields, one primary photo support, registered or external parents, and the absence of automatic physical-animal deduplication are settled requirements.

### Transactions and Synchronization

1. How are transactions signed without storing private keys in PostgreSQL?
2. What confirmation threshold establishes success?
3. How are uncertain broadcasts, dropped transactions, replacements, and repeated requests handled safely?
4. How is successful chain execution reconciled after a database failure?
5. How are reorganizations and local development-chain resets handled?
6. How will later modules discover relevant operations performed directly on-chain?

Confirmed execution is required for success. Failed attempts preserve the profile for correction and retry; neither rule is an open question.

### Certificates and Laboratories

1. Which hash algorithm and version-reference format are used?
2. What are the exact supersession and revocation rules, including whether revocation affects one version or a full certificate history?
3. May deauthorized laboratories revise or revoke earlier certificates?
4. How is laboratory authorization at issuance established during verification?
5. Who may retrieve previous certificate files, and how are laboratory address changes represented?

Append-only revisions and accessible, traceable previous versions are settled requirements.

### Transfers

1. How are transfer references generated?
2. How are competing acceptance, rejection, and cancellation requests reported?
3. How is historical event data retrieved for keeper-history displays?
4. How are husbandry writes coordinated with confirmed keeper changes?

Recipient acceptance/rejection, current-keeper initiation/cancellation, one pending transfer per snake, traceable history, and no required MVP expiration are settled.

### Husbandry Integrity

1. What care categories and fields are needed, and who may read historical records?
2. What correction policy preserves original attribution and existing integrity evidence?
3. Which records receive commitments, what data is committed, and how is integrity checked?
4. Who may submit commitments, when are they submitted, and what record-to-transaction relationship is needed?

The Level 2 strategy must precede a detailed commitment schema. Detailed content remaining in PostgreSQL, support for selected on-chain commitments, original authorship, and the prohibition on former keepers appending new records are settled.

### Files and Access

1. Where are files stored, and which media types and size limits are allowed?
2. Who may upload, replace, or retrieve the primary photo and other files?
3. What retention rules apply to unreferenced uploads and verification uploads?

The first version supports one primary profile photo; a photo gallery is not part of this design.

Resolve these remaining details in the relevant Level 2 specifications before implementing dependent functionality. No change to Level 0 architecture is introduced by this design.
