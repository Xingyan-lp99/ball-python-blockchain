# Collaborator handoff — PythonPass

## What this update includes

- Streamlit login, account registration, and breeder/buyer/laboratory workspaces.
- The original `frontend/assets/pythonpass-logo.png`, six independent homepage
  photos, local Jersey 10 and Space Grotesk fonts, and their license files.
- Shared purple borders/hard shadows, cream surfaces, yellow actions, pixel
  headings, and Space Grotesk body text and native widget theming.
- Breeder and buyer profile sections: Certificate History, Keeper Management,
  and Husbandry Records. Records belong to the selected saved profile.
- Existing API, session validation, permissions, original-PDF downloads,
  submission locks, and explicit uncertain-result handling.
- The current AGENTS.md, design references, and an isolated acceptance test.

## Safely synchronize an existing checkout

Use the repository URL:
`https://github.com/Xingyan-lp99/ball-python-blockchain`.

First inspect without reading local credentials:

```powershell
git status --short --branch
git branch --show-current
git remote -v
```

If there are uncommitted changes, a different remote, or divergent branches,
preserve all files and report the situation. Do not reset, clean, overwrite,
force-switch, automatically stash, or automatically merge the collaborator's work.
When the checkout is clean and a fast-forward is possible:

```powershell
git fetch origin
git switch main
git pull --ff-only origin main
git status --short --branch
```

For a new checkout, clone the repository instead. Read AGENTS.md and the relevant
Level 0–3 documents before implementation. The owner's direct-edit permissions
from another session do not replace this collaborator's learning workflow.

## Open the pages on the collaborator's computer

GitHub contains source and static assets, not a running backend or the owner's
database. A `127.0.0.1` link refers to the computer where the browser is running.
GitHub Pages cannot run this Streamlit/FastAPI/PostgreSQL/Hardhat application.

Follow [README first-time setup](../README.md#first-time-setup) in VS Code:

1. Install the locked Python and Node dependencies, and compile the contracts.
2. Create a private local `.env` with a local database password. Do not copy the
   owner's settings, private keys, login passwords, or session tokens.
3. Start PostgreSQL and apply migrations 001–007 to a fresh database. On an
   existing database, check migration state first; never blindly repeat SQL.
4. Start a dedicated local Hardhat node and keep it running.
5. Deploy SnakeRegistry on that node. Save its printed public address as
   `DEMO_REGISTRY_ADDRESS`; seed the four predefined participants.
6. Run `backend.setup_certificates`. Save its public address as
   `DEMO_CERTIFICATE_REGISTRY_ADDRESS`. This also authorizes LAB001 and LAB002.
7. Start FastAPI with the local environment file and Streamlit in separate
   terminals, using the commands below.
8. Register local breeder, buyer, LAB001, and LAB002 accounts. For the documented
   fresh demonstration, register the fictional snake `SNAKE001` with a PNG/JPEG
   photo through the breeder page. Keep the ID consistent throughout the demo.
9. Run `backend.setup_keeper_transfers` after SNAKE001 is registered. Save the
   printed address as `DEMO_KEEPER_TRANSFERS_ADDRESS`, then restart FastAPI with
   all four settings. Husbandry writes need this contract even before a transfer.
10. Use the two laboratory accounts to create fresh reports, revise LAB001's
    own series, and query the snake through the buyer/breeder profile pages.

FastAPI terminal, from the repository root:

```powershell
uv run --locked --env-file .env python -m uvicorn backend.main:app --host 127.0.0.1 --port 8001
```

Streamlit terminal, from the repository root:

```powershell
uv run --locked python -m streamlit run frontend/app.py --server.address 127.0.0.1 --server.port 8502
```

Open [PythonPass](http://127.0.0.1:8502),
[backend health](http://127.0.0.1:8001/health), and
[database readiness](http://127.0.0.1:8001/ready).
VS Code can open the same local URL in its integrated browser or the system
browser. Sign out and sign in with each role to see its workspace. The website
itself runs in Streamlit; VS Code is the editor and terminal host.

If VS Code runs on a remote machine or dev container, forward port 8502 through
VS Code and use the forwarded browser URL. Keep backend and database ports
private. A public shared deployment is a separate task and is not included here.

## Assets versus business data

The homepage images and Logo arrive through Git automatically. A photo uploaded
through snake registration, a laboratory PDF, accounts, sessions, and database
records do not. Those remain under ignored local settings/storage or PostgreSQL.
Create local fictional demonstration data to see populated workspaces. This
handoff does not reproduce the owner's BP-S001 database or upload history.

Do not reuse the owner's contract addresses without verifying code on your own
running chain. Hardhat restarts can erase deployments while PostgreSQL survives.
Never treat old database transaction hashes as confirmed on a fresh chain.
`/ready` checks database connectivity, not all contracts or historic evidence.

## Verification and limitations

See [the functional audit](level-3/functional-audit-2026-11-19.md) for the successful
complete isolated flow and 19 additional focused tests. This is not a claim that
the historical full repository test suite passes.

On the owner's computer, BP-S001 is the current working-chain profile. Older
SNAKE001/SNAKE002 records belong to a previous chain and retain their explicit
unconfirmed state. On a collaborator's fresh database/chain, the documented new
SNAKE001 is a new local demonstration, not restoration of those old records.

If desired, run the opt-in isolated acceptance test using the audit document's
command. It uses a temporary database, separate Hardhat node, and temporary
uploads; it does not populate the normal website database.

## Prompt to send to the collaborator's Codex

```text
Safely synchronize https://github.com/Xingyan-lp99/ball-python-blockchain,
branch main, using the shared commit supplied with this handoff message.

First inspect status, branch, and remotes. Preserve every uncommitted change.
Do not reset, clean, force-switch, overwrite, automatically stash, or merge.
If clean and fast-forwardable, fetch origin, switch main, and pull --ff-only.
Otherwise report the exact divergence and a safe way forward.
Verify that main contains the shared commit and check final worktree status.

Read AGENTS.md and docs/collaborator-handoff-2026-11-19.md, then the relevant
L0–L3 documentation and README. Verify the Logo, all six homepage photos,
Jersey 10, Space Grotesk, and licenses are present.

Help me start the existing app in VS Code and give me the working browser URL.
Inspect my existing database/chain before setup. Do not delete or reset data.
For a fresh environment, follow the documented dependency, migration, local
contract deployment, participant, laboratory authorization, and keeper setup
sequence. Check all three contracts, their registry references, and both lab
permissions; a successful /ready alone is insufficient.

The owner's database, uploaded photos/PDFs, .env, credentials, and local chain
are not synchronized by Git. Use my own local settings and fictional demo
data. Do not read or print existing .env contents, passwords, private keys,
password hashes, or session tokens. Loading .env through the documented uv
startup command is permitted. Do not copy contract addresses blindly or turn
unconfirmed historic chain evidence into success.

Keep Streamlit and the existing APIs, pixel titles, original Logo, Space
Grotesk body font, and shared purple/yellow styling. Preserve all role/session
checks, submission locks, and error handling. Follow my AGENTS.md learning
workflow for further code changes. Do not commit, push, expose services
publicly, or send messages to others without my authorization.
```
