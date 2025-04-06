from flask import Flask
from flask_socketio import SocketIO
from threading import Thread
from src.utils.console import print_ascii_art, print_message
from src.utils.logger import setup_logger
from src.config.config_loader import load_config
from src.utils.redis_client import redis_client
from src.sync.sync_endpoints import sync_blueprint
from src.utils.file_checker import print_file_paths_once

# Constants
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 5000
CONFIG_PATH = "src/config/config.json"
LOG_PATH = "logs/syncnote.log"
APP_NAME = "SyncNote"
REDIS_CONNECTED_MESSAGE = "Redis client connected successfully."
REDIS_ERROR_MESSAGE = "[ERROR] Redis client initialization failed. Please check the configuration."


def get_redis_status_message(redis_client) -> tuple[str, str]:
    """Returns Redis connection status message."""
    if redis_client:
        return REDIS_CONNECTED_MESSAGE, "green"
    else:
        return REDIS_ERROR_MESSAGE, "red"


def register_routes(app, logger):
    """Registers routes to the Flask app."""

    @app.route('/', methods=['GET'])
    def home():
        """Home endpoint to confirm server is running."""
        logger.info("Home endpoint accessed")
        return {"message": "Welcome to SyncNote Backend"}, 200


def initialize_flask_app():
    """Initializes the Flask app and performs setup."""
    # App and SocketIO setup
    app = Flask(__name__)
    socketio = SocketIO(app)

    # Logger, Config, and Redis setup
    logger = setup_logger(APP_NAME)
    config = load_config()
    redis_message, message_color = get_redis_status_message(redis_client)
    print_message(redis_message, message_color)

    # Additional setup
    print_file_paths_once(CONFIG_PATH, LOG_PATH)
    app.register_blueprint(sync_blueprint)
    register_routes(app, logger)

    return app, socketio, config, logger


def launch_console_manager(logger):
    """Launches the console manager in a separate thread."""
    logger.info("Starting Console Manager")
    print_message("Starting Console Manager", "gray")


if __name__ == '__main__':
    # ASCII art and app initialization
    print_ascii_art(APP_NAME)
    app, socketio, config, logger = initialize_flask_app()
    logger.info(f"Initializing {APP_NAME} Backend")

    # Start Console Manager
    Thread(target=launch_console_manager, args=(logger,), daemon=True).start()

    # Start Backend
    print_message(f"Starting {APP_NAME} Backend", "gray")
    try:
        socketio.run(app, host=DEFAULT_HOST, port=config.get("PORT", DEFAULT_PORT), allow_unsafe_werkzeug=True)
    except Exception as e:
        logger.error(f"Error starting backend: {e}")
        print_message(f"[ERROR] Error starting backend: {e}", "red")
