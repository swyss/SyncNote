# src/analysis/analysis_manager.py
import logging  # Standard library first
from typing import List, Dict, Any  # Standard library typing, second group

# Logger configuration
logger = logging.getLogger("SyncNote")

# Constants
ERROR_MESSAGE_TEMPLATE = "Error in {}: {}"
LOG_COMPLETION_RATE = "Completion rate calculated: {}%"


def safe_division(numerator: float, denominator: float, default: float = 0) -> float:
    """Safely divide two numbers, returning a default value if division by zero occurs."""
    return numerator / denominator if denominator != 0 else default


def log_and_handle_error(source: str, exception: Exception) -> Dict[str, str]:
    """
    Centralized error handling and logging.
    Args:
        source (str): Identifier for the error source (e.g., function name or process).
        exception (Exception): The exception to log and report.
    Returns:
        Dict[str, str]: A dictionary containing the error message.
    """
    error_message = ERROR_MESSAGE_TEMPLATE.format(source, str(exception))
    logger.error(error_message)
    return {"error": str(exception)}


def calculate_completion_rate(task_list: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calculate the completion rate for a list of tasks.
    Args:
        task_list (List[Dict[str, Any]]): A list of tasks, where each task is a dictionary.
    Returns:
        Dict[str, float]: A dictionary containing the completion rate.
    """
    try:
        total_tasks = len(task_list)
        completed_tasks = sum(1 for task in task_list if task.get("completed", False))
        completion_rate = safe_division(completed_tasks * 100, total_tasks)  # Using safe_division
        logger.info(LOG_COMPLETION_RATE.format(completion_rate))
        return {"completion_rate": completion_rate}
    except Exception as e:
        return log_and_handle_error("calculate_completion_rate", e)
