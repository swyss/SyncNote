# tests/test_status.py
import pytest
from src.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_status(client):
    response = client.get('/status')
    assert response.status_code == 200
    assert response.json == {"status": "SyncNote Backend Running"}


from src.utils.error_handler import handle_error

def test_handle_error():
    error = Exception("Test error")
    response, status = handle_error(error)
    assert status == 500
    assert response["status"] == "failure"
    assert response["message"] == "An error occurred during the request"