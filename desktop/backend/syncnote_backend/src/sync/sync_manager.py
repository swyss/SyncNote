# src/sync/sync_manager.py

from datetime import datetime
import json
import logging

logger = logging.getLogger("SyncNote")

def log_sync_event(redis_client, event_type, message):
    """Log sync events with timestamp."""
    try:
        event = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "message": message
        }
        redis_client.rpush("sync_logs", json.dumps(event))
        logger.info(f"Sync event logged: {event_type} - {message}")
    except Exception as e:
        logger.error(f"Failed to log sync event: {e}")

def resolve_conflict(local_data, remote_data):
    """Resolve conflicts based on timestamp."""
    try:
        local_time = datetime.fromisoformat(local_data.get("updated_at", "1970-01-01T00:00:00"))
        remote_time = datetime.fromisoformat(remote_data.get("updated_at", "1970-01-01T00:00:00"))

        if remote_time > local_time:
            logger.info("Conflict resolved: taking remote version")
            return remote_data  # Take the newer version
        logger.info("Conflict resolved: keeping local version")
        return local_data  # Keep the local version
    except Exception as e:
        logger.error(f"Error resolving conflict: {e}")
        return local_data

def synchronize_data(local_data, remote_data):
    """Synchronize data between desktop and mobile."""
    try:
        synced_data = []
        for remote_item in remote_data:
            match = next((item for item in local_data if item['title'] == remote_item['title']), None)
            if match:
                resolved = resolve_conflict(match, remote_item)
                synced_data.append(resolved)
            else:
                synced_data.append(remote_item)
        logger.info("Data synchronized successfully")
        return synced_data
    except Exception as e:
        logger.error(f"Error synchronizing data: {e}")
        return local_data
