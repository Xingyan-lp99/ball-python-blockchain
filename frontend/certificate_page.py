import base64
from urllib.parse import quote

import requests
import streamlit as st


def upload_v1(api_url, certificate_id, snake_id, document):
    return requests.post(
        f"{api_url}/api/v1/certificates",
        data={"certificate_id": certificate_id, "snake_id": snake_id},
        files={"file": (document.name, document.getvalue(), "application/pdf")}, timeout=20,
    )


def verify_v1(api_url, certificate_id, document):
    return requests.post(
        f"{api_url}/api/v1/certificates/{quote(certificate_id, safe='')}/versions/1/verification",
        files={"file": (document.name, document.getvalue(), "application/pdf")}, timeout=20,
    )


def verify_stored_v1(api_url, certificate_id):
    return requests.post(
        f"{api_url}/api/v1/certificates/{quote(certificate_id, safe='')}/versions/1/verification/stored",
        json={}, timeout=20,
    )


def api_error(response):
    messages = {
        403: "The server demo identity cannot perform this action.",
        404: "The selected snake or certificate V1 does not exist.",
        409: "V1 cannot be overwritten, another transaction is processing, or chain evidence conflicts. Refresh the selected certificate.",
        413: "The PDF exceeds the 10 MiB limit.",
        422: "Check the identifiers and PDF file. Wallets, hashes and version numbers are assigned by the server.",
    }
    try:
        payload = response.json()
        detail = payload.get("detail") if isinstance(payload, dict) else None
        if isinstance(detail, dict) and isinstance(detail.get("message"), str):
            code = detail.get("code")
            st.error(f"{detail['message']} ({code})" if isinstance(code, str) else detail["message"])
            return
        if isinstance(detail, str):
            st.error(detail)
            return
    except (ValueError, requests.RequestException):
        pass
    st.error(messages.get(response.status_code, "The service could not complete this request. Refresh before retrying."))


def show_registration(state):
    st.subheader("Selected certificate registration")
    if state.get("status") == "confirmed" and state.get("chain_check") == "verified":
        st.success("This certificate V1 is registered on the current local chain.")
    elif state.get("status") == "processing":
        st.warning("Certificate issuance is processing or confirmation is unavailable; not currently confirmed.")
    elif state.get("status") == "failed":
        st.warning("Certificate registration failed or its historical deployment evidence is stale/conflicting.")
    else:
        st.info("Certificate V1 has not been submitted to the chain.")
    if state.get("error"):
        code = state.get("error_code")
        st.warning(f"{state['error']} ({code})" if code else state["error"])
    st.json(state)


def show_file_result(result):
    st.subheader("平台原件核验" if result.get("file_source") == "platform" else "外部文件比较")
    label = "平台保存的 PDF" if result.get("file_source") == "platform" else "外部上传的 PDF"
    if result["file_result"] == "match":
        st.success(f"{label}与此链上登记版本一致 (matches this registered V1).")
    elif result["file_result"] == "mismatch":
        st.warning(f"{label}与此链上登记版本不同 (differs from this registered V1).")
    else:
        st.warning("Unable to verify this file against current chain evidence.")
    st.write(result.get("message", ""))
    st.json(result)
    show_registration(result["registration"])


def buyer_snake_profile(api_url: str) -> bool:
    with st.form("buyer_find_snake"):
        snake_id = st.text_input("球蟒编号", key="buyer_snake_lookup")
        find = st.form_submit_button("查询球蟒档案")
    if find:
        if not snake_id.strip():
            st.error("请输入球蟒编号。")
            return False
        st.session_state["buyer_snake_id"] = snake_id.strip()
    if "buyer_snake_id" not in st.session_state:
        return False
    snake_id = st.session_state["buyer_snake_id"]
    endpoint = f"{api_url}/api/v1/snakes/{quote(snake_id, safe='')}"
    try:
        profile = requests.get(endpoint, timeout=20)
        if profile.status_code != 200:
            api_error(profile)
            return False
        response = requests.get(endpoint + "/certificates", timeout=20)
        if response.status_code != 200:
            api_error(response)
            return False
        certificates = response.json()
        st.subheader("球蟒档案")
        st.json(profile.json())
        st.caption("Morph description is breeder-provided and has not been certified by a laboratory.")
        st.subheader("此球蟒的证书列表")
        if not certificates:
            st.info("此档案暂无实验室证书。")
            return False
        st.dataframe([{
            "证书编号": item["certificate_id"], "版本": item["version"], "实验室": item["lab_name"],
            "签发钱包": item["issuer_address"], "登记状态": item["issuance"]["status"],
        } for item in certificates], hide_index=True)
        selected = st.selectbox("选择此档案的证书", [item["certificate_id"] for item in certificates],
                                key="buyer_certificate_choice_" + snake_id)
        st.session_state["buyer_selected_certificate_id"] = selected
        return True
    except (requests.RequestException, ValueError):
        st.warning("球蟒档案或证书列表暂不可用，不显示缓存核验结果。")
        return False


