# src/sync/sync_endpoints.py

from flask import Blueprint, jsonify, request

from src.sync.delta_sync_manager import calculate_delta, update_local_data
from src.utils.redis_client import redis_client
from src.sync.sync_manager import synchronize_data, log_sync_event
from src.crud.task_crud import get_all_tasks, add_task
import json
import logging

from src.utils.time_sync import get_server_time

logger = logging.getLogger("SyncNote")

sync_blueprint = Blueprint('sync', __name__)

@sync_blueprint.route('/sync/delta', methods=['POST'])
def sync_delta():
    """Synchronize only the data that has changed."""
    try:
        data = request.json
        local_tasks = get_all_tasks(redis_client)
        deltas = calculate_delta(local_tasks, data.get("tasks", []))

        if deltas:
            update_local_data(redis_client, deltas)

        return jsonify({"message": "Delta sync completed", "deltas": deltas}), 200
    except Exception as e:
        logger.error(f"Delta sync failed: {e}")
        return jsonify({"error": "Delta sync failed"}), 500

@sync_blueprint.route('/sync/time', methods=['GET'])
def sync_time():
    """Get server time for synchronization."""
    try:
        server_time = get_server_time()
        return jsonify({"server_time": server_time}), 200
    except Exception as e:
        logger.error(f"Time sync failed: {e}")
        return jsonify({"error": "Time sync failed"}), 500

@sync_blueprint.route('/sync/tasks', methods=['GET'])
def sync_tasks():
    """Retrieve the latest tasks from the server."""
    try:
        tasks = get_all_tasks(redis_client)
        log_sync_event(redis_client, "Sync", "Tasks retrieved successfully")
        return jsonify(tasks), 200
    except Exception as e:
        log_sync_event(redis_client, "Error", f"Failed to sync tasks: {str(e)}")
        logger.error(f"Sync tasks failed: {e}")
        return jsonify({"error": "Sync failed"}), 500

@sync_blueprint.route('/sync/update', methods=['POST'])
def sync_update():
    """Update tasks from the mobile client."""
    try:
        data = request.json
        local_tasks = get_all_tasks(redis_client)
        synced_tasks = synchronize_data(local_tasks, data.get("tasks", []))

        # Clear existing tasks and update with synchronized tasks
        redis_client.delete("tasks")
        for task in synced_tasks:
            add_task(redis_client, task)

        log_sync_event(redis_client, "Sync", "Tasks updated successfully")
        logger.info("Tasks synchronized from mobile client")
        return jsonify({"message": "Tasks synchronized"}), 200
    except Exception as e:
        log_sync_event(redis_client, "Error", f"Failed to update tasks: {str(e)}")
        logger.error(f"Update tasks failed: {e}")
        return jsonify({"error": "Update failed"}), 500

@sync_blueprint.route('/sync/status', methods=['GET'])
def sync_status():
    """Check the synchronization status."""
    try:
        logs = redis_client.lrange("sync_logs", 0, -1)
        log_sync_event(redis_client, "Info", "Sync status accessed")
        return jsonify([json.loads(log) for log in logs]), 200
    except Exception as e:
        log_sync_event(redis_client, "Error", f"Failed to retrieve sync status: {str(e)}")
        logger.error(f"Sync status retrieval failed: {e}")
        return jsonify({"error": "Status retrieval failed"}), 500
