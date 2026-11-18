from datetime import date

import streamlit as st

from frontend.api import (
    HusbandryRequestError,
    create_husbandry_record,
    edit_husbandry_record,
    fetch_husbandry_records,
    remove_husbandry_record,
)


# Field name, English label, widget type, and whether input is required.
RECORD_FIELDS = {
    "growth": [
        ("weight_g", "Weight (g)", "number", True),
        ("length_cm", "Length (cm)", "number", False),
        ("notes", "Notes", "text", False),
    ],
    "shedding": [
        ("outcome", "Outcome", "text", True),
        ("follow_up", "Follow-up", "text", False),
    ],
    "feeding": [
        ("food", "Food", "text", True),
        ("feeding_outcome", "Feeding Outcome", "text", True),
        ("notes", "Notes", "text", False),
    ],
    "health": [
        ("event", "Event", "text", True),
        ("follow_up", "Follow-up", "text", False),
        ("status", "Status", "text", True),
    ],
}


def _reload_records(
    state: dict, record_type: str, api_base_url: str, access_token: str
) -> None:
    try:
        state["records"][record_type] = fetch_husbandry_records(
            api_base_url=api_base_url,
            snake_id=state["snake_id"],
            record_type=record_type,
            access_token=access_token,
        )
    except HusbandryRequestError as error:
        state["records"].pop(record_type, None)
        state["errors"][record_type] = str(error)
    else:
        state["errors"].pop(record_type, None)
        state["blocked"].discard(record_type)
        state["versions"][record_type] += 1


def _record_inputs(record_type: str, record: dict, key: str) -> dict:
    existing_date = record.get("record_date")
    record_date = st.date_input(
        "Date *",
        value=date.fromisoformat(existing_date) if existing_date else date.today(),
        key=f"{key}:date",
    )
    data = {
        "record_date": record_date.isoformat() if record_date is not None else None
    }

    for field, label, widget, required in RECORD_FIELDS[record_type]:
        value = record.get(field)
        display_label = f"{label} *" if required else label

        if widget == "number":
            data[field] = st.number_input(
                display_label,
                value=float(value) if value is not None else None,
                step=0.1,
                key=f"{key}:{field}",
            )
        else:
            text = st.text_area(
                display_label,
                value=value if value is not None else "",
                key=f"{key}:{field}",
            )
            data[field] = text if required or text.strip() else None

    return data


def _valid_required_fields(record_type: str, data: dict) -> bool:
    if data["record_date"] is None:
        return False
    for field, _, widget, required in RECORD_FIELDS[record_type]:
        if not required:
            continue
        value = data[field]
        if value is None or (widget == "text" and not value.strip()):
            return False
    return True


