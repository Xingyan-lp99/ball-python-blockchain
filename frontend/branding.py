from pathlib import Path

import streamlit as st


PYTHONPASS_LOGO_PATH = Path(__file__).parent / "assets" / "pythonpass-logo.png"


def render_pythonpass_logo(*, width_px: int = 280) -> None:
    st.image(
        str(PYTHONPASS_LOGO_PATH),
        width=width_px,
        alt="PythonPass",
    )
