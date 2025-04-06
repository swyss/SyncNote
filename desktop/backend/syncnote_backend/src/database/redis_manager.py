import redis
import logging

logger = logging.getLogger("SyncNote")

def init_redis(config):
    """Initialize the Redis client."""
    try:
        client = redis.Redis(
            host=config.get("REDIS_HOST", "localhost"),
            port=config.get("REDIS_PORT", 6379),
            db=config.get("REDIS_DB", 0)
        )
        # Test connection
        client.ping()
        logger.info("Redis connection successful.")
        return client
    except Exception as e:
        logger.error(f"Redis connection failed: {e}")
        return None
