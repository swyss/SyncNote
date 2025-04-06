# src/utils/time_sync.py

from datetime import datetime
import logging

logger = logging.getLogger("SyncNote")

def get_server_time():
    """Get the server's current time."""
    try:
        current_time = datetime.now().isoformat()
        logger.info(f"Server time retrieved: {current_time}")
        return current_time
    except Exception as e:
        logger.error(f"Error retrieving server time: {e}")
        return None

def adjust_client_time(client_time):
    """Calculate the difference between client and server time."""
    try:
        server_time = datetime.now()
        client_time = datetime.fromisoformat(client_time)
        time_diff = (server_time - client_time).total_seconds()
        logger.info(f"Time difference calculated: {time_diff} seconds")
        return time_diff
    except Exception as e:
        logger.error(f"Error adjusting client time: {e}")
        return 0
