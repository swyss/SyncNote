# src/message/message_storage.py

import json
from datetime import datetime

def store_message(redis_client, message_type, content):
    try:
        timestamp = datetime.now().isoformat()
        message = {
            "type": message_type,
            "content": content,
            "timestamp": timestamp
        }
        redis_client.rpush("messages", json.dumps(message))
        print(f"[INFO] Message stored: {content}")
    except Exception as e:
        print(f"[ERROR] Failed to store message: {e}")

def get_all_messages(redis_client):
    try:
        messages = redis_client.lrange("messages", 0, -1)
        return [json.loads(msg) for msg in messages]
    except Exception as e:
        print(f"[ERROR] Failed to retrieve messages: {e}")
        return []
