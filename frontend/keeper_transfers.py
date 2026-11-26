from typing import Literal

import streamlit as st

from frontend.api import (
    KeeperTransferRequestError,
    verify_keeper_acceptance,
    recover_keeper_acceptance,
    fetch_keeper_transfer_status,
    submit_keeper_transfer_request,
    submit_keeper_transfer_action,
)


STATUS_LABELS = {
    "no_pending_transfer": "No Pending Transfer",
    "pending_acceptance": "Pending Acceptance",
    "accepted": "Accepted",
    "rejected": "Rejected",
    "cancelled": "Cancelled",
    "unable_to_confirm": "Unable to Confirm",
}


def _participant_label(participant: dict | None) -> str:
    if participant is None:
        return "Unable to Confirm"
    name = participant.get("display_name") or participant.get("wallet_address", "Unknown")
    username = participant.get("username")
    return f"{name} ({username})" if username else name


# Purpose: retain the last outcome and lock uncertain writes against repetition.
# Without this display, a lost response could prompt a duplicate transfer action.
def _render_last_result(result: dict | None) -> bool:
    if result is None:
        return False

    payload = result["payload"]
    uncertain = payload.get("outcome", "unknown") in {
        "unknown", "unverified", "storage_error",
    }
    if result["status_code"] in {200, 201} and "outcome" not in payload:
        st.success(f"Transaction confirmed. Transfer status: {payload.get('status', 'confirmed')}.")
        uncertain = False
    else:
        detail = payload.get("detail")
        message = detail if isinstance(detail, str) else "The transfer action could not be completed."
        if payload.get("historical_verified"):
            st.info(message)
        else:
            st.error(message)

    if payload.get("transaction_hash"):
        st.caption("Last Action Transaction")
        st.code(payload["transaction_hash"])
    if payload.get("etherscan_url"):
        st.link_button("View transaction on Sepolia Etherscan", payload["etherscan_url"])
    if uncertain:
        st.warning(
            "Transfer actions are locked because the last submission has an uncertain "
            "result. Check the request and transaction before continuing."
        )
    return uncertain


# Submit through the authenticated backend using local demonstration accounts.
def _submit_transfer(
    *,
    api_base_url: str,
    snake_id: str,
    action: Literal["initiate", "accept", "reject", "cancel"],
    access_token: str,
    network: str,
    recipient_username: str = "",
    transfer_id: str = "",
) -> None:
    with st.spinner("Submitting and confirming the transfer action..."):
        if action == "initiate":
            status_code, payload = submit_keeper_transfer_request(
                api_base_url=api_base_url, snake_id=snake_id,
                recipient_username=recipient_username, access_token=access_token,
                network=network,
            )
        else:
            status_code, payload = submit_keeper_transfer_action(
                api_base_url=api_base_url, transfer_id=transfer_id,
                action=action, access_token=access_token, network=network,
            )

    st.session_state[f"keeper_transfer_result_{network}_{snake_id}"] = {
        "action": action, "status_code": status_code, "payload": payload,
        "snake_id": snake_id, "transfer_id": transfer_id or None,
    }
    st.session_state.pop(f"keeper_transfer_status_{network}_{snake_id}", None)
    st.rerun()



# Purpose: show the current manager and only the signed-in party's transfer controls.
# Backend live-state and identity checks remain responsible for write authorization.
def _reconcile_acceptance_result(
    last_result: dict, state: dict, evidence: dict, *,
    snake_id: str, participant_id: str, requested_hash: str | None = None,
) -> dict:
    """Clear only a lock bound to the same fully verified acceptance."""
    payload = last_result.get("payload", {})
    original_id = last_result.get("transfer_id") or payload.get("transfer_id") or payload.get("business_id")
    expected_hash = payload.get("transaction_hash") or requested_hash
    keeper = state.get("current_keeper") or {}
    matches = (
        last_result.get("action") == "accept" and bool(original_id or expected_hash)
        and evidence.get("verified") is True and evidence.get("database_synced") is True
        and evidence.get("historical_verified") is True
        and evidence.get("status") == "accepted" and evidence.get("receipt_status") == 1
        and evidence.get("chain_id") == 11155111 and evidence.get("snake_id") == snake_id
        and evidence.get("to_participant_id") == participant_id
        and (not original_id or evidence.get("transfer_id") == original_id)
        and (not expected_hash or str(evidence.get("transaction_hash", "")).lower() == expected_hash.lower())
        and state.get("transfer_status") == "accepted" and state.get("transaction_status") == "confirmed"
        and state.get("transfer_id") == evidence.get("transfer_id")
        and str(state.get("transaction_hash", "")).lower() == str(evidence.get("transaction_hash", "")).lower()
        and keeper.get("participant_id") == participant_id
        and str(keeper.get("wallet_address", "")).lower() == str(evidence.get("current_keeper_address", "")).lower()
    )
    if not matches:
        return last_result
    return {
        "action": "accept", "status_code": 200, "snake_id": snake_id,
        "transfer_id": evidence["transfer_id"], "payload": evidence,
    }


