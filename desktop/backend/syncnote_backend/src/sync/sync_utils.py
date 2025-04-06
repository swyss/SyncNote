# src/sync/sync_utils.py

import json
from datetime import datetime
import logging

logger = logging.getLogger("SyncNote")

def generate_sync_report(logs):
    """Generate a sync report from the log data."""
    try:
        report = []
        for log in logs:
            entry = json.loads(log)
            report.append(f"[{entry['timestamp']}] {entry['event_type']}: {entry['message']}")
        logger.info("Sync report generated")
        return "\n".join(report)
    except Exception as e:
        logger.error(f"Error generating sync report: {e}")
        return "Failed to generate report"

def cleanup_old_sync_logs(redis_client, max_logs=100):
    """Remove old sync logs if the limit is exceeded."""
    try:
        log_count = redis_client.llen("sync_logs")
        if log_count > max_logs:
            redis_client.ltrim("sync_logs", log_count - max_logs, -1)
            logger.info("Old sync logs cleaned up")
    except Exception as e:
        logger.error(f"Error cleaning up old sync logs: {e}")
