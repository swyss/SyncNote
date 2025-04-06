# src/core/health_check.py
import logging
from src.utils.redis_client import redis_client

logger = logging.getLogger("SyncNote")

def check_database():
    """Check the status of the Redis database connection."""
    try:
        if redis_client and redis_client.ping():
            logger.info("Database connection successful.")
            return "connected"
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return "disconnected"


def check_modules(modules):
    """Check the status of all running modules."""
    status = {}
    for module_name, info in modules.items():
        status[module_name] = "running" if info.get("status") == "running" else "stopped"
    logger.info("Module status checked.")
    return status
