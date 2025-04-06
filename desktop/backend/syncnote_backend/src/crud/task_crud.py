# src/crud/task_crud.py

import json
import logging

logger = logging.getLogger("SyncNote")

def add_task(redis_client, task):
    try:
        redis_client.rpush("tasks", json.dumps(task.to_dict()))
        logger.info("Task added successfully")
        return {"success": True, "message": "Task added"}
    except Exception as e:
        logger.error(f"Failed to add task: {e}")
        return {"success": False, "message": str(e)}

def get_all_tasks(redis_client):
    try:
        tasks = redis_client.lrange("tasks", 0, -1)
        logger.info(f"Fetched {len(tasks)} tasks")
        return [json.loads(task) for task in tasks]
    except Exception as e:
        logger.error(f"Failed to retrieve tasks: {e}")
        return []

def update_task(redis_client, index, updated_task):
    try:
        redis_client.lset("tasks", index, json.dumps(updated_task.to_dict()))
        logger.info(f"Task at index {index} updated successfully")
        return {"success": True, "message": "Task updated"}
    except Exception as e:
        logger.error(f"Failed to update task at index {index}: {e}")
        return {"success": False, "message": str(e)}

def delete_task(redis_client, index):
    try:
        redis_client.lset("tasks", index, "__deleted__")
        redis_client.lrem("tasks", 0, "__deleted__")
        logger.info(f"Task at index {index} deleted successfully")
        return {"success": True, "message": "Task deleted"}
    except Exception as e:
        logger.error(f"Failed to delete task at index {index}: {e}")
        return {"success": False, "message": str(e)}
