from unittest.mock import Mock

from frontend.api import submit_snake_registration


def test_registration_request_posts_explicit_network(monkeypatch):
    response = Mock(status_code=422)
    response.json.return_value = {"detail": "Preview only"}
    post = Mock(return_value=response)
    monkeypatch.setattr("frontend.api.requests.post", post)

    submit_snake_registration(
        url="http://127.0.0.1:8001/api/v1/snakes",
        profile={
            "snake_id": "NETWORK-REQUEST-TEST",
            "species": "Dog",
            "sex": "Female",
            "date_of_birth": "2025-03-04",
        },
        photo_name="pet.jpg",
        photo_content=b"preview-only",
        access_token="preview-token",
        network="sepolia",
    )

    assert post.call_args.kwargs["data"]["network"] == "sepolia"
    assert post.call_args.args[0].endswith("/api/v1/snakes")
