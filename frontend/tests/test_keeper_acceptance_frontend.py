import json
from unittest.mock import Mock, patch

import pytest
import requests
from streamlit.testing.v1 import AppTest

from frontend.api import submit_keeper_transfer_action
from frontend.keeper_transfers import _reconcile_acceptance_result

PET = "PET-RESPONSE-TEST"
TRANSFER = "TRANSFER-RESPONSE-TEST"
TX_HASH = "0x" + "4" * 64
BUYER = "0x" + "2" * 40
EVIDENCE = {
    "verified": True, "historical_verified": True, "database_synced": True,
    "transfer_id": TRANSFER, "snake_id": PET,
    "from_participant_id": "BREEDER001", "to_participant_id": "BUYER001",
    "recipient_username": "registered_buyer", "status": "accepted", "receipt_status": 1,
    "transaction_hash": TX_HASH, "current_keeper_address": BUYER,
    "initiated_at": "2026-01-01T00:00:00Z", "resolved_at": "2026-01-01T00:01:00Z",
    "chain_id": 11155111, "contract_address": "0x" + "3" * 40,
    "etherscan_url": f"https://sepolia.etherscan.io/tx/{TX_HASH}",
    "estimated_gas": 50000, "gas_limit": 400000, "max_fee_per_gas": 1, "max_cost_wei": 400000,
}
STATE = {
    "snake_id": PET, "transfer_status": "accepted", "transaction_status": "confirmed",
    "transfer_id": TRANSFER, "transaction_hash": TX_HASH,
    "current_keeper": {
        "participant_id": "BUYER001", "display_name": "Buyer",
        "username": "registered_buyer", "wallet_address": BUYER,
    },
}
OLD_RESULT = {
    "action": "accept", "status_code": 500, "transfer_id": TRANSFER,
    "payload": {"outcome": "unknown", "detail": "Old unreadable response."},
}


def response(status, body, content_type):
    result = requests.Response()
    result.status_code = status
    result._content = body
    result.headers["Content-Type"] = content_type
    return result


@pytest.mark.parametrize("case", ["json", "empty", "html", "timeout"])
def test_accept_response_handling_preserves_request_identity(case):
    post = Mock()
    if case == "json":
        post.return_value = response(200, json.dumps(EVIDENCE).encode(), "application/json")
    elif case == "empty":
        post.return_value = response(200, b"", "application/json")
    elif case == "html":
        post.return_value = response(502, b"<html>Bad Gateway</html>", "text/html")
    else:
        post.side_effect = requests.Timeout()
    with patch("frontend.api.requests.post", post):
        code, payload = submit_keeper_transfer_action(
            api_base_url="http://unused", transfer_id=TRANSFER, action="accept",
            access_token="test-token", network="sepolia",
        )
    assert post.call_count == 1
    assert payload["transfer_id"] == TRANSFER
    if case == "json":
        assert code == 200 and payload["status"] == "accepted"
        assert "outcome" not in payload
    else:
        assert payload["outcome"] == "unknown"


@pytest.mark.parametrize("mismatch", [None, "transfer", "hash", "keeper", "verified", "database"])
def test_lock_requires_matching_verified_evidence(mismatch):
    evidence = dict(EVIDENCE)
    if mismatch == "transfer":
        evidence["transfer_id"] = "ANOTHER-TRANSFER"
    elif mismatch == "hash":
        evidence["transaction_hash"] = "0x" + "9" * 64
    elif mismatch == "keeper":
        evidence["current_keeper_address"] = "0x" + "1" * 40
    elif mismatch == "verified":
        evidence["verified"] = False
    elif mismatch == "database":
        evidence["database_synced"] = False
    result = _reconcile_acceptance_result(
        OLD_RESULT, STATE, evidence, snake_id=PET, participant_id="BUYER001",
    )
    if mismatch is None:
        assert result["status_code"] == 200 and "outcome" not in result["payload"]
    else:
        assert result is OLD_RESULT


@pytest.mark.parametrize("verified", [True, False])
def test_refresh_updates_stale_lock_without_posting(verified):
    source = f'''
import streamlit as st
from frontend.keeper_transfers import render_keeper_transfer_section
if "test_initialized" not in st.session_state:
    st.session_state["test_initialized"] = True
    st.session_state["keeper_transfer_result_sepolia_{PET}"] = {OLD_RESULT!r}
    st.session_state["keeper_transfer_status_sepolia_{PET}"] = {STATE!r}
render_keeper_transfer_section(
    api_base_url="http://unused", snake_id={PET!r},
    account={{"role": "buyer", "participant_id": "BUYER001"}},
    access_token="test-token", network="sepolia",
)
'''
    verification = (200, EVIDENCE) if verified else (503, {
        "outcome": "unverified", "detail": "The database pet Keeper does not match the accepted Buyer.",
        "transaction_hash": TX_HASH, "business_id": TRANSFER,
    })
    with (
        patch("frontend.keeper_transfers.fetch_keeper_transfer_status", return_value=STATE),
        patch("frontend.keeper_transfers.verify_keeper_acceptance", return_value=verification) as verify,
        patch("frontend.keeper_transfers.submit_keeper_transfer_action") as submit,
        patch("frontend.keeper_transfers.recover_keeper_acceptance") as recover,
    ):
        page = AppTest.from_string(source).run()
        assert not page.exception
        page.button(key=f"refresh_keeper_{PET}").click().run()
        assert not page.exception
        verify.assert_called_once()
        submit.assert_not_called()
        recover.assert_not_called()
        result = page.session_state[f"keeper_transfer_result_sepolia_{PET}"]
        if verified:
            assert "outcome" not in result["payload"]
            assert not page.error and not page.warning and page.success
        else:
            assert result["payload"]["outcome"] == "unverified"
            assert any("database pet Keeper" in item.value for item in page.error)
            assert page.warning


def test_historical_success_alone_does_not_unlock_current_transfer():
    historical = {
        **EVIDENCE, "verified": False, "latest_keeper_address": "0x" + "6" * 40,
        "detail": "Historical acceptance confirmed; the current Keeper has changed.",
    }
    assert _reconcile_acceptance_result(
        OLD_RESULT, STATE, historical, snake_id=PET, participant_id="BUYER001",
    ) is OLD_RESULT


@pytest.mark.parametrize(("network", "action"), [
    ("sepolia", "initiate"), ("sepolia", "accept"), ("anvil", "initiate"),
    ("anvil", "accept"), ("anvil", "reject"), ("anvil", "cancel"),
])
def test_shared_keeper_submit_preserves_existing_callers(network, action):
    from frontend.api import submit_keeper_transfer_request
    statuses = {"initiate": "pending", "accept": "accepted", "reject": "rejected", "cancel": "cancelled"}
    payload = {key: value for key, value in EVIDENCE.items()
               if key not in {"verified", "historical_verified", "database_synced"}}
    payload["status"] = statuses[action]
    if action == "initiate":
        payload["resolved_at"] = None
    http_status = 201 if action == "initiate" else 200
    reply = response(http_status, json.dumps(payload).encode(), "application/json")
    with patch("frontend.api.requests.post", return_value=reply) as post:
        if action == "initiate":
            code, result = submit_keeper_transfer_request(
                api_base_url="http://unused", snake_id=PET, recipient_username="registered_buyer",
                access_token="test-token", network=network,
            )
        else:
            code, result = submit_keeper_transfer_action(
                api_base_url="http://unused", transfer_id=TRANSFER, action=action,
                access_token="test-token", network=network,
            )
    assert code == http_status and result["status"] == statuses[action]
    assert "outcome" not in result and post.call_count == 1
    prefix = "/api/v1/sepolia" if network == "sepolia" else "/api/v1"
    if action == "initiate":
        assert post.call_args.args[0] == f"http://unused{prefix}/snakes/{PET}/keeper-transfers"
        assert post.call_args.kwargs["json"] == {"recipient_username": "registered_buyer"}
    else:
        assert post.call_args.args[0] == f"http://unused{prefix}/keeper-transfers/{TRANSFER}/{action}"
        assert post.call_args.kwargs["json"] is None


def test_verification_uses_get_and_never_posts():
    from frontend.api import verify_keeper_acceptance
    reply = response(200, json.dumps(EVIDENCE).encode(), "application/json")
    with (
        patch("frontend.api.requests.get", return_value=reply) as get,
        patch("frontend.api.requests.post") as post,
    ):
        code, result = verify_keeper_acceptance(
            api_base_url="http://unused", access_token="test-token", transfer_id=TRANSFER,
        )
    assert code == 200 and result["verified"] is True
    assert get.call_args.args[0] == "http://unused/api/v1/sepolia/keeper-acceptance"
    assert get.call_args.kwargs["params"] == {"transfer_id": TRANSFER}
    post.assert_not_called()


def test_database_recovery_uses_dedicated_endpoint_not_accept():
    from frontend.api import recover_keeper_acceptance
    reply = response(200, json.dumps(EVIDENCE).encode(), "application/json")
    with patch("frontend.api.requests.post", return_value=reply) as post:
        code, result = recover_keeper_acceptance(
            api_base_url="http://unused", access_token="test-token",
            transfer_id=TRANSFER, transaction_hash=TX_HASH,
        )
    assert code == 200 and result["transaction_hash"] == TX_HASH
    post.assert_called_once()
    assert post.call_args.args[0] == "http://unused/api/v1/sepolia/keeper-acceptance/recover"
    assert post.call_args.kwargs["json"] == {"transfer_id": TRANSFER, "transaction_hash": TX_HASH}

