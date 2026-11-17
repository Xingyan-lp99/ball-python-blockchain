from typing import Literal

import streamlit as st

from frontend.api import (
    KeeperTransferRequestError,
    fetch_keeper_transfer_status,
    submit_keeper_transfer_action,
    submit_keeper_transfer_request,
)


STATUS_LABELS = {
    "no_pending_transfer": "No Pending Transfer",
    "pending_acceptance": "Pending Acceptance",
    "accepted": "Accepted",
    "rejected": "Rejected",
    "cancelled": "Cancelled",
    "unable_to_confirm": "Unable to Confirm",
}
SUCCESS_MESSAGES = {
    "initiate": "Transfer request confirmed. Awaiting buyer acceptance.",
    "accept": "Transfer accepted successfully.",
    "reject": "Transfer rejected successfully.",
    "cancel": "Transfer cancelled successfully.",
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
        st.success(SUCCESS_MESSAGES[result["action"]])
        uncertain = False
    else:
        detail = payload.get("detail")
        st.error(detail if isinstance(detail, str) else "The transfer action could not be completed.")

    if payload.get("transaction_hash"):
        st.caption("Last Action Transaction")
        st.code(payload["transaction_hash"])
    if uncertain:
        st.warning(
            "Transfer actions are locked because the last submission has an uncertain "
            "result. Check the request and transaction before continuing."
        )
    return uncertain


# Purpose: submit once, retain the result, and reload manager/status information.
# Without this step, the page could keep displaying its pre-transfer snapshot.
def _submit_transfer(
    *,
    api_base_url: str,
    snake_id: str,
    action: Literal["initiate", "accept", "reject", "cancel"],
    access_token: str,
    recipient_username: str = "",
    transfer_id: str = "",
) -> None:
    with st.spinner("Submitting and confirming the transfer action..."):
        if action == "initiate":
            status_code, payload = submit_keeper_transfer_request(
                api_base_url=api_base_url, snake_id=snake_id,
                recipient_username=recipient_username, access_token=access_token,
            )
        else:
            status_code, payload = submit_keeper_transfer_action(
                api_base_url=api_base_url, transfer_id=transfer_id,
                action=action, access_token=access_token,
            )

    st.session_state[f"keeper_transfer_result_{snake_id}"] = {
        "action": action, "status_code": status_code, "payload": payload,
    }
    st.session_state.pop(f"keeper_transfer_status_{snake_id}", None)
    st.rerun()


# Purpose: show the current manager and only the signed-in party's transfer controls.
# Backend live-state and identity checks remain responsible for write authorization.
def render_keeper_transfer_section(
    *, api_base_url: str, snake_id: str, account: dict, access_token: str
) -> None:
    st.subheader("Keeper Management")
    locked = _render_last_result(
        st.session_state.get(f"keeper_transfer_result_{snake_id}")
    )
    state_key = f"keeper_transfer_status_{snake_id}"
    refresh = st.button("Refresh Transfer Status", key=f"refresh_keeper_{snake_id}")

    if refresh or state_key not in st.session_state:
        try:
            with st.spinner("Loading the current keeper and transfer status..."):
                st.session_state[state_key] = fetch_keeper_transfer_status(
                    api_base_url=api_base_url, snake_id=snake_id,
                    access_token=access_token,
                )
        except KeeperTransferRequestError as error:
            st.session_state.pop(state_key, None)
            st.write("**Current Keeper:** Unable to Confirm")
            st.write("**Transfer Status:** Unable to Confirm")
            st.error(str(error))
            return

    state = st.session_state[state_key]
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

    if state.get("transfer_id"):
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
                    )
            with reject_column:
                if st.button("Reject Transfer", key=f"reject_keeper_{transfer_id}"):
                    _submit_transfer(
                        api_base_url=api_base_url, snake_id=snake_id,
                        transfer_id=transfer_id, action="reject", access_token=access_token,
                    )
        elif is_keeper and is_sender:
            if st.button("Cancel Transfer", key=f"cancel_keeper_{transfer_id}"):
                _submit_transfer(
                    api_base_url=api_base_url, snake_id=snake_id,
                    transfer_id=transfer_id, action="cancel", access_token=access_token,
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
            )
    else:
        st.caption("Only the current keeper may initiate a transfer.")
