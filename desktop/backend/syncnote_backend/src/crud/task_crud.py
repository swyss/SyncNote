# src/crud/task_crud.py

import json

def add_task(redis_client, task):
    redis_client.rpush("tasks", json.dumps(task.to_dict()))

def get_all_tasks(redis_client):
    tasks = redis_client.lrange("tasks", 0, -1)
    return [json.loads(task) for task in tasks]

def update_task(redis_client, index, updated_task):
    try:
        redis_client.lset("tasks", index, json.dumps(updated_task.to_dict()))
        return True
    except Exception:
        return False

def delete_task(redis_client, index):
    try:
        redis_client.lset("tasks", index, "__deleted__")
        redis_client.lrem("tasks", 0, "__deleted__")
        return True
    except Exception:
        return False
