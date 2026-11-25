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
