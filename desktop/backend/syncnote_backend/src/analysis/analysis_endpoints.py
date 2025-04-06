# src/analysis/analysis_endpoints.py
from flask import Blueprint, jsonify
from src.utils.redis_client import redis_client
from src.analysis.analysis_manager import calculate_completion_rate, average_completion_time
from src.crud.task_crud import get_all_tasks

analysis_blueprint = Blueprint('analysis', __name__)


def process_tasks(task_processor):
    """Fetch tasks and process them with the provided function."""
    tasks = get_all_tasks(redis_client)
    return task_processor(tasks)


@analysis_blueprint.route('/analysis/completion_rate', methods=['GET'])
def get_completion_rate():
    """Get the task completion rate."""
    result = process_tasks(calculate_completion_rate)
    return jsonify(result), 200


@analysis_blueprint.route('/analysis/average_time', methods=['GET'])
def get_average_time():
    """Get the average time taken to complete tasks."""
    result = process_tasks(average_completion_time)
    return jsonify(result), 200
