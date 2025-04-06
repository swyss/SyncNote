# src/crud/reminder_crud.py

import json
import logging

logger = logging.getLogger("SyncNote")

def add_reminder(redis_client, reminder):
    try:
        redis_client.rpush("reminders", json.dumps(reminder.to_dict()))
        logger.info("Reminder added successfully")
        return {"success": True, "message": "Reminder added"}
    except Exception as e:
        logger.error(f"Failed to add reminder: {e}")
        return {"success": False, "message": str(e)}

def get_all_reminders(redis_client):
    try:
        reminders = redis_client.lrange("reminders", 0, -1)
        logger.info(f"Fetched {len(reminders)} reminders")
        return [json.loads(reminder) for reminder in reminders]
    except Exception as e:
        logger.error(f"Failed to retrieve reminders: {e}")
        return []

def update_reminder(redis_client, index, updated_reminder):
    try:
        redis_client.lset("reminders", index, json.dumps(updated_reminder.to_dict()))
        logger.info(f"Reminder at index {index} updated successfully")
        return {"success": True, "message": "Reminder updated"}
    except Exception as e:
        logger.error(f"Failed to update reminder at index {index}: {e}")
        return {"success": False, "message": str(e)}

def delete_reminder(redis_client, index):
    try:
        redis_client.lset("reminders", index, "__deleted__")
        redis_client.lrem("reminders", 0, "__deleted__")
        logger.info(f"Reminder at index {index} deleted successfully")
        return {"success": True, "message": "Reminder deleted"}
    except Exception as e:
        logger.error(f"Failed to delete reminder at index {index}: {e}")
        return {"success": False, "message": str(e)}
