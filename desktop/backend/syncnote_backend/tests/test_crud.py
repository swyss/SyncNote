# tests/test_crud.py
import pytest
from src.models.task import Task
from src.crud.task_crud import add_task, get_all_tasks

def test_add_task(redis_client):
    task = Task("Test Task", "Testing task addition")
    add_task(redis_client, task)
    tasks = get_all_tasks(redis_client)
    assert len(tasks) > 0
    assert tasks[-1]["title"] == "Test Task"
