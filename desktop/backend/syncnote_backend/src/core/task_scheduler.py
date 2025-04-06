# src/core/task_scheduler.py

import threading
import time
import logging

logger = logging.getLogger("SyncNote")

def schedule_task(interval, task, *args):
    """Run a task at a specified interval."""
    def wrapper():
        while True:
            logger.info(f"Running scheduled task: {task.__name__}")
            try:
                task(*args)
            except Exception as e:
                logger.error(f"Error in scheduled task: {e}")
            time.sleep(interval)

    thread = threading.Thread(target=wrapper, daemon=True)
    thread.start()
    logger.info(f"Scheduled task {task.__name__} to run every {interval} seconds.")
