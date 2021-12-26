import pytest
import os

from dotenv import load_dotenv
from flask import request

load_dotenv(dotenv_path=os.path.dirname(os.path.realpath(__file__)) + "/../.env")
auth = os.environ.get("BASIC_AUTHENTICATION")


@pytest.mark.order(5)
def test_tests_endpoint_no_auth(client):

    mock_data = {"set_message": "Hello World"}
    mock_type = "application/json"

    response = client.post("/api/v1/tests", json=mock_data, content_type=mock_type)

    assert request.json == mock_data
    assert response.status_code == 401


@pytest.mark.order(6)
def test_tests_endpoint_wrong_auth(client):

    mock_req_headers = {"Authorization": "Basic WRONG_PW"}
    mock_data = {"set_message": "Hello World"}
    mock_type = "application/json"

    response = client.post(
        "/api/v1/tests",
        json=mock_data,
        content_type=mock_type,
        headers=mock_req_headers,
    )

    assert response.status_code == 401


@pytest.mark.order(7)
def test_tests_endpoint_no_data(client):

    mock_req_headers = {"Authorization": auth}
    mock_type = "application/json"

    response = client.post(
        "/api/v1/tests", content_type=mock_type, headers=mock_req_headers
    )

    assert "Data must be sent as JSON" in response.json["error"]
    assert response.status_code == 400


@pytest.mark.order(8)
def test_tests_endpoint_too_much_data(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"set_message": "Hello World", "message2": "true"}
    mock_type = "application/json"

    response = client.post(
        "/api/v1/tests",
        json=mock_data,
        content_type=mock_type,
        headers=mock_req_headers,
    )

    assert "Only 'set_message' allowed in body" in response.json["error"]
    assert response.status_code == 400


@pytest.mark.order(9)
def test_tests_endpoint_post_route_success(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"set_message": "Hello World"}
    mock_type = "application/json"

    response = client.post(
        "/api/v1/tests",
        json=mock_data,
        content_type=mock_type,
        headers=mock_req_headers,
    )

    assert request.json == mock_data
    assert response.status_code == 204
