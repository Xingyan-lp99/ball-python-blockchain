from pathlib import Path

import streamlit as st
from PIL import Image


IMAGE_DIRECTORY = Path(__file__).resolve().parent / "assets"

LOGIN_IMAGES = (
    "pet-1.png",
    "pet-2.png",
    "pet-3.png",
    "pet-4.png",
    "pet-5.png",
    "pet-6.webp",
)


# Purpose: display six independently configured, original photos.
# Workflow: present the welcome page without querying or changing business data.
# Without this function, the six slots and missing-file guidance are unavailable.
def render_login_gallery() -> None:
    with st.grid(
        columns=3,
        min_column_width=80,
        wrap=True,
        gap=14,
        row_height=160,
        height="content",
        key="login_snake_showcase",
    ):
        for index, filename in enumerate(LOGIN_IMAGES):
            path = IMAGE_DIRECTORY / filename

            with st.container(
                key=f"login_photo_slot_{index}",
                height="stretch",
                border=False,
                vertical_alignment="center",
            ):
                try:
                    with Image.open(path) as image:
                        image.verify()

                    st.image(
                        path,
                        width="stretch",
                        alt=f"Pet showcase photo {index + 1}",
                    )
                except (OSError, SyntaxError):
                    st.caption("Image unavailable")
                    st.caption(f"frontend/assets/{filename}")
