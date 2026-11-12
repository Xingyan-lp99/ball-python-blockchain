# Level 3 - Implementation Tasks

## Snake registration: database iteration (2026-11-12)

Status: **Complete** for the database stage. Automated checks passed, and the user
completed manual browser acceptance on 2026-11-12. Blockchain registration, real
authentication and certificate features remain pending.

### Implemented

- [x] Inspect existing docs, dependencies, code, services and API conventions.
- [x] Add a focused Snake Registry module with separate routes, schemas and service.
- [x] Add an ordered, transactional SQL migration and database unique/check constraints.
- [x] Implement `POST /api/v1/snakes` and `GET /api/v1/snakes/{snake_id}`.
- [x] Assign explicit server-side demo identity BR001 and initial manager.
- [x] Reject user-supplied server fields, invalid sex, blank ID and future birth dates.
- [x] Return 409 for duplicate IDs and 404 for missing IDs.
- [x] Add Streamlit registration/query forms with saved-profile display.
- [x] Label morph descriptions as breeder-provided and not laboratory certified.
- [x] Clearly distinguish database storage from blockchain/certificate verification.
- [x] Package new modules and migrations in the backend container.
- [x] Add Just commands and local run instructions.
- [x] Record the requested differences from Level 1 without editing higher-level docs.

### Tested

- [x] Backend: 26 tests passed against PostgreSQL, including direct database checks.
- [x] Real HTTP registration, Uvicorn process stop/start, and persistent lookup.
- [x] Repeat migration without losing the saved test profile.
- [x] Frontend: 5 Streamlit AppTest tests passed using mocked HTTP.
- [x] Apply migration to the existing development PostgreSQL database.
- [x] Validate Docker Compose configuration.
- [x] Build and start both application containers against the existing database volume.
- [x] Container HTTP smoke checks: API/database health, 404, 422 and Streamlit health.
- [x] Validate Just command listing.
- [x] Manual browser acceptance performed by the user: registration, lookup,
  duplicate-ID rejection, preservation of the original record, missing-ID feedback
  and status explanations all met expectations.

Container build/start results and remaining checks are recorded in
`snake-registration-development.md`.

### Pending

- [ ] Review and reconcile the broader Level 1 design with this requested database slice.
- [ ] Replace demo identity with real login and authorization.
- [ ] Implement the chain registration work listed in the Level 2 spec.
- [ ] Implement laboratory certificate issuance and verification.

No existing contracts are changed. The user authorized a local feature commit after
acceptance; remote push and existing-data deletion are outside this iteration.
