from unittest.mock import patch

from streamlit.testing.v1 import AppTest


def test_history_has_download_for_every_version_without_selector():
    versions = [
        {"version_id": f"v{number}", "version_number": number, "issued_at": None,
         "status": "current" if number == 2 else "superseded", "evidence_status": "confirmed"}
        for number in (1, 2)
    ]
    history = {"chain_block_number": 5, "warnings": [], "series": [
        {"laboratory_id": "LAB001", "title": "Genetic report", "series_id": "report", "versions": versions}
    ]}
    with patch("frontend.certificates.fetch_certificate_history", return_value=history), patch("frontend.certificates.fetch_certificate_pdf", return_value=b"%PDF-1.4\n") as download:
        at = AppTest.from_string("""
from frontend.certificates import render_certificate_history
render_certificate_history(api_base_url='http://unused',snake_id='PREVIEW',access_token='preview-only')
""").run()
        assert not at.exception
        assert not at.selectbox and not at.expander
        assert len(at.get("download_button")) == 2
        assert download.call_count == 2
        assert not any("chain block" in caption.value for caption in at.caption)


def test_same_title_reports_are_separate_revision_choices():
    reports = [
        {"series_id": f"series-{i}", "snake_id": "PREVIEW", "title": "Same title",
         "laboratory_id": "LAB001", "latest_version_number": i}
        for i in (1, 2)
    ]
    with patch("frontend.certificates.fetch_laboratory_reports", return_value=reports), patch("frontend.certificates.submit_certificate_revision") as submit:
        at = AppTest.from_string("""
from frontend.certificates import _render_certificate_revision
_render_certificate_revision(api_base_url='http://unused',account={'participant_id':'LAB001'},access_token='preview-only')
""").run()
        assert not at.exception and not at.text_input
        selector = at.selectbox[0]
        assert selector.label == "Report Title *" and selector.value is None
        assert len(selector.options) == 2 and selector.options[0] != selector.options[1]
        selector.select_index(1)
        next(button for button in at.button if button.label == "Issue Revision").click().run()
        assert not at.exception and at.selectbox[0].value == "series-2"
        assert not submit.called


def test_login_username_is_empty_with_autocomplete_off():
    at = AppTest.from_string("""
from frontend.auth import render_login_page
render_login_page()
""").run()
    assert not at.exception
    username = at.text_input(key="login_username")
    assert username.value == "" and username.proto.autocomplete == "off"


def test_uncertain_sepolia_issue_offers_hash_recovery_without_upload() -> None:
    transaction_hash = "0x" + "a" * 64
    source = f"""
import streamlit as st
from frontend.certificates import _render_original_certificate
st.session_state['certificate_issue_result_LAB001_sepolia'] = {{
    'status_code': 503,
    'payload': {{'outcome':'unverified','transaction_hash':'{transaction_hash}'}},
}}
_render_original_certificate(
    api_base_url='http://unused', account={{'participant_id':'LAB001'}},
    access_token='preview-only', network='sepolia',
)
"""
    recovered = {"status": "current", "transaction_hash": transaction_hash}
    with patch(
        "frontend.certificates.recover_sepolia_certificate_transaction",
        return_value=(201, recovered),
    ) as recover:
        app = AppTest.from_string(source).run()
        assert not app.exception
        button = next(item for item in app.button if item.label == "Verify and Sync Existing Transaction")
        button.click().run()

    assert not app.exception
    assert recover.call_args.kwargs["transaction_hash"] == transaction_hash


def test_uncertain_sepolia_revision_offers_hash_recovery() -> None:
    transaction_hash = "0x" + "b" * 64
    source = f"""
import streamlit as st
from frontend.certificates import _render_certificate_revision
st.session_state['certificate_revision_result_LAB001_sepolia'] = {{
    'status_code': 503,
    'payload': {{'outcome':'unverified','transaction_hash':'{transaction_hash}'}},
}}
_render_certificate_revision(
    api_base_url='http://unused', account={{'participant_id':'LAB001'}},
    access_token='preview-only', network='sepolia',
)
"""
    with patch("frontend.certificates.fetch_laboratory_reports", return_value=[]), patch(
        "frontend.certificates.recover_sepolia_certificate_transaction",
        return_value=(201, {"status": "current", "transaction_hash": transaction_hash}),
    ) as recover:
        app = AppTest.from_string(source).run()
        assert not app.exception
        button = next(item for item in app.button if item.label == "Verify and Sync Existing Transaction")
        button.click().run()

    assert not app.exception
    assert recover.call_args.kwargs["transaction_hash"] == transaction_hash


