# src/crud/settings_crud.py

import json
import logging

logger = logging.getLogger("SyncNote")

def save_setting(redis_client, key, value):
    """Save a user-specific setting."""
    try:
        redis_client.hset("settings", key, json.dumps(value))
        logger.info(f"Setting {key} saved successfully")
        return {"success": True, "message": "Setting saved"}
    except Exception as e:
        logger.error(f"Failed to save setting {key}: {e}")
        return {"success": False, "message": str(e)}

def get_setting(redis_client, key):
    """Retrieve a setting by key."""
    try:
        value = redis_client.hget("settings", key)
        if value:
            logger.info(f"Setting {key} retrieved successfully")
            return json.loads(value)
        return None
    except Exception as e:
        logger.error(f"Failed to retrieve setting {key}: {e}")
        return None

def delete_setting(redis_client, key):
    """Delete a user setting."""
    try:
        redis_client.hdel("settings", key)
        logger.info(f"Setting {key} deleted successfully")
        return {"success": True, "message": "Setting deleted"}
    except Exception as e:
        logger.error(f"Failed to delete setting {key}: {e}")
        return {"success": False, "message": str(e)}