# Purpose: render one record type using shared forms and fixed display columns.
# Without this function, the four tabs would duplicate the same editing flow.
def _render_record_tab(
    state: dict,
    record_type: str,
    participant_id: str,
    api_base_url: str,
    access_token: str,
) -> None:
    if record_type in state["errors"]:
        st.error(state["errors"][record_type])
        return

    records = state["records"][record_type]
    columns = [
        ("record_date", "Date"),
        *[(field, label) for field, label, _, _ in RECORD_FIELDS[record_type]],
        ("author_name", "Author"),
    ]
    table = {
        label: [record.get(field) for record in records]
        for field, label in columns
    }
    st.dataframe(table, hide_index=True, width="stretch")

    if not records:
        st.info("No records yet.")

    blocked = record_type in state["blocked"]
    if blocked:
        st.warning("Reload records to check the result before making another change.")

    context = repr((
        state["snake_id"],
        participant_id,
        record_type,
        state["versions"][record_type],
    ))
    action = st.selectbox(
        "Action",
        ["Add Record", "Edit My Record", "Delete My Record"],
        key=f"husbandry:{context}:action",
    )

    record = {}
    if action != "Add Record":
        own_records = {
            item["record_id"]: item
            for item in records
            if item["created_by"] == participant_id
        }
        if not own_records:
            st.info("You have no records of your own in this table.")
            return

        record_id = st.selectbox(
            "Record",
            list(own_records),
            format_func=lambda item_id: (
                f"#{item_id} - {own_records[item_id]['record_date']}"
            ),
            key=f"husbandry:{context}:record",
        )
        record = own_records[record_id]

    form_key = f"husbandry:{context}:{action}:{record.get('record_id', 'new')}"
    with st.form(form_key):
        if action == "Delete My Record":
            st.write(f"Delete record #{record['record_id']} dated {record['record_date']}?")
            data = None
        else:
            data = _record_inputs(record_type, record, form_key)

        button_label = {
            "Add Record": "Add Record",
            "Edit My Record": "Save Changes",
            "Delete My Record": "Delete Record",
        }[action]
        submitted = st.form_submit_button(button_label, disabled=blocked)

    if not submitted:
        return

    if data is not None and not _valid_required_fields(record_type, data):
        st.error("Please complete all required fields.")
        return

    arguments = {
        "api_base_url": api_base_url,
        "snake_id": state["snake_id"],
        "record_type": record_type,
        "access_token": access_token,
    }
    try:
        with st.spinner("Saving the record..."):
            if action == "Add Record":
                create_husbandry_record(**arguments, data=data)
            elif action == "Edit My Record":
                edit_husbandry_record(
                    **arguments, record_id=record["record_id"], data=data
                )
            else:
                remove_husbandry_record(
                    **arguments, record_id=record["record_id"]
                )
    except HusbandryRequestError as error:
        if error.outcome_unknown:
            state["blocked"].add(record_type)
            state["notice"] = ("error", str(error))
            st.rerun()
        st.error(str(error))
        return

    state["notice"] = ("success", {
        "Add Record": "Record added.",
        "Edit My Record": "Record updated.",
        "Delete My Record": "Record deleted.",
    }[action])
    _reload_records(state, record_type, api_base_url, access_token)
    st.rerun()


# Purpose: display all four husbandry tables and their authorized operations.
# Workflow: maintain care records while preserving the breeder's profile.
# Without this section, users cannot manage records through the demo page.
def render_husbandry_section(
    *, api_base_url: str, account: dict, access_token: str,
    snake_id: str | None = None,
) -> None:
    if snake_id is None:
        st.divider()
    st.subheader("Husbandry Records")

    bound_profile = snake_id is not None
    state_key = f"husbandry_section_{snake_id}" if bound_profile else "husbandry_section"
    state = st.session_state.setdefault(state_key, {
        "snake_id": None,
        "records": {},
        "errors": {},
        "versions": {record_type: 0 for record_type in RECORD_FIELDS},
        "blocked": set(),
    })

    notice = state.pop("notice", None)
    if notice is not None:
        level, message = notice
        if level == "success":
            st.success(message)
        else:
            st.error(message)

    if bound_profile:
        st.caption(f"Snake ID: {snake_id}")
    else:
        snake_id = st.text_input(
            "Snake ID", value="SNAKE001", key="husbandry_snake_id"
        )
    participant_id = account["participant_id"]
    st.caption(f"Acting as {account['display_name']} ({account['username']})")
    st.caption(
        "Author is assigned automatically. Changes require current keeper rights; "
        "you can only edit or delete records you authored."
    )

    reload_requested = st.button(
        "Refresh Records" if bound_profile else "Load Records",
        key=f"refresh_husbandry_{snake_id}" if bound_profile else "load_husbandry_records",
    )
    if reload_requested or (bound_profile and state["snake_id"] is None):
        if snake_id == "":
            st.error("Please enter a snake ID.")
            return

        if state["snake_id"] != snake_id:
            state["records"] = {}
            state["errors"] = {}
            state["blocked"] = set()
        state["snake_id"] = snake_id

        with st.spinner("Loading husbandry records..."):
            for record_type in RECORD_FIELDS:
                _reload_records(state, record_type, api_base_url, access_token)

    if state["snake_id"] != snake_id:
        st.info("Enter a snake ID and select Load Records.")
        return

    tabs = st.tabs(["Growth", "Shedding", "Feeding", "Health"])
    for tab, record_type in zip(tabs, RECORD_FIELDS):
        with tab:
            _render_record_tab(
                state, record_type, participant_id, api_base_url, access_token
            )
