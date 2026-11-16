import requests
import json

from urllib.parse import quote, urljoin

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
) -> tuple[int | None, dict]:
    try:
        response = requests.post(
            url,
            data={"profile_json": json.dumps(profile)},
            files={"photo": (photo_name, photo_content)},
            timeout=(5, 60),
        )
    except requests.RequestException:
        return None, {
            "detail": "The registration request could not be completed. Its outcome may be unknown. Do not submit again.",
            "outcome": "unknown",
        }

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
) -> tuple[dict | None, bytes | None, str | None]:
    url = (
        f"{api_base_url.rstrip('/')}/api/v1/snakes/"
        f"{quote(snake_id, safe='')}"
    )

    try:
        response = requests.get(url, timeout=5)
    except requests.RequestException:
        return None, None, "Cannot connect to the profile service."

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
            timeout=5,
        )
    except requests.RequestException:
        return profile, None, "The profile photo could not be loaded."

    if (
        photo_response.status_code != 200
        or not photo_response.headers.get(
            "Content-Type", ""
        ).startswith("image/")
    ):
        return profile, None, "The profile photo is unavailable."

    return profile, photo_response.content, None