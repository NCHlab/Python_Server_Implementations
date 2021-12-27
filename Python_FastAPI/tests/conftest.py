import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# @pytest.fixture
# def client():
#     app.config["TESTING"] = True

#     with app.app_context():
#         with app.test_client() as client:
#             yield client


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client
