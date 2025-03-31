# tests/test_main.py
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
