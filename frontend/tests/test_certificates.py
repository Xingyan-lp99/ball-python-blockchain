import io
import unittest
from unittest.mock import Mock, patch
from pathlib import Path

from streamlit.testing.v1 import AppTest

from certificate_page import upload_v1, verify_v1, verify_stored_v1, api_error

APP_PATH = Path(__file__).resolve().parents[1] / "main.py"
CERTIFICATE = {
    "certificate_id": "TEST-C001", "snake_id": "TEST-S001", "lab_id": "LAB001",
    "lab_name": "TEST ONLY Laboratory", "issuer_address": "0x" + "72" * 20,
    "version": 1, "sha256": "ab" * 32,
    "issuance": {"status": "confirmed", "chain_check": "verified", "transaction_hash": "0x" + "34" * 32},
}


class CertificatePageTests(unittest.TestCase):
    def fake_get(self, url, **kwargs):
        if "/snakes/" in url and url.endswith("/certificates"):
            return Mock(status_code=200, json=lambda: [CERTIFICATE])
        if "/snakes/" in url:
            return Mock(status_code=200, json=lambda: {"snake_id": "TEST-S001", "name": "TEST ONLY"})
        if url.endswith("/file"):
            return Mock(status_code=200, content=self.document().getvalue())
        return Mock(status_code=200, json=lambda: CERTIFICATE)

    def buyer_profile(self):
        app = AppTest.from_file(str(APP_PATH), default_timeout=15).run()
        app.radio[0].set_value("Buyer").run()
        app.text_input[0].set_value("TEST-S001")
        next(button for button in app.button if button.label == "查询球蟒档案").click().run()
        return app

    def document(self):
        document = io.BytesIO(b"%PDF-1.4 TEST ONLY original bytes\n%%EOF\n")
        document.name = "renamed-test.pdf"
        return document

    def test_upload_preserves_bytes_and_cannot_select_wallet(self):
        document = self.document()
        with patch("requests.post", return_value=Mock(status_code=201)) as post:
            upload_v1("http://test", "TEST-C001", "TEST-S001", document)
        self.assertEqual(post.call_args.kwargs["data"], {"certificate_id": "TEST-C001", "snake_id": "TEST-S001"})
        self.assertEqual(post.call_args.kwargs["files"]["file"][1], document.getvalue())
        self.assertNotIn("sha256", post.call_args.kwargs["data"])

    def test_verification_sends_independent_bytes_only(self):
        document = self.document()
        with patch("requests.post", return_value=Mock(status_code=200)) as post:
            verify_v1("http://test", "TEST-C001", document)
        self.assertTrue(post.call_args.args[0].endswith("/TEST-C001/versions/1/verification"))
        self.assertNotIn("data", post.call_args.kwargs)
        self.assertEqual(post.call_args.kwargs["files"]["file"][1], document.getvalue())

    def test_lab_workspace_labels_demo_and_has_no_authorization_control(self):
        app = AppTest.from_file(str(APP_PATH)).run()
        app.radio[0].set_value("Laboratory").run()
        self.assertFalse(app.exception)
        self.assertTrue(any("not authentication" in item.value for item in app.warning))
        self.assertTrue(any(item.label == "Save original V1 PDF" for item in app.button))
        self.assertFalse(any("Authorize" in item.label for item in app.button))

    def test_buyer_selected_target_and_lifecycle_limits(self):
        with patch("requests.get", side_effect=self.fake_get):
            app = self.buyer_profile()
            self.assertFalse(app.exception)
            self.assertTrue(any("Latest-version and revocation checks are not implemented" in item.value for item in app.caption))
            self.assertTrue(any("not certify every fact" in item.value for item in app.caption))
            self.assertFalse(any("matches this registered" in item.value for item in app.success))
            self.assertEqual(app.selectbox[0].value, "TEST-C001")
            self.assertTrue(any(button.label == "核验证书" for button in app.button))
            self.assertFalse(app.expander[0].proto.expanded)

    def test_file_result_displays_three_distinct_outcomes(self):
        # Run the display with AppTest; no cached file result is used by the page.
        for outcome, phrase in [("match", "matches"), ("mismatch", "differs"), ("unable_to_verify", "Unable to verify")]:
            code = f'''from certificate_page import show_file_result
show_file_result({{"file_result": {outcome!r}, "message": "TEST ONLY", "registration": {{"status": "processing"}}}})
'''
            app = AppTest.from_string(code).run()
            self.assertFalse(app.exception)
            values = [item.value for item in app.success] + [item.value for item in app.warning]
            self.assertTrue(any(phrase in value for value in values))

    def test_buyer_does_not_reuse_confirmation_after_rpc_error(self):
        with patch("requests.get", return_value=Mock(status_code=503)):
            app = self.buyer_profile()
            self.assertFalse(app.exception)
            self.assertFalse(app.success)

    def test_primary_verification_needs_no_upload(self):
        result = {"file_source": "platform", "file_result": "match", "message": "TEST ONLY", "registration": CERTIFICATE["issuance"]}
        with patch("requests.get", side_effect=self.fake_get), patch("requests.post", return_value=Mock(status_code=200, json=lambda: result)) as post:
            app = self.buyer_profile()
            next(button for button in app.button if button.label == "核验证书").click().run()
            self.assertFalse(app.exception)
            self.assertTrue(post.call_args.args[0].endswith("/TEST-C001/versions/1/verification/stored"))
            self.assertEqual(post.call_args.kwargs["json"], {})
            self.assertNotIn("files", post.call_args.kwargs)
            self.assertTrue(any("平台保存的 PDF" in item.value and "matches" in item.value for item in app.success))

    def test_primary_transport_cannot_choose_bytes_or_signer(self):
        with patch("requests.post", return_value=Mock(status_code=200)) as post:
            verify_stored_v1("http://test", "TEST-C001")
        self.assertEqual(post.call_args.kwargs["json"], {})
        self.assertNotIn("files", post.call_args.kwargs)

    def test_no_certificates_has_no_verification_target(self):
        def no_certificates(url, **kwargs):
            if url.endswith("/snakes/TEST-S001/certificates"):
                return Mock(status_code=200, json=lambda: [])
            return self.fake_get(url, **kwargs)
        with patch("requests.get", side_effect=no_certificates):
            app = self.buyer_profile()
            self.assertFalse(app.exception)
            self.assertFalse(any(button.label == "核验证书" for button in app.button))

    def test_preview_is_selected_platform_pdf(self):
        with patch("requests.get", side_effect=self.fake_get):
            app = self.buyer_profile()
            next(button for button in app.button if button.label == "预览证书 PDF").click().run()
            self.assertFalse(app.exception)

    def test_structured_api_conflict_displays_the_specific_cause(self):
        response = Mock(status_code=409, json=lambda: {"detail": {
            "code": "snake_not_registered", "message": "BP-S001 is not registered in the referenced SnakeRegistry",
        }})
        with patch("certificate_page.st.error") as show_error:
            api_error(response)
        message = show_error.call_args.args[0]
        self.assertIn("BP-S001", message)
        self.assertIn("snake_not_registered", message)

    def test_lab_refresh_explains_unsubmitted_preflight_and_prevents_issue(self):
        certificate = {**CERTIFICATE, "issuance": {
            "status": "not_submitted", "chain_check": "verified", "transaction_hash": None,
            "error_code": "snake_not_registered", "error": "BP-S001 is not registered; complete its Breeder chain registration first",
        }}
        def get(url, **kwargs):
            if url.endswith("/file"):
                return self.fake_get(url, **kwargs)
            return Mock(status_code=200, json=lambda: certificate)
        with patch("requests.get", side_effect=get):
            app = AppTest.from_file(str(APP_PATH), default_timeout=15).run()
            app.radio[0].set_value("Laboratory").run()
            app.text_input[2].set_value("TEST-C001")
            next(button for button in app.button if button.label == "Select certificate V1").click().run()
            self.assertFalse(app.exception)
            self.assertTrue(any("snake_not_registered" in item.value and "BP-S001" in item.value for item in app.warning))
            self.assertTrue(next(button for button in app.button if button.label == "Issue selected V1 on local chain").disabled)
            certificate["issuance"] = {"status": "not_submitted", "chain_check": "verified", "transaction_hash": None}
            next(button for button in app.button if button.label == "Refresh selected certificate status").click().run()
            self.assertFalse(app.exception)
            self.assertFalse(next(button for button in app.button if button.label == "Issue selected V1 on local chain").disabled)


if __name__ == "__main__":
    unittest.main()
