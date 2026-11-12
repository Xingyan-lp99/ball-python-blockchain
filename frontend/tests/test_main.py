"""Run using the existing frontend environment: python -m unittest discover -s tests."""

import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import requests
from streamlit.testing.v1 import AppTest

APP_PATH = Path(__file__).resolve().parents[1] / "main.py"
PROFILE = {
    "snake_id": "S001", "name": None, "sex": "unknown", "date_of_birth": None,
    "breeder_internal_id": None, "morph_description": None,
    "breeder_id": "BR001", "current_manager_id": "BR001",
    "created_at": "2026-11-12T00:00:00Z",
    "registration_status": "not_submitted", "certificate_status": "not_verified",
}


class RegistrationPageTests(unittest.TestCase):
    def chain_profile(self, status="confirmed", check="verified"):
        return {
            **PROFILE, "registration_status": status,
            "chain_registration": {
                "status": status, "chain_check": check, "recorded_status": "confirmed",
                "transaction_hash": "0x" + "ab" * 32, "manager_address": "0x" + "11" * 20,
                "chain_id": 31337, "contract_address": "0x" + "22" * 20,
                "block_number": 2,
            },
        }

    def test_submit_local_chain_registration(self):
        registration = self.chain_profile()["chain_registration"]
        with patch("requests.post", side_effect=[
            Mock(status_code=201, json=lambda: dict(PROFILE)),
            Mock(status_code=200, json=lambda: registration),
        ]) as post:
            app = AppTest.from_file(str(APP_PATH)).run()
            app.text_input[0].set_value("S001")
            app.button[1].click().run()
            next(button for button in app.button if button.label == "Submit local-chain registration").click().run()
            self.assertFalse(app.exception)
            self.assertEqual(post.call_args.kwargs["json"], {})
            self.assertTrue(post.call_args.args[0].endswith("/S001/registration"))
            self.assertTrue(any("Confirmed on the current local" in item.value for item in app.success))
            self.assertTrue(any("not been certified" in item.value for item in app.caption))

    def test_pending_profile_does_not_show_confirmation(self):
        profile = self.chain_profile("processing")
        with patch("requests.get", return_value=Mock(status_code=200, json=lambda: profile)):
            app = AppTest.from_file(str(APP_PATH)).run()
            app.text_input[3].set_value("S001")
            app.button[2].click().run()
            self.assertFalse(app.exception)
            self.assertFalse(app.success)
            submit = next(button for button in app.button if button.label == "Submit local-chain registration")
            self.assertTrue(submit.disabled)

    def test_stale_history_does_not_show_confirmation(self):
        profile = self.chain_profile("failed", "stale")
        with patch("requests.get", return_value=Mock(status_code=200, json=lambda: profile)):
            app = AppTest.from_file(str(APP_PATH)).run()
            app.text_input[3].set_value("S001")
            app.button[2].click().run()
            self.assertFalse(app.success)
            self.assertTrue(any("historical chain evidence is stale" in item.value for item in app.error))
            self.assertTrue(next(button for button in app.button if button.label == "Submit local-chain registration").disabled)

    def test_rpc_failure_removes_cached_success(self):
        profile = self.chain_profile()
        with patch("requests.get", side_effect=[
            Mock(status_code=200, json=lambda: profile), requests.ConnectionError(),
        ]):
            app = AppTest.from_file(str(APP_PATH)).run()
            app.text_input[3].set_value("S001")
            app.button[2].click().run()
            self.assertFalse(app.success)
            self.assertTrue(any("historical success is not current" in item.value for item in app.warning))

    def test_submit_timeout_is_processing(self):
        with patch("requests.post", side_effect=[
            Mock(status_code=201, json=lambda: dict(PROFILE)), requests.Timeout(),
        ]):
            app = AppTest.from_file(str(APP_PATH)).run()
            app.text_input[0].set_value("S001")
            app.button[1].click().run()
            next(button for button in app.button if button.label == "Submit local-chain registration").click().run()
            self.assertFalse(app.exception)
            self.assertTrue(any("timeout is not proof of failure" in item.value for item in app.warning))

    def test_registration_uses_api_and_displays_saved_profile(self):
        with patch("requests.post", return_value=Mock(status_code=201, json=lambda: dict(PROFILE))) as post:
            app = AppTest.from_file(str(APP_PATH)).run()
            app.text_input[0].set_value("S001")
            app.button[1].click().run()
            self.assertFalse(app.exception)
            self.assertEqual(post.call_args.kwargs["json"]["snake_id"], "S001")
            self.assertNotIn("breeder_id", post.call_args.kwargs["json"])
            self.assertTrue(app.success)
            self.assertTrue(app.json)
            self.assertIn("not been submitted", app.info[0].value)
            self.assertIn("BR001", app.warning[0].value)

    def test_duplicate_error(self):
        with patch("requests.post", return_value=Mock(status_code=409)):
            app = AppTest.from_file(str(APP_PATH)).run()
            app.text_input[0].set_value("S001")
            app.button[1].click().run()
            self.assertFalse(app.exception)
            self.assertIn("already registered", app.error[0].value)

    def test_query_saved_profile(self):
        with patch("requests.get", return_value=Mock(status_code=200, json=lambda: dict(PROFILE))) as get:
            app = AppTest.from_file(str(APP_PATH)).run()
            app.text_input[3].set_value("S001")
            app.button[2].click().run()
            self.assertFalse(app.exception)
            self.assertTrue(get.call_args.args[0].endswith("/api/v1/snakes/S001"))
            self.assertTrue(app.json)

    def test_query_missing_profile(self):
        with patch("requests.get", return_value=Mock(status_code=404)):
            app = AppTest.from_file(str(APP_PATH)).run()
            app.text_input[3].set_value("missing")
            app.button[2].click().run()
            self.assertIn("not found", app.error[0].value)

    def test_registration_network_failure(self):
        with patch("requests.post", side_effect=requests.ConnectionError()):
            app = AppTest.from_file(str(APP_PATH)).run()
            app.text_input[0].set_value("S001")
            app.button[1].click().run()
            self.assertFalse(app.exception)
            self.assertIn("Query the snake ID before retrying", app.error[0].value)


if __name__ == "__main__":
    unittest.main()