def test_certificate_recovery_api_uses_saved_hash_only() -> None:
    from unittest.mock import Mock

    from frontend.api import recover_sepolia_certificate_transaction

    transaction_hash = "0x" + "c" * 64
    response = Mock(status_code=200)
    response.json.return_value = {
        "transaction_hash": transaction_hash,
        "receipt_status": 1,
        "chain_id": 11155111,
        "status": "current",
        "snake_id": "BP-S004",
        "series_id": "SERIES-1",
        "version_id": "VERSION-1",
        "file_hash": "d" * 64,
        "issuer_address": "0x" + "1" * 40,
        "contract_address": "0x" + "2" * 40,
        "etherscan_url": f"https://sepolia.etherscan.io/tx/{transaction_hash}",
        "issued_at": "2026-11-26T00:00:00Z",
        "version_number": 1,
    }
    with patch("frontend.api.requests.post", return_value=response) as post:
        status, payload = recover_sepolia_certificate_transaction(
            api_base_url="http://127.0.0.1:8001",
            transaction_hash=transaction_hash,
            access_token="preview-only",
        )

    assert status == 201
    assert payload["transaction_hash"] == transaction_hash
    assert post.call_args.args[0] == "http://127.0.0.1:8001/api/v1/sepolia/certificate-transactions/recover"
    assert post.call_args.kwargs["json"] == {"transaction_hash": transaction_hash}


def test_certificate_recovery_failure_keeps_submission_locked() -> None:
    from unittest.mock import Mock

    from frontend.api import recover_sepolia_certificate_transaction

    response = Mock(status_code=404)
    response.json.return_value = {"detail": "No saved certificate checkpoint."}
    with patch("frontend.api.requests.post", return_value=response):
        status, payload = recover_sepolia_certificate_transaction(
            api_base_url="http://127.0.0.1:8001",
            transaction_hash="0x" + "e" * 64,
            access_token="preview-only",
        )

    assert status == 404
    assert payload["outcome"] == "unverified"


def test_anvil_certificate_error_does_not_show_sepolia_recovery_button() -> None:
    source = """
import streamlit as st
from frontend.certificates import _render_original_certificate
st.session_state['certificate_issue_result_LAB001_anvil'] = {
    'status_code': 503,
    'payload': {'outcome':'unverified','transaction_hash':'0x' + 'f' * 64},
}
_render_original_certificate(
    api_base_url='http://unused', account={'participant_id':'LAB001'},
    access_token='preview-only', network='anvil',
)
"""
    app = AppTest.from_string(source).run()

    assert not app.exception
    assert not any(button.label == "Verify and Sync Existing Transaction" for button in app.button)
    assert any(button.label == "Issue Certificate" for button in app.button)


def test_lab2_sepolia_security_demo_has_two_read_only_actions() -> None:
    from frontend.certificates import render_certificate_issuance

    source = """
from frontend.certificates import render_certificate_issuance
render_certificate_issuance(
    api_base_url='http://unused',
    account={'participant_id':'LAB002'},
    access_token='preview-only', network='sepolia',
)
"""
    result = {
        "network": "Sepolia Testnet", "contract": "CertificateRegistry",
        "contract_address": "0x" + "1" * 40, "pet_id": "BP-S004",
        "series_id": "SERIES-1", "simulated_caller": "0x" + "2" * 40,
        "operation": "issueCertificate(string,string,string,bytes32)",
        "authorization_status": "Unauthorized", "contract_result": "Reverted",
        "revert_reason": "Unauthorized()", "state_unchanged": "Yes",
        "read_only_notice": "Read-only eth_call. No transaction broadcast. No Gas Fee.",
        "permission_denied": True,
    }
    with patch("frontend.certificates.fetch_laboratory_reports", return_value=[]), patch(
        "frontend.certificates.run_sepolia_certificate_permission_demo",
        return_value=result,
    ) as run_demo:
        app = AppTest.from_string(source).run()
        assert not app.exception
        labels = {button.label for button in app.button}
        assert "Test Unauthorized Issuance" in labels
        assert "Test Cross-Lab Revision" in labels
        next(button for button in app.button if button.label == "Test Unauthorized Issuance").click().run()

    assert not app.exception
    assert run_demo.call_args.kwargs["operation"] == "unauthorized_issuance"
    assert any("Permission Denied" in item.value for item in app.success)


def test_anvil_certificate_workspace_has_no_sepolia_permission_buttons() -> None:
    source = """
from frontend.certificates import render_certificate_issuance
render_certificate_issuance(
    api_base_url='http://unused',
    account={'participant_id':'LAB002'},
    access_token='preview-only', network='anvil',
)
"""
    with patch("frontend.certificates.fetch_laboratory_reports", return_value=[]):
        app = AppTest.from_string(source).run()

    assert not app.exception
    labels = {button.label for button in app.button}
    assert "Test Unauthorized Issuance" not in labels
    assert "Test Cross-Lab Revision" not in labels
