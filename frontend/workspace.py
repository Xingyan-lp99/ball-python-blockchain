import streamlit as st

from frontend.api import (
    check_backend_readiness,
    fetch_snake_profile,
    submit_snake_registration,
)
from frontend.auth import sign_out_current_account
from frontend.husbandry import render_husbandry_section
from frontend.keeper_transfers import render_keeper_transfer_section

from frontend.certificates import render_certificate_history, render_certificate_issuance


def _render_connection_status(api_base_url: str) -> None:
    with st.expander("Connection Status"):
        if st.button("Check Backend and Database"):
            result = check_backend_readiness(f"{api_base_url}/ready")
            messages = {
                "database_unavailable": "The database is not ready.",
                "backend_unavailable": "Cannot connect to the backend.",
                "unexpected_response": "The backend returned an unexpected response.",
            }
            if result == "ok":
                st.success("Backend and database are ready.")
            else:
                st.error(messages[result])


def _render_snake_registration(api_base_url: str, access_token: str) -> None:
    st.subheader("Register a Ball Python")
    previous = st.session_state.get("registration_result")
    locked = False

    if previous is not None:
        status_code = previous["status_code"]
        payload = previous["payload"]
        outcome = payload.get("outcome")
        locked = status_code == 201 or outcome in {
            "unknown", "failed", "unverified", "storage_error",
        }

        if status_code == 201:
            profile = previous["profile"]
            st.success(f"Registration successful: {profile['snake_id']}")
            st.image(previous["photo_content"], width=320)
            st.write({
                "Breeder Internal ID": profile["breeder_internal_id"],
                "Species": profile["species"],
                "Sex": profile["sex"],
                "Date of Birth": profile["date_of_birth"],
                "Genetic Description": profile["genetic_description"],
            })
        elif status_code == 409:
            st.error("This snake ID already has a profile or on-chain registration.")
        elif outcome == "not_submitted":
            st.error("Registration is not configured yet. No transaction was submitted.")
        elif locked:
            st.error(
                "Registration could not be confirmed as complete. "
                "Check the result before submitting again."
            )
            if payload.get("transaction_hash"):
                st.caption("Transaction to Check")
                st.code(payload["transaction_hash"])
        else:
            detail = payload.get("detail")
            st.error(
                detail if isinstance(detail, str)
                else "Please check the required fields and photo."
            )

    if locked:
        return

    with st.form("snake_registration"):
        snake_id = st.text_input("Snake ID *", value="SNAKE001")
        breeder_internal_id = st.text_input("Breeder Internal ID *")
        species = st.text_input("Species *", value="Python regius")
        sex = st.text_input("Sex *", placeholder="For example, Female")
        date_of_birth = st.date_input("Date of Birth *", value=None)
        genetic_description = st.text_area("Genetic Description *")
        photo = st.file_uploader(
            "Photo * (JPEG / PNG, up to 5 MiB)",
            type=["jpg", "jpeg", "png"],
            max_upload_size=5,
        )

        with st.expander("Optional Details"):
            nickname = st.text_input("Nickname")
            introduction = st.text_area("Introduction")
            sire_description = st.text_area("Sire Description")
            dam_description = st.text_area("Dam Description")

        submitted = st.form_submit_button("Register")

    if not submitted:
        return

    required_text = [breeder_internal_id, species, sex, genetic_description]
    if (
        snake_id == ""
        or any(not value.strip() for value in required_text)
        or date_of_birth is None
        or photo is None
    ):
        st.error("Please complete all required fields and upload a photo.")
        return

    profile = {
        "snake_id": snake_id,
        "breeder_internal_id": breeder_internal_id,
        "species": species,
        "sex": sex,
        "date_of_birth": date_of_birth.isoformat(),
        "genetic_description": genetic_description,
        "nickname": nickname if nickname.strip() else None,
        "introduction": introduction if introduction.strip() else None,
        "sire_description": sire_description if sire_description.strip() else None,
        "dam_description": dam_description if dam_description.strip() else None,
    }
    photo_content = photo.getvalue()

    with st.spinner("Saving the profile and confirming on-chain registration..."):
        status_code, payload = submit_snake_registration(
            url=f"{api_base_url}/api/v1/snakes",
            profile=profile,
            photo_name=photo.name,
            photo_content=photo_content,
            access_token=access_token,
        )

    st.session_state["registration_result"] = {
        "status_code": status_code,
        "payload": payload,
        "profile": profile,
        "photo_content": photo_content,
    }
    st.rerun()


