# Level 0 - System Architecture

## 1. Project Overview

Project name: Ball Python Blockchain Registry

The application is a one-week learning demonstration of ball python identity, laboratory certificate integrity, and keeper management rights. It is not a production platform.

Primary participants:
- Breeders register ball pythons and provide identity information.
- Two authorized laboratories issue reports in different testing directions; one revises its report once. Both use the same certificate workflow without parsing test results.
- Buyers view certificate history, download original PDFs, and may become new keepers.

The fixed demonstration uses one fictional snake: registration by its breeder, two independently issued reports, one report revision, certificate history and original PDF downloads, one keeper transfer after an offline sale, and buyer creation, editing, and deletion of their own husbandry records. Buyer-uploaded file verification was removed from this iteration by the human. See [the logical data model](../level-1/data-model.md) for the acceptance sequence.

Use distinct local Hardhat test accounts for the demonstration roles. The approved local demonstration includes account registration, sign-in, sign-out, and role-specific workspaces. Accounts bind to the four predefined demonstration participants: BREEDER001, BUYER001, LAB001, and LAB002, with one account per participant. Backend identity checks complement on-chain laboratory and keeper permissions. This is not a production authentication platform. Browser wallet integration, payments, marketplace features, production deployment, laboratory deauthorization screens, and report-result parsing are outside this iteration.

## 2. Architecture Style

The system uses a separated frontend and backend with a modular monolith backend.

Frontend: Streamlit
Backend: FastAPI
Database: PostgreSQL
Blockchain integration: web3.py
Smart contracts: Solidity
Contract development and testing: Hardhat
Python dependency management: uv
Infrastructure: Docker and Docker Compose
Developer commands: Just
Version control: Git

## 3. Component Responsibilities

### Streamlit Frontend

- Display ball python profiles.
- Display certificate history and original PDF downloads.
- Provide registration and transfer workflows.
- Provide sign-in and account registration entry points, and show the workspace for the signed-in role.
- Communicate with FastAPI over HTTP.
- Do not connect directly to PostgreSQL.

### FastAPI Backend

- Expose REST API endpoints.
- Validate requests and enforce application rules.
- Validate account credentials and login sessions, and derive the acting participant from the authenticated account.
- Manage off-chain records and file storage.
- Calculate hashes of uploaded certificate files.
- Use web3.py to read blockchain state and submit authorized transactions.
- Organize business features into internal modules.

### PostgreSQL Database

- Store detailed snake profiles and metadata.
- Store references to photos and certificate files.
- Store off-chain husbandry records.
- Store application records linked to blockchain transactions.
- Store account profiles, password hashes, login token hashes, and session expiry times off-chain.

### Solidity Smart Contracts

- Register snake identifiers and current keepers.
- Manage authorized laboratory addresses.
- Record certificate hashes, versions, issuers, and statuses.
- Enforce certificate issuer permissions.
- Enforce keeper transfer authorization.
- Emit events for important state changes.

### Hardhat

- Compile Solidity contracts.
- Run contract tests.
- Deploy contracts to a local development blockchain.
- Use a local development blockchain for this iteration; test-network deployment is outside the demonstration.

### web3.py

- Connect FastAPI to the Ethereum-compatible blockchain.
- Read contract state.
- Prepare and submit transactions using an authorized signing method.
- Retrieve transaction receipts and contract events.

## 4. On-Chain and Off-Chain Boundaries

On-chain:
- Snake identifiers
- Current keeper addresses
- Authorized laboratory addresses
- Certificate file hashes
- Certificate version references and statuses
- Keeper transfer state and relevant events

Off-chain:
- Account profiles, password hashes, and login session records
- Detailed identity profiles
- Genetic descriptions
- Photographs
- Original certificate PDFs
- Husbandry records
- User-facing metadata

Only certificate file integrity and keeper management rights use blockchain evidence in this iteration. Husbandry records, profile content, and photographs have no on-chain hashes or commitments. Snake identifiers connect the on-chain rights and certificates to the off-chain profile; they do not put the full profile on-chain.

The approved keeper integration uses a separate KeeperTransfers contract linked immutably to the existing SnakeRegistry. SnakeRegistry retains registrations and initial keeper values; KeeperTransfers falls back to those values until a transfer is accepted, then stores and returns the accepted keeper. After activation, all backend keeper authorization must use KeeperTransfers as the single current-keeper authority. CertificateRegistry continues using the original SnakeRegistry for snake existence, so existing certificate evidence and PDF references need not be recreated. This is an additional contract, not an upgrade or replacement of either deployed registry. See [the keeper contract specification](../level-2/keeper-transfers.md) for implementation and activation status.

Do not store large PDFs, photographs, or sensitive personal information directly on-chain.

## 5. Trust and Authorization

- Usernames and email addresses are unique ignoring case. Password confirmation is not stored; passwords and reusable login tokens must not be stored in plaintext.
- Account registration binds an existing demonstration participant without changing snake breeder attribution or historical record authorship. Display names remain in participants.
- A laboratory account selects LAB001 or LAB002. Account registration does not grant on-chain laboratory issuance permission.
- The target login flow derives identity from a valid, unexpired backend session. Hiding frontend controls alone does not enforce authorization.
- Only authorized laboratories can issue certificates.
- A laboratory may revise or revoke only certificates it issued.
- Historical certificate versions remain traceable.
- Revocation targets a specified certificate version and does not restore a superseded version. Revocation remains part of the logical design; a revocation demonstration screen is outside this iteration.
- The registering account becomes the initial keeper. Breeder attribution does not change when keeper rights are transferred.
- Only the current keeper may initiate a transfer.
- Only the designated recipient may accept a transfer.
- Only the current keeper may add husbandry records, and may edit or delete only records they originally authored. Former keeper records are read-only to both parties after transfer. Ordinary husbandry edits retain only the latest content.
- Administrators may manage laboratory authorization but cannot forcibly transfer snake records.
- A file hash proves byte-level consistency with a recorded hash, not the biological truth of the laboratory's findings.

## 6. Development Principles

- Build a minimal working vertical slice before expanding features.
- Start with one snake, two laboratories, three certificate versions, and one keeper transfer.
- Test authorization failures as well as successful operations.
- Keep blockchain and application business responsibilities separate.
- Use Docker Compose for reproducible local services.
- Use Just to simplify developer commands.
- Do not introduce additional frameworks without approval.
- Follow the mandatory human-AI learning workflow in AGENTS.md. The human inserts all program code; the AI may maintain agreed documentation and diagrams.
- Keep all four husbandry tables simple and off-chain. Their purpose is to demonstrate the practical effect of a keeper transfer, not a complete animal-care product.

## 7. Architecture Decisions Requiring Approval

On 2026-11-20 the human approved local chain persistence. Hardhat remains the
Solidity build/test tool; the daily local demonstration uses Anvil v1.10.0 on
chain ID 31337 with periodic state files under ignored `storage/chain/`.
PostgreSQL and uploaded files retain their existing roles. The restart audit
verified contract code/storage, original transactions/receipts/logs, pending
transfers and accepted keeper state. This does not restore the previous lost
Hardhat chain, and no replay or authority fallback is permitted. Coordinated
local backups include the database, uploads and matching chain checkpoint.

The coding agent must request approval before:
- Changing the technology stack.
- Changing the modular monolith architecture.
- Moving data between on-chain and off-chain storage.
- Changing contract authorization rules.
- Introducing new infrastructure services.
- Changing the project's core business scope.
