import streamlit as st


# Purpose: centralize shared visual values and component styles.
# Workflow: load after page configuration, before rendering any page.
# Without this function, the custom cards and button styles are not applied.
def apply_styles() -> None:
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
