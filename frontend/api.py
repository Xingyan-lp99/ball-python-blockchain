import binascii
import base64
import json
import requests

from urllib.parse import quote, urljoin
from typing import Literal, cast


class SignInRequired(RuntimeError):
    """The backend rejected the current login session."""


class AccountRequestError(RuntimeError):
    """An account request failed without exposing its submitted credentials."""


def _authorization(access_token: str) -> dict[str, str]:
    if not access_token:
        raise SignInRequired("Please sign in to continue.")
    return {"Authorization": f"Bearer {access_token}"}


def _check_session_response(response: requests.Response) -> None:
    if response.status_code == 401:
        raise SignInRequired("Your session is invalid or expired. Please sign in again.")


def _account_request(
    method: str,
    url: str,
    *,
    body: dict | None = None,
    access_token: str | None = None,
    expected_status: int = 200,
) -> dict | None:
    headers = _authorization(access_token) if access_token is not None else {}
    try:
        response = requests.request(
            method, url, json=body, headers=headers, timeout=(5, 40)
        )
    except requests.RequestException:
        raise AccountRequestError(
            "The account request could not be completed. Check the result before trying again."
        ) from None

    if access_token is not None:
        _check_session_response(response)

    if response.status_code != expected_status:
        try:
            detail = response.json().get("detail")
        except (ValueError, AttributeError):
            detail = None
        raise AccountRequestError(
            detail if isinstance(detail, str) else "The account service is unavailable."
        )

    if expected_status == 204:
        return None

    try:
        payload = response.json()
    except ValueError:
        payload = None
    if not isinstance(payload, dict):
        raise AccountRequestError("The account service returned an unreadable response.")
    return payload


def register_user_account(*, api_base_url: str, data: dict) -> dict:
    return cast(dict, _account_request(
        "POST", f"{api_base_url.rstrip('/')}/api/v1/accounts",
        body=data, expected_status=201,
    ))


def sign_in_account(*, api_base_url: str, username: str, password: str) -> dict:
    session = cast(dict, _account_request(
        "POST", f"{api_base_url.rstrip('/')}/api/v1/sessions",
        body={"username": username, "password": password},
    ))
    if (
        not isinstance(session.get("access_token"), str)
        or not session["access_token"]
        or not isinstance(session.get("account"), dict)
        or session["account"].get("role") not in {"buyer", "breeder", "lab"}
    ):
        raise AccountRequestError("The sign-in service returned an invalid session.")
    return session


def fetch_current_account(*, api_base_url: str, access_token: str) -> dict:
    account = cast(dict, _account_request(
        "GET", f"{api_base_url.rstrip('/')}/api/v1/sessions/current",
        access_token=access_token,
    ))
    if (
        account.get("role") not in {"buyer", "breeder", "lab"}
        or not isinstance(account.get("participant_id"), str)
        or not isinstance(account.get("username"), str)
        or not isinstance(account.get("display_name"), str)
    ):
        raise AccountRequestError("The sign-in service returned an invalid account.")
    return account


def fetch_public_snake_showcase_images(*, api_base_url: str) -> list[bytes]:
    try:
        response = requests.get(
            f"{api_base_url.rstrip('/')}/api/v1/snakes/showcase-images",
            timeout=(3, 10),
        )
    except requests.RequestException:
        raise AccountRequestError("Snake photos are temporarily unavailable.") from None

    if response.status_code != 200:
        raise AccountRequestError("Snake photos are temporarily unavailable.")

    try:
        payload = response.json()
    except ValueError:
        raise AccountRequestError("The photo service returned an unreadable response.") from None

    items = payload.get("images") if isinstance(payload, dict) else None
    if not isinstance(items, list) or len(items) > 3:
        raise AccountRequestError("The photo service returned an invalid response.")

    photos = []
    for item in items:
        if (
            not isinstance(item, dict)
            or item.get("content_type") not in {"image/jpeg", "image/png"}
            or not isinstance(item.get("content_base64"), str)
        ):
            raise AccountRequestError("The photo service returned an invalid response.")
        try:
            content = base64.b64decode(item["content_base64"], validate=True)
        except (binascii.Error, ValueError):
            raise AccountRequestError("The photo service returned an invalid image.") from None
        if not content or len(content) > 5 * 1024 * 1024:
            raise AccountRequestError("The photo service returned an invalid image.")
        photos.append(content)

    return photos


def sign_out_account(*, api_base_url: str, access_token: str) -> None:
    _account_request(
        "DELETE", f"{api_base_url.rstrip('/')}/api/v1/sessions/current",
        access_token=access_token, expected_status=204,
    )


# Purpose: classify the backend/database readiness response.
# Workflow: Day 1, frontend-to-backend connection check.
# Removing this function removes the page's HTTP readiness check.
def check_backend_readiness(url: str) -> str:
    try:
        response = requests.get(url, timeout=5)
    except requests.RequestException:
        return "backend_unavailable"

    try:
        payload = response.json()
    except ValueError:
        return "unexpected_response"

    if response.status_code == 200 and payload == {
        "status": "ok",
        "database": "ok",
    }:
        return "ok"

    if response.status_code == 503 and payload == {
        "status": "unavailable",
        "database": "unavailable",
    }:
        return "database_unavailable"

    return "unexpected_response"

# Purpose: submit a registration form and photo through HTTP.
# Workflow: demo step 1, Streamlit-to-FastAPI registration.
# Without this helper, the page cannot submit its registration.
def submit_snake_registration(
    *,
    url: str,
    profile: dict[str, str | None],
    photo_name: str,
    photo_content: bytes,
    access_token: str,
) -> tuple[int | None, dict]:
    try:
        response = requests.post(
            url,
            data={"profile_json": json.dumps(profile)},
            files={"photo": (photo_name, photo_content)},
            headers=_authorization(access_token),
            timeout=(5, 60),
        )
    except requests.RequestException:
        return None, {
            "detail": "The registration request could not be completed. Its outcome may be unknown. Do not submit again.",
            "outcome": "unknown",
        }

    _check_session_response(response)

    try:
        payload = response.json()
    except ValueError:
        payload = None

    if not isinstance(payload, dict):
        return response.status_code, {
            "detail": "The backend returned an unreadable response. Check the registration result before submitting again.",
            "outcome": "unknown",
        }

    if response.status_code == 201 and (
        payload.get("receipt_status") != 1
        or payload.get("snake_id") != profile["snake_id"]
    ):
        return None, {
            "detail": "The registration response does not match the submitted data. Check the result before submitting again.",
            "outcome": "unknown",
        }

    return response.status_code, payload


# Purpose: load a persisted profile and photo through the backend.
# Workflow: demo step 1, viewing an existing snake.
# Without this helper, the page cannot retrieve saved data after reopening.
def fetch_snake_profile(
    *,
    api_base_url: str,
    snake_id: str,
    access_token: str,
) -> tuple[dict | None, bytes | None, str | None]:
    url = (
        f"{api_base_url.rstrip('/')}/api/v1/snakes/"
        f"{quote(snake_id, safe='')}"
    )

    try:
        response = requests.get(url, headers=_authorization(access_token), timeout=5)
    except requests.RequestException:
        return None, None, "Cannot connect to the profile service."

    _check_session_response(response)

    if response.status_code == 404:
        return None, None, "Snake profile not found."

    if response.status_code != 200:
        return None, None, "The profile service is unavailable."

    try:
        profile = response.json()
    except ValueError:
        return None, None, "The profile service returned an unreadable response."

    if not isinstance(profile, dict) or profile.get("snake_id") != snake_id:
        return None, None, "The profile response does not match the requested snake."

    photo_url = profile.get("photo_url")

    if not isinstance(photo_url, str):
        return profile, None, "The profile photo is unavailable."

    try:
        photo_response = requests.get(
            urljoin(api_base_url, photo_url),
            headers=_authorization(access_token),
            timeout=5,
        )
    except requests.RequestException:
        return profile, None, "The profile photo could not be loaded."

    _check_session_response(photo_response)

    if (
        photo_response.status_code != 200
        or not photo_response.headers.get(
            "Content-Type", ""
        ).startswith("image/")
    ):
        return profile, None, "The profile photo is unavailable."

    return profile, photo_response.content, None


def fetch_random_snake_profiles(
    *,
    api_base_url: str,
    access_token: str,
) -> list[tuple[dict | None, bytes | None, str | None]]:
    payload = cast(dict, _account_request(
        "GET",
        f"{api_base_url.rstrip('/')}/api/v1/snakes/random-profiles",
        access_token=access_token,
    ))
    items = payload.get("snakes")
    if not isinstance(items, list) or len(items) > 3:
        raise AccountRequestError("The profile service returned an invalid list.")

    profiles = []
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("snake_id"), str):
            raise AccountRequestError("The profile service returned an invalid list.")
        profiles.append(fetch_snake_profile(
            api_base_url=api_base_url,
            snake_id=item["snake_id"],
            access_token=access_token,
        ))

    return profiles


class HusbandryRequestError(RuntimeError):
    """Report an HTTP failure and whether a write may already have completed."""

    def __init__(self, message: str, *, outcome_unknown: bool = False) -> None:
        super().__init__(message)
        self.outcome_unknown = outcome_unknown


def _husbandry_url(
    api_base_url: str,
    snake_id: str,
    record_type: str,
    record_id: int | None = None,
) -> str:
    if record_type not in {"growth", "shedding", "feeding", "health"}:
        raise ValueError("Unknown husbandry record type.")

    url = (
        f"{api_base_url.rstrip('/')}/api/v1/snakes/"
        f"{quote(snake_id, safe='')}/husbandry/{record_type}"
    )
    return url if record_id is None else f"{url}/{record_id}"


# Purpose: normalize the four husbandry HTTP operations without retrying writes.
# Without this helper, each operation would repeat error and response handling.
def _husbandry_request(
    method: str,
    url: str,
    *,
    access_token: str,
    body: dict | None = None,
) -> list[dict] | dict | None:
    writing = method != "GET"

    try:
        response = requests.request(
            method,
            url,
            json=body,
            headers=_authorization(access_token),
            timeout=(5, 40),
        )
    except requests.RequestException:
        message = (
            "The change could not be confirmed. Reload records before trying again."
            if writing
            else "Cannot connect to the husbandry service."
        )
        raise HusbandryRequestError(
            message, outcome_unknown=writing
        ) from None

    _check_session_response(response)
    expected_status = {"GET": 200, "POST": 201, "PUT": 200, "DELETE": 204}[method]

    if response.status_code != expected_status:
        try:
            detail = response.json().get("detail")
        except (ValueError, AttributeError):
            detail = None

        message = (
            detail
            if isinstance(detail, str)
            else "Please check the record fields and service availability."
        )
        uncertain = writing and response.status_code >= 500
        if uncertain:
            message += " Reload records before trying again."
        raise HusbandryRequestError(message, outcome_unknown=uncertain)

    if method == "DELETE":
        return None

    try:
        payload = response.json()
    except ValueError:
        payload = None

    valid = (
        isinstance(payload, list)
        and all(isinstance(record, dict) for record in payload)
        if method == "GET"
        else isinstance(payload, dict)
    )
    if not valid:
        raise HusbandryRequestError(
            "The service returned an unreadable response. Reload records before trying again.",
            outcome_unknown=writing,
        )

    return payload


# Purpose: load husbandry history and its system-assigned author names.
# Without this operation, the page cannot display persisted records.
def fetch_husbandry_records(
    *, api_base_url: str, snake_id: str, record_type: str, access_token: str
) -> list[dict]:
    return cast(list[dict], _husbandry_request(
        "GET", _husbandry_url(api_base_url, snake_id, record_type),
        access_token=access_token,
    ))


# Purpose: submit a new observation for the acting participant.
# The backend assigns authorship and checks current keeper rights.
def create_husbandry_record(
    *,
    api_base_url: str,
    snake_id: str,
    record_type: str,
    access_token: str,
    data: dict,
) -> dict:
    return cast(dict, _husbandry_request(
        "POST",
        _husbandry_url(api_base_url, snake_id, record_type),
        access_token=access_token,
        body={"data": data},
    ))


# Purpose: submit a complete edit without accepting author or snake changes.
# Without this operation, the page cannot correct permitted records.
def edit_husbandry_record(
    *,
    api_base_url: str,
    snake_id: str,
    record_type: str,
    record_id: int,
    access_token: str,
    data: dict,
) -> dict:
    return cast(dict, _husbandry_request(
        "PUT",
        _husbandry_url(api_base_url, snake_id, record_type, record_id),
        access_token=access_token,
        body={"data": data},
    ))


# Purpose: request deletion of a permitted husbandry row, not project files.
# Without this operation, the page cannot remove an unwanted observation.
def remove_husbandry_record(
    *,
    api_base_url: str,
    snake_id: str,
    record_type: str,
    record_id: int,
    access_token: str,
) -> None:
    _husbandry_request(
        "DELETE",
        _husbandry_url(api_base_url, snake_id, record_type, record_id),
        access_token=access_token,
    )


# Purpose: share authenticated PDF upload and uncertain-result handling.
# Without this helper, issuance and revision could disagree about safe retries.
def _submit_certificate_upload(
    *,
    url: str,
    form_fields: dict,
    expected_fields: dict,
    minimum_version: int,
    pdf_name: str,
    pdf_content: bytes,
    access_token: str,
) -> tuple[int | None, dict]:
    try:
        response = requests.post(
            url,
            data=form_fields,
            files={
                "pdf": (pdf_name, pdf_content, "application/pdf"),
            },
            headers=_authorization(access_token),
            timeout=(5, 60),
        )
    except requests.RequestException:
        return None, {
            "detail": "The request could not be completed. "
            "The transaction may already have been submitted. "
            "Check the result before submitting again.",
            "outcome": "unknown",
        }

    _check_session_response(response)

    try:
        payload = response.json()
    except ValueError:
        payload = None

    if not isinstance(payload, dict):
        return response.status_code, {
            "detail": "The backend returned an unreadable response. "
            "Check the result before submitting again.",
            "outcome": "unknown",
        }

    if response.status_code == 201:
        required_text = (
            "snake_id",
            "title",
            "series_id",
            "version_id",
            "file_hash",
            "transaction_hash",
            "issuer_address",
            "laboratory_id",
            "issued_at",
        )
        if minimum_version >= 2:
            required_text += ("previous_version_id",)

        valid_result = (
            payload.get("receipt_status") == 1
            and isinstance(payload.get("version_number"), int)
            and payload["version_number"] >= minimum_version
            and payload.get("status") == "current"
            and all(
                payload.get(field) == value
                for field, value in expected_fields.items()
            )
            and all(
                isinstance(payload.get(field), str)
                and bool(payload[field])
                for field in required_text
            )
        )

        if not valid_result:
            return None, {
                "detail": "The certificate response is incomplete or does "
                "not match the request. Do not submit again.",
                "outcome": "unknown",
                **{
                    field: payload[field]
                    for field in ("series_id", "version_id", "transaction_hash")
                    if isinstance(payload.get(field), str)
                },
            }
    else:
        payload.setdefault(
            "outcome",
            "not_submitted"
            if response.status_code in {403, 404, 409, 422}
            else "unknown",
        )

    return response.status_code, payload


# Purpose: send a laboratory's original report to the V1 endpoint.
# Without this helper, the original upload form cannot request issuance.
def submit_certificate_issuance(
    *,
    api_base_url: str,
    snake_id: str,
    title: str,
    pdf_name: str,
    pdf_content: bytes,
    access_token: str,
) -> tuple[int | None, dict]:
    return _submit_certificate_upload(
        url=f"{api_base_url.rstrip('/')}/api/v1/certificate-series",
        form_fields={"snake_id": snake_id, "title": title},
        expected_fields={"snake_id": snake_id, "version_number": 1},
        minimum_version=1,
        pdf_name=pdf_name,
        pdf_content=pdf_content,
        access_token=access_token,
    )


# Purpose: upload a corrected PDF for an existing report series.
# Without this helper, the revision form would have no backend request.
def submit_certificate_revision(
    *,
    api_base_url: str,
    series_id: str,
    pdf_name: str,
    pdf_content: bytes,
    access_token: str,
) -> tuple[int | None, dict]:
    return _submit_certificate_upload(
        url=(
            f"{api_base_url.rstrip('/')}/api/v1/certificate-series/"
            f"{quote(series_id, safe='')}/versions"
        ),
        form_fields={},
        expected_fields={
            "series_id": series_id,
            "previous_version_status": "superseded",
        },
        minimum_version=2,
        pdf_name=pdf_name,
        pdf_content=pdf_content,
        access_token=access_token,
    )


class CertificateRequestError(RuntimeError):
    """Report a history or PDF read failure without leaking request details."""


# Purpose: share authenticated read handling for certificate history and PDFs.
# Without this helper, downloads could overlook expired sessions or HTTP errors.
def _get_certificate_response(
    *, url: str, access_token: str
) -> requests.Response:
    try:
        response = requests.get(
            url, headers=_authorization(access_token), timeout=(5, 60)
        )
    except requests.RequestException:
        raise CertificateRequestError(
            "Cannot connect to the certificate service."
        ) from None

    _check_session_response(response)

    if response.status_code != 200:
        try:
            detail = response.json().get("detail")
        except (ValueError, AttributeError):
            detail = None
        raise CertificateRequestError(
            detail if isinstance(detail, str)
            else "The certificate service is unavailable."
        )

    return response


# Purpose: retrieve all series and versions belonging to a snake.
# Without this helper, the profile page cannot display certificate history.
def fetch_certificate_history(
    *, api_base_url: str, snake_id: str, access_token: str
) -> dict:
    response = _get_certificate_response(
        url=(
            f"{api_base_url.rstrip('/')}/api/v1/snakes/"
            f"{quote(snake_id, safe='')}/certificate-series"
        ),
        access_token=access_token,
    )
    try:
        payload = response.json()
    except ValueError:
        payload = None

    if (
        not isinstance(payload, dict)
        or payload.get("snake_id") != snake_id
        or not isinstance(payload.get("series"), list)
    ):
        raise CertificateRequestError(
            "The certificate service returned an invalid history response."
        )

    return payload


# Purpose: retrieve the selected version's PDF using the login session.
# Without this helper, Streamlit cannot offer an authenticated file download.
def fetch_certificate_pdf(
    *, api_base_url: str, version_id: str, access_token: str
) -> bytes:
    response = _get_certificate_response(
        url=(
            f"{api_base_url.rstrip('/')}/api/v1/certificate-versions/"
            f"{quote(version_id, safe='')}/file"
        ),
        access_token=access_token,
    )
    if (
        not response.headers.get("Content-Type", "").startswith("application/pdf")
        or not response.content
    ):
        raise CertificateRequestError("The original PDF could not be loaded.")

    return response.content


class KeeperTransferRequestError(RuntimeError):
    """Report a failed keeper-status read without exposing request credentials."""


# Purpose: retrieve authoritative manager identity and the transfer's latest state.
# Without this read, the page cannot choose which transfer controls to display.
def fetch_keeper_transfer_status(
    *, api_base_url: str, snake_id: str, access_token: str
) -> dict:
    try:
        response = requests.get(
            f"{api_base_url.rstrip('/')}/api/v1/snakes/"
            f"{quote(snake_id, safe='')}/keeper",
            headers=_authorization(access_token),
            timeout=(5, 45),
        )
    except requests.RequestException:
        raise KeeperTransferRequestError("Cannot connect to the keeper status service.") from None

    _check_session_response(response)
    try:
        payload = response.json()
    except ValueError:
        payload = None

    if response.status_code != 200:
        detail = payload.get("detail") if isinstance(payload, dict) else None
        raise KeeperTransferRequestError(
            detail if isinstance(detail, str) else "Keeper status could not be loaded."
        )

    valid_states = {
        "no_pending_transfer", "pending_acceptance", "accepted",
        "rejected", "cancelled", "unable_to_confirm",
    }
    if (
        not isinstance(payload, dict)
        or payload.get("snake_id") != snake_id
        or payload.get("transfer_status") not in valid_states
        or any(
            payload.get(field) is not None and not isinstance(payload[field], dict)
            for field in ("current_keeper", "from_participant", "to_participant")
        )
        or (
            payload.get("transfer_status") != "unable_to_confirm"
            and not isinstance(payload.get("current_keeper"), dict)
        )
        or (
            payload.get("transfer_status") == "pending_acceptance"
            and not payload.get("transfer_id")
        )
    ):
        raise KeeperTransferRequestError("The keeper status response is invalid.")

    return payload


