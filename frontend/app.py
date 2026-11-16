import streamlit as st

from frontend.api import (
    check_backend_readiness,
    submit_snake_registration,
    fetch_snake_profile,
)


st.set_page_config(page_title="Ball Python Registry")
st.title("Ball Python Registry")

with st.expander("Connection Status"):
    if st.button("Check Backend and Database"):
        result = check_backend_readiness(
            "http://127.0.0.1:8001/ready"
        )

        if result == "ok":
            st.success("Backend and database are ready.")
        elif result == "database_unavailable":
            st.error("The database is not ready.")
        elif result == "backend_unavailable":
            st.error("Cannot connect to the backend.")
        else:
            st.error("The backend returned an unexpected response.")

st.subheader("Register a Ball Python")
st.caption("Current role: Breeder · BREEDER001")

previous = st.session_state.get("registration_result")
locked = False

if previous is not None:
    status_code = previous["status_code"]
    payload = previous["payload"]
    outcome = payload.get("outcome")

    locked = status_code == 201 or outcome in {
        "unknown",
        "failed",
        "unverified",
        "storage_error",
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
        st.error("This snake ID already has a profile or on-chain registration. Do not register it again.")
    elif outcome == "not_submitted":
        st.error("Registration is not configured yet. No transaction was submitted.")
    elif locked:
        st.error("Registration could not be confirmed as complete. Check the result before submitting again.")
        if payload.get("transaction_hash"):
            st.caption("Transaction to Check")
            st.code(payload["transaction_hash"])
    else:
        detail = payload.get("detail")
        st.error(
            detail
            if isinstance(detail, str)
            else "Please check the required fields and photo."
        )

if not locked:
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

    if submitted:
        required_text = [
            breeder_internal_id,
            species,
            sex,
            genetic_description,
        ]

        if (
            snake_id == ""
            or any(not value.strip() for value in required_text)
            or date_of_birth is None
            or photo is None
        ):
            st.error("Please complete all required fields and upload a photo.")
        else:
            profile = {
                "snake_id": snake_id,
                "breeder_internal_id": breeder_internal_id,
                "species": species,
                "sex": sex,
                "date_of_birth": date_of_birth.isoformat(),
                "genetic_description": genetic_description,
                "nickname": nickname if nickname.strip() else None,
                "introduction": introduction if introduction.strip() else None,
                "sire_description": (
                    sire_description if sire_description.strip() else None
                ),
                "dam_description": (
                    dam_description if dam_description.strip() else None
                ),
            }

            photo_content = photo.getvalue()

            with st.spinner("Saving the profile and confirming on-chain registration..."):
                status_code, payload = submit_snake_registration(
                    url="http://127.0.0.1:8001/api/v1/snakes",
                    profile=profile,
                    photo_name=photo.name,
                    photo_content=photo_content,
                )

            st.session_state["registration_result"] = {
                "status_code": status_code,
                "payload": payload,
                "profile": profile,
                "photo_content": photo_content,
            }
            st.rerun()


st.divider()
st.subheader("Snake Profile")

with st.form("view_snake_profile"):
    lookup_snake_id = st.text_input(
        "Snake ID",
        value="SNAKE001",
        key="profile_lookup_id",
    )
    view_profile = st.form_submit_button("View Profile")

if view_profile:
    if lookup_snake_id == "":
        st.error("Please enter a snake ID.")
    else:
        with st.spinner("Loading the saved profile..."):
            st.session_state["saved_snake_profile"] = fetch_snake_profile(
                api_base_url="http://127.0.0.1:8001",
                snake_id=lookup_snake_id,
            )

saved_profile = st.session_state.get("saved_snake_profile")

if saved_profile is not None:
    stored_profile, stored_photo, load_error = saved_profile

    if stored_profile is None:
        st.error(load_error)
    else:
        st.subheader(f"Profile: {stored_profile['snake_id']}")

        if stored_photo is not None:
            st.image(stored_photo, width=320)

        if load_error is not None:
            st.warning(load_error)

        fields = [
            ("Snake ID", "snake_id"),
            ("Breeder", "breeder_name"),
            ("Breeder Internal ID", "breeder_internal_id"),
            ("Nickname", "nickname"),
            ("Species", "species"),
            ("Sex", "sex"),
            ("Date of Birth", "date_of_birth"),
            ("Genetic Description", "genetic_description"),
            ("Introduction", "introduction"),
            ("Sire Description", "sire_description"),
            ("Dam Description", "dam_description"),
        ]

        st.table([
            {
                "Field": label,
                "Value": stored_profile.get(field) or "Not provided",
            }
            for label, field in fields
        ])