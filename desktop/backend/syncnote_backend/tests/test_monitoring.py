# tests/test_monitoring.py

from src.core.monitoring import get_system_metrics

def test_get_system_metrics():
    metrics = get_system_metrics()
    assert "cpu_usage" in metrics
    assert "memory_usage" in metrics
    assert "disk_usage" in metrics
