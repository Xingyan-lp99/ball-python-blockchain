# Level 0 - Development Conventions

## 1. General Principles

- Use English for code, filenames, and documentation.
- Use clear and descriptive names.
- Prefer simple solutions over unnecessary abstractions.
- Keep modules focused on one business responsibility.
- Follow the architecture defined in architecture.md.
- Explain technical decisions in simple terms.

## 2. Project Structure

- frontend/ contains the Streamlit application.
- backend/ contains the FastAPI application.
- contracts/ contains the Hardhat project.
- infrastructure/ contains infrastructure configuration.
- tests/ contains cross-component integration tests.
- docs/ contains project documentation.

## 3. Python Conventions

- Use snake_case for files, variables, and functions.
- Use PascalCase for classes.
- Use UPPER_SNAKE_CASE for constants.
- Use type hints for function parameters and return values.
- Use uv for Python dependency management.
- Keep API routes separate from business logic.
- Use pytest for Python tests.

## 4. Solidity Conventions

- Use PascalCase for contract names.
- Use camelCase for functions and variables.
- Use UPPER_SNAKE_CASE for constants.
- Use descriptive event and error names.
- Enforce authorization inside smart contracts.
- Use Hardhat for compilation, deployment, and tests.
- Avoid unnecessary contract complexity.

## 5. API Conventions

- Use REST-style HTTP endpoints.
- Prefix endpoints with /api/v1.
- Use plural resource names.
- Use snake_case for JSON fields.
- Use appropriate HTTP status codes.
- Validate input with Pydantic.
- Do not expose internal error details or secrets.

## 6. Database Conventions

- Use PostgreSQL.
- Use snake_case for tables and columns.
- Use plural table names.
- Use explicit primary and foreign keys.
- Use migrations for schema changes.
- Do not store private keys in the database.

## 7. Git Conventions

- Use main as the default branch.
- Write meaningful commit messages.
- Do not commit secrets or .env files.
- Do not commit virtual environments or node_modules.
- Review changes before committing.
- The agent must not commit or push without approval.

## 8. Agent Workflow

Before implementation:
1. Read AGENTS.md.
2. Read relevant Level 0 and Level 1 documents.
3. Read the relevant Level 2 specification.
4. Check the current Level 3 task.
5. Explain the implementation plan.
6. Explain the workflow step and proposed inputs and outputs, with reasons and an example. Obtain explicit human agreement before providing implementation code in chat.

During implementation:
1. Make small, focused changes.
2. Stay within the approved task scope.
3. Add or update relevant tests.
4. Do not change architecture without approval.
5. Follow AGENTS.md: the human inserts all program code, tests, SQL, and executable configuration. The AI may directly write only agreed explanatory comments in code files, and agreed documentation and diagrams. Do not bypass this rule with generation or formatting commands.

After implementation:
1. Run relevant tests.
2. Report what changed.
3. Report test results and limitations.
4. Propose updates to Level 3 tasks.
5. Request approval before changing higher-level documents.

## 9. Documentation Change Policy

- Level 0 changes require explicit approval.
- Level 1 changes require design review and approval.
- Level 2 changes follow approved feature requirements.
- Level 3 is updated frequently as tasks progress.
- Lower-level documents must not contradict higher-level documents.
