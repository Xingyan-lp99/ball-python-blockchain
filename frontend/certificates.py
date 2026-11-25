import streamlit as st

from frontend.api import (
    CertificateRequestError,
    fetch_certificate_history,
    fetch_certificate_pdf,
    fetch_laboratory_reports,
    submit_certificate_issuance,
    submit_certificate_revision,
)


# Purpose: separate a new report from a correction to an existing series.
# Without these two views, a correction could be submitted as an unrelated V1.
def render_certificate_issuance(
    *,
    api_base_url: str,
    account: dict,
    access_token: str,
) -> None:
    issue_tab, revision_tab = st.tabs(["New Report", "Revise Report"])

    with issue_tab:
        _render_original_certificate(
            api_base_url=api_base_url,
            account=account,
            access_token=access_token,
        )

    with revision_tab:
        _render_certificate_revision(
            api_base_url=api_base_url,
            account=account,
            access_token=access_token,
        )


# Purpose: let signed-in laboratory staff upload and issue an original PDF.
# Without this section, the laboratory workspace has no usable V1 workflow.
def _render_original_certificate(
    *,
    api_base_url: str,
    account: dict,
    access_token: str,
) -> None:
    st.subheader("Issue a Certificate")
    st.caption(
        f"Issuing laboratory: {account['participant_id']}. "
        "Each submission creates a new report series with Version 1."
    )

    result_key = f"certificate_issue_result_{account['participant_id']}"
    attempt_key = f"certificate_issue_attempt_{account['participant_id']}"

    previous = st.session_state.get(result_key)
    locked = False

    if previous is not None:
        status_code = previous["status_code"]
        payload = previous["payload"]

        locked = (
            status_code == 201
            or payload.get("outcome", "unknown") != "not_submitted"
        )

        if status_code == 201:
            st.success("Certificate issued successfully.")
            st.json(
                {
                    "snake_id": payload["snake_id"],
                    "laboratory_id": payload["laboratory_id"],
                    "title": payload["title"],
                    "series_id": payload["series_id"],
                    "version_id": payload["version_id"],
                    "version_number": payload["version_number"],
                    "status": payload["status"],
                    "file_hash": payload["file_hash"],
                    "issuer_address": payload["issuer_address"],
                    "issued_at": payload["issued_at"],
                    "transaction_hash": payload["transaction_hash"],
                }
            )

            if st.button("Start Another Report", key="another_certificate"):
                del st.session_state[result_key]
                st.session_state[attempt_key] = (
                    st.session_state.get(attempt_key, 0) + 1
                )
                st.rerun()
        else:
            detail = payload.get("detail")
            st.error(
                detail
                if isinstance(detail, str)
                else "Check the required fields and uploaded PDF."
            )

            identifiers = {
                field: payload[field]
                for field in (
                    "series_id",
                    "version_id",
                    "transaction_hash",
                )
                if payload.get(field)
            }

            if identifiers:
                st.json(identifiers)

            if locked:
                st.warning(
                    "Submission is locked to prevent duplicate issuance. "
                    "Check the existing transaction before continuing."
                )

    attempt = st.session_state.get(attempt_key, 0)

    with st.container(key="certificate_issue_form_frame"):
        with st.form(
            f"certificate_issuance_{account['participant_id']}_{attempt}"
        ):
            id_column, title_column = st.columns(2, gap="medium")

            with id_column:
                snake_id = st.text_input(
                    "Pet ID *",
                    disabled=locked,
                )

            with title_column:
                title = st.text_input(
                    "Report Title *",
                    disabled=locked,
                )
            pdf = st.file_uploader(
                "PDF File *",
                type=["pdf"],
                max_upload_size=10,
                disabled=locked,
            )
            st.caption(
                "Maximum file size: 10 MiB (10,485,760 bytes). "
                "The original PDF is stored off-chain; "
                "its SHA-256 digest is recorded on-chain."
            )

            submitted = st.form_submit_button(
                "Issue Certificate",
                type="primary",
                disabled=locked,
            )

    if not submitted:
        return

    if not snake_id or not title.strip() or pdf is None:
        st.error("Please provide the Pet ID, report title, and PDF file.")
        return

    content = pdf.getvalue()

    if len(content) > 10 * 1024 * 1024:
        st.error("The PDF must not exceed 10 MB.")
        return

    with st.spinner("Submitting and confirming certificate issuance..."):
        status_code, payload = submit_certificate_issuance(
            api_base_url=api_base_url,
            snake_id=snake_id,
            title=title.strip(),
            pdf_name=pdf.name,
            pdf_content=content,
            access_token=access_token,
        )

    st.session_state[result_key] = {
        "status_code": status_code,
        "payload": payload,
    }
    st.rerun()


def _version_status_label(version: dict) -> str:
    if version["evidence_status"] == "confirmed":
        return version["status"].title()
    return {
        "unconfirmed": "Unconfirmed",
        "unavailable": "Unable to Confirm",
        "mismatch": "Metadata Mismatch",
    }.get(version["evidence_status"], "Unable to Confirm")


