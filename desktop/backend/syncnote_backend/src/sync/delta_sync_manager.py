# src/sync/delta_sync_manager.py

from datetime import datetime
import json
import logging

logger = logging.getLogger("SyncNote")

def calculate_delta(local_data, remote_data):
    """Calculate the difference between local and remote data."""
    try:
        delta = []
        for remote_item in remote_data:
            match = next((item for item in local_data if item['title'] == remote_item['title']), None)
            if not match or match['updated_at'] != remote_item['updated_at']:
                delta.append(remote_item)
        logger.info(f"Delta calculated: {len(delta)} changes")
        return delta
    except Exception as e:
        logger.error(f"Error calculating delta: {e}")
        return []

def update_local_data(redis_client, deltas):
    """Update local data with the given deltas."""
    try:
        for delta in deltas:
            redis_client.rpush("tasks", json.dumps(delta))
        logger.info(f"Local data updated with {len(deltas)} changes")
        return True
    except Exception as e:
        logger.error(f"Error updating local data: {e}")
        return False
