from pathlib import Path
import json
from unittest.mock import patch

from streamlit.testing.v1 import AppTest

from frontend.auth import DEMO_ACCOUNTS

APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


def test_demo_config_requires_opt_in_and_loopback_binding(tmp_path):
    from frontend.auth import _demo_settings

    path = tmp_path / "demo.json"
    with patch("frontend.auth.DEMO_CONFIG_PATH", path), patch("frontend.auth.st.get_option", return_value="127.0.0.1"):
        assert _demo_settings() == {}
        settings = _settings()
        settings["enabled"] = False
        path.write_text(json.dumps(settings))
        assert _demo_settings() == {}
        settings["enabled"] = True
        path.write_text(json.dumps(settings))
        assert _demo_settings() == settings
        with patch("frontend.auth.st.get_option", return_value="0.0.0.0"):
            assert _demo_settings() == {}


def _account(label):
    role, participant = DEMO_ACCOUNTS[label]
    return {
        "role": role, "participant_id": participant,
        "username": label, "display_name": label,
    }


def _settings():
    return {"enabled": True, **{
        label: {"username": label, "password": "test-only-placeholder"}
        for label in DEMO_ACCOUNTS
    }}


def _session(**kwargs):
    label = kwargs["username"]
    return {"access_token": label, "account": _account(label)}


def _current(**kwargs):
    return _account(kwargs["access_token"])


def test_demo_switches_authenticated_identity_and_clears_page_state():
    rendered = []
    with (
        patch("frontend.auth._demo_settings", return_value=_settings()),
        patch("frontend.auth.sign_in_account", side_effect=_session) as login,
        patch("frontend.auth.fetch_current_account", side_effect=_current),
        patch("frontend.auth.sign_out_account") as logout,
        patch("frontend.workspace.render_workspace", side_effect=lambda **kw: rendered.append(kw)),
    ):
        # Patch the imported API too: AppTest executes app.py in its own module.
        with patch("frontend.api.fetch_current_account", side_effect=_current):
            page = AppTest.from_file(APP_PATH, default_timeout=10).run()
            page.button(key="enter_demo").click().run()
            assert not page.exception
            assert rendered[-1]["access_token"] == "Seller"
            for label in ["Buyer", "Lab 1", "Lab 2"]:
                page.session_state["saved_snake_profile"] = "previous-private-profile"
                page.session_state["unfinished_form"] = "previous-input"
                page.get("button_group")[0].set_value(label).run()
                assert not page.exception
                assert rendered[-1]["access_token"] == label
                assert rendered[-1]["account"] == _account(label)
                assert "saved_snake_profile" not in page.session_state
                assert "unfinished_form" not in page.session_state
            assert login.call_count == 4
            assert [c.kwargs["access_token"] for c in logout.call_args_list] == [
                "Seller", "Buyer", "Lab 1",
            ]
            page.button(key="exit_demo").click().run()
            assert "auth_session" not in page.session_state
            assert "demo_role" not in page.session_state
            assert logout.call_args.kwargs["access_token"] == "Lab 2"
            assert not page.exception


def test_demo_rejects_valid_session_for_wrong_participant():
    with (
        patch("frontend.auth._demo_settings", return_value=_settings()),
        patch("frontend.auth.sign_in_account", side_effect=_session),
        patch("frontend.auth.fetch_current_account", return_value=_account("Buyer")),
        patch("frontend.auth.sign_out_account") as logout,
        patch("frontend.workspace.render_workspace") as workspace,
    ):
        page = AppTest.from_file(APP_PATH, default_timeout=10).run()
        page.button(key="enter_demo").click().run()
        assert not page.exception
        assert "auth_session" not in page.session_state
        workspace.assert_not_called()
        logout.assert_called_once()
        assert any("Demo sign-in failed" in message.value for message in page.info)


def test_normal_login_and_registration_entry_remain_available():
    with (
        patch("frontend.auth._demo_settings", return_value={}),
        patch("frontend.auth.sign_in_account", side_effect=_session) as login,
        patch("frontend.api.fetch_current_account", side_effect=_current),
        patch("frontend.workspace.render_workspace") as workspace,
    ):
        page = AppTest.from_file(APP_PATH, default_timeout=10).run()
        assert page.button(key="enter_demo").disabled
        page.text_input(key="login_username").input("Buyer")
        next(w for w in page.text_input if w.label == "Password *").input("test-only-placeholder")
        page.button(key="sign_in").click().run()
        assert not page.exception
        login.assert_called_once()
        assert workspace.call_args.kwargs["account"] == _account("Buyer")
        assert "demo_role" not in page.session_state

        registration = AppTest.from_file(APP_PATH, default_timeout=10).run()
        registration.button(key="open_account_registration").click().run()
        assert not registration.exception
        assert registration.selectbox[0].options == ["Buyer", "Seller"]
