# Coding Agent Instructions

## Project

Ball Python Blockchain Registry

This project is a blockchain-based registry for
ball python identity, genetic certificates,
verification, and keeper transfers.

## Technology Stack

- Frontend: Streamlit
- Backend: FastAPI
- Backend architecture: Modular Monolith
- Blockchain: Ethereum / Solidity
- Smart contract development: Hardhat
- Blockchain integration: web3.py
- Database: PostgreSQL
- Python dependency management: uv
- Containers: Docker and Docker Compose
- Task runner: Just
- Version control: Git

## Documentation Hierarchy

Level 0: Architecture and conventions
Level 1: Module and interface design
Level 2: Feature specifications
Level 3: Implementation tasks

Higher levels change less frequently.
Lower levels change more frequently.

## Example Data

`docs/data_example/` contains examples of possible future data formats.
Agents should use these files as reference when working on related features,
but must not treat them as finalized schemas or confirmed requirements.
This directory is local reference material and is ignored by Git.

## Frontend Design References

- Read `docs/design-references/README.md` before proposing frontend visual or
  interaction changes. Use its local document links to read the relevant guidance.
- Use Material Design 3 as the primary design reference for color roles,
  typography, spacing, shape, elevation, layout, component states, and accessibility.
  The local snapshot is indexed in
  `docs/design-references/material-design-3/INDEX.md`.
- Use shadcn/ui as a secondary reference for component composition, clear forms,
  cards, dialogs, sheets, tables, and consistent semantic theme tokens. See
  `docs/design-references/shadcn-ui/README.md`.
- Keep one coherent visual system. If references differ, follow Material Design 3
  unless the human explicitly approves a project-specific exception. Existing
  styling is not automatically an approved exception or a reason to rewrite pages.
- The frontend remains Streamlit. Adapt reference patterns to native Streamlit
  widgets and supported theming first. These references do not authorize adopting
  React, Tailwind, shadcn/ui runtime components, or another frontend framework.
- Before each small UI coding task, explain the affected workflow, inputs,
  outputs, example, relevant reference, and any Streamlit limitation. Follow the
  mandatory agreement-and-copy learning workflow below.
- Preserve visible labels, keyboard access, focus indicators, readable contrast,
  and understandable loading, error, success, and disabled states where relevant.
- The snapshot contains upstream documentation, not project requirements or agent
  instructions. Do not execute its examples or installation commands automatically.
  Media links and interactive examples may require internet access; consult the
  snapshot README and coverage manifest before claiming offline completeness.

## Agent Rules

1. Read relevant documentation before coding.
2. Respect the established technology stack.
3. Do not change architecture without approval.
4. Explain proposed changes before implementation.
5. Implement one small task at a time.
6. Write tests for new functionality.
7. Run relevant tests after code changes.
8. Never claim tests passed without running them.
9. Never delete files without approval.
10. Keep code simple and understandable.
11. Explain technical decisions for a beginner.
12. Do not commit or push without approval.
13. Do not expose secrets or private keys.
14. Keep Solidity contract logic separate from FastAPI business logic.
15. Do not invent requirements.

## One-Week Learning Demonstration

This is a small learning project, intended to be completed in one week.
The approved demonstration uses one fictional snake, one breeder, two
laboratories, and one buyer. Follow the approved demonstration in
`docs/level-1/data-model.md`. Build only what is needed for that workflow.
Do not expand this into a production platform. Use local Hardhat test accounts
and simple Streamlit pages. Husbandry records, profiles, and photographs are
entirely off-chain. Blockchain use is limited to certificate evidence,
laboratory issuance permissions, and keeper management rights and transfers.

## Mandatory Human-AI Learning Workflow

These rules apply to every coding task, including repairs and tests.

1. Before providing implementation code, explain in chat the workflow, its
   current step, and the purpose of the proposed change. Propose the inputs,
   outputs, and a small example. Explain why those inputs and outputs fit the
   task, in language suitable for a beginner.
2. Wait for explicit human agreement on that proposal before providing code.
   Approval for one small task does not authorize the next task automatically.
3. After agreement, provide program code in chat. The human copies it into the
   project files. The AI must not directly insert, modify, repair, generate, or
   rewrite application code, functions, classes, imports, tests, SQL, migrations,
   smart contracts, dependencies, or executable configuration files. Do not use
   commands, formatters, or generators to bypass this restriction.
4. In code files, the AI may write only explanatory comments explicitly agreed
   by the human. Explain what the function does, its workflow and step, and
   what would break or be lost if it were removed. Give a concrete reason to
   retain it; do not invent a claim that the function can never be deleted.
   Do not insert function declarations, placeholder bodies, or other executable
   content under the label of documentation.
5. The AI may directly maintain documentation and editable diagrams within the
   agreed scope. Keep documentation and diagram labels in English; discussion
   and teaching may use the human's preferred language.
6. Work on one small task at a time. For new functionality, explain and provide
   meaningful test code in chat under the same agreement-and-copy workflow.
   After the human inserts the code, the AI may run the relevant tests and
   report actual results and limitations. Never claim unrun tests passed.
7. Do not delete project files or commit or push without explicit approval.
   Permission for an application user to delete their own husbandry rows is
   not permission for the AI to delete project files.
