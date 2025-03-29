# src/database/redis_manager.py
import redis

def init_redis(config):
    try:
        client = redis.Redis(
            host=config["REDIS_HOST"],
            port=config["REDIS_PORT"],
            decode_responses=True
        )
        if client.ping():
            print("[INFO] Successfully connected to Redis")
        return client
    except redis.ConnectionError as e:
        print(f"[ERROR] Redis connection failed: {e}")
        return None
