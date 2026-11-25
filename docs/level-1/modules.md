# Level 1 - Backend Modules

## Laboratory report selection — 2026-11-20

The approved revision UI selects a stored report title rather than accepting a
manually copied Series ID. `GET /api/v1/laboratories/me/certificate-series` is a
read-only, authenticated laboratory endpoint. It returns series ID, snake ID,
title, laboratory ID, and the highest stored version number for each series.
The laboratory scope comes exclusively from the authenticated participant, not
query parameters. Duplicate titles remain separate series and the UI includes
identifiers to distinguish them. A stored version number does not imply confirmed
chain evidence; the existing revision operation retains issuer and chain checks.
No schema or write API change is required. Certificate history offers a separate
original-PDF download for every version without a version-selection dropdown.

## 1. Purpose and Architecture

This document describes the six business modules inside the FastAPI backend and how they work together. It follows the architecture and conventions defined in Level 0. Unresolved details are listed as open design questions.

This iteration is a one-week local demonstration, limited to the approved workflow in [the logical data model](data-model.md). Module names describe responsibilities inside one application, not six independently built products. Use fixed local Hardhat role accounts and simple Streamlit views. Do not add production login, wallets, payments, marketplace features, report parsing, or husbandry blockchain evidence.

The backend is a modular monolith: one FastAPI application containing separate, focused business modules. The modules are parts of the same application, not independently deployed services.

Streamlit communicates with FastAPI through REST-style HTTP endpoints under `/api/v1`. FastAPI manages PostgreSQL records and file storage, and uses web3.py to interact with Solidity contracts on an Ethereum-compatible blockchain. Streamlit does not access PostgreSQL directly.

## 2. Snake Registry

### Business Responsibility

Maintain each snake's registered identity and detailed profile.

### Main Operations

- Register a snake and its initial keeper.
- Retrieve a snake's identity and profile.
- Provide up to three randomly selected existing profiles for Buyer previews through `GET /api/v1/snakes/random-profiles`; profile and photo content remain off-chain.
- Provide up to three random profile photos on the unauthenticated login page without returning snake identifiers or profile fields.
- Save the breeder's initial profile and display it. Post-transfer profile and photo editing screens are outside this demonstration.
- Provide other modules with snake existence and current keeper information.

### On-Chain Responsibilities

Coordinate registration of the snake identifier and initial keeper address. Read the current keeper from contract state. Later keeper changes belong to Keeper Transfers.

### Off-Chain Responsibilities

Maintain detailed identity profiles, photographs or their references, and user-facing metadata in PostgreSQL and file storage.

### Dependencies

No required dependency on another business module for basic registration. This module provides identity and keeper queries to other modules. Reading the current keeper does not require calling Keeper Transfers.

### Authorization Boundaries

The breeder registers the demonstration snake. The registering address becomes the initial keeper on confirmation; initial keeper assignment to someone else is not part of this iteration. Breeder attribution remains unchanged by transfer. This module must not provide a way to bypass keeper transfer rules.

## 3. Laboratory Authorization

### Business Responsibility

Manage which laboratory addresses are authorized to issue certificates.

### Main Operations

- Grant laboratory authorization.
- Laboratory deauthorization is outside this demonstration; do not build a screen for it.
- Check whether a laboratory address is currently authorized.

### On-Chain Responsibilities

Coordinate and read laboratory authorization changes. Solidity enforces permission to change this authorization.

### Off-Chain Responsibilities

Store the laboratory identifier, name, descriptive testing direction, and participant link defined in the logical model. Track setup transactions where needed. Both laboratories use the same certificate logic; directions do not introduce separate result schemas.

### Dependencies

No required dependency on another business module. Certificate Management and Certificate Verification use its authorization queries where needed.

### Authorization Boundaries

Only administrators may manage laboratory authorization. This authority does not allow administrators to forcibly transfer snakes or revise another issuer's certificates.

Provision the two local laboratory addresses during administrative setup. Removing laboratory authorization and its effect on earlier certificates are deferred; those decisions must not block the fixed demonstration.

## 4. Certificate Management

### Business Responsibility

Manage certificate issuance, append-only revision, revocation, and traceable version history.

### Main Operations

- Issue a certificate for a registered snake.
- Revise a certificate by appending a new version, without overwriting previous versions.
- Represent specified-version revocation in the logical design; a revocation demonstration screen is outside this iteration.
- Retrieve certificate details and all previous versions, subject to file access permissions.

### On-Chain Responsibilities

Coordinate recording of certificate hashes, version references, issuers, and statuses. Each version must preserve its own hash, issuer, version reference, and status information. Solidity enforces certificate issuer permissions.

Status changes must not erase a version's identity or evidence. A confirmed correction adds a current version and supersedes the predecessor. Revocation targets a specified version and does not restore an older version. Detailed contract representation is a later small coding task.

### Off-Chain Responsibilities

