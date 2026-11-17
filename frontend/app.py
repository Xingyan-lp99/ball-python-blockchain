import streamlit as st

from frontend.api import AccountRequestError, SignInRequired, fetch_current_account
from frontend.auth import API_BASE_URL, render_login_page, return_to_login
from frontend.styles import apply_styles
from frontend.workspace import render_workspace


st.set_page_config(page_title="Ball Python Registry")
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
        session["account"] = account


def workspace_page() -> None:
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
