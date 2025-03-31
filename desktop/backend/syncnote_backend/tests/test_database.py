# tests/test_database.py
import pytest
from src.database.redis_manager import init_redis

@pytest.fixture
def redis_client():
    config = {
        "REDIS_HOST": "localhost",
        "REDIS_PORT": 6379
    }
    client = init_redis(config)
    yield client

def test_redis_connection(redis_client):
    assert redis_client.ping() is True

def test_store_and_retrieve(redis_client):
    redis_client.set("key", "value")
    assert redis_client.get("key") == "value"
