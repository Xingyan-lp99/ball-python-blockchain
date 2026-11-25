from pathlib import Path

import streamlit as st


PYTHONPASS_LOGO_PATH = Path(__file__).parent / "assets" / "Pet Lifetime Records Logo.png"


def render_pythonpass_logo(*, width_px: int = 280) -> None:
    st.image(str(PYTHONPASS_LOGO_PATH), width=width_px, alt="Pet Lifetime Records")
