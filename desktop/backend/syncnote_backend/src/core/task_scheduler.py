# src/core/task_scheduler.py
import threading
import time
import logging
from typing import Callable, Any

# Logger specifically for task scheduling
task_logger = logging.getLogger("SyncNote")

# Constants
DEFAULT_DAEMON_SETTING = True


def execute_task_with_logging(task: Callable[..., Any], *args: Any) -> None:
    """Execute a task and handle logging for errors."""
    task_logger.info(f"Running scheduled task: {task.__name__}")
    try:
        task(*args)
    except Exception as e:
        task_logger.error(f"Error in scheduled task '{task.__name__}': {e}")


def schedule_task(interval: float, task: Callable[..., Any], *args: Any) -> None:
    """Schedule a task to run repeatedly at a specified interval."""

    def schedule_runner() -> None:
        while True:
            execute_task_with_logging(task, *args)
            time.sleep(interval)

    thread = threading.Thread(target=schedule_runner, daemon=DEFAULT_DAEMON_SETTING)
    thread.start()
    task_logger.info(f"Scheduled task '{task.__name__}' to run every {interval} seconds.")
