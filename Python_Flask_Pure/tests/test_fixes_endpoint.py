import pytest
import os

from dotenv import load_dotenv
from flask import request

load_dotenv("../.env")

auth = os.environ.get("OAUTH_AUTHENTICATION")


@pytest.mark.order(11)
def test_fixes_endpoint_no_auth(client):

    mock_data = {"set_message": "Hello World", "mymessage": "sending req", "flask_app": "True"}
    mock_type = "application/x-www-form-urlencoded"

    response = client.put("/fixes/id/1", data=mock_data, content_type=mock_type)

    assert request.form.get("set_message") == "Hello World"
    assert response.status_code == 403


@pytest.mark.order(12)
def test_fixes_endpoint_wrong_auth(client):

    mock_req_headers = {"Authorization": "Bearer BAD_TOKEN"}
    mock_data = {"set_message": "Hello World", "mymessage": "sending req", "flask_app": "True"}
    mock_type = "application/x-www-form-urlencoded"

    response = client.put("/fixes/id/1", data=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert response.status_code == 401


@pytest.mark.order(13)
def test_fixes_endpoint_wrong_endpoint_num(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"set_message": "Hello World", "mymessage": "sending req", "flask_app": "True"}
    mock_type = "application/x-www-form-urlencoded"

    response = client.put("/fixes/id/2", data=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert response.status_code == 400


@pytest.mark.order(14)
def test_fixes_endpoint_no_form_data(client):

    mock_req_headers = {"Authorization": auth}
    mock_type = "application/x-www-form-urlencoded"

    response = client.put("/fixes/id/1", content_type=mock_type, headers=mock_req_headers)

    assert response.status_code == 400


@pytest.mark.order(15)
def test_fixes_endpoint_success_message_false(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"set_message": "False", "mymessage": "sending req", "flask_app": "True"}
    mock_type = "application/x-www-form-urlencoded"
    expected_outupt = "set_message=False\nmymessage=sending req\nflask_app=True"

    response = client.put("/fixes/id/1", data=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert response.data.decode("utf-8") == expected_outupt
    assert response.status_code == 201


@pytest.mark.order(17)
def test_fixes_endpoint_success_message_true(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"set_message": "Hello World", "mymessage": "sending req", "flask_app": "True"}
    mock_type = "application/x-www-form-urlencoded"
    expected_outupt = "set_message=Hello World\nmymessage=sending req\nflask_app=True"

    response = client.put("/fixes/id/1", data=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert response.data.decode("utf-8") == expected_outupt
    assert response.status_code == 201


@pytest.mark.order(19)
def test_fixes_endpoint_success_no_message(client):

    mock_req_headers = {"Authorization": auth}
    mock_data = {"mymessage": "sending req", "flask_app": "True"}
    mock_type = "application/x-www-form-urlencoded"
    expected_outupt = "mymessage=sending req\nflask_app=True"

    response = client.put("/fixes/id/1", data=mock_data, content_type=mock_type, headers=mock_req_headers)

    assert response.data.decode("utf-8") == expected_outupt
    assert response.status_code == 201
