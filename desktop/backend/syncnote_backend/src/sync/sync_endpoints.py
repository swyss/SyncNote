# src/sync/sync_endpoints.py
from flask import Blueprint, jsonify
from src.utils.error_handler import handle_error

sync_blueprint = Blueprint('sync', __name__)

@sync_blueprint.route('/sync/tasks', methods=['GET'])
def sync_tasks():
    try:
        return jsonify({"message": "Task synchronization endpoint"}), 200
    except Exception as e:
        return handle_error(e)

@sync_blueprint.route('/sync/reminders', methods=['GET'])
def sync_reminders():
    try:
        return jsonify({"message": "Reminder synchronization endpoint"}), 200
    except Exception as e:
        return handle_error(e)

@sync_blueprint.route('/sync/passwords', methods=['GET'])
def sync_passwords():
    try:
        return jsonify({"message": "Password synchronization endpoint"}), 200
    except Exception as e:
        return handle_error(e)
