# Level 1 - Backend Modules

## 1. Purpose and Architecture

This document describes the six business modules inside the FastAPI backend and how they work together. It follows the architecture and conventions defined in Level 0. Unresolved details are listed as open design questions.

The backend is a modular monolith: one FastAPI application containing separate, focused business modules. The modules are parts of the same application, not independently deployed services.

Streamlit communicates with FastAPI through REST-style HTTP endpoints under `/api/v1`. FastAPI manages PostgreSQL records and file storage, and uses web3.py to interact with Solidity contracts on an Ethereum-compatible blockchain. Streamlit does not access PostgreSQL directly.

## 2. Snake Registry

### Business Responsibility

Maintain each snake's registered identity and detailed profile.

### Main Operations

- Register a snake and its initial keeper.
- Retrieve a snake's identity and profile.
- Maintain profile information, subject to an agreed editing policy.
- Provide other modules with snake existence and current keeper information.

### On-Chain Responsibilities

Coordinate registration of the snake identifier and initial keeper address. Read the current keeper from contract state. Later keeper changes belong to Keeper Transfers.

### Off-Chain Responsibilities

Maintain detailed identity profiles, photographs or their references, and user-facing metadata in PostgreSQL and file storage.

### Dependencies

No required dependency on another business module for basic registration. This module provides identity and keeper queries to other modules. Reading the current keeper does not require calling Keeper Transfers.

### Authorization Boundaries

Breeders register snakes according to Level 0. Precise registration permissions, initial keeper assignment rules, and profile editing permissions remain open. This module must not provide a way to bypass keeper transfer rules.

## 3. Laboratory Authorization

### Business Responsibility

Manage which laboratory addresses are authorized to issue certificates.

### Main Operations

- Grant laboratory authorization.
- Remove laboratory authorization.
- Check whether a laboratory address is currently authorized.

### On-Chain Responsibilities

Coordinate and read laboratory authorization changes. Solidity enforces permission to change this authorization.

### Off-Chain Responsibilities

Track application records associated with authorization transactions. Any additional laboratory profile information requires a defined feature requirement.

### Dependencies

No required dependency on another business module. Certificate Management and Certificate Verification use its authorization queries where needed.

### Authorization Boundaries

Only administrators may manage laboratory authorization. This authority does not allow administrators to forcibly transfer snakes or revise another issuer's certificates.

The effect of removing laboratory authorization on existing certificates and later revision or revocation remains an open question.

## 4. Certificate Management

### Business Responsibility

Manage certificate issuance, append-only revision, revocation, and traceable version history.

### Main Operations

- Issue a certificate for a registered snake.
- Revise a certificate by appending a new version, without overwriting previous versions.
- Revoke a certificate according to the agreed status rules.
- Retrieve certificate details and all previous versions, subject to file access permissions.

### On-Chain Responsibilities

Coordinate recording of certificate hashes, version references, issuers, and statuses. Each version must preserve its own hash, issuer, version reference, and status information. Solidity enforces certificate issuer permissions.

Status changes such as supersession or revocation must remain traceable and must not erase a version's identity or evidence. The precise status transition and history representation is a Level 2 decision.

### Off-Chain Responsibilities

Manage original certificate PDFs, file references, genetic descriptions, and related metadata. Calculate certificate file hashes before submitting them for recording on-chain.

Revisions are append-only. Previous files and version records remain accessible under the agreed access policy; uploading a revision must not replace or delete them.

### Dependencies

- Snake Registry confirms the snake exists.
- Laboratory Authorization supplies laboratory authorization information.

### Authorization Boundaries

Only authorized laboratories may issue certificates. A laboratory may revise or revoke only certificates it issued. Keeping a snake does not grant permission to alter laboratory certificates.

The backend validates requests, while the contracts enforce on-chain permissions independently.

## 5. Certificate Verification

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

Snake Registry provides snake identity and current keeper queries.

### Authorization Boundaries

- Only the current keeper may initiate a transfer.
- Only the designated recipient may accept or reject it.
- The current keeper may cancel a pending transfer.
- Administrators cannot forcibly transfer snake records.
- After completion, the former keeper cannot append new keeper records.

Husbandry Records enforces the final rule using current keeper information. Rejection and cancellation do not grant keeper rights to the recipient.

## 7. Husbandry Records

### Business Responsibility

Maintain care records associated with a registered snake, preserving their original authorship across keeper changes.

