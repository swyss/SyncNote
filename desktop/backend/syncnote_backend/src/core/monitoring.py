# src/core/monitoring.py

import psutil
import logging

logger = logging.getLogger("SyncNote")

def get_system_metrics():
    """Retrieve basic system metrics."""
    metrics = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent
    }
    logger.info(f"System metrics collected: {metrics}")
    return metrics
