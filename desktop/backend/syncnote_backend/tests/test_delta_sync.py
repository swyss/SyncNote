# tests/test_delta_sync.py

import pytest
from src.sync.delta_sync_manager import calculate_delta

def test_delta_calculation():
    local = [{"title": "Task A", "updated_at": "2025-04-01T10:00:00"}]
    remote = [{"title": "Task A", "updated_at": "2025-04-01T11:00:00"}]
    delta = calculate_delta(local, remote)
    assert len(delta) == 1
    assert delta[0]["updated_at"] == "2025-04-01T11:00:00"