# Purpose: display the saved photo and profile in clearly grouped sections.
# Workflow: query a registered snake before viewing its rights and certificates.
# Without this function, users cannot retrieve profiles through the workspace.
def _render_snake_profile(
    api_base_url: str,
    access_token: str,
    account: dict,
) -> None:
    st.divider()
    st.subheader("Snake Profile")

    with st.form("view_snake_profile"):
        snake_id = st.text_input(
            "Snake ID", value="SNAKE001", key="profile_lookup_id"
        )
        submitted = st.form_submit_button(
            "View Profile",
            type="primary",
            key="view_profile",
        )

    if submitted:
        if snake_id == "":
            st.error("Please enter a snake ID.")
        else:
            st.session_state.pop(f"certificate_history_{snake_id}", None)
            st.session_state.pop(f"keeper_transfer_status_{snake_id}", None)
            with st.spinner("Loading the saved profile..."):
                st.session_state["saved_snake_profile"] = fetch_snake_profile(
                    api_base_url=api_base_url,
                    snake_id=snake_id,
                    access_token=access_token,
                )

    saved = st.session_state.get("saved_snake_profile")
    if saved is None:
        return

    profile, photo_content, error = saved
    if profile is None:
        st.error(error)
        return

    with st.container(border=False, key="snake_profile_card"):
        st.subheader(profile.get("nickname") or profile["snake_id"])
        st.caption(f"Snake ID: {profile['snake_id']}")

        if error is not None:
            st.warning(error)

        photo_column, details_column = st.columns(2, gap="large")

        with photo_column:
            if photo_content is not None:
                st.image(photo_content, width="stretch")
            else:
                st.info("Profile photo is unavailable.")

        with details_column:
            st.markdown("**Basic Information**")
            basic_fields = [
                ("Snake ID", "snake_id"),
                ("Breeder", "breeder_name"),
                ("Breeder Internal ID", "breeder_internal_id"),
                ("Species", "species"),
                ("Sex", "sex"),
                ("Date of Birth", "date_of_birth"),
            ]
            st.table([
                {
                    "Field": label,
                    "Value": profile.get(field) or "Not provided",
                }
                for label, field in basic_fields
            ])

        st.divider()
        st.markdown("**Profile Details**")
        description_fields = [
            ("Genetic Description", "genetic_description"),
            ("Introduction", "introduction"),
            ("Sire Description", "sire_description"),
            ("Dam Description", "dam_description"),
        ]
        for label, field in description_fields:
            st.markdown(f"**{label}**")
            st.write(profile.get(field) or "Not provided")

    render_keeper_transfer_section(
        api_base_url=api_base_url,
        snake_id=profile["snake_id"],
        account=account,
        access_token=access_token,
    )

    render_certificate_history(
        api_base_url=api_base_url,
        snake_id=profile["snake_id"],
        access_token=access_token,
    )


# Purpose: display only the signed-in role's business operations.
# Backend session and chain checks remain responsible for write authorization.
def render_workspace(
    *, api_base_url: str, account: dict, access_token: str
) -> None:
    titles = {
        "breeder": "Breeder Workspace",
        "buyer": "Buyer Workspace",
        "lab": "Laboratory Workspace",
    }
    role = account["role"]
    with st.container(border=False, key="workspace_header"):
        with st.container(horizontal=True, vertical_alignment="center", gap="large"):
            with st.container(width="stretch"):
                st.markdown("**Ball Python Blockchain Registry**")
                st.title(titles[role])
                st.caption(
                    f"Signed in as {account['display_name']} ({account['username']})"
                )
                if role == "lab":
                    st.caption(f"Laboratory: {account['participant_id']}")

            if st.button("Sign Out", key="account_sign_out", type="secondary"):
                sign_out_current_account(access_token=access_token)

    _render_connection_status(api_base_url)

    if role == "lab":
        render_certificate_issuance(
            api_base_url=api_base_url,
            account=account,
            access_token=access_token,
        )
        return

    if role == "breeder":
        _render_snake_registration(api_base_url, access_token)

    _render_snake_profile(api_base_url, access_token, account)
    render_husbandry_section(
        api_base_url=api_base_url,
        account=account,
        access_token=access_token,
    )
