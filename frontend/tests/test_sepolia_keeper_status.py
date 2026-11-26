from unittest.mock import Mock, patch

from streamlit.testing.v1 import AppTest

from frontend.api import fetch_keeper_transfer_status


SELLER = "0x53c31f84Ea3F2b0A1c856a30ab519b8c8Dc55a57"
STATUS = {
    "snake_id": "BP-S004",
    "current_keeper": {
        "participant_id": "BREEDER001",
        "display_name": "Seller",
        "username": "seller",
        "wallet_address": SELLER,
    },
    "transfer_status": "no_pending_transfer",
    "transfer_id": None,
    "from_participant": None,
    "to_participant": None,
    "initiated_at": None,
    "resolved_at": None,
    "transaction_hash": None,
    "transaction_status": None,
    "chain_block_number": 12_212_316,
    "detail": None,
    "etherscan_url": None,
}


def test_sepolia_keeper_api_uses_sepolia_route_and_validates_payload() -> None:
    response = Mock(status_code=200)
    response.json.return_value = STATUS
    with patch("frontend.api.requests.get", return_value=response) as get:
        result = fetch_keeper_transfer_status(
            api_base_url="http://127.0.0.1:8001",
            snake_id="BP-S004",
            access_token="preview-only",
            network="sepolia",
        )

    assert get.call_args.args[0] == "http://127.0.0.1:8001/api/v1/sepolia/snakes/BP-S004/keeper"
    assert result["current_keeper"]["wallet_address"] == SELLER
    assert result["transfer_status"] == "no_pending_transfer"


def test_seller_sepolia_page_shows_transfer_entry_without_submitting() -> None:
    source = """
from frontend.keeper_transfers import render_keeper_transfer_section
render_keeper_transfer_section(
    api_base_url='http://unused', snake_id='BP-S004',
    account={'role':'breeder','participant_id':'BREEDER001'},
    access_token='preview-only', network='sepolia',
)
"""
    with patch("frontend.keeper_transfers.fetch_keeper_transfer_status", return_value=STATUS), patch(
        "frontend.keeper_transfers.submit_keeper_transfer_request"
    ) as submit:
        app = AppTest.from_string(source).run()

    assert not app.exception
    assert any(button.label == "Initiate Transfer" for button in app.button)
    assert not submit.called


def test_uncertain_sepolia_accept_offers_existing_transaction_recovery() -> None:
    source = """
import streamlit as st
from frontend.keeper_transfers import render_keeper_transfer_section
st.session_state['keeper_transfer_result_sepolia_BP-S004'] = {
    'action': 'accept', 'status_code': 503,
    'payload': {
        'outcome': 'unverified', 'business_id': 'TRANSFER-TEST',
        'transaction_hash': '0x' + '1' * 64,
    },
}
render_keeper_transfer_section(
    api_base_url='http://unused', snake_id='BP-S004',
    account={'role':'buyer','participant_id':'BUYER001'},
    access_token='preview-only', network='sepolia',
)
"""
    pending_status = {
        **STATUS,
        "transfer_status": "pending_acceptance",
        "transfer_id": "TRANSFER-TEST",
        "to_participant": {
            "participant_id": "BUYER001",
            "display_name": "Buyer",
            "username": "core_test_buyer",
            "wallet_address": "0x5D30F8dB977193e62502B3bD596C05314e5d19aA",
        },
    }
    with patch("frontend.keeper_transfers.fetch_keeper_transfer_status", return_value=pending_status), patch(
        "frontend.keeper_transfers.verify_keeper_acceptance",
        return_value=(503, {"outcome": "unverified", "detail": "The checkpoint is not confirmed."}),
    ) as verify, patch("frontend.keeper_transfers.submit_keeper_transfer_action") as submit:
        app = AppTest.from_string(source).run()

        assert not app.exception
        recovery = app.button(key="recover_keeper_accept_BP-S004")
        recovery.click().run()

    assert verify.call_args.kwargs["transfer_id"] == "TRANSFER-TEST"
    assert verify.call_args.kwargs["transaction_hash"] == "0x" + "1" * 64
    submit.assert_not_called()


def test_anvil_buyer_accept_flow_does_not_show_sepolia_recovery_action() -> None:
    source = """
from frontend.keeper_transfers import render_keeper_transfer_section
render_keeper_transfer_section(
    api_base_url='http://unused', snake_id='BP-S004',
    account={'role':'buyer','participant_id':'BUYER001'},
    access_token='preview-only', network='anvil',
)
"""
    pending_status = {
        **STATUS,
        "transfer_status": "pending_acceptance",
        "transfer_id": "ANVIL-TRANSFER",
        "from_participant": {
            "participant_id": "BREEDER001", "display_name": "Seller",
            "username": "seller", "wallet_address": SELLER,
        },
        "to_participant": {
            "participant_id": "BUYER001", "display_name": "Buyer",
            "username": "buyer", "wallet_address": "0xBuyer",
        },
    }
    with patch("frontend.keeper_transfers.fetch_keeper_transfer_status", return_value=pending_status), patch(
        "frontend.keeper_transfers.submit_keeper_transfer_action"
    ) as submit:
        app = AppTest.from_string(source).run()

    assert not app.exception
    assert any(button.label == "Accept Transfer" for button in app.button)
    assert not any(button.label in {"Verify Existing Transaction", "Recover Saved Acceptance"} for button in app.button)
    assert not submit.called
