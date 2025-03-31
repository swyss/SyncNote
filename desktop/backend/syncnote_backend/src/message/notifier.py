# src/message/notifier.py
import time
from threading import Thread

def send_notification(message):
    print(f"[NOTIFICATION] {message}")

def notification_worker(redis_client):
    while True:
        try:
            if redis_client is None:
                print("[ERROR] Redis client is not available. Stopping notification worker.")
                break

            messages = redis_client.lrange("messages", 0, -1)
            if messages:
                for msg in messages:
                    send_notification(msg)
            time.sleep(60)  # Check for new messages every minute
        except Exception as e:
            print(f"[ERROR] Notification worker failed: {e}")

def start_notification_service(redis_client):
    if redis_client is None:
        print("[ERROR] Cannot start notification service: Redis client is None")
        return

    thread = Thread(target=notification_worker, args=(redis_client,))
    thread.daemon = True
    thread.start()
    print("[INFO] Notification service started.")
