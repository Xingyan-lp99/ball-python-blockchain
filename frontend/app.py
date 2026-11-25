import streamlit as st

from frontend.api import AccountRequestError, SignInRequired, fetch_current_account
from frontend.auth import API_BASE_URL, DEMO_ACCOUNTS, render_demo_navigation, render_login_page, return_to_login
from frontend.styles import apply_styles
from frontend.workspace import render_workspace


st.set_page_config(
    page_title="Pet Lifetime Records",
    layout=(
        "wide"
        if st.session_state.get("auth_session") is None
        and st.session_state.get("auth_view") != "register"
        else "centered"
    ),
)
apply_styles()

# Validate the backend session before rendering any cached business content.
session = st.session_state.get("auth_session")
account = None

if session is not None:
    try:
        account = fetch_current_account(
            api_base_url=API_BASE_URL,
            access_token=session["access_token"],
        )
    except SignInRequired as error:
        return_to_login(str(error))
    except AccountRequestError as error:
        st.title("Login Service Unavailable")
        st.error(str(error))
        if st.button("Back to Login"):
            return_to_login()
        st.stop()
    else:
        demo_role = st.session_state.get("demo_role")
        if demo_role and (account["role"], account["participant_id"]) != DEMO_ACCOUNTS[demo_role]:
            return_to_login("Demo account identity changed. Please sign in again.")
        session["account"] = account


def workspace_page() -> None:
    is_wide = account["role"] in {"lab", "buyer", "breeder"}

    if is_wide:
        st.set_page_config(layout="wide")

    with st.container(horizontal_alignment="center"):
        with st.container(
            width=1100 if is_wide else "stretch",
            key="role_workspace",
        ):
            render_demo_navigation()
            render_workspace(
                api_base_url=API_BASE_URL,
                account=account,
                access_token=session["access_token"],
            )


if account is not None:
    page = st.Page(workspace_page, title="Workspace", default=True)
elif st.session_state.get("auth_view") == "register":
    page = st.Page(
        "pages/1_User_Registration.py", title="User Registration", default=True
    )
else:
    page = st.Page(render_login_page, title="Login", default=True)

try:
    st.navigation([page], position="hidden").run()
except SignInRequired as error:
    return_to_login(str(error))