Manage original certificate PDFs, file references, series/version identifiers, and display metadata. Calculate certificate file hashes before submitting them for recording on-chain. New independent tests create new series; corrections append versions within the existing series. Do not extract genetic or pathogen results from PDFs. Breeder genetic descriptions belong to the off-chain snake profile.

Revisions are append-only. Previous files and version records remain accessible under the agreed access policy; uploading a revision must not replace or delete them.

### Dependencies

- Snake Registry confirms the snake exists.
- Laboratory Authorization supplies laboratory authorization information.

### Authorization Boundaries

Only authorized laboratories may issue certificates. A laboratory may revise or revoke only certificates it issued. Keeping a snake does not grant permission to alter laboratory certificates.

The backend validates requests, while the contracts enforce on-chain permissions independently.

## 5. Certificate Verification (Deferred)

The human removed buyer-uploaded file verification from the current demonstration.
The operations below describe a deferred module, not implementation requirements
for this iteration. Certificate Management provides the approved history and PDF
download functionality.

### Business Responsibility

Check whether a certificate file matches its recorded blockchain evidence and explain certificate validity separately from that file comparison.

### Main Operations

- Calculate the hash of a supplied certificate file.
- Compare that hash with the selected on-chain certificate version.
- Retrieve the recorded issuer, version, and status.
- Report file hash matching separately from certificate validity and lifecycle status.
- Distinguish a completed check from a check that could not finish because blockchain data was unavailable.

### On-Chain Responsibilities

Read certificate evidence and relevant laboratory information. Verification itself does not change contract state.

### Off-Chain Responsibilities

Process the supplied file and prepare a verification result. Permanent storage of verification uploads or results is not assumed.

A matching hash establishes byte-level consistency with the recorded file. It does not establish certificate validity or prove the biological truth of the findings. A matching file may still be superseded or revoked, and the result must make this clear. Detailed validity rules remain a Level 2 decision.

### Dependencies

- Certificate Management provides certificate and version references.
- Laboratory Authorization provides current authorization information when needed.

Current laboratory authorization must not be presented as proof of authorization at the time of issuance.

### Authorization Boundaries

Buyers must be able to verify certificates. Whether verification requires login, and who may retrieve original files or private metadata, remains open. Permission to verify does not imply permission to issue or revise certificates.

## 6. Keeper Transfers

### Business Responsibility

Manage transfer of a registered snake from its current keeper to a designated recipient while preserving traceable keeper history.

### Main Operations

- Initiate a transfer to a designated recipient.
- Accept or reject a pending transfer.
- Cancel a pending transfer.
- Retrieve transfer state and historical keeper records.

Each snake may have at most one pending transfer. Acceptance completes the transfer and changes the current keeper. Rejection or cancellation ends the pending transfer without changing the keeper. Transfer expiration is not required for the MVP.

### On-Chain Responsibilities

Coordinate transfer transactions and read transfer state and events. Solidity enforces transfer permissions and the limit of one pending transfer per snake, including when requests compete with each other.

The contract updates the current keeper when a transfer completes. Transfer state and relevant events must support traceable historical keeper records.

### Off-Chain Responsibilities

Maintain application records linked to transfer transactions and information needed to display transfer progress and keeper history. Historical keeper records must remain traceable after later transfers.

A submitted transaction must not be presented as a completed transfer before the required blockchain confirmation. A transfer that is pending recipient action is distinct from a transaction awaiting blockchain confirmation.

### Dependencies

The existing SnakeRegistry provides identity and initial keeper values. The
separate KeeperTransfers contract is the authoritative current-keeper source
after activation; see [the keeper contract specification](../level-2/keeper-transfers.md).

### Authorization Boundaries

- Only the current keeper may initiate a transfer.
- Only the designated recipient may accept or reject it.
- The current keeper may cancel a pending transfer.
- Administrators cannot forcibly transfer snake records.
- After completion, the former keeper cannot add, edit, or delete husbandry records, even records they originally authored. The new keeper cannot edit or delete the predecessor's records.

Husbandry Records enforces the final rule using current keeper information. Rejection and cancellation do not grant keeper rights to the recipient.

## 7. Husbandry Records

### Business Responsibility

Maintain care records associated with a registered snake, preserving their original authorship across keeper changes.

### Main Operations

- Add a husbandry record.
- Display separate fixed-column tables for growth, shedding, feeding, and health records.
- Edit or delete only rows authored by the acting current keeper.
- Retrieve retained husbandry history without changing original authorship.

Fields and permissions are defined in [the logical data model](data-model.md). These are parallel off-chain tables; no generic parent record or audit subsystem is required.

### On-Chain Responsibilities

Read confirmed current keeper information for authorization through Snake Registry. This module submits no blockchain transactions, hashes, or commitments. All husbandry content remains off-chain.

### Off-Chain Responsibilities