# Purpose: show retained report versions and authenticated PDF downloads.
# Without this section, buyers cannot inspect V1 after a correction adds V2.
def render_certificate_history(
    *, api_base_url: str, snake_id: str, access_token: str
) -> None:
    st.subheader("Certificate History")
    history_key = f"certificate_history_{snake_id}"
    refresh = st.button("Refresh Certificates", key=f"refresh_certificates_{snake_id}")

    if refresh or history_key not in st.session_state:
        try:
            with st.spinner("Loading certificate history and chain status..."):
                st.session_state[history_key] = fetch_certificate_history(
                    api_base_url=api_base_url,
                    snake_id=snake_id,
                    access_token=access_token,
                )
        except CertificateRequestError as error:
            st.session_state.pop(history_key, None)
            st.error(str(error))
            return

    history = st.session_state[history_key]
    for warning in history["warnings"]:
        st.warning(warning)

    if not history["series"]:
        st.info("No certificate reports have been uploaded for this snake.")
        return

    for series in history["series"]:
        st.markdown(f"**{series['laboratory_id']}: {series['title']}**")
        st.caption(f"Series ID: {series['series_id']}")
        versions = series["versions"]
        if not versions:
            st.info("No report versions are available in this series.")
            continue

        st.table([
            {
                "Version": f"V{version['version_number']}",
                "Status": _version_status_label(version),
                "Issued At (UTC)": version["issued_at"] or "Not recorded",
            }
            for version in versions
        ])

        for version in versions:
            version_id = version["version_id"]
            st.caption(f"V{version['version_number']} - {_version_status_label(version)}")
            file_key = f"certificate_pdf_{version_id}"
            try:
                if file_key not in st.session_state:
                    st.session_state[file_key] = fetch_certificate_pdf(
                        api_base_url=api_base_url,
                        version_id=version_id,
                        access_token=access_token,
                    )
            except CertificateRequestError as error:
                st.error(str(error))
                continue

            st.download_button(
                "Download Original PDF",
                data=st.session_state[file_key],
                file_name=f"{version_id}.pdf",
                mime="application/pdf",
                key=f"download_certificate_{version_id}",
                type="primary",
            )


# Purpose: append a corrected PDF while retaining the original report and series.
# Without this form, staff cannot request a revision through the demo website.
def _render_certificate_revision(
    *,
    api_base_url: str,
    account: dict,
    access_token: str,
) -> None:
    st.subheader("Revise a Certificate")
    st.caption(
        "Select a report previously issued by your laboratory. "
        "The correction appends a new version and preserves earlier PDFs."
    )

    result_key = f"certificate_revision_result_{account['participant_id']}"
    previous = st.session_state.get(result_key)
    locked = False

    if previous is not None:
        payload = previous["payload"]
        locked = (
            previous["status_code"] == 201
            or payload.get("outcome", "unknown") != "not_submitted"
        )

        if previous["status_code"] == 201:
            st.success("Certificate revision issued successfully.")
            st.json(payload)
            st.info(
                "The previous version is Superseded. "
                "Its original file and evidence have been retained."
            )
        else:
            detail = payload.get("detail")
            st.error(
                detail if isinstance(detail, str)
                else "Check the selected report and revised PDF."
            )
            identifiers = {
                field: payload[field]
                for field in ("series_id", "version_id", "transaction_hash")
                if payload.get(field)
            }
            if identifiers:
                st.json(identifiers)
            if locked:
                st.warning(
                    "Submission is locked to prevent duplicate revision. "
                    "Check the existing transaction before continuing."
                )

    try:
        reports = fetch_laboratory_reports(api_base_url=api_base_url, access_token=access_token)
    except CertificateRequestError as error:
        st.error(str(error))
        return
    if not reports:
        st.info("Your laboratory has not uploaded any reports yet.")
        return
    by_id = {report["series_id"]: report for report in reports}

    with st.form(f"certificate_revision_{account['participant_id']}"):
        series_id = st.selectbox(
            "Report Title *", options=list(by_id), index=None,
            placeholder="Select a report to revise", disabled=locked,
            format_func=lambda value: (
                f"{by_id[value]['title']} · {by_id[value]['snake_id']} · "
                f"V{by_id[value]['latest_version_number']} · {value}"
            ),
            key=f"revision_report_{account['participant_id']}",
        )
        pdf = st.file_uploader(
            "Revised PDF *", type=["pdf"], max_upload_size=10, disabled=locked
        )
        st.caption(
            "Maximum file size: 10 MiB (10,485,760 bytes). "
            "The next version number is assigned automatically."
        )
        submitted = st.form_submit_button(
            "Issue Revision",
            type="primary",
            disabled=locked,
        )

    if not submitted:
        return

    if series_id is None or pdf is None:
        st.error("Please select a report and provide the revised PDF.")
        return

    content = pdf.getvalue()
    if len(content) > 10 * 1024 * 1024:
        st.error("The PDF must not exceed 10 MB.")
        return

    with st.spinner("Submitting and confirming the certificate revision..."):
        status_code, payload = submit_certificate_revision(
            api_base_url=api_base_url,
            series_id=series_id.strip(),
            pdf_name=pdf.name,
            pdf_content=content,
            access_token=access_token,
        )

    if status_code == 201:
        original_result = st.session_state.get(
            f"certificate_issue_result_{account['participant_id']}"
        )
        if (
            original_result is not None
            and original_result.get("payload", {}).get("version_id")
            == payload["previous_version_id"]
        ):
            original_result["payload"]["status"] = "superseded"

    st.session_state[result_key] = {
        "status_code": status_code,
        "payload": payload,
    }
    st.rerun()
