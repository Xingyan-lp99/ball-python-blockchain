# Level 0 - System Architecture

## 1. Project Overview

Project name: Ball Python Blockchain Registry

The application provides a shared digital registry for ball python identity, genetic certificates, certificate verification, and keeper history.

Primary participants:
- Breeders register ball pythons and provide identity information.
- Authorized laboratories issue and revise genetic certificates.
- Buyers verify certificates and may become new keepers.

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
- Display certificate history and verification results.
- Provide registration and transfer workflows.
- Communicate with FastAPI over HTTP.
- Do not connect directly to PostgreSQL.

### FastAPI Backend

- Expose REST API endpoints.
- Validate requests and enforce application rules.
- Manage off-chain records and file storage.
- Calculate hashes of uploaded certificate files.
- Use web3.py to read blockchain state and submit authorized transactions.
- Organize business features into internal modules.

### PostgreSQL Database

- Store detailed snake profiles and metadata.
- Store references to photos and certificate files.
- Store off-chain husbandry records.
- Store application records linked to blockchain transactions.

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
- Support later deployment to a test network.

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
- Detailed identity profiles
- Genetic descriptions
- Photographs
- Original certificate PDFs
- Husbandry records
- User-facing metadata

Where an off-chain record requires blockchain integrity verification, store a corresponding cryptographic commitment on-chain.

Do not store large PDFs, photographs, or sensitive personal information directly on-chain.

## 5. Trust and Authorization

- Only authorized laboratories can issue certificates.
- A laboratory may revise or revoke only certificates it issued.
- Historical certificate versions remain traceable.
- Only the current keeper may initiate a transfer.
- Only the designated recipient may accept a transfer.
- The former keeper cannot add new keeper records after a completed transfer.
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

## 7. Architecture Decisions Requiring Approval

The coding agent must request approval before:
- Changing the technology stack.
- Changing the modular monolith architecture.
- Moving data between on-chain and off-chain storage.
- Changing contract authorization rules.
- Introducing new infrastructure services.
- Changing the project's core business scope.