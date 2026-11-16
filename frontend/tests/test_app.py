from pathlib import Path
from unittest.mock import Mock, patch

import pytest
import requests
from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


# Purpose: verify button-triggered requests and response messages.
# Workflow: Day 1, frontend readiness validation.
# Removing this test loses coverage of HTTP response classification.
@pytest.mark.parametrize(
    ("status_code", "payload", "expected_message"),
    [
        (
            200,
            {"status": "ok", "database": "ok"},
            "后端与数据库正常",
        ),
        (
            503,
            {"status": "unavailable", "database": "unavailable"},
            "后端可连接，数据库未就绪",
        ),
        (
            200,
            {"status": "unexpected"},
            "后端返回内容不符合预期",
        ),
    ],
)
def test_check_button_displays_response(
    status_code: int,
    payload: dict[str, str],
    expected_message: str,
) -> None:
    response = Mock(status_code=status_code)
    response.json.return_value = payload

    with patch(
        "frontend.api.requests.get",
        return_value=response,
    ) as request:
        page = AppTest.from_file(str(APP_PATH)).run()
        request.assert_not_called()

        page.button[0].click().run()

        request.assert_called_once_with(
            "http://127.0.0.1:8001/ready",
            timeout=5,
        )

    assert not page.exception

    messages = list(page.success) + list(page.error)
    assert len(messages) == 1
    assert messages[0].value == expected_message
    assert page.button[0].disabled is False


# Purpose: verify that network failures leave the page usable.
# Workflow: Day 1, frontend connection failure validation.
# Removing this test loses coverage of timeout and connection errors.
@pytest.mark.parametrize(
    "network_error",
    [
        requests.Timeout("Simulated timeout"),
        requests.ConnectionError("Simulated connection failure"),
    ],
)
def test_check_button_handles_network_failure(
    network_error: requests.RequestException,
) -> None:
    with patch(
        "frontend.api.requests.get",
        side_effect=network_error,
    ):
        page = AppTest.from_file(str(APP_PATH)).run()
        page.button[0].click().run()

    assert not page.exception
    assert page.error[0].value == "无法连接后端或请求超时"
    assert page.button[0].disabled is False


# Purpose: verify that invalid JSON produces a clear page message.
# Workflow: Day 1, frontend response validation.
# Removing this test loses coverage of malformed responses.
def test_check_button_handles_invalid_json() -> None:
    response = Mock(status_code=200)
    response.json.side_effect = ValueError("Invalid JSON")

    with patch(
        "frontend.api.requests.get",
        return_value=response,
    ):
        page = AppTest.from_file(str(APP_PATH)).run()
        page.button[0].click().run()

    assert not page.exception
    assert page.error[0].value == "后端返回内容不符合预期"
    assert page.button[0].disabled is False