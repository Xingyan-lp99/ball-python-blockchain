import streamlit as st

from frontend.api import (
    AccountRequestError,
    SignInRequired,
    sign_in_account,
    sign_out_account,
)


API_BASE_URL = "http://127.0.0.1:8001"


# Clear cached profiles, forms, and the previous account's login credential.
# Without this reset, switching accounts could retain another workspace's data.
def return_to_login(message: str | None = None) -> None:
    st.session_state.clear()
    st.session_state["auth_view"] = "login"
    if message:
        st.session_state["auth_notice"] = message
    st.rerun()


def open_registration() -> None:
    st.session_state.clear()
    st.session_state["auth_view"] = "register"
    st.rerun()


# Purpose: authenticate before exposing any business workspace.
# Without this page, users have no entry point for the backend login flow.
def render_login_page() -> None:
    st.title("Login")
    st.caption("Ball Python Blockchain Registry")

    notice = st.session_state.pop("auth_notice", None)
    if notice:
        st.info(notice)

    with st.form("account_login", clear_on_submit=True):
        username = st.text_input("Username *")
        password = st.text_input("Password *", type="password", max_chars=1024)
        submitted = st.form_submit_button("Sign In")

    if submitted:
        if not username.strip() or not password:
            st.error("Please enter your username and password.")
        else:
            try:
                with st.spinner("Signing in..."):
                    session = sign_in_account(
                        api_base_url=API_BASE_URL,
                        username=username.strip(),
                        password=password,
                    )
            except AccountRequestError as error:
                st.error(str(error))
            else:
                st.session_state.clear()
                st.session_state["auth_session"] = session
                st.rerun()

    st.write("Do not have an account?")
    if st.button("Create Account", key="open_account_registration"):
        open_registration()


def sign_out_current_account(*, access_token: str) -> None:
    message = "You have signed out."
    try:
        sign_out_account(api_base_url=API_BASE_URL, access_token=access_token)
    except SignInRequired:
        pass
    except AccountRequestError:
        message = (
            "You have signed out on this page, but the server session could not "
            "be revoked. It will expire automatically."
        )
    return_to_login(message)
