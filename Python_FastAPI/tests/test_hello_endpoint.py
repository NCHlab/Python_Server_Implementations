import pytest


@pytest.mark.order(1)
def test_hello_endpoint(client):

    response = client.get("/hello?message=TEST")
    expected_data = {"message": "TEST"}

    assert response.status_code == 200
    assert response.json() == expected_data
    assert response.headers.get("Authorization") is None


@pytest.mark.order(2)
def test_hello_endpoint_no_query(client):

    response = client.get("/hello")

    assert response.status_code == 422


@pytest.mark.order(3)
def test_hello_endpoint_more_than_1_query(client):

    response = client.get("/hello?message=TEST&message2=true")

    assert response.status_code == 400


@pytest.mark.order(4)
def test_hello_endpoint_post_request(client):

    response = client.post("/hello?message=TEST")

    assert response.status_code == 405


@pytest.mark.order(10)
def test_hello_endpoint_after_post(client):

    response = client.get("/hello?message=TEST")
    expected_data = {"message": "TEST"}

    assert response.headers.get("set_message") == "Hello World"
    assert response.status_code == 200
    assert response.json() == expected_data
    assert response.headers.get("Authorization") is None


@pytest.mark.order(16)
def test_hello_endpoint_again_after_put_endpoint_false(client):

    response = client.get("/hello?message=TEST")
    expected_data = {"message": "TEST"}

    assert response.headers.get("set_message") is None
    assert response.status_code == 200
    assert response.json() == expected_data
    assert response.headers.get("Authorization") is None


@pytest.mark.order(18)
def test_hello_endpoint_again_after_out_endpoint_true(client):

    response = client.get("/hello?message=TEST")
    expected_data = {"message": "TEST"}

    assert response.headers.get("set_message") == "Hello World"
    assert response.status_code == 200
    assert response.json() == expected_data
    assert response.headers.get("Authorization") is None


@pytest.mark.order(20)
def test_hello_endpoint_again_after_put_endpoint_missing(client):

    response = client.get("/hello?message=TEST")
    expected_data = {"message": "TEST"}

    assert response.headers.get("set_message") is None
    assert response.status_code == 200
    assert response.json() == expected_data
    assert response.headers.get("Authorization") is None
