# src/crud/reminder_crud.py

import json

def add_reminder(redis_client, reminder):
    redis_client.rpush("reminders", json.dumps(reminder.to_dict()))

def get_all_reminders(redis_client):
    reminders = redis_client.lrange("reminders", 0, -1)
    return [json.loads(reminder) for reminder in reminders]

def delete_reminder(redis_client, index):
    try:
        redis_client.lset("reminders", index, "__deleted__")
        redis_client.lrem("reminders", 0, "__deleted__")
        return True
    except Exception:
        return False
