# src/utils/console_manager.py

import logging

logger = logging.getLogger("SyncNote")

def display_service_status(service_name, status):
    """Display the status of a specific service."""
    status_color = "\033[92m" if status == "running" else "\033[91m"
    print(f"{status_color}{service_name} is {status}\033[0m")

def display_live_logs():
    """Display live logs from the system."""
    try:
        with open("logs/syncnote.log", "r") as log_file:
            for line in log_file:
                print(line.strip())
    except Exception as e:
        logger.error(f"Error displaying live logs: {e}")



