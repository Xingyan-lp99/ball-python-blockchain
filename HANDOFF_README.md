# Pet Lifetime Records - collaborator handoff

This archive captures the current working directory, including uncommitted and untracked source changes. It is not a Git commit or a complete running-environment backup.

Included: backend, frontend, local assets/fonts and licenses, Solidity sources, existing compiler Artifacts/build-info, migration SQL, scripts, tests, documentation, dependency lockfiles and configuration without credentials.

The preserved storage/sepolia/sepolia-p0-001/state.json records six confirmed steps. This is saved evidence, not a new on-chain verification. Keep it together with the exact included Artifacts. Do not rerun deployment from an empty checkpoint or rebuild and overwrite these Artifacts when resuming this deployment. No signing keys are included.

Excluded: .git, virtual environments, node_modules, caches, local .env files, RPC credentials, demo passwords/sessions, PostgreSQL backups, Anvil state, uploaded reports/photos in storage, logs, previous exports, and docs/data_example local reference material.

Setup:
- Read README.md, AGENTS.md and justfile before running commands.
- Python >=3.12: uv sync --locked.
- If contract tooling is needed: run npm ci in contracts. Preserve the included Artifacts for the existing Sepolia checkpoint.
- Configure local .env values separately. Coordinate database and Anvil state handover with the owner; this archive alone does not reproduce existing Anvil records.
- Streamlit: uv run --locked python -m streamlit run frontend/app.py --server.address 127.0.0.1 --server.port 8502.
- Backend address expected by frontend: http://127.0.0.1:8001.
- Demo Mode is disabled until storage/frontend-demo.json is configured locally. It needs enabled=true and Seller, Buyer, Lab 1, Lab 2 objects with username/password. Use real accounts bound to BREEDER001, BUYER001, LAB001 and LAB002 respectively; never commit that file.

Streamlit business operations use local Anvil. Sepolia is a separate Python-script demonstration, not a Streamlit integration. The standalone additional Pet ID registration command has not been implemented in this handoff.

Do not infer that the full pytest suite passes. Known older tests were not comprehensively repaired. Recent UI checks were limited to targeted Demo Mode tests and page startup/layout smoke checks. No tests or transactions were run as part of packaging.

SNAPSHOT_MANIFEST.json lists SHA-256 hashes of the captured project files.

The manifest describes the original working-directory bytes; Git may normalize text-file line endings. Deployment Artifacts and the public checkpoint are explicitly protected from newline conversion in .gitattributes.
