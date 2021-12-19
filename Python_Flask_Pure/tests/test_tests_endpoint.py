import pytest
import os

from dotenv import load_dotenv
from flask import request

load_dotenv("../.env")

auth = os.environ.get("BASIC_AUTHENTICATION")


@pytest.mark.order(5)
def test_tests_endpoint_no_auth(client):

    mock_data = {"set_message": "Hello World"}
    mock_type = "application/x-www-form-urlencoded"

    response = client.post("/tests", data=mock_data, content_type=mock_type)

    assert request.form.get("set_message") == mock_data["set_message"]
    assert response.status_code == 401


@pytest.mark.order(6)
def test_tests_endpoint_wrong_auth(client):

    mock_req_headers = {"Authorization": "Basic WRONG_PW"}
    mock_data = {"set_message": "Hello World"}
    mock_type = "application/x-www-form-urlencoded"

    response = client.post("/tests", data=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert response.status_code == 401


@pytest.mark.order(7)
def test_tests_endpoint_no_data(client):

    mock_req_headers = {"Authorization": auth}
    mock_type = "application/x-www-form-urlencoded"

    response = client.post("/tests", content_type=mock_type, headers=mock_req_headers)

    assert response.status_code == 400


@pytest.mark.order(8)
def test_tests_endpoint_too_much_data(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"set_message": "Hello World", "message2": "true"}
    mock_type = "application/x-www-form-urlencoded"

    response = client.post("/tests", data=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert response.status_code == 400


@pytest.mark.order(9)
def test_tests_endpoint_post_route_success(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"set_message": "Hello World"}
    mock_type = "application/x-www-form-urlencoded"

    response = client.post("/tests", data=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert request.form.get("set_message") == "Hello World"
    assert response.status_code == 200
    assert response.headers.get("Content-Length") == "0"
