# src/core/health_check.py
import logging
from src.utils.redis_client import redis_client

logger = logging.getLogger("SyncNote")

# Define constants for log messages to improve readability
DATABASE_CONNECTION_SUCCESS_MSG = "Database connection successful."
DATABASE_CONNECTION_FAILED_MSG = "Database connection failed: {}"
MODULE_STATUS_CHECKED_MSG = "Module status checked."


def check_database():
    """Check and return the status of the Redis database connection."""
    try:
        if redis_client and redis_client.ping():
            logger.info(DATABASE_CONNECTION_SUCCESS_MSG)
            return "connected"
    except Exception as e:
        logger.error(DATABASE_CONNECTION_FAILED_MSG.format(e))
        return "disconnected"


def get_module_status(info):
    """Determine the status of a module based on its info dictionary."""
    return "running" if info.get("status") == "running" else "stopped"


def check_modules(module_status_map):
    """
    Check the status of all running modules.

    Args:
        module_status_map (dict): A dictionary mapping module names to their info.

    Returns:
        dict: A dictionary with module names as keys and their statuses as values.
    """
    status = {module_name: get_module_status(info) for module_name, info in module_status_map.items()}
    logger.info(MODULE_STATUS_CHECKED_MSG)
    return status
