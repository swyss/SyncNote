# tests/test_time_sync.py

from src.utils.time_sync import adjust_client_time

def test_time_adjustment():
    client_time = "2025-04-01T10:00:00"
    time_diff = adjust_client_time(client_time)
    assert abs(time_diff) < 10  # Allow a small difference
