from unittest.mock import patch

import pytest
from streamlit.testing.v1 import AppTest

@pytest.mark.parametrize("network", ["anvil", "sepolia"])
def test_demo_transfer_sends_real_buyer_username(network):
    source = f'''
import streamlit as st
from frontend.keeper_transfers import render_keeper_transfer_section
st.session_state["demo_role"] = "Seller"
render_keeper_transfer_section(
    api_base_url="http://unused", snake_id="BP-S004",
    account={{"role": "breeder", "participant_id": "BREEDER001"}},
    access_token="test-token", network={network!r},
)
'''
    state = {
        "transfer_status": "no_pending_transfer",
        "current_keeper": {
            "participant_id": "BREEDER001", "display_name": "Seller",
            "username": "spec01_breeder",
        },
    }
    with (
        patch("frontend.keeper_transfers.fetch_keeper_transfer_status", return_value=state),
        patch("frontend.keeper_transfers.submit_keeper_transfer_request", return_value=(
            201, {"status": "pending"},
        )) as submit,
    ):
        page = AppTest.from_string(source).run()
        assert not page.exception
        assert any("spec01_breeder" in item.value for item in page.markdown)
        assert page.text_input[0].label == "Buyer Username *"
        page.text_input[0].input(" core_test_buyer ")
        next(button for button in page.button if button.label == "Initiate Transfer").click().run()
        assert not page.exception
        submit.assert_called_once_with(
            api_base_url="http://unused", snake_id="BP-S004",
            recipient_username="core_test_buyer", access_token="test-token",
            network=network,
        )
