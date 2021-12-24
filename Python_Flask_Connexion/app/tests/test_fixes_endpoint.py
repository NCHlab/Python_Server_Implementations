import pytest
import os

from dotenv import load_dotenv
from flask import request

load_dotenv(dotenv_path=os.path.dirname(os.path.realpath(__file__)) + "/../.env")

auth = os.environ.get("OAUTH_AUTHENTICATION")


@pytest.mark.order(11)
def test_fixes_endpoint_no_auth(client):

    mock_data = {"set_message": "Hello World", "mymessage": "sending req", "flask_app": "True"}
    mock_type = "application/json"

    response = client.put("/fixes/id/1", json=mock_data, content_type=mock_type)

    assert response.status_code == 401


@pytest.mark.order(12)
def test_fixes_endpoint_wrong_auth(client):

    mock_req_headers = {"Authorization": "Bearer BAD_TOKEN"}
    mock_data = {"set_message": "Hello World", "mymessage": "sending req", "flask_app": "True"}
    mock_type = "application/json"

    response = client.put("/fixes/id/1", json=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert response.status_code == 401


@pytest.mark.order(13)
def test_fixes_endpoint_wrong_endpoint_num(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"set_message": "Hello World", "mymessage": "sending req", "flask_app": "True"}
    mock_type = "application/json"

    response = client.put("/fixes/id/2", json=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert "Valid id range: 1-1" in response.json["error"]
    assert response.status_code == 400


@pytest.mark.order(14)
def test_fixes_endpoint_no_json_data(client):

    mock_req_headers = {"Authorization": auth}
    mock_type = "application/json"

    response = client.put("/fixes/id/1", content_type=mock_type, headers=mock_req_headers)

    assert "Data must be sent as JSON" in response.json["error"]
    assert response.status_code == 400


@pytest.mark.order(15)
def test_fixes_endpoint_success_message_false(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"set_message": False, "mymessage": "sending req", "flask_app": "True"}
    mock_type = "application/json"

    response = client.put("/fixes/id/1", json=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert response.json == mock_data
    assert response.status_code == 201


@pytest.mark.order(17)
def test_fixes_endpoint_success_message_true(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"set_message": "Hello World", "mymessage": "sending req", "flask_app": "True"}
    mock_type = "application/json"

    response = client.put("/fixes/id/1", json=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert response.json == mock_data
    assert response.status_code == 201


@pytest.mark.order(19)
def test_fixes_endpoint_success_no_message(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"mymessage": "sending req", "flask_app": "True"}
    mock_type = "application/json"

    response = client.put("/fixes/id/1", json=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert response.json == mock_data
    assert response.status_code == 201
