import re

import streamlit as st

from frontend.api import AccountRequestError, register_user_account
from frontend.auth import API_BASE_URL, return_to_login


# Center the existing registration workflow without changing its submission rules.
with st.container(horizontal_alignment="center"):
    with st.container(width=680):
        with st.container(key="registration_intro"):
            st.markdown("**Pet Lifetime Records**")
            st.title("Create an Account")
            st.write("Register as a Buyer or Seller.")
            st.caption("Laboratory staff: sign in with your preconfigured demo account.")

        with st.container(border=False, key="registration_card"):
            registered = st.session_state.get("registered_account")
            if registered is not None:
                st.success(f"Account created: {registered['username']}. You can now sign in.")
                if st.button(
                    "Back to Login", key="registered_back_to_login", width="stretch"
                ):
                    return_to_login("Account created successfully. Please sign in.")
                st.stop()

            # Keep role selection outside the form so its fields update immediately.
            role = st.selectbox(
                "Account Role *",
                options=["Buyer", "Breeder"],
                format_func=lambda value: "Seller" if value == "Breeder" else value,
            )

            with st.form("user_registration", border=False):
                st.subheader("Account Information")

                username = st.text_input("Username *")
                email = st.text_input("Email *")
                password = st.text_input("Password *", type="password", max_chars=1024)
                confirm_password = st.text_input(
                    "Confirm Password *", type="password", max_chars=1024
                )

                st.divider()
                st.subheader("Basic Information")

                display_name = st.text_input("Display Name *")
                country_or_region = st.text_input("Country or Region *")
                contact = st.text_input("Contact Information (Optional)")

                breeder_name = ""
                breeder_region = ""
                breeder_introduction = ""

                if role == "Breeder":
                    st.divider()
                    st.subheader("Seller Information")

                    breeder_name = st.text_input("Seller Name *")
                    breeder_region = st.text_input("Seller Region (Optional)")
                    breeder_introduction = st.text_area(
                        "Seller Introduction (Optional)"
                    )

                consent = st.checkbox(
                    "I confirm that the information above is fictional demo information."
                )

                submitted = st.form_submit_button(
                    "Register",
                    type="primary",
                    key="register_account",
                    width="stretch",
                )

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
                    or not consent
                ):
                    st.error(
                        "Please complete the required fields and check the email, "
                        "password confirmation and demo consent."
                    )
                else:
                    registration = {
                        "username": username.strip(),
                        "email": email.strip(),
                        "password": password,
                        "role": {
                            "Buyer": "buyer",
                            "Breeder": "breeder",
                        }[role],
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

            st.divider()
            if st.button(
                "Back to Login", key="registration_back_to_login", width="stretch"
            ):
                return_to_login()
