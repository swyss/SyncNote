# tests/test_sync.py

import pytest
from src.sync.sync_manager import resolve_conflict

def test_resolve_conflict():
    local = {"title": "Task 1", "updated_at": "2025-03-31T10:00:00"}
    remote = {"title": "Task 1", "updated_at": "2025-03-31T11:00:00"}
    resolved = resolve_conflict(local, remote)
    assert resolved == remote

def test_generate_sync_report(redis_client):
    redis_client.rpush("sync_logs", '{"timestamp": "2025-03-31T10:00:00", "event_type": "Sync", "message": "Test sync"}')
    from src.sync.sync_utils import generate_sync_report
    logs = redis_client.lrange("sync_logs", 0, -1)
    report = generate_sync_report(logs)
    assert "Test sync" in report
