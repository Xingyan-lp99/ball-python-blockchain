import os
from datetime import datetime, timezone
from urllib.parse import quote
import requests
import streamlit as st

API_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="Ball Python Blockchain Registry",
    page_icon="🐍",
    layout="wide",
)

st.title("Ball Python Blockchain Registry")
st.write("Ball python identity and genetic certificate verification.")

st.subheader("Backend Connection")

if st.button("Check Backend Connection"):
    try:
        response = requests.get(
            f"{API_URL}/api/v1/health",
            timeout=5,
        )
        response.raise_for_status()

        data = response.json()

        if data.get("status") == "ok":
            st.success("FastAPI backend is connected!")
        else:
            st.warning("Unexpected backend response.")

    except requests.RequestException:
        st.error("Backend connection failed. Check that FastAPI is running.")


def show_profile(profile: dict) -> None:
    st.subheader("Saved snake profile")
    st.json(profile)
    registration = profile.get("chain_registration") or {}
    status = registration.get("status", "not_submitted")
    if status == "confirmed" and registration.get("chain_check") == "verified":
        st.success("Confirmed on the current local Hardhat chain. Snake profile details are not laboratory certified; verify individual certificate files separately.")
    elif status == "processing":
        st.warning("Processing / confirmation unavailable. This profile is not currently confirmed on-chain.")
    elif status == "failed":
        st.error("Registration failed or historical chain evidence is stale. The database profile is retained.")
    else:
        st.info("Saved in the database only. Blockchain registration has not been submitted. Snake profile details are not laboratory certified.")
    if registration:
        st.write("Registration status:", status)
        st.write("Transaction hash:", registration.get("transaction_hash") or "Not yet available")
        st.write("Manager wallet:", registration.get("manager_address") or "Not yet available")
        st.write("Chain ID:", registration.get("chain_id"))
        st.write("Registry contract:", registration.get("contract_address"))
        st.write("Confirmation block:", registration.get("block_number"))
        if registration.get("error"):
            st.warning(registration["error"])
    st.caption("Morph description is breeder-provided and has not been certified by a laboratory.")


def show_api_error(response: requests.Response) -> None:
    if response.status_code == 409:
        st.error("This snake ID is already registered.")
    elif response.status_code == 404:
        st.error("Snake not found.")
    elif response.status_code == 422:
        st.error("Invalid input. Check the snake ID, sex and date of birth.")
    else:
        st.error("The service could not complete the request. Check backend and database availability.")


role = st.radio("Demo workspace", ["Breeder", "Laboratory", "Buyer"], horizontal=True)
st.caption("Demonstration workspaces only; selecting a role is not production authentication.")
if role != "Breeder":
    from certificate_page import render_certificate_workspace
    render_certificate_workspace(API_URL, role)
    st.stop()

st.header("Snake Registration")
st.warning("Demo identity: BR001 is assigned by the server. Real authentication is not implemented. Local-chain transactions are signed by the server-controlled Hardhat development wallet.")
with st.form("register_snake"):
    snake_id = st.text_input("Snake ID (required)")
    name = st.text_input("Name (optional)")
    sex = st.selectbox("Sex", ["unknown", "male", "female"])
    date_of_birth = st.date_input(
        "Date of birth (optional)", value=None,
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.now(timezone.utc).date(),
    )
    breeder_internal_id = st.text_input("Breeder internal ID (optional)")
    morph_description = st.text_area("Morph description (optional)")
    st.caption("Breeder-provided description; not laboratory certified.")
    register = st.form_submit_button("Register snake")

if register:
    try:
        response = requests.post(
            f"{API_URL}/api/v1/snakes",
            json={
                "snake_id": snake_id,
                "name": name or None,
                "sex": sex,
                "date_of_birth": date_of_birth.isoformat() if date_of_birth else None,
                "breeder_internal_id": breeder_internal_id or None,
                "morph_description": morph_description or None,
            },
            timeout=10,
        )
        if response.status_code == 201:
            st.success("Snake profile saved to the database.")
            st.session_state["saved_profile"] = response.json()
        else:
            show_api_error(response)
    except (requests.RequestException, ValueError):
        st.error("Registration response could not be received. Query the snake ID before retrying.")

st.header("Find a snake")
with st.form("find_snake"):
    lookup_id = st.text_input("Snake ID")
    lookup = st.form_submit_button("Find snake")

if lookup:
    if not lookup_id.strip():
        st.error("Enter a snake ID.")
    else:
        try:
            response = requests.get(
                f"{API_URL}/api/v1/snakes/{quote(lookup_id.strip(), safe='')}",
                timeout=10,
            )
            if response.status_code == 200:
                st.session_state["saved_profile"] = response.json()
            else:
                show_api_error(response)
        except (requests.RequestException, ValueError):
            st.error("Query failed. Check backend availability and try again.")

if "saved_profile" in st.session_state:
    profile = st.session_state["saved_profile"]
    registration = profile.get("chain_registration") or {}
    endpoint = f"{API_URL}/api/v1/snakes/{quote(profile['snake_id'], safe='')}/registration"
    operation = None
    if registration.get("status") != "confirmed":
        if st.button(
            "Submit local-chain registration",
            disabled=(registration.get("status") == "processing" and not (
                registration.get("recorded_status") == "prepared" and registration.get("chain_check") == "verified"
            )) or registration.get("chain_check") in {"stale", "conflict"},
        ):
            operation = "submit"
    if st.button("Refresh chain status"):
        operation = "refresh"
    if operation:
        try:
            response = (
                requests.post(endpoint, json={}, timeout=15) if operation == "submit"
                else requests.get(endpoint, timeout=15)
            )
            if response.status_code == 200:
                registration = response.json()
                profile["chain_registration"] = registration
                profile["registration_status"] = registration["status"]
            else:
                # Clear any previously displayed success after an unsuccessful check.
                profile["chain_registration"] = {
                    **registration, "status": "processing", "chain_check": "unavailable",
                    "error": "Registration could not be confirmed. Refresh status before retrying.",
                }
                profile["registration_status"] = "processing"
                if response.status_code in {403, 409}:
                    st.error("Registration is forbidden, conflicts with chain state, or another request is processing. Refresh status for details.")
                else:
                    show_api_error(response)
        except (requests.RequestException, ValueError):
            profile["chain_registration"] = {
                **registration, "status": "processing", "chain_check": "unavailable",
                "error": "Response unavailable; a timeout is not proof of failure. Refresh chain status.",
            }
            profile["registration_status"] = "processing"
        st.session_state["saved_profile"] = profile
    elif registration.get("status") == "confirmed":
        # A Streamlit rerun/session cache alone is not current blockchain evidence.
        try:
            response = requests.get(endpoint, timeout=15)
            response.raise_for_status()
            registration = response.json()
            profile["chain_registration"] = registration
            profile["registration_status"] = registration["status"]
        except (requests.RequestException, ValueError):
            profile["chain_registration"] = {
                **registration, "status": "processing", "chain_check": "unavailable",
                "error": "Current chain could not be checked; historical success is not current confirmation.",
            }
            profile["registration_status"] = "processing"
    show_profile(profile)
