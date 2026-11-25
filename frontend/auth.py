import json
from pathlib import Path

import streamlit as st

from frontend.branding import render_pythonpass_logo
from frontend.api import (
    AccountRequestError,
    SignInRequired,
    fetch_current_account,
    sign_in_account,
    sign_out_account,
)
from frontend.login_gallery import render_login_gallery


API_BASE_URL = "http://127.0.0.1:8001"

DEMO_ACCOUNTS = {
    "Seller": ("breeder", "BREEDER001"),
    "Buyer": ("buyer", "BUYER001"),
    "Lab 1": ("lab", "LAB001"),
    "Lab 2": ("lab", "LAB002"),
}
DEMO_CONFIG_PATH = Path(__file__).resolve().parents[1] / "storage/frontend-demo.json"


def _demo_settings() -> dict:
    """Load opt-in credentials on the server, never into page/widget state."""
    if st.get_option("server.address") not in {"127.0.0.1", "localhost", "::1"}:
        return {}
    try:
        settings = json.loads(DEMO_CONFIG_PATH.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError):
        return {}
    if not isinstance(settings, dict) or settings.get("enabled") is not True:
        return {}
    for label in DEMO_ACCOUNTS:
        credentials = settings.get(label)
        if not isinstance(credentials, dict) or not all(
            isinstance(credentials.get(field), str) and credentials[field].strip()
            for field in ("username", "password")
        ):
            return {}
    return settings


def _revoke_demo_session(session: dict | None) -> None:
    if session:
        try:
            sign_out_account(api_base_url=API_BASE_URL, access_token=session["access_token"])
        except (AccountRequestError, SignInRequired):
            pass  # Local credentials are still cleared; server sessions expire.


def _activate_demo_account(label: str) -> None:
    """Authenticate the selected account, then discard all previous page state."""
    settings = _demo_settings()
    _revoke_demo_session(st.session_state.get("auth_session"))
    st.session_state.clear()
    if not settings or label not in DEMO_ACCOUNTS:
        return_to_login("Demo Mode is unavailable.")
    session = None
    try:
        session = sign_in_account(api_base_url=API_BASE_URL, **{
            field: settings[label][field] for field in ("username", "password")
        })
        account = fetch_current_account(
            api_base_url=API_BASE_URL, access_token=session["access_token"]
        )
        if (account["role"], account["participant_id"]) != DEMO_ACCOUNTS[label]:
            raise AccountRequestError("Demo account identity mismatch.")
    except (AccountRequestError, SignInRequired):
        _revoke_demo_session(session)
        return_to_login("Demo sign-in failed. Check the local demo account configuration.")
    session["account"] = account
    st.session_state["auth_session"] = session
    st.session_state["demo_role"] = label
    st.rerun()


def render_demo_navigation() -> None:
    if not st.session_state.get("demo_role"):
        return
    if not _demo_settings():
        _revoke_demo_session(st.session_state.get("auth_session"))
        return_to_login("Demo Mode is unavailable.")
    with st.container(key="demo_navigation"):
        render_pythonpass_logo()
        st.caption("Demo Mode · Local Anvil · Changes use real demo accounts")
        selected = st.segmented_control(
            "Demo account", list(DEMO_ACCOUNTS),
            default=st.session_state["demo_role"], required=True,
            key="demo_role_picker", width="stretch",
        )
        if st.button("Exit Demo Mode", key="exit_demo"):
            sign_out_current_account(access_token=st.session_state["auth_session"]["access_token"])
        if selected != st.session_state["demo_role"]:
            _activate_demo_account(selected)


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
                render_pythonpass_logo(width_px=360)
                st.divider()

            with st.container(
                key="login_layout",
                horizontal=True,
                horizontal_alignment="center",
                vertical_alignment="top",
                gap=48,
            ):
                with st.container(
                    width=600,
                    height="content",
                    gap=56,
                    key="login_gallery_column",
                ):
                    with st.container(key="login_marketing_copy", gap=16):
                        st.title("Each pet has a lifetime story.")

                    render_login_gallery()

                with st.container(
                    width=440,
                    height="content",
                    key="login_form_column",
                ):
                    with st.container(
                        border=False,
                        height="content",
                        gap=12,
                        key="login_card",
                    ):
                        st.subheader("Welcome back")
                        st.write("Sign in to open your workspace.")

                        notice = st.session_state.pop("auth_notice", None)
                        if notice:
                            st.info(notice)

                        with st.form(
                            "account_login",
                            clear_on_submit=True,
                            border=False,
                        ):
                            username = st.text_input("Username *", key="login_username", autocomplete="off")
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
                        st.write("New to Pet Lifetime Records?")
                        if st.button(
                            "Create Account",
                            key="open_account_registration",
                            width="stretch",
                        ):
                            open_registration()

                        if st.button(
                            "Enter Demo Mode", key="enter_demo", width="stretch",
                            disabled=not bool(_demo_settings()),
                            help="Available when local classroom demo accounts are configured.",
                        ):
                            _activate_demo_account("Seller")


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
