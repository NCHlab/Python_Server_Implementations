import pytest
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.dirname(os.path.realpath(__file__)) + "/../.env")
auth = os.environ.get("BASIC_AUTHENTICATION")


@pytest.mark.order(5)
def test_tests_endpoint_no_auth(client):

    mock_data = {"set_message": "Hello World"}

    response = client.post("/tests", json=mock_data)

    assert response.status_code == 401


@pytest.mark.order(6)
def test_tests_endpoint_wrong_auth(client):

    mock_req_headers = {"Authorization": "Basic WRONG_PW"}
    mock_data = {"set_message": "Hello World"}

    response = client.post(
        "/tests",
        json=mock_data,
        headers=mock_req_headers,
    )

    assert response.status_code == 401


@pytest.mark.order(7)
def test_tests_endpoint_no_data(client):

    mock_req_headers = {"Authorization": auth}

    response = client.post("/tests", headers=mock_req_headers)

    assert response.status_code == 422


@pytest.mark.order(8)
def test_tests_endpoint_too_much_data(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"set_message": "Hello World", "message2": "true"}

    response = client.post(
        "/tests",
        json=mock_data,
        headers=mock_req_headers,
    )

    assert response.status_code == 400


@pytest.mark.order(9)
def test_tests_endpoint_post_route_success(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"set_message": "Hello World"}

    response = client.post(
        "/tests",
        json=mock_data,
        headers=mock_req_headers,
    )

    assert response.status_code == 204
