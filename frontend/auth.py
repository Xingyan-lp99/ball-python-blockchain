from io import BytesIO

import streamlit as st
from PIL import Image

from frontend.branding import render_pythonpass_logo
from frontend.api import (
    AccountRequestError,
    SignInRequired,
    fetch_public_snake_showcase_images,
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


def _render_login_snake_showcase() -> None:
    if "login_snake_showcase_images" not in st.session_state:
        try:
            st.session_state["login_snake_showcase_images"] = (
                fetch_public_snake_showcase_images(api_base_url=API_BASE_URL)
            )
        except AccountRequestError:
            return

    photos = st.session_state["login_snake_showcase_images"]
    if not photos:
        return

    valid_photos = []
    photo_ratios = []
    for photo in photos:
        try:
            with Image.open(BytesIO(photo)) as image:
                photo_ratios.append(image.width / image.height)
            valid_photos.append(photo)
        except (OSError, ZeroDivisionError):
            continue

    if not photo_ratios:
        return

    photos = valid_photos
    scale_height = min(180, 508 / sum(photo_ratios))
    photo_widths = [
        max(1, int(ratio * scale_height)) for ratio in photo_ratios
    ]

    with st.container(horizontal_alignment="center"):
        with st.container(width=520, key="login_snake_showcase"):
            columns = st.columns(photo_widths, gap=None)
            for column, photo, photo_width in zip(
                columns, photos, photo_widths, strict=True
            ):
                with column:
                    st.image(
                        photo,
                        width=photo_width,
                        alt="Ball python profile photo",
                    )


# Purpose: present sign-in inside a readable, centered card.
# Workflow: authenticate before exposing any business workspace.
# Without this function, users cannot access the workspace through sign-in.
def render_login_page() -> None:
    with st.container(horizontal_alignment="center"):
        with st.container(width=520):
            with st.container(key="login_intro"):
                with st.container(horizontal_alignment="center"):
                    render_pythonpass_logo(width_px=260)
                st.markdown("**Ball Python Blockchain Registry**")
                st.title("Login")
                st.write("Sign in to open your role workspace.")

            with st.container(border=False, key="login_card"):
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
                st.write("Do not have an account?")
                if st.button(
                    "Create Account",
                    key="open_account_registration",
                    width="stretch",
                ):
                    open_registration()

            _render_login_snake_showcase()


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
