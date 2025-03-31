# tests/test_sync.py
import pytest
from src.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_sync_tasks(client):
    response = client.get('/sync/tasks')
    assert response.status_code == 200
    assert "Task synchronization endpoint" in response.json["message"]
