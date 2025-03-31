# src/sync/sync_endpoints.py
from flask import Blueprint, jsonify, request
from src.crud.task_crud import add_task, get_all_tasks, update_task, delete_task
from src.crud.reminder_crud import add_reminder, get_all_reminders, delete_reminder
from src.models.task import Task
from src.models.reminder import Reminder

sync_blueprint = Blueprint('sync', __name__)

@sync_blueprint.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = Task.from_dict(data)
    add_task(redis_client, task)
    return jsonify({"message": "Task created successfully"}), 201

@sync_blueprint.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = get_all_tasks(redis_client)
    return jsonify(tasks), 200

@sync_blueprint.route('/tasks/<int:index>', methods=['PUT'])
def update_task_endpoint(index):
    data = request.json
    task = Task.from_dict(data)
    success = update_task(redis_client, index, task)
    if success:
        return jsonify({"message": "Task updated successfully"}), 200
    return jsonify({"message": "Task not found"}), 404

@sync_blueprint.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task_endpoint(index):
    success = delete_task(redis_client, index)
    if success:
        return jsonify({"message": "Task deleted successfully"}), 200
    return jsonify({"message": "Task not found"}), 404
