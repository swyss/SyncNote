# src/analysis/analysis_manager.py

import json
import logging

logger = logging.getLogger("SyncNote")

def calculate_completion_rate(tasks):
    """Calculate the completion rate of tasks."""
    try:
        total = len(tasks)
        completed = sum(1 for task in tasks if task.get("completed", False))
        completion_rate = (completed / total) * 100 if total > 0 else 0
        logger.info(f"Completion rate calculated: {completion_rate}%")
        return {"completion_rate": completion_rate}
    except Exception as e:
        logger.error(f"Error calculating completion rate: {e}")
        return {"error": str(e)}

def average_completion_time(tasks):
    """Calculate the average time taken to complete tasks."""
    try:
        times = [
            (task['completed_at'] - task['created_at']).total_seconds()
            for task in tasks if task.get("completed", False)
        ]
        average_time = sum(times) / len(times) if times else 0
        logger.info(f"Average completion time calculated: {average_time} seconds")
        return {"average_completion_time": average_time}
    except Exception as e:
        logger.error(f"Error calculating average completion time: {e}")
        return {"error": str(e)}
