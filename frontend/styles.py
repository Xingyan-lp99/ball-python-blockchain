import base64
from pathlib import Path

import streamlit as st


# Purpose: centralize shared visual values and component styles.
# Workflow: load after page configuration, before rendering any page.
# Without this function, the custom cards and button styles are not applied.
def apply_styles() -> None:
    font_path = (
        Path(__file__).parent
        / "assets"
        / "fonts"
        / "PressStart2P-Regular.ttf"
    )
    font_data = base64.b64encode(font_path.read_bytes()).decode("ascii")
    jersey_font_data = base64.b64encode(
        (font_path.parent / "Jersey10-Regular.ttf").read_bytes()
    ).decode("ascii")

    st.html(
        f"""
        <style>
        @font-face {{
            font-family: "Press Start 2P";
            src: url("data:font/ttf;base64,{font_data}") format("truetype");
            font-style: normal;
            font-weight: 400;
            font-display: swap;
        }}

        @font-face {{
            font-family: "Jersey 10";
            src: url("data:font/ttf;base64,{jersey_font_data}") format("truetype");
            font-style: normal;
            font-weight: 400;
            font-display: swap;
        }}

        .st-key-workspace_header [data-testid="stImage"] img {{
            width: 280px !important;
            height: auto !important;
            object-fit: contain;
            flex: 0 0 auto;
        }}

        .st-key-login_intro [data-testid="stImage"] img {{
            width: 240px !important;
            max-width: 100%;
            height: auto !important;
            object-fit: contain;
        }}

        .st-key-login_intro hr {{
            margin: 8px 0 32px;
        }}

        .st-key-login_snake_showcase {{
            flex: 1;
            align-self: stretch;
            grid-auto-rows: minmax(128px, 1fr);
        }}

        [class*="st-key-login_photo_slot_"] {{
            position: relative;
            min-height: 128px;
            box-sizing: border-box;
            padding: 8px;
            background-color: var(--registry-surface);
            border: var(--registry-border);
        }}

        [class*="st-key-login_photo_slot_"] img {{
            position: absolute;
            inset: 8px;
            width: calc(100% - 16px);
            height: calc(100% - 16px);
            object-fit: contain;
        }}

        /* Keep native image wrappers from becoming the sizing reference. */
        [class*="st-key-login_photo_slot_"]
            :is([data-testid="stElementContainer"], :has(> [data-testid="stImage"])) {{
            position: static;
        }}

        [class*="st-key-login_photo_slot_"] p {{
            color: var(--registry-muted-text);
            text-align: center;
            overflow-wrap: anywhere;
        }}

        .st-key-login_gallery_column h1,
        .st-key-login_card h3 {{
            font-family: "Jersey 10", sans-serif;
            font-weight: 400;
            font-synthesis: none;
            line-height: 1.2;
            letter-spacing: normal;
            word-spacing: normal;
        }}

        .st-key-login_gallery_column h1 {{
            font-size: clamp(1.5rem, 3.5vw, 3rem);
            white-space: nowrap;
            margin: 0;
            padding: 0;
        }}

        .st-key-login_card h3 {{
            font-size: clamp(1.25rem, 2.5vw, 2rem);
        }}

        @media (max-width: 1100px) {{
            .st-key-login_layout > :has(> .st-key-login_form_column) {{
                order: -1;
            }}
        }}

        .st-key-role_workspace h3,
        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections) [role="tab"],
        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections) [role="tab"] p {{
            font-family: "Jersey 10", sans-serif;
            font-weight: 400;
            font-synthesis: none;
            line-height: 1.25;
            color: var(--registry-on-surface);
        }}

        .st-key-role_workspace h3 {{
            font-size: 2rem;
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections) [role="tab"] {{
            font-size: 1.375rem;
            background-color: var(--registry-surface);
            border: var(--registry-border);
            border-radius: var(--registry-radius);
            min-height: 44px;
            padding: 0.5rem 1.25rem;
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections) [role="tab"] p {{
            font-size: 1.375rem;
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections)
            [role="tab"][aria-selected="true"] {{
            background-color: var(--registry-action);
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections)
            [role="tab"]:hover:not([aria-selected="true"]) {{
            background-color: var(--registry-secondary-hover);
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections) [data-testid="stForm"] {{
            background-color: var(--registry-surface);
            border: var(--registry-border);
            border-radius: var(--registry-radius);
            box-shadow: var(--registry-shadow);
            padding: var(--registry-card-padding);
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections)
            :is([data-testid="stFormSubmitButton"],
                [data-testid="stFileUploader"]) button {{
            font-family: "Space Grotesk", sans-serif;
            font-size: 1rem;
            font-weight: 600;
            border-radius: var(--registry-radius);
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections)
            [data-testid="stFormSubmitButton"] button:not(:disabled) {{
            background-color: var(--registry-action);
            color: var(--registry-on-action);
            border: var(--registry-border);
            box-shadow: var(--registry-shadow);
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections)
            [data-testid="stFileUploader"] button:not(:disabled) {{
            background-color: var(--registry-surface);
            color: var(--registry-on-surface);
            border: var(--registry-border);
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections)
            :is([data-testid="stFormSubmitButton"],
                [data-testid="stFileUploader"]) button p {{
            color: inherit;
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections)
            :is([role="tab"],
                [data-testid="stFormSubmitButton"] button,
                [data-testid="stFileUploader"] button):focus-visible {{
            outline: 3px solid var(--registry-focus);
            outline-offset: 3px;
        }}

        .workspace-account {{
            display: flex;
            align-items: center;
            gap: 0.45rem;
            color: #291344;
            font-weight: 700;
            white-space: nowrap;
        }}

        .workspace-account svg {{
            width: 24px;
            height: 24px;
            flex: 0 0 auto;
        }}

        .st-key-workspace_header [data-testid="stHorizontalBlock"] {{
            flex-wrap: nowrap !important;
            align-items: center;
            gap: clamp(0.4rem, 1vw, 1rem);
            overflow-x: auto;
        }}

        .st-key-workspace_header [data-testid="stHorizontalBlock"] > div {{
            flex: 0 0 auto !important;
            min-width: max-content;
        }}

        .st-key-buyer_snake_card_frame_0,
        .st-key-buyer_snake_card_frame_1,
        .st-key-buyer_snake_card_frame_2 {{
            position: relative;
        }}

        .st-key-buyer_snake_card_frame_0 [data-testid="stImage"] img,
        .st-key-buyer_snake_card_frame_1 [data-testid="stImage"] img,
        .st-key-buyer_snake_card_frame_2 [data-testid="stImage"] img {{
            width: 100%;
            height: 180px;
            object-fit: cover;
        }}

        .st-key-buyer_snake_card_frame_0 .st-key-buyer_snake_card_0,
        .st-key-buyer_snake_card_frame_1 .st-key-buyer_snake_card_1,
        .st-key-buyer_snake_card_frame_2 .st-key-buyer_snake_card_2 {{
            position: absolute !important;
            top: 0;
            left: 0;
            right: 0;
            height: 180px;
            z-index: 2;
        }}

        .st-key-buyer_snake_card_frame_0 .st-key-buyer_snake_card_0 button,
        .st-key-buyer_snake_card_frame_1 .st-key-buyer_snake_card_1 button,
        .st-key-buyer_snake_card_frame_2 .st-key-buyer_snake_card_2 button {{
            width: 100%;
            height: 180px;
            cursor: pointer;
            color: transparent !important;
            background-color: transparent !important;
            border-color: transparent !important;
            box-shadow: none !important;
        }}

        .st-key-buyer_snake_card_frame_0 .st-key-buyer_snake_card_0 button p,
        .st-key-buyer_snake_card_frame_1 .st-key-buyer_snake_card_1 button p,
        .st-key-buyer_snake_card_frame_2 .st-key-buyer_snake_card_2 button p {{
            color: transparent !important;
        }}

        .st-key-buyer_snake_card_frame_0 .st-key-buyer_snake_card_0 button:focus-visible,
        .st-key-buyer_snake_card_frame_1 .st-key-buyer_snake_card_1 button:focus-visible,
        .st-key-buyer_snake_card_frame_2 .st-key-buyer_snake_card_2 button:focus-visible {{
            opacity: 0.95;
            background-color: rgba(41, 19, 68, 0.9) !important;
            color: #FFFDF3 !important;
        }}

        .st-key-buyer_snake_card_frame_0 .st-key-buyer_snake_card_0 button:focus-visible p,
        .st-key-buyer_snake_card_frame_1 .st-key-buyer_snake_card_1 button:focus-visible p,
        .st-key-buyer_snake_card_frame_2 .st-key-buyer_snake_card_2 button:focus-visible p {{
            color: #FFFDF3 !important;
        }}

        @media (max-width: 640px) {{
            .st-key-workspace_header [data-testid="stImage"] img {{
                width: 190px !important;
            }}

            .st-key-login_intro [data-testid="stImage"] img {{
                width: 220px !important;
            }}

            .st-key-buyer_snake_card_frame_0 [data-testid="stImage"] img,
            .st-key-buyer_snake_card_frame_1 [data-testid="stImage"] img,
            .st-key-buyer_snake_card_frame_2 [data-testid="stImage"] img,
            .st-key-buyer_snake_card_frame_0 .st-key-buyer_snake_card_0,
            .st-key-buyer_snake_card_frame_1 .st-key-buyer_snake_card_1,
            .st-key-buyer_snake_card_frame_2 .st-key-buyer_snake_card_2,
            .st-key-buyer_snake_card_frame_0 .st-key-buyer_snake_card_0 button,
            .st-key-buyer_snake_card_frame_1 .st-key-buyer_snake_card_1 button,
            .st-key-buyer_snake_card_frame_2 .st-key-buyer_snake_card_2 button {{
                height: 150px;
            }}

            .workspace-account svg {{
                width: 20px;
                height: 20px;
            }}
        }}
        </style>
        """
    )

    st.html(
        """
        <style>
        :root {
            /* Project-specific semantic tokens for the approved pixel style. */
            --registry-surface: #FFFDF3;
            --registry-on-surface: #291344;
            --registry-muted-text: #6E627D;
            --registry-outline: #6330BA;

            --registry-action: #F4EF48;
            --registry-on-action: #291344;
            --registry-secondary-hover: #E2D3FA;
            --registry-focus: #6330BA;

            --registry-border: 2px solid var(--registry-outline);
            --registry-radius: 0;
            --registry-shadow: 4px 4px 0 var(--registry-outline);
            --registry-card-shadow: var(--registry-shadow);
            --registry-shadow-hover: 2px 2px 0 var(--registry-outline);

            --registry-card-padding: 1.5rem;
            --registry-small-gap: 0.5rem;
        }

        :is(.st-key-view_profile, .st-key-sign_in, .st-key-open_account_registration,
            .st-key-register_account, .st-key-registration_back_to_login,
            .st-key-registered_back_to_login, .st-key-account_sign_out) button {
            background-color: var(--registry-surface);
            color: var(--registry-on-surface);
            border: var(--registry-border);
            border-radius: var(--registry-radius);
            box-shadow: var(--registry-shadow);
            min-height: 44px;
            padding: 0.5rem 1.25rem;
            font-weight: 700;
        }

        :is(.st-key-view_profile, .st-key-sign_in, .st-key-register_account) button {
            background-color: var(--registry-action);
            color: var(--registry-on-action);
        }

        :is(.st-key-view_profile, .st-key-sign_in, .st-key-open_account_registration,
            .st-key-register_account, .st-key-registration_back_to_login,
            .st-key-registered_back_to_login, .st-key-account_sign_out) button p {
            color: inherit;
        }

        :is(.st-key-view_profile, .st-key-sign_in, .st-key-open_account_registration,
            .st-key-register_account, .st-key-registration_back_to_login,
            .st-key-registered_back_to_login, .st-key-account_sign_out)
            button:hover:not(:disabled) {
            color: var(--registry-on-surface);
            border-color: var(--registry-outline);
            box-shadow: var(--registry-shadow-hover);
        }

        :is(.st-key-view_profile, .st-key-sign_in, .st-key-register_account)
            button:hover:not(:disabled) {
            background-color: var(--registry-action);
            color: var(--registry-on-action);
        }

        :is(.st-key-open_account_registration, .st-key-registration_back_to_login,
            .st-key-registered_back_to_login, .st-key-account_sign_out)
            button:hover:not(:disabled) {
            background-color: var(--registry-secondary-hover);
        }

        :is(.st-key-view_profile, .st-key-sign_in, .st-key-open_account_registration,
            .st-key-register_account, .st-key-registration_back_to_login,
            .st-key-registered_back_to_login, .st-key-account_sign_out)
            button:focus-visible {
            outline: 3px solid var(--registry-focus);
            outline-offset: 5px;
        }

        :is(.st-key-view_profile, .st-key-sign_in, .st-key-open_account_registration,
            .st-key-register_account, .st-key-registration_back_to_login,
            .st-key-registered_back_to_login, .st-key-account_sign_out)
            button:disabled {
            background-color: var(--registry-surface);
            color: var(--registry-muted-text);
            border-color: var(--registry-muted-text);
            box-shadow: none;
            cursor: not-allowed;
        }

        .st-key-login_card,
        .st-key-registration_card,
        .st-key-workspace_header,
        .st-key-snake_profile_card {
            box-sizing: border-box;
            background-color: var(--registry-surface);
            border: var(--registry-border);
            border-radius: var(--registry-radius);
            box-shadow: var(--registry-card-shadow);
            padding: var(--registry-card-padding);
        }

        .st-key-workspace_header h1 {
            font-size: clamp(1.5rem, 3vw, 2.5rem);
            overflow-wrap: anywhere;
        }

        .st-key-workspace_header p {
            color: var(--registry-muted-text);
            overflow-wrap: anywhere;
        }

        .st-key-login_intro h1,
        .st-key-registration_intro h1 {
            margin-bottom: var(--registry-small-gap);
        }

        .st-key-login_intro p,
        .st-key-registration_intro p {
            color: var(--registry-muted-text);
        }

        .st-key-login_card .st-key-sign_in,
        .st-key-login_card .st-key-open_account_registration,
        .st-key-registration_card .st-key-register_account,
        .st-key-registration_card .st-key-registration_back_to_login,
        .st-key-registration_card .st-key-registered_back_to_login {
            margin-bottom: var(--registry-small-gap);
        }
        </style>
        """
    )

    st.html(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            color: #291344;
            letter-spacing: normal;
            line-height: 1.5;
        }

        [data-testid="stWidgetLabel"] p {
            font-weight: 500;
        }

        [data-testid="stAppViewContainer"] button,
        [data-testid="stAppViewContainer"] button p {
            font-weight: 600;
        }

        [data-testid="stCaptionContainer"] p,
        [data-testid="stFileUploaderDropzone"] small {
            font-size: 14px;
            color: #6E627D;
            line-height: 1.5;
        }

        [data-testid="stMarkdownContainer"] p {
            line-height: 1.5;
        }

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections)
            [role="tab"],
        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections)
            [role="tab"] p {
            font-weight: 400;
            line-height: 1.25;
        }
        </style>
        """
    )