# Purpose: share authenticated writes and preserve uncertain transaction results.
# Without this helper, a timeout could lead the page to offer a duplicate submission.
def _submit_keeper_transfer(
    *,
    url: str,
    body: dict | None,
    expected_status: str,
    expected_http_status: int,
    snake_id: str | None,
    transfer_id: str | None,
    access_token: str,
) -> tuple[int | None, dict]:
    try:
        response = requests.post(
            url, json=body, headers=_authorization(access_token), timeout=(5, 60)
        )
    except requests.RequestException:
        return None, {
            "detail": "The transfer request could not be completed. Its outcome "
            "may be unknown. Check the existing request before submitting again.",
            "outcome": "unknown",
        }

    _check_session_response(response)
    try:
        payload = response.json()
    except ValueError:
        payload = None

    if not isinstance(payload, dict):
        return response.status_code, {
            "detail": "The transfer service returned an unreadable response. "
            "Check the result before submitting again.",
            "outcome": "unknown",
        }

    if response.status_code == expected_http_status:
        valid_result = (
            payload.get("receipt_status") == 1
            and payload.get("status") == expected_status
            and (snake_id is None or payload.get("snake_id") == snake_id)
            and (transfer_id is None or payload.get("transfer_id") == transfer_id)
            and all(
                isinstance(payload.get(field), str) and bool(payload[field])
                for field in (
                    "snake_id", "transfer_id", "transaction_hash",
                    "current_keeper_address", "initiated_at",
                )
            )
            and (
                expected_status == "pending"
                or isinstance(payload.get("resolved_at"), str)
            )
        )
        if not valid_result:
            return None, {
                "detail": "The transfer response does not match the request. "
                "Check the result before submitting again.",
                "outcome": "unknown",
                **{
                    field: payload[field]
                    for field in ("transfer_id", "transaction_hash")
                    if isinstance(payload.get(field), str)
                },
            }
    else:
        payload.setdefault(
            "outcome",
            "not_submitted" if response.status_code in {403, 404, 409, 422}
            else "unknown",
        )

    return response.status_code, payload


# Purpose: start a handover to the buyer identified by their registered username.
# Without this helper, the keeper form cannot create a platform transfer request.
def submit_keeper_transfer_request(
    *, api_base_url: str, snake_id: str,
    recipient_username: str, access_token: str,
) -> tuple[int | None, dict]:
    return _submit_keeper_transfer(
        url=(
            f"{api_base_url.rstrip('/')}/api/v1/snakes/"
            f"{quote(snake_id, safe='')}/keeper-transfers"
        ),
        body={"recipient_username": recipient_username},
        expected_status="pending", expected_http_status=201,
        snake_id=snake_id, transfer_id=None, access_token=access_token,
    )


# Purpose: send only the selected request ID and action, deriving identity server-side.
# Without this helper, buyer decisions and keeper cancellation cannot reach the API.
def submit_keeper_transfer_action(
    *, api_base_url: str, transfer_id: str,
    action: Literal["accept", "reject", "cancel"], access_token: str,
) -> tuple[int | None, dict]:
    statuses = {"accept": "accepted", "reject": "rejected", "cancel": "cancelled"}
    if action not in statuses:
        raise ValueError("Unsupported transfer action.")

    return _submit_keeper_transfer(
        url=(
            f"{api_base_url.rstrip('/')}/api/v1/keeper-transfers/"
            f"{quote(transfer_id, safe='')}/{action}"
        ),
        body=None,
        expected_status=statuses[action], expected_http_status=200,
        snake_id=None, transfer_id=transfer_id, access_token=access_token,
    )
