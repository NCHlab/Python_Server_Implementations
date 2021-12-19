from app import create_app
import pytest


app = create_app()


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.app_context():
        with app.test_client() as client:
            yield client
