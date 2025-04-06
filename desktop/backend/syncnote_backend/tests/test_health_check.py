# tests/test_health_check.py

from src.core.health_check import check_database

def test_check_database():
    status = check_database()
    assert status in ["connected", "disconnected"]
