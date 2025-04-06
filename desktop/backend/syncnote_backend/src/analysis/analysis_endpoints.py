# src/analysis/analysis_endpoints.py

from flask import Blueprint, jsonify
from src.utils.redis_client import redis_client
from src.analysis.analysis_manager import calculate_completion_rate, average_completion_time
from src.crud.task_crud import get_all_tasks

analysis_blueprint = Blueprint('analysis', __name__)

@analysis_blueprint.route('/analysis/completion_rate', methods=['GET'])
def get_completion_rate():
    """Get the task completion rate."""
    tasks = get_all_tasks(redis_client)
    result = calculate_completion_rate(tasks)
    return jsonify(result), 200

@analysis_blueprint.route('/analysis/average_time', methods=['GET'])
def get_average_time():
    """Get the average time taken to complete tasks."""
    tasks = get_all_tasks(redis_client)
    result = average_completion_time(tasks)
    return jsonify(result), 200