def render_certificate_workspace(api_url: str, role: str) -> None:
    st.header("Laboratory certificate V1" if role == "Laboratory" else "买家 · 球蟒档案与证书")
    st.warning("Server demo identities and signing only: LAB001 uses a wallet separate from BR001. The workspace selector is not authentication. Real login is not implemented.")
    st.caption("File hash matching proves consistency with one registered version, not biological findings or who changed a file. It does not certify every fact about the snake.")
    st.caption("Version 1 only. Latest-version and revocation checks are not implemented.")
    if role == "Laboratory":
        st.write("Issuing laboratory: LAB001. Laboratory authorization is configured by the local deployment administrator.")
        with st.form("upload_certificate_v1"):
            certificate_id = st.text_input("New certificate ID", key="new_certificate_id")
            snake_id = st.text_input("Registered snake ID", key="certificate_snake_id")
            document = st.file_uploader("Original V1 PDF (maximum 10 MiB)", type=["pdf"], key="original_v1_pdf")
            upload = st.form_submit_button("Save original V1 PDF")
        if upload:
            if document is None:
                st.error("Select an original V1 PDF.")
            else:
                try:
                    response = upload_v1(api_url, certificate_id, snake_id, document)
                    if response.status_code in {200, 201}:
                        st.session_state["selected_certificate_id"] = response.json()["certificate_id"]
                        st.success("Original PDF and V1 metadata saved. Chain issuance is a separate action.")
                    else:
                        api_error(response)
                except (requests.RequestException, ValueError):
                    st.warning("Upload response unavailable. Look up the same certificate ID before retrying.")
    selection_key = "selected_certificate_id" if role == "Laboratory" else "buyer_selected_certificate_id"
    if role == "Buyer":
        if not buyer_snake_profile(api_url):
            return
    else:
        with st.form("select_certificate_v1"):
            selected_id = st.text_input("Certificate ID to select", key="certificate_lookup_id")
            select = st.form_submit_button("Select certificate V1")
        if select:
            if selected_id.strip():
                st.session_state[selection_key] = selected_id.strip()
            else:
                st.error("Enter a certificate ID.")
    if selection_key not in st.session_state:
        return
    selected_id = st.session_state[selection_key]
    endpoint = f"{api_url}/api/v1/certificates/{quote(selected_id, safe='')}/versions/1"
    try:
        response = requests.get(endpoint, timeout=20)
        if response.status_code != 200:
            api_error(response)
            return
        certificate = response.json()
    except (requests.RequestException, ValueError):
        st.warning("Selected certificate could not be refreshed; no cached confirmation is shown.")
        return
    st.subheader("Selected certificate V1")
    st.write("Certificate ID:", certificate["certificate_id"])
    st.write("Snake ID:", certificate["snake_id"])
    st.write("Laboratory:", certificate["lab_id"], certificate["lab_name"])
    st.write("Issuer wallet:", certificate["issuer_address"])
    st.write("Version:", certificate["version"])
    st.json(certificate)
    state = certificate["issuance"]
    show_registration(state)
    if role == "Laboratory":
        disabled = bool(state.get("error_code")) or state.get("status") == "confirmed" or state.get("chain_check") in {"stale", "conflict"} or (
            state.get("status") == "processing" and not (
                state.get("recorded_status") == "prepared" and state.get("chain_check") == "verified"
            )
        )
        if st.button("Issue selected V1 on local chain", disabled=disabled):
            try:
                response = requests.post(endpoint + "/issuance", json={}, timeout=20)
                if response.status_code == 200:
                    st.rerun()
                api_error(response)
            except (requests.RequestException, ValueError):
                st.warning("Issuance response unavailable. Timeout is not failure; refresh status before retrying.")
    if st.button("Refresh selected certificate status"):
        st.rerun()
    # Download/preview the selected platform file through FastAPI; no browser RPC or signer.
    try:
        response = requests.get(endpoint + "/file", timeout=20)
        if response.status_code == 200:
            st.download_button("下载证书 PDF", data=response.content,
                               file_name=f"certificate-{certificate['version']}.pdf", mime="application/pdf")
            if st.button("预览证书 PDF"):
                encoded = base64.b64encode(response.content).decode("ascii")
                st.iframe("data:application/pdf;base64," + encoded, height=620)
                st.caption("若浏览器不支持内嵌 PDF 预览，可直接下载原件。")
        else:
            st.warning("平台原件暂不可读取，核验将显示无法核验。")
    except requests.RequestException:
        st.warning("平台原件暂不可读取，核验将显示无法核验。")
    if role == "Buyer":
        st.caption("直接核验平台实际保存的 PDF；无需重新上传。后端会重新读取文件并与链上 V1 比较。")
        if st.button("核验证书", type="primary"):
            try:
                response = verify_stored_v1(api_url, selected_id)
                if response.status_code == 200:
                    show_file_result(response.json())
                else:
                    api_error(response)
            except (requests.RequestException, ValueError):
                st.warning("无法核验：服务当前不可用，没有得出一致或不一致的结论。")
        with st.expander("上传外部文件核验（可选）", expanded=False):
            st.caption("比较从卖家或其他渠道收到的 PDF。不会创建证书、覆盖实验室原件或发起签发交易。")
            with st.form("verify_certificate_v1"):
                candidate = st.file_uploader("外部 PDF", type=["pdf"], key="candidate_v1_pdf")
                verify = st.form_submit_button("比较外部文件")
            if verify:
                if candidate is None:
                    st.error("请先选择待比较的外部 PDF。")
                else:
                    try:
                        response = verify_v1(api_url, selected_id, candidate)
                        if response.status_code == 200:
                            show_file_result(response.json())
                        else:
                            api_error(response)
                    except (requests.RequestException, ValueError):
                        st.warning("无法核验：服务当前不可用，没有得出一致或不一致的结论。")