def render_keeper_transfer_section(
    *, api_base_url: str, snake_id: str, account: dict, access_token: str,
    network: str = "anvil",
) -> None:
    st.subheader("Keeper Management")
    result_key = f"keeper_transfer_result_{network}_{snake_id}"
    state_key = f"keeper_transfer_status_{network}_{snake_id}"
    last_result = st.session_state.get(result_key)
    refresh = st.button("Refresh Transfer Status", key=f"refresh_keeper_{snake_id}")
    loaded = refresh or state_key not in st.session_state
    if loaded:
        try:
            with st.spinner("Loading the current keeper and transfer status..."):
                st.session_state[state_key] = fetch_keeper_transfer_status(
                    api_base_url=api_base_url, snake_id=snake_id, access_token=access_token, network=network,
                )
        except KeeperTransferRequestError as error:
            st.session_state.pop(state_key, None)
            _render_last_result(last_result)
            st.write("**Current Keeper:** Unable to Confirm")
            st.write("**Transfer Status:** Unable to Confirm")
            st.error(str(error))
            return
    state = st.session_state[state_key]
    uncertain_accept = (
        network == "sepolia" and account.get("role") == "buyer" and last_result is not None
        and last_result.get("action") == "accept"
        and last_result.get("payload", {}).get("outcome") in {"unknown", "unverified", "storage_error"}
    )
    if uncertain_accept:
        payload = last_result.get("payload", {})
        original_id = last_result.get("transfer_id") or payload.get("transfer_id") or payload.get("business_id")
        original_hash = payload.get("transaction_hash")
        requested_hash = original_hash
        if not original_id and not original_hash:
            requested_hash = st.text_input(
                "Existing acceptance transaction Hash", key=f"keeper_recovery_hash_{snake_id}",
                help="Paste the original acceptance Hash. Verification never sends a transaction.",
            ).strip() or None
        recover_clicked = st.button(
            "Recover Saved Acceptance", key=f"sync_keeper_accept_{snake_id}",
            disabled=not bool(original_id or requested_hash),
            help="Verifies the existing transaction and synchronizes missing database state. Never signs or broadcasts.",
        )
        if recover_clicked:
            with st.spinner("Recovering the saved acceptance without broadcasting..."):
                code, recovered = recover_keeper_acceptance(
                    api_base_url=api_base_url, access_token=access_token,
                    transfer_id=original_id, transaction_hash=requested_hash,
                )
            successful = code == 200 and "outcome" not in recovered
            retained = {
                **payload, "outcome": "unverified",
                "detail": "The saved acceptance was recovered. Verifying current state..."
                if successful else recovered.get("detail", "Recovery could not be completed."),
            }
            if original_id:
                retained["transfer_id"] = original_id
            elif successful:
                retained["transfer_id"] = recovered["transfer_id"]
            if requested_hash:
                retained["transaction_hash"] = requested_hash
            elif successful:
                retained["transaction_hash"] = recovered["transaction_hash"]
            st.session_state[result_key] = {**last_result, "status_code": code, "payload": retained}
            st.session_state.pop(state_key, None)
            st.rerun()
        verify_clicked = st.button(
            "Verify Existing Transaction", key=f"recover_keeper_accept_{snake_id}",
            disabled=not bool(original_id or requested_hash),
            help="Reads the saved checkpoint, Receipt and Keeper state. No transaction is sent.",
        )
        # Unknown legacy identifiers require an explicit Hash and button click.
        should_verify = verify_clicked or (loaded and bool(original_id or original_hash))
        if should_verify:
            with st.spinner("Verifying the existing acceptance..."):
                code, evidence = verify_keeper_acceptance(
                    api_base_url=api_base_url, access_token=access_token,
                    transfer_id=original_id, transaction_hash=requested_hash,
                )
            reconciled = _reconcile_acceptance_result(
                last_result, state, evidence, snake_id=snake_id,
                participant_id=account["participant_id"], requested_hash=requested_hash,
            )
            if code == 200 and reconciled is not last_result:
                last_result = reconciled
            else:
                detail = evidence.get("detail")
                preserved = {
                    **payload, "outcome": "unverified",
                    "historical_verified": evidence.get("historical_verified") is True,
                    "detail": detail if isinstance(detail, str)
                    else "The verified acceptance does not match the current transfer, Keeper, "
                    "or original request. The lock is retained.",
                }
                if original_id:
                    preserved["transfer_id"] = original_id
                if requested_hash:
                    preserved["transaction_hash"] = requested_hash
                elif (
                    (evidence.get("transfer_id") or evidence.get("business_id")) == original_id
                    and isinstance(evidence.get("transaction_hash"), str)
                ):
                    preserved["transaction_hash"] = evidence["transaction_hash"]
                last_result = {**last_result, "status_code": code, "payload": preserved}
            st.session_state[result_key] = last_result
    locked = _render_last_result(last_result)
    status = state["transfer_status"]
    keeper = state.get("current_keeper")
    sender = state.get("from_participant")
    recipient = state.get("to_participant")

    st.write("**Current Keeper:**", _participant_label(keeper))
    st.write("**Transfer Status:**", STATUS_LABELS[status])
    if sender is not None:
        st.write("**From:**", _participant_label(sender))
    if recipient is not None:
        st.write("**To:**", _participant_label(recipient))
    if state.get("detail"):
        st.warning(state["detail"])
    if state.get("chain_block_number") is not None:
        st.caption(
            f"Status checked at chain block {state['chain_block_number']}. "
            "Use Refresh Transfer Status to update this view."
        )
    if state.get("etherscan_url"):
        st.link_button("View last transfer transaction on Etherscan", state["etherscan_url"])

    if state.get("transfer_id") and account["role"] != "buyer":
        with st.expander("Transfer Details"):
            st.json({
                "transfer_id": state["transfer_id"],
                "initiated_at": state.get("initiated_at"),
                "resolved_at": state.get("resolved_at"),
                "transaction_hash": state.get("transaction_hash"),
                "transaction_status": state.get("transaction_status"),
            })

    if locked or status == "unable_to_confirm":
        return

    participant_id = account["participant_id"]
    is_keeper = (
        keeper is not None and keeper.get("participant_id") == participant_id
        and account["role"] in {"buyer", "breeder"}
    )

    if status == "pending_acceptance":
        transfer_id = state["transfer_id"]
        is_recipient = recipient is not None and recipient.get("participant_id") == participant_id
        is_sender = sender is not None and sender.get("participant_id") == participant_id

        if is_recipient:
            accept_column, reject_column = st.columns(2)
            with accept_column:
                if st.button("Accept Transfer", key=f"accept_keeper_{transfer_id}"):
                    _submit_transfer(
                        api_base_url=api_base_url, snake_id=snake_id,
                        transfer_id=transfer_id, action="accept", access_token=access_token,
                        network=network,
                    )
            if network == "anvil":
                with reject_column:
                    if st.button("Reject Transfer", key=f"reject_keeper_{transfer_id}"):
                        _submit_transfer(
                            api_base_url=api_base_url, snake_id=snake_id,
                            transfer_id=transfer_id, action="reject", access_token=access_token,
                            network=network,
                        )
        elif is_keeper and is_sender:
            if network == "anvil" and st.button("Cancel Transfer", key=f"cancel_keeper_{transfer_id}"):
                _submit_transfer(
                    api_base_url=api_base_url, snake_id=snake_id,
                    transfer_id=transfer_id, action="cancel", access_token=access_token,
                    network=network,
                )
        else:
            st.info("This request is awaiting the designated buyer's decision.")
        return

    if is_keeper:
        st.caption("After an offline sale, request a handover to the registered buyer.")
        with st.form(f"initiate_keeper_transfer_{snake_id}"):
            recipient_username = st.text_input("Buyer Username *")
            submitted = st.form_submit_button("Initiate Transfer")
        if submitted:
            if not recipient_username.strip():
                st.error("Please enter the registered buyer's username.")
                return
            _submit_transfer(
                api_base_url=api_base_url, snake_id=snake_id, action="initiate",
                recipient_username=recipient_username.strip(), access_token=access_token,
                network=network,
            )
    elif account["role"] != "buyer":
        st.caption("Only the current keeper may initiate a transfer.")
