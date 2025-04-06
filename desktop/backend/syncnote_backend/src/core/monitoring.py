# src/core/monitoring.py
import psutil
import logging

logger = logging.getLogger("SyncNote")

DISK_PATH = '/'


def collect_metrics():
    """Collect basic system metrics."""
    return {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage(DISK_PATH).percent
    }


def collect_and_log_system_metrics():
    """Retrieve and log basic system metrics."""
    metrics = collect_metrics()
    logger.info(f"System metrics collected: {metrics}")
    return metrics
