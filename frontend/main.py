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
    st.info("Saved in the database only. Blockchain registration has not been submitted; certificates have not been verified.")
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


st.header("Snake Registration")
st.warning("Demo identity: BR001 is assigned by the server. Real authentication is not implemented.")
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
            show_profile(response.json())
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
                show_profile(response.json())
            else:
                show_api_error(response)
        except (requests.RequestException, ValueError):
            st.error("Query failed. Check backend availability and try again.")
