# Level 3 - One-Week Implementation Roadmap

## Current State and Reading Order

The design documents and logical diagram are prepared. Application functionality
has not been implemented. The day numbers below are a suggested sequence, not a
claim that any implementation or test has been completed.

New collaborators should read:
1. [AGENTS.md](../../AGENTS.md): scope and mandatory human-AI learning rules.
2. [Architecture](../level-0/architecture.md): stack and storage boundaries.
3. [Logical data model](../level-1/data-model.md): seven-step demonstration and permissions.
4. [Combined diagram](../diagram/data-model.drawio): editable overview.
5. [Backend modules](../level-1/modules.md): responsibilities inside FastAPI.

The Level 2 registration specification is currently empty. Before dependent
coding, discuss and document that small feature's agreed inputs, outputs, and
acceptance cases. Do not treat an empty document as an approved specification.

## Suggested Coding Sequence

| Stage | Tasks | Acceptance target | Status |
|---|---|---|---|
| Day 1: minimal skeleton | Start with a minimal FastAPI response; then connect PostgreSQL, start a local Hardhat chain, and create a simple Streamlit-to-FastAPI view. | The development services run and the page can reach the backend. | Not started |
| Day 2: snake registration | Test Solidity registration and keeper queries; connect web3.py and off-chain profile persistence; add a registration view. | Breeder registers one snake and sees its profile and confirmed keeper. | Not started |
| Day 3: laboratory reports | Implement and test laboratory permissions, certificate issuance and correction; connect PDF storage and upload views. | LAB001 and LAB002 each issue V1; LAB001 appends V2 without replacing V1. | Not started |
| Day 4: file verification | Calculate a supplied PDF's hash, compare with chain evidence, and display match separately from version status. | Original V2 matches; modified V2 does not. Verification registers nothing. | Not started |
| Day 5: keeper transfer | Test transfer authorization and state; connect backend and initiate/accept views. | Breeder initiates and buyer accepts; confirmed chain state changes keeper. | Not started |
| Day 6: husbandry records | Add four simple parallel database tables and views; enforce current-keeper and original-author checks for writes. | Buyer can add/edit/delete their own rows; breeder rows remain read-only. | Not started |
| Day 7: rehearsal | Run the complete seven-step workflow, relevant tests, and key permission failures; prepare repeatable demo data and fix issues. | A clear end-to-end demonstration; actual test results recorded. | Not started |

Blockchain setup begins on Day 1 and core Solidity work begins on Day 2. FastAPI
integration runs throughout. Add only the simple frontend controls needed for
each working feature, then improve presentation during rehearsal. Do not spend
the week building separate complete layers before trying them together.

For every small task: explain workflow/step and proposed inputs/outputs, reasons,
and an example; wait for explicit agreement; provide code and relevant tests in
chat; the human inserts them; run appropriate checks and report actual outcomes.
Start with the minimal FastAPI response task, not the entire Day 1 at once.

## Two-Person Collaboration

- Use the shared GitHub repository and separate local clones. Private access is
  sufficient; invite the teammate as a collaborator rather than publishing it.
- Before starting, synchronize the latest shared work. Agree who owns each small
  task and use short-lived feature branches. Prefer different files when working
  at the same time.
- Review changes in a pull request before merging; communicate before changing
  shared interfaces. Human-AI coding restrictions apply to both contributors.
- GitHub synchronizes committed files, not chat sessions or local environments.
  Put agreed decisions and progress in documentation so both people have context.
- `docs/data_example/` is intentionally ignored. Share the fictional DOCX/PDF
  references separately and place them at that local path. Do not commit the
  virtual environment, secrets, or private keys.
- Keep this a one-week local demonstration. Do not add payments, production
  authentication, wallets, report parsing, or a marketplace.