Store detailed husbandry records in PostgreSQL. Associate each record with its snake and original author, and preserve that attribution when the keeper changes. A transfer must not reassign historical authorship to the new keeper.

Ordinary edits retain only the latest content. A permitted deletion removes the author's husbandry row; it must not cascade into certificate or transfer history. No content revision archive or soft-delete system is required.

### Dependencies

SnakeRegistry provides identity and initial keeper information. After activation,
KeeperTransfers provides confirmed current keeper information for all husbandry
writes. The original-author check remains in the backend and husbandry records
remain entirely off-chain. Buyer-uploaded certificate verification is deferred.

### Authorization Boundaries

Only the current keeper may add records. Editing or deletion requires both current keeper status and original authorship. Former keepers cannot write after transfer, and the new keeper cannot alter predecessor-authored rows. Never reassign a record's author during transfer or editing. If current keeper evidence is unavailable, do not authorize writes from a cached historical relationship. The local demonstration can show retained history to its role accounts; a production privacy/access system is outside scope.

## 8. Communication Inside One FastAPI Application

Each module exposes a small internal interface: a defined set of operations that other modules can call.

Modules communicate through ordinary Python function or method calls inside the application. They do not send HTTP requests to one another. HTTP is used between Streamlit and FastAPI.

For example, when issuing a certificate:

1. The FastAPI route receives and validates the request.
2. Certificate Management asks Snake Registry whether the snake exists.
3. It asks Laboratory Authorization about the issuing laboratory.
4. It calculates the file hash and coordinates the authorized blockchain transaction through web3.py.
5. It tracks the transaction outcome and associated off-chain records.

API routes handle HTTP concerns. Business operations and decisions belong inside the modules. Requests follow Level 0 API conventions, including Pydantic input validation, plural resource names, and snake_case JSON fields.

Each module owns its off-chain records. Other modules use its internal interface instead of directly changing its database tables. The modules share PostgreSQL; separate databases are not required.

Shared technical helpers can support database connections, file access, hashing, authentication, and web3.py integration. These helpers are not additional business modules and must not take over business decisions.

The six backend modules do not imply six Solidity contracts. Contract organization needs separate design, while contract authorization remains separate from FastAPI business logic.

## 9. Consistency Between PostgreSQL and the Blockchain

A PostgreSQL update and a blockchain transaction cannot be treated as one automatically atomic operation: one may succeed while the other fails.

The design tracks transaction progress and distinguishes submitted, confirmed, and failed outcomes. Modules must use confirmed blockchain state for on-chain facts rather than assuming that submission succeeded. This applies to registration, laboratory setup, certificates, and transfers. Husbandry records have no blockchain transactions.

Backend permission checks help reject invalid requests early. Solidity must independently enforce on-chain authorization and state rules when a transaction executes, including competing transfer actions.

Discuss the minimal local confirmation and failure-handling behavior during the relevant coding task. Read confirmed keeper state before husbandry writes; do not claim that SQL and the blockchain form one atomic system. Production retry infrastructure, general event indexing, and distributed race recovery are not requirements for this sequential local demonstration.

Private keys must not be stored in PostgreSQL or exposed through API responses.

## 10. Open Design Questions

| Area | Question to resolve |
|---|---|
| Local signing setup | Explain the local role-to-account mapping and development-only signing configuration; never put private keys in SQL or API responses. |
| Registration identifiers | Agree on the identifier representation when defining registration inputs/outputs. The registering address is already settled as initial keeper. |
| Certificate evidence | Agree on hash algorithm, identifier encoding, version/status representation, and function inputs/outputs during the certificate task. |
| File handling | Agree on minimal local storage paths, PDF upload checks, and downloads. Verification uploads need no permanent storage. |
| Transfer responses | Define minimal responses for ended or invalid transfers during the transfer task; retain the agreed authorization rules. |
| Transaction confirmation | Define local confirmation and failed-transaction display during the first chain integration task. |
| Contract organization | Keep the design small; six backend responsibilities do not require six contracts. Agree on the structure before the human inserts contract code. |

Transfer acceptance and rejection by the designated recipient, cancellation by the current keeper, one pending transfer per snake, and traceable keeper history are settled requirements. Transfer expiration is outside the MVP requirements.

Append-only certificate revisions, accessible previous files, version evidence, separate hash and lifecycle results, fully off-chain husbandry details, and original author attribution are settled requirements. Current keepers may add records and edit/delete only their own rows; former keeper rows are read-only after transfer. Ordinary husbandry changes keep no content version history.

Do not reopen these decisions as production-platform requirements. Laboratory deauthorization, revocation screens, post-registration profile/photo editing, report-result parsing, and production authentication are outside this demonstration.

Open questions should be resolved in the relevant Level 1 designs and Level 2 specifications before dependent implementation tasks are approved. Any decision that changes Level 0 boundaries or authorization rules requires explicit architecture approval.