### Main Operations

- Add a husbandry record.
- Retrieve husbandry history according to the agreed access policy.
- Support recording and checking on-chain integrity commitments for selected records, with the exact workflow defined at Level 2.

Record fields and editing or deletion policies are not defined here.

### On-Chain Responsibilities

Read current keeper information for authorization through Snake Registry. Support cryptographic commitments for selected husbandry records so that their integrity can be checked against blockchain evidence.

A commitment is a compact cryptographic value used to check whether the associated off-chain data has changed. Detailed husbandry content remains off-chain. Record selection, commitment format, submission timing, and verification strategy are Level 2 design decisions.

### Off-Chain Responsibilities

Store detailed husbandry records in PostgreSQL. Associate each record with its snake and original author, and preserve that attribution when the keeper changes. A transfer must not reassign historical authorship to the new keeper.

Maintain the association between selected records and their on-chain commitments and transaction outcomes, according to the Level 2 strategy.

### Dependencies

Snake Registry provides snake identity and current keeper information. Shared web3.py integration supports commitment operations; Certificate Verification remains focused on certificates.

### Authorization Boundaries

The proposed write policy is that only the current keeper may append husbandry records. Former keepers cannot append new records after transfer completion. Permission must be checked against current keeper information, not merely the record author's past relationship to the snake.

Access to historical records, permission to correct earlier entries, and authorization to submit commitments remain open. Any correction policy must preserve attribution to original authors and respect existing integrity evidence.

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

The design tracks transaction progress and distinguishes submitted, confirmed, and failed outcomes. Modules must use confirmed blockchain state for on-chain facts rather than assuming that submission succeeded. This applies to registration, laboratory authorization, certificates, transfers, and husbandry commitments.

Backend permission checks help reject invalid requests early. Solidity must independently enforce on-chain authorization and state rules when a transaction executes, including competing transfer actions.

The detailed confirmation, retry, duplicate-request, and recovery policies remain open. The husbandry write policy must also account for a transfer completing near the time a record is added; the exact coordination rule is a Level 2 decision.

Private keys must not be stored in PostgreSQL or exposed through API responses.

## 10. Open Design Questions

| Area | Question to resolve |
|---|---|
| Identity and signing | How are users authenticated, linked to blockchain addresses, and authorized to sign transactions? |
| Registration | Who may register snakes, how are identifiers assigned, and how is the initial keeper established? |
| Profile changes | Who may edit identity information, and which fields may change? |
| Laboratory governance | How are administrators established, and what happens to existing certificates when a laboratory loses authorization? May a deauthorized issuer revise or revoke earlier certificates? |
| Certificate lifecycle | Within append-only revision and accessible version history, what are the exact supersession and revocation rules? How are status transitions recorded, and does revocation apply to one version or a certificate's full history? |
| Verification | Is login required? What evidence establishes laboratory authorization at issuance, and how do status and authorization determine certificate validity separately from hash matching? |
| File access | Where are files stored, who may download current and previous versions, and how long are verification uploads retained? |
| Transfers | How are transfer attempts identified and their histories presented? What responses should callers receive when competing acceptance, rejection, or cancellation requests encounter a transfer that has already ended? |
| Husbandry records | Which fields are needed, who may read or correct historical records, and does "keeper records" include anything beyond husbandry? Is the proposed current-keeper-only append policy sufficient? |
| Husbandry commitments | At Level 2, which records are selected, what data and format are committed, who may submit commitments, when are they submitted, and how are integrity checks and later corrections handled? |
| Transaction consistency | What confirmation rule, retry behavior, and recovery process should the application use? How are husbandry writes coordinated with confirmed keeper changes? |
| Contract structure | How will Solidity contracts organize shared identities, authorization, certificates, transfers, and selected husbandry commitments? |

Transfer acceptance and rejection by the designated recipient, cancellation by the current keeper, one pending transfer per snake, and traceable keeper history are settled requirements. Transfer expiration is outside the MVP requirements.

Append-only certificate revisions, accessible previous versions, preservation of each version's evidence, separate hash and validity results, off-chain husbandry details, support for selected on-chain commitments, and original author attribution are also settled requirements.

Open questions should be resolved in the relevant Level 1 designs and Level 2 specifications before dependent implementation tasks are approved. Any decision that changes Level 0 boundaries or authorization rules requires explicit architecture approval.
