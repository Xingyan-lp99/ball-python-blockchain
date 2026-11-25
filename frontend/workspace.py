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


def _render_snake_registration(api_base_url: str, access_token: str) -> None:
    st.subheader("Register a Pet")
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
                "Pet ID": profile["snake_id"],
                "Species": profile["species"],
                "Sex": profile["sex"],
                "Date of Birth": profile["date_of_birth"],
                "Transaction Hash": payload["transaction_hash"],
                "Receipt Status": payload["receipt_status"],
                "Initial Keeper": payload["initial_keeper"],
            })
        elif status_code == 409:
            st.error("This pet ID already has a profile or on-chain registration.")
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
        snake_id = st.text_input("Pet ID *")
        species = st.text_input("Species *", max_chars=100, placeholder="e.g. Dog, Cat, Snake, Bird")
        sex = st.selectbox("Sex *", ["Male", "Female"], index=None, placeholder="Select sex")
        date_of_birth = st.date_input(
            "Date of Birth *",
            value=None,
            min_value=date(1900, 1, 1),
            max_value=date.today(),
            format="YYYY-MM-DD",
            key="snake_date_of_birth",
        )
        photo = st.file_uploader(
            "Photo * (JPEG / PNG, up to 5 MiB)",
            type=["jpg", "jpeg", "png"],
            max_upload_size=5,
        )

        with st.expander("Optional Details"):
            nickname = st.text_input("Pet Name")
            introduction = st.text_area("Additional Information")
            sire_description = st.text_area("Sire Description")
            dam_description = st.text_area("Dam Description")

        submitted = st.form_submit_button("Register", type="primary", key="register_snake")

    if not submitted:
        return

    if (
        snake_id == ""
        or sex is None
        or photo is None
    ):
        st.error("Please complete all required fields and upload a photo.")
        return

    if not species.strip() or len(species) > 100:
        st.error("Please enter a Species of 1 to 100 characters, not just whitespace.")
        return

    if date_of_birth is None or date_of_birth > date.today():
        st.error("Please select a date of birth that is not in the future.")
        return

    profile = {
        "snake_id": snake_id,
        "species": species,
        "sex": sex,
        "date_of_birth": date_of_birth.isoformat(),
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
    st.subheader("Pet Profile")

    st.session_state.setdefault("profile_lookup_id", "")
    selected_id = st.session_state.pop("buyer_selected_snake_id", None)
    if selected_id is not None:
        st.session_state["profile_lookup_id"] = selected_id

    with st.form("view_snake_profile"):
        snake_id = st.text_input(
            "Pet ID", key="profile_lookup_id"
        )
        submitted = st.form_submit_button(
            "View Profile",
            type="primary",
            key="view_profile",
        )

    if submitted:
        if snake_id == "":
            st.error("Please enter a pet ID.")
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
        st.caption(f"Pet ID: {profile['snake_id']}")

        if error is not None:
            st.warning(error)

        photo_column, details_column = st.columns(2, gap="large")

        with photo_column:
            if photo_content is not None:
                st.image(photo_content, width="stretch")
            else:
                st.info("Profile photo is unavailable.")

        with details_column:
            st.markdown('<p class="profile-section-title">Basic Information</p>', unsafe_allow_html=True)
            basic_fields = [
                ("Pet ID", "snake_id"),
                ("Pet Name", "nickname"),
                ("Species", "species"),
                ("Seller", "breeder_name"),
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
        st.markdown('<p class="profile-section-title">Profile Details</p>', unsafe_allow_html=True)
        description_fields = [
            ("Genetic Description", "genetic_description"),
            ("Additional Information", "introduction"),
            ("Sire Description", "sire_description"),
            ("Dam Description", "dam_description"),
        ]
        for label, field in description_fields:
            if field == "genetic_description" and not profile.get(field):
                continue
            st.markdown(f'<p class="profile-field-label">{label}</p>', unsafe_allow_html=True)
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
    st.subheader("Explore Pet Profiles")

    if st.button("Shuffle Profiles", key="shuffle_buyer_snake_profiles"):
        st.session_state.pop("buyer_snake_showcase", None)
        st.session_state.pop("buyer_snake_showcase_error", None)
        st.rerun()

    if "buyer_snake_showcase" not in st.session_state and (
        "buyer_snake_showcase_error" not in st.session_state
    ):
        try:
            with st.spinner("Finding pet profiles..."):
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
                    st.info("No additional pet profile is available.")
                continue

            profile, photo_content, photo_error = profiles[index]
            if profile is None:
                st.info(photo_error or "Pet profile is unavailable.")
                continue

            snake_id = profile["snake_id"]
            nickname = profile.get("nickname") or snake_id
            card_key = f"buyer_snake_card_{index}"
            with st.container(key=f"buyer_snake_card_frame_{index}"):
                if photo_content is not None:
                    st.image(
                        photo_content,
                        width="stretch",
                        alt=f"Photo of pet {nickname}",
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
                    with st.spinner("Opening the pet profile..."):
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
        "breeder": "Seller",
        "buyer": "Buyer",
        "lab": "Laboratory",
    }
    role = account["role"]
    role_label = role_labels[role]
    if role == "lab":
        role_label = f"{role_label} · {account['participant_id']}"

    with st.container(border=False, key="workspace_header"):
        with st.container(horizontal=True, vertical_alignment="center", gap="large"):
            if not st.session_state.get("demo_role"):
                render_pythonpass_logo(width_px=280)
            st.markdown(f"**{role_label}**", width="content")
            st.html(
                f"""
                <div class="workspace-account">
                  <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                    <circle cx="12" cy="7" r="3.5" fill="none" stroke="#243B30" stroke-width="2" />
                    <path d="M4.5 21v-2a7.5 7.5 0 0 1 15 0v2z" fill="none" stroke="#243B30" stroke-width="2" />
                  </svg>
                  <span>{escape(account['username'])}</span>
                </div>
                """,
                width="content",
            )

            if st.button("Exit Demo Mode" if st.session_state.get("demo_role") else "Sign Out", key="account_sign_out", type="secondary"):
                sign_out_current_account(access_token=access_token)

    st.subheader(f"{st.session_state.get('demo_role') or role_label} Workspace")
    mode_label = "Demo Mode" if st.session_state.get("demo_role") else "Normal Mode"
    st.caption(f"{mode_label} · Local Anvil · Sepolia is a separate script demonstration.")

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
