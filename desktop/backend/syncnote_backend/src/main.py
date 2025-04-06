from flask import Flask
from flask_socketio import SocketIO
from threading import Thread

# Utils imports
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


def initialize_app():
    """Initialisiert die Flask-App und führt die vorbereitenden Schritte aus."""
    # App und SocketIO-Setup
    app = Flask(__name__)
    socketio = SocketIO(app)

    # Logger, Config & Redis
    logger = setup_logger("SyncNote")
    config = load_config()
    redis_status = redis_client is not None
    redis_message = "Redis client connected successfully." if redis_status else "[ERROR] Redis client initialization failed. Please check the configuration."
    print_message(redis_message, "green" if redis_status else "red")

    # Weitere Initialisierung
    print_file_paths_once(CONFIG_PATH, LOG_PATH)
    app.register_blueprint(sync_blueprint)

    @app.route('/', methods=['GET'])
    def home():
        """Home endpoint to confirm server is running"""
        logger.info("Home endpoint accessed")
        return {"message": "Welcome to SyncNote Backend"}, 200

    return app, socketio, config, logger


def start_console_manager(logger):
    """Startet den Konsolenmanager in einem separaten Thread."""
    logger.info("Starting Console Manager")
    print_message("Starting Console Manager", "gray")


if __name__ == '__main__':
    print_ascii_art("SyncNote")
    app, socketio, config, logger = initialize_app()
    logger.info("Initializing SyncNote Backend")

    # Start Console Manager
    Thread(target=start_console_manager, args=(logger,), daemon=True).start()

    # Start Backend
    print_message("Starting SyncNote Backend", "gray")
    try:
        socketio.run(app, host=DEFAULT_HOST, port=config.get("PORT", DEFAULT_PORT), allow_unsafe_werkzeug=True)
    except Exception as e:
        logger.error(f"Error starting backend: {e}")
        print_message(f"[ERROR] Error starting backend: {e}", "red")
