# src/crud/notification_crud.py

import json
import logging

logger = logging.getLogger("SyncNote")

def add_notification(redis_client, notification):
    try:
        redis_client.rpush("notifications", json.dumps(notification))
        logger.info("Notification added successfully")
        return {"success": True, "message": "Notification added"}
    except Exception as e:
        logger.error(f"Failed to add notification: {e}")
        return {"success": False, "message": str(e)}

def get_notifications(redis_client):
    try:
        notifications = redis_client.lrange("notifications", 0, -1)
        logger.info("Notifications retrieved successfully")
        return [json.loads(notification) for notification in notifications]
    except Exception as e:
        logger.error(f"Failed to retrieve notifications: {e}")
        return []
