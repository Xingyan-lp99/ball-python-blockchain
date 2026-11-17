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

        .st-key-workspace_header [data-testid="stImage"] img {{
            width: 280px !important;
            height: auto !important;
            object-fit: contain;
            flex: 0 0 auto;
        }}

        .st-key-login_intro [data-testid="stImage"] img {{
            width: 260px !important;
            height: auto !important;
            object-fit: contain;
        }}

        .st-key-login_snake_showcase [data-testid="stImage"] {{
            display: table;
            width: fit-content !important;
            border: 2px solid #291344;
            box-shadow: 3px 3px 0 #291344;
            line-height: 0;
            margin: 0 auto;
        }}

        .st-key-login_snake_showcase {{
            width: min(520px, 100%) !important;
            max-width: 100%;
        }}

        .st-key-login_snake_showcase [data-testid="stImage"] img {{
            display: block;
            width: auto;
            height: auto;
            max-width: 100%;
        }}

        .st-key-lab_certificate_workspace h3 {{
            color: #291344;
            font-family: "Press Start 2P", monospace;
            font-size: 0.9rem;
            line-height: 1.8;
        }}

        .st-key-lab_certificate_workspace [role="tab"],
        .st-key-lab_certificate_workspace [role="tab"] *,
        .st-key-lab_certificate_workspace [data-baseweb="tab"],
        .st-key-lab_certificate_workspace [data-baseweb="tab"] * {{
            color: #291344 !important;
            font-family: "Press Start 2P", monospace !important;
            font-size: 9px;
            line-height: 1.8;
        }}

        .st-key-lab_certificate_workspace [role="tab"],
        .st-key-lab_certificate_workspace [data-baseweb="tab"] {{
            background-color: #F4EF48 !important;
            border: 2px solid #291344 !important;
            border-radius: 0 !important;
            box-shadow: 4px 4px 0 #291344 !important;
            min-height: 44px;
            padding: 0.5rem 1.25rem;
        }}

        .st-key-lab_certificate_workspace [role="tab"]:hover,
        .st-key-lab_certificate_workspace [data-baseweb="tab"]:hover {{
            box-shadow: 2px 2px 0 #291344 !important;
            transform: translate(2px, 2px);
        }}

        .st-key-lab_certificate_workspace [role="tab"]:focus-visible,
        .st-key-lab_certificate_workspace [data-baseweb="tab"]:focus-visible {{
            outline: 3px solid #6330BA;
            outline-offset: 4px;
        }}

        .st-key-lab_certificate_workspace [data-testid="stFormSubmitButton"] button:not(:disabled),
        .st-key-lab_certificate_workspace [data-testid="stFileUploader"] button:not(:disabled),
        .st-key-lab_certificate_workspace [data-testid="stFileUploaderDropzone"] button:not(:disabled) {{
            background-color: #F4EF48 !important;
            color: #291344 !important;
            border: 2px solid #291344 !important;
            border-radius: 0 !important;
            box-shadow: 4px 4px 0 #291344 !important;
            font-family: "Press Start 2P", monospace !important;
            font-size: 7px !important;
        }}

        .st-key-lab_certificate_workspace [data-testid="stFormSubmitButton"] button:not(:disabled):hover,
        .st-key-lab_certificate_workspace [data-testid="stFileUploader"] button:not(:disabled):hover,
        .st-key-lab_certificate_workspace [data-testid="stFileUploaderDropzone"] button:not(:disabled):hover {{
            box-shadow: 2px 2px 0 #291344 !important;
            transform: translate(2px, 2px);
        }}

        .st-key-lab_certificate_workspace [data-testid="stFormSubmitButton"] button:focus-visible,
        .st-key-lab_certificate_workspace [data-testid="stFileUploader"] button:focus-visible,
        .st-key-lab_certificate_workspace [data-testid="stFileUploaderDropzone"] button:focus-visible {{
            outline: 3px solid #6330BA;
            outline-offset: 4px;
        }}

        .st-key-certificate_issue_form_frame [data-testid="stForm"] {{
            background-color: #6330BA;
            border: 2px solid #291344;
            border-radius: 0;
            box-shadow: 4px 4px 0 #291344;
            padding: 1.5rem;
        }}

        .st-key-certificate_issue_form_frame [data-testid="stWidgetLabel"] *,
        .st-key-certificate_issue_form_frame [data-testid="stWidgetLabel"] {{
            color: #FFFDF3 !important;
            font-family: "Press Start 2P", monospace !important;
            font-size: 14px !important;
            line-height: 1.8;
        }}

        .st-key-certificate_issue_form_frame [data-testid="stCaptionContainer"],
        .st-key-certificate_issue_form_frame [data-testid="stCaptionContainer"] * {{
            color: #FFFDF3 !important;
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
            --registry-outline: #291344;

            --registry-action: #F4EF48;
            --registry-on-action: #291344;
            --registry-secondary-hover: #E2D3FA;
            --registry-focus: #6330BA;

            --registry-border: 2px solid var(--registry-outline);
            --registry-radius: 0;
            --registry-shadow: 4px 4px 0 var(--registry-outline);
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
            box-shadow: var(--registry-shadow);
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
