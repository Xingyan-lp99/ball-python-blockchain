from unittest.mock import patch
from datetime import date
from types import SimpleNamespace

import pytest
from streamlit.testing.v1 import AppTest

from frontend.api import KeeperTransferRequestError


HUSBANDRY = """
from frontend.husbandry import render_husbandry_section
render_husbandry_section(
    api_base_url='http://unused',
    account={'role':'buyer','participant_id':'BUYER001','display_name':'Preview','username':'preview'},
    access_token='preview-only',snake_id='PREVIEW',
)
"""


@pytest.mark.parametrize("status,participant", [
    ("no_pending_transfer", "BREEDER001"),
    ("pending_acceptance", "BREEDER001"),
    ("unable_to_confirm", "BUYER001"),
    ("no_pending_transfer", None),
])
def test_nonkeeper_or_unconfirmed_account_has_no_actions(status, participant):
    state = {"transfer_status": status, "current_keeper": {"participant_id": participant} if participant else None}
    with patch("frontend.husbandry.fetch_husbandry_records", return_value=[]), patch("frontend.husbandry.fetch_keeper_transfer_status", return_value=state), patch("frontend.husbandry.create_husbandry_record") as write:
        at = AppTest.from_string(HUSBANDRY).run()
        assert not at.exception
        assert len(at.tabs) == 4 and len(at.dataframe) == 4
        assert not at.selectbox and not at.number_input and not at.date_input
        assert not any(button.label in {"Add Record", "Save Changes", "Delete Record"} for button in at.button)
        assert not write.called


def test_permission_read_failure_stays_read_only():
    with patch("frontend.husbandry.fetch_husbandry_records", return_value=[]), patch("frontend.husbandry.fetch_keeper_transfer_status", side_effect=KeeperTransferRequestError("Unavailable")):
        at = AppTest.from_string(HUSBANDRY).run()
        assert not at.exception and len(at.warning) == 1
        assert not at.selectbox and len(at.dataframe) == 4


def test_permissions_are_rechecked_after_transfer_without_writes():
    owned = {"transfer_status": "accepted", "current_keeper": {"participant_id": "BUYER001"}}
    other = {"transfer_status": "accepted", "current_keeper": {"participant_id": "BREEDER001"}}
    with patch("frontend.husbandry.fetch_husbandry_records", return_value=[]), patch("frontend.husbandry.fetch_keeper_transfer_status", return_value=owned) as keeper, patch("frontend.husbandry.create_husbandry_record") as write:
        at = AppTest.from_string(HUSBANDRY).run()
        assert not at.exception and len(at.selectbox) == 4
        keeper.return_value = other
        at.run()
        assert not at.exception and not at.selectbox
        keeper.return_value = owned
        at.run()
        assert not at.exception and len(at.selectbox) == 4
        assert not write.called


def test_registration_uses_sex_choices_without_species_input():
    source = """
from frontend.workspace import _render_snake_registration
_render_snake_registration('http://unused','preview-only')
"""
    with patch("frontend.workspace.submit_snake_registration") as submit:
        at = AppTest.from_string(source).run()
        assert not at.exception
        assert next(widget for widget in at.text_input if widget.label == "Snake ID *").value == ""
        assert not any("Species" in widget.label for widget in at.text_input)
        sex = next(widget for widget in at.selectbox if widget.label == "Sex *")
        assert sex.options == ["Male", "Female"] and sex.value is None
        assert len(at.date_input) == 1 and at.date_input[0].value is None
        assert not at.number_input
        assert not any(widget.label in {"Month", "Day", "Year"} for widget in at.selectbox)
        at.button(key="register_snake").click().run()
        assert not at.exception and at.error
        submit.assert_not_called()


def test_calendar_selection_submits_existing_iso_date_contract():
    source = """
from frontend.workspace import _render_snake_registration
_render_snake_registration('http://unused','preview-only')
"""
    photo = SimpleNamespace(name="preview.png", getvalue=lambda: b"preview-only")
    with patch("frontend.workspace.st.file_uploader", return_value=photo), patch("frontend.workspace.submit_snake_registration", return_value=(422, {"detail": "Preview only"})) as submit:
        at = AppTest.from_string(source).run()
        next(w for w in at.text_input if w.label == "Snake ID *").set_value("PREVIEW")
        next(w for w in at.selectbox if w.label == "Sex *").select("Female")
        at.date_input[0].set_value(date(2025, 3, 4))
        next(w for w in at.text_area if w.label == "Genetic Description *").set_value("Fictional preview")
        at.button(key="register_snake").click().run()
        assert not at.exception
        assert submit.call_count == 1
        assert submit.call_args.kwargs["profile"]["date_of_birth"] == "2025-03-04"
