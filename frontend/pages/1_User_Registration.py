import re

import streamlit as st

from frontend.api import AccountRequestError, register_user_account
from frontend.auth import API_BASE_URL, return_to_login


st.title("Create an Account")
st.caption("Register as a Buyer, Breeder, or Laboratory Staff member.")

registered = st.session_state.get("registered_account")
if registered is not None:
    st.success(f"Account created: {registered['username']}. You can now sign in.")
    if st.button("Back to Login", key="registered_back_to_login"):
        return_to_login("Account created successfully. Please sign in.")
    st.stop()

# Keep role selection outside the form so its fields update immediately.
role = st.selectbox(
    "Account Role *",
    options=["Buyer", "Breeder", "Laboratory Staff"],
)

with st.form("user_registration"):
    st.subheader("Account Information")

    username = st.text_input("Username *")
    email = st.text_input("Email *")
    password = st.text_input("Password *", type="password", max_chars=1024)
    confirm_password = st.text_input(
        "Confirm Password *", type="password", max_chars=1024
    )

    st.subheader("Basic Information")

    display_name = st.text_input("Display Name *")
    country_or_region = st.text_input("Country or Region *")
    contact = st.text_input("Contact Information (Optional)")

    breeder_name = ""
    breeder_region = ""
    breeder_introduction = ""
    laboratory_id = None

    if role == "Breeder":
        st.subheader("Breeder Information")

        breeder_name = st.text_input("Breeder Name *")
        breeder_region = st.text_input("Breeder Region (Optional)")
        breeder_introduction = st.text_area(
            "Breeder Introduction (Optional)"
        )

    if role == "Laboratory Staff":
        st.subheader("Laboratory Information")
        laboratory_id = st.selectbox(
            "Laboratory *",
            options=["LAB001", "LAB002"],
            index=None,
            placeholder="Select a laboratory",
        )

    consent = st.checkbox(
        "I confirm that the information above is fictional demo information."
    )

    submitted = st.form_submit_button("Register")

# Validate before submission; passwords are never put into a preview or page state.
if submitted:
    required_values = [
        username,
        email,
        password,
        confirm_password,
        display_name,
        country_or_region,
    ]

    valid_email = re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+",
        email.strip(),
    )
    passwords_match = password == confirm_password
    breeder_name_provided = (
        role != "Breeder" or bool(breeder_name.strip())
    )

    if (
        any(not value.strip() for value in required_values)
        or valid_email is None
        or not passwords_match
        or not breeder_name_provided
        or (role == "Laboratory Staff" and laboratory_id is None)
        or not consent
    ):
        st.error(
            "Please complete the required fields and check the email, "
            "password confirmation, laboratory selection, and demo consent."
        )
    else:
        registration = {
            "username": username.strip(),
            "email": email.strip(),
            "password": password,
            "role": {
                "Buyer": "buyer",
                "Breeder": "breeder",
                "Laboratory Staff": "lab",
            }[role],
            "laboratory_id": laboratory_id,
            "display_name": display_name.strip(),
            "country_or_region": country_or_region.strip(),
            "contact": contact.strip() or None,
            "demo_consent": consent,
        }

        if role == "Breeder":
            registration.update({
                "breeder_name": breeder_name.strip(),
                "breeder_region": breeder_region.strip() or None,
                "breeder_introduction": (
                    breeder_introduction.strip() or None
                ),
            })

        try:
            with st.spinner("Creating your account..."):
                account = register_user_account(
                    api_base_url=API_BASE_URL, data=registration
                )
        except AccountRequestError as error:
            st.error(str(error))
        else:
            st.session_state["registered_account"] = account
            st.rerun()

if st.button("Back to Login", key="registration_back_to_login"):
    return_to_login()
