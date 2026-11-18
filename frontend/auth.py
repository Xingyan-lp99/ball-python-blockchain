import streamlit as st

from frontend.branding import render_pythonpass_logo
from frontend.api import (
    AccountRequestError,
    SignInRequired,
    sign_in_account,
    sign_out_account,
)
from frontend.login_gallery import render_login_gallery


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


# Purpose: pair a welcome message and photo showcase with the sign-in card.
# Workflow: authenticate before exposing any business workspace.
# Without this function, users cannot access the workspace through sign-in.
def render_login_page() -> None:
    with st.container(horizontal_alignment="center"):
        with st.container(width=1100):
            with st.container(key="login_intro", gap=0):
                render_pythonpass_logo(width_px=240)
                st.divider()

            with st.container(
                key="login_layout",
                horizontal=True,
                horizontal_alignment="center",
                vertical_alignment="distribute",
                gap=48,
            ):
                with st.container(
                    width=600,
                    height="stretch",
                    key="login_gallery_column",
                ):
                    with st.container(key="login_marketing_copy", gap=16):
                        st.title("Every python has a story.")
                        st.write(
                            "Discover the records behind every ball python."
                        )

                    render_login_gallery()

                with st.container(
                    width=420,
                    height="stretch",
                    key="login_form_column",
                ):
                    with st.container(
                        border=False,
                        height="stretch",
                        key="login_card",
                    ):
                        st.subheader("WELCOME BACK")
                        st.write("Sign in to open your workspace.")

                        notice = st.session_state.pop("auth_notice", None)
                        if notice:
                            st.info(notice)

                        with st.form(
                            "account_login",
                            clear_on_submit=True,
                            border=False,
                        ):
                            username = st.text_input("Username *")
                            password = st.text_input(
                                "Password *",
                                type="password",
                                max_chars=1024,
                            )
                            submitted = st.form_submit_button(
                                "Sign In",
                                type="primary",
                                key="sign_in",
                                width="stretch",
                            )

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

                        st.divider()
                        st.write("New to PythonPass?")
                        if st.button(
                            "Create Account",
                            key="open_account_registration",
                            width="stretch",
                        ):
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
