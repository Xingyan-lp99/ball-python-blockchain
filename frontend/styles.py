import base64
from pathlib import Path

import streamlit as st


# Purpose: centralize shared visual values and component styles.
# Workflow: load after page configuration, before rendering any page.
# Without this function, the custom cards and button styles are not applied.
def apply_styles() -> None:
    font_data = base64.b64encode(
        (Path(__file__).parent / "assets/fonts/Manrope[wght].ttf").read_bytes()
    ).decode("ascii")
    st.html(
        f"""
        <style>
        @font-face {{
            font-family: "Manrope";
            src: url("data:font/ttf;base64,{font_data}") format("truetype");
            font-style: normal;
            font-weight: 200 800;
            font-display: swap;
        }}
        .st-key-workspace_header [data-testid="stImage"] img {{
            width: 280px !important;
            height: auto !important;
            object-fit: contain;
            flex: 0 0 auto;
        }}

        .st-key-login_intro [data-testid="stImage"] img {{
            width: 360px !important;
            max-width: 100%;
            height: auto !important;
            object-fit: contain;
        }}

        .st-key-login_intro hr {{
            margin: 12px 0 24px;
        }}

        .st-key-login_snake_showcase {{
            flex: 0 0 auto;
            grid-auto-rows: 160px;
        }}

        [class*="st-key-login_photo_slot_"] {{
            position: relative;
            height: 160px;
            min-height: 0;
            box-sizing: border-box;
            padding: 6px;
            background-color: var(--registry-surface);
            border: var(--registry-border);
        }}

        [class*="st-key-login_photo_slot_"] img {{
            position: absolute;
            inset: 6px;
            width: calc(100% - 12px);
            height: calc(100% - 12px);
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
            font-family: "Space Grotesk", sans-serif;
            font-weight: 400;
            font-synthesis: none;
            line-height: 1.2;
            letter-spacing: normal;
            word-spacing: normal;
        }}

        .st-key-login_gallery_column h1 {{
            font-family: "Manrope", sans-serif;
            font-weight: 700;
            font-size: clamp(1.875rem, 2.4vw, 2.125rem);
            color: #243B30;
            line-height: 1.15;
            white-space: nowrap;
            margin: 0;
            padding: 0;
        }}

        .st-key-login_card h3 {{
            font-size: 1.75rem;
            font-weight: 700;
            margin: 0;
            padding: 0;
        }}

        .st-key-login_marketing_copy {{
            padding-top: 24px;
        }}

        .st-key-login_card [data-testid="stForm"] {{
            padding: 0;
            border: 0;
            box-shadow: none;
        }}

        .st-key-login_card hr {{
            margin: 8px 0;
        }}

        .st-key-login_card [data-testid="stTextInput"] input {{
            min-height: 44px;
        }}

        .st-key-login_card .st-key-enter_demo button:not(:disabled) {{
            background: #E7F0E7;
            color: #243B30;
            border: 1px solid #D9E5DA;
        }}

        .st-key-login_card .st-key-enter_demo button p {{
            color: inherit;
        }}

        .st-key-role_workspace h3,
        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections) [role="tab"],
        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections) [role="tab"] p {{
            font-family: "Space Grotesk", sans-serif;
            font-weight: 400;
            font-synthesis: none;
            line-height: 1.25;
            color: var(--registry-on-surface);
        }}

        .st-key-role_workspace h3 {{
            font-size: 1.5rem;
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections) [role="tab"] {{
            font-size: 1rem;
            background-color: var(--registry-surface);
            border: var(--registry-border);
            border-radius: var(--registry-radius);
            min-height: 44px;
            padding: 0.5rem 1.25rem;
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections) [role="tab"] p {{
            font-size: 1rem;
        }}

        :is(.st-key-lab_certificate_workspace, .st-key-buyer_profile_sections)
            [role="tab"][aria-selected="true"] {{
            background-color: var(--registry-secondary-hover);
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
            color: #243B30;
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
            background-color: rgba(53, 107, 85, 0.95) !important;
            color: #FFFFFF !important;
        }}

        .st-key-buyer_snake_card_frame_0 .st-key-buyer_snake_card_0 button:focus-visible p,
        .st-key-buyer_snake_card_frame_1 .st-key-buyer_snake_card_1 button:focus-visible p,
        .st-key-buyer_snake_card_frame_2 .st-key-buyer_snake_card_2 button:focus-visible p {{
            color: #FFFFFF !important;
        }}

        @media (max-width: 640px) {{
            .st-key-login_gallery_column h1 {{
                white-space: normal;
                font-size: clamp(1.75rem, 6vw, 2.375rem);
            }}
            .st-key-workspace_header [data-testid="stImage"] img {{
                width: 190px !important;
            }}

            .st-key-login_intro [data-testid="stImage"] img {{
                width: 280px !important;
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
            /* Project-specific semantic tokens for the pet record interface. */
            --registry-surface: #FFFFFF;
            --registry-on-surface: #243B30;
            --registry-muted-text: #60796A;
            --registry-outline: #D9E5DA;

            --registry-action: #356B55;
            --registry-on-action: #FFFFFF;
            --registry-secondary-hover: #E7F0E7;
            --registry-focus: #356B55;

            --registry-border: 1px solid var(--registry-outline);
            --registry-radius: 12px;
            --registry-shadow: none;
            --registry-card-shadow: var(--registry-shadow);
            --registry-shadow-hover: none;

            --registry-card-padding: 1.5rem;
            --registry-small-gap: 0.5rem;
        }

        :is(.st-key-view_profile, .st-key-register_snake, [class*="st-key-download_certificate_"], .st-key-sign_in, .st-key-open_account_registration,
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

        :is(.st-key-view_profile, .st-key-register_snake, [class*="st-key-download_certificate_"], .st-key-sign_in, .st-key-register_account) button {
            background-color: var(--registry-action);
            color: var(--registry-on-action);
        }

        :is(.st-key-view_profile, .st-key-register_snake, [class*="st-key-download_certificate_"], .st-key-sign_in, .st-key-open_account_registration,
            .st-key-register_account, .st-key-registration_back_to_login,
            .st-key-registered_back_to_login, .st-key-account_sign_out) button p {
            color: inherit;
        }

        :is(.st-key-view_profile, .st-key-register_snake, [class*="st-key-download_certificate_"], .st-key-sign_in, .st-key-open_account_registration,
            .st-key-register_account, .st-key-registration_back_to_login,
            .st-key-registered_back_to_login, .st-key-account_sign_out)
            button:hover:not(:disabled) {
            color: var(--registry-on-surface);
            border-color: var(--registry-outline);
            box-shadow: var(--registry-shadow-hover);
        }

        :is(.st-key-view_profile, .st-key-register_snake, [class*="st-key-download_certificate_"], .st-key-sign_in, .st-key-register_account)
            button:hover:not(:disabled) {
            background-color: var(--registry-action);
            color: var(--registry-on-action);
        }

        :is(.st-key-open_account_registration, .st-key-registration_back_to_login,
            .st-key-registered_back_to_login, .st-key-account_sign_out)
            button:hover:not(:disabled) {
            background-color: var(--registry-secondary-hover);
        }

        :is(.st-key-view_profile, .st-key-register_snake, [class*="st-key-download_certificate_"], .st-key-sign_in, .st-key-open_account_registration,
            .st-key-register_account, .st-key-registration_back_to_login,
            .st-key-registered_back_to_login, .st-key-account_sign_out)
            button:focus-visible {
            outline: 3px solid var(--registry-focus);
            outline-offset: 5px;
        }

        :is(.st-key-view_profile, .st-key-register_snake, [class*="st-key-download_certificate_"], .st-key-sign_in, .st-key-open_account_registration,
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
            color: #243B30;
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
            color: #60796A;
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

    st.html(
        """
        <style>
        .st-key-snake_profile_card .profile-section-title {
            font-family: "Space Grotesk", sans-serif;
            font-size: 20px;
            font-weight: 600;
            color: #243B30;
            margin-bottom: 16px;
        }
        .st-key-snake_profile_card .profile-field-label {
            font-family: "Space Grotesk", sans-serif;
            font-size: 16px;
            font-weight: 600;
            color: #356B55;
            margin-top: 16px;
            margin-bottom: 4px;
        }
        </style>
        """
    )

    st.html("""
    <style>
    .pet-brand { font-family: "Space Grotesk", sans-serif; font-size: clamp(1.25rem, 2.5vw, 1.8rem); font-weight: 700; color: #243B30; line-height: 1.25; }
    .pet-brand-subtitle { color: #60796A; font-size: .85rem; margin-top: .4rem; }
    .st-key-demo_navigation { padding: 1rem 0; max-width: 1100px; margin: auto; }
    .st-key-demo_navigation [data-testid="stCaptionContainer"] { background: #F5E7B5; border-radius: 8px; padding: .4rem .75rem; width: fit-content; }
    .st-key-snake_profile_card [data-testid="stImage"] img { width: 100%; max-height: 360px; object-fit: contain; border-radius: 12px; background: #F7F9F5; }
    [class*="st-key-login_photo_slot_"] { border-radius: 10px; }
    [data-testid="stForm"] { border: 1px solid #D9E5DA; border-radius: 12px; background: #FFFFFF; padding: 1.25rem; }
    [data-testid="stFileUploaderDropzone"] { border: 1px dashed #60796A; border-radius: 12px; background: #F7F9F5; }
    [data-testid="stTable"], [data-testid="stDataFrame"] { border-radius: 8px; }
    button:focus-visible, input:focus-visible, textarea:focus-visible { outline: 3px solid #356B55; outline-offset: 3px; }
    [data-testid="stBaseButton-primary"] { background: #356B55; color: white; }
    [data-testid="stBaseButton-primary"] p { color: inherit; }
    .st-key-demo_role_picker [aria-pressed="true"] { background: #E7F0E7; color: #243B30; }
    [data-testid="stAlert"][data-baseweb="notification"] { border-radius: 8px; }
    code, pre { font-family: ui-monospace, Consolas, monospace; }
    </style>
    """)
