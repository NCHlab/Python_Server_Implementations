from ..python_API_server import app
import pytest


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.app_context():
        with app.test_client() as client:
            yield client
