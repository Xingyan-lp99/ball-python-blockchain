from datetime import date
from html import escape

import streamlit as st

from frontend.api import (
    AccountRequestError,
    fetch_random_snake_profiles,
    fetch_snake_profile,
    submit_snake_registration,
)
from frontend.branding import render_pythonpass_logo
from frontend.auth import sign_out_current_account
from frontend.husbandry import render_husbandry_section
from frontend.keeper_transfers import render_keeper_transfer_section

from frontend.certificates import render_certificate_history, render_certificate_issuance


MONTH_NAMES = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
)


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
        st.markdown("**Date of Birth** *")
        month_column, day_column, year_column = st.columns(3, gap="small")
        with month_column:
            birth_month = st.selectbox(
                "Month",
                MONTH_NAMES,
                index=None,
                placeholder="Select month",
                key="snake_birth_month",
            )
        with day_column:
            birth_day = st.number_input(
                "Day",
                min_value=1,
                max_value=31,
                value=None,
                step=1,
                placeholder="Select day",
                key="snake_birth_day",
            )
        with year_column:
            birth_year = st.selectbox(
                "Year",
                range(date.today().year, 1899, -1),
                index=None,
                placeholder="Select year",
                key="snake_birth_year",
            )

        date_of_birth = None
        invalid_birth_date = False
        if birth_month is not None and birth_day is not None and birth_year is not None:
            try:
                date_of_birth = date(
                    int(birth_year),
                    MONTH_NAMES.index(birth_month) + 1,
                    int(birth_day),
                )
            except ValueError:
                invalid_birth_date = True
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
        or photo is None
    ):
        st.error("Please complete all required fields and upload a photo.")
        return

    if date_of_birth is None:
        st.error(
            "Please select a valid date of birth."
            if invalid_birth_date
            else "Please select the month, day, and year of birth."
        )
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

    st.session_state.setdefault("profile_lookup_id", "SNAKE001")
    selected_id = st.session_state.pop("buyer_selected_snake_id", None)
    if selected_id is not None:
        st.session_state["profile_lookup_id"] = selected_id

    with st.form("view_snake_profile"):
        snake_id = st.text_input(
            "Snake ID", key="profile_lookup_id"
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
            with st.spinner("Loading the saved profile..."):
                _select_snake_profile(
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

    if account["role"] in {"buyer", "breeder"}:
        with st.container(key="buyer_profile_sections"):
            certificates, keeper, husbandry = st.tabs([
                "Certificate History", "Keeper Management", "Husbandry Records"
            ])
            with certificates:
                render_certificate_history(
                    api_base_url=api_base_url,
                    snake_id=profile["snake_id"],
                    access_token=access_token,
                )
            with keeper:
                render_keeper_transfer_section(
                    api_base_url=api_base_url,
                    snake_id=profile["snake_id"],
                    account=account,
                    access_token=access_token,
                )
            with husbandry:
                render_husbandry_section(
                    api_base_url=api_base_url,
                    account=account,
                    access_token=access_token,
                    snake_id=profile["snake_id"],
                )
        return

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


def _select_snake_profile(
    *,
    api_base_url: str,
    snake_id: str,
    access_token: str,
) -> tuple[dict | None, bytes | None, str | None]:
    st.session_state.pop(f"certificate_history_{snake_id}", None)
    st.session_state.pop(f"keeper_transfer_status_{snake_id}", None)
    saved_profile = fetch_snake_profile(
        api_base_url=api_base_url,
        snake_id=snake_id,
        access_token=access_token,
    )
    st.session_state["saved_snake_profile"] = saved_profile
    return saved_profile


def _render_buyer_snake_showcase(
    *,
    api_base_url: str,
    access_token: str,
) -> None:
    st.divider()
    st.subheader("Explore Snake Profiles")

    if st.button("Shuffle Profiles", key="shuffle_buyer_snake_profiles"):
        st.session_state.pop("buyer_snake_showcase", None)
        st.session_state.pop("buyer_snake_showcase_error", None)
        st.rerun()

    if "buyer_snake_showcase" not in st.session_state and (
        "buyer_snake_showcase_error" not in st.session_state
    ):
        try:
            with st.spinner("Finding snake profiles..."):
                st.session_state["buyer_snake_showcase"] = (
                    fetch_random_snake_profiles(
                        api_base_url=api_base_url,
                        access_token=access_token,
                    )
                )
        except AccountRequestError as error:
            st.session_state["buyer_snake_showcase_error"] = str(error)

    error = st.session_state.get("buyer_snake_showcase_error")
    if error:
        st.error(error)
        if st.button("Retry Profiles", key="retry_buyer_snake_showcase"):
            st.session_state.pop("buyer_snake_showcase_error", None)
            st.rerun()
        return

    profiles = st.session_state.get("buyer_snake_showcase", [])
    columns = st.columns(3, gap="medium")
    for index, column in enumerate(columns):
        with column:
            if index >= len(profiles):
                with st.container(border=True):
                    st.info("No additional snake profile is available.")
                continue

            profile, photo_content, photo_error = profiles[index]
            if profile is None:
                st.info(photo_error or "Snake profile is unavailable.")
                continue

            snake_id = profile["snake_id"]
            nickname = profile.get("nickname") or snake_id
            card_key = f"buyer_snake_card_{index}"
            with st.container(key=f"buyer_snake_card_frame_{index}"):
                if photo_content is not None:
                    st.image(
                        photo_content,
                        width="stretch",
                        alt=f"Photo of ball python {nickname}",
                    )
                    clicked = st.button(
                        f"View profile: {nickname} ({snake_id})",
                        key=card_key,
                        width="stretch",
                    )
                    st.caption(f"{nickname} · {snake_id} · Click photo to view")
                else:
                    st.info(photo_error or "Profile photo is unavailable.")
                    clicked = st.button(
                        f"View profile: {nickname} ({snake_id})",
                        key=card_key,
                        width="stretch",
                    )

                if clicked:
                    with st.spinner("Opening the snake profile..."):
                        _select_snake_profile(
                            api_base_url=api_base_url,
                            snake_id=snake_id,
                            access_token=access_token,
                        )
                    st.session_state["buyer_selected_snake_id"] = snake_id
                    st.rerun()


# Purpose: display only the signed-in role's business operations.
# Backend session and chain checks remain responsible for write authorization.
def render_workspace(
    *, api_base_url: str, account: dict, access_token: str
) -> None:
    role_labels = {
        "breeder": "BREEDER",
        "buyer": "BUYER",
        "lab": "LAB STAFF",
    }
    role = account["role"]
    role_label = role_labels[role]
    if role == "lab":
        role_label = f"{role_label} · {account['participant_id']}"

    with st.container(border=False, key="workspace_header"):
        with st.container(horizontal=True, vertical_alignment="center", gap="large"):
            render_pythonpass_logo(width_px=280)
            st.markdown(f"**{role_label}**", width="content")
            st.html(
                f"""
                <div class="workspace-account">
                  <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                    <circle cx="12" cy="7" r="3.5" fill="none" stroke="#291344" stroke-width="2" />
                    <path d="M4.5 21v-2a7.5 7.5 0 0 1 15 0v2z" fill="none" stroke="#291344" stroke-width="2" />
                  </svg>
                  <span>{escape(account['username'])}</span>
                </div>
                """,
                width="content",
            )

            if st.button("Sign Out", key="account_sign_out", type="secondary"):
                sign_out_current_account(access_token=access_token)

    if role == "lab":
        with st.container(key="lab_certificate_workspace"):
            render_certificate_issuance(
                api_base_url=api_base_url,
                account=account,
                access_token=access_token,
            )
        return

    if role == "breeder":
        _render_snake_registration(api_base_url, access_token)

    _render_snake_profile(api_base_url, access_token, account)

    if role == "buyer":
        _render_buyer_snake_showcase(
            api_base_url=api_base_url,
            access_token=access_token,
        )
