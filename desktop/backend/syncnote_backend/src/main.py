# src/main.py
from flask import Flask
from flask_socketio import SocketIO
from src.utils.console import print_ascii_art, print_message
from src.utils.logger import setup_logger
from src.config.config_loader import load_config
from src.utils.redis_client import redis_client
from src.message.notifier import start_notification_service
from src.sync.sync_endpoints import sync_blueprint
from src.utils.error_handler import handle_error
from src.utils.file_checker import print_file_paths_once
from threading import Thread

# Initialize application and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Setup logger
logger = setup_logger("SyncNote")

# Load configuration
config = load_config()

# Display file paths only once
print_file_paths_once("src/config/config.json", "logs/syncnote.log")

def start_console():
    """Start the console manager in a separate thread."""
    logger.info("Starting Console Manager")
    print_message("Starting Console Manager", "gray")

def start_backend():
    """Start the SyncNote Backend."""
    print_message("Starting SyncNote Backend", "gray")
    try:
        socketio.run(app, host="0.0.0.0", port=config.get("PORT", 5000), allow_unsafe_werkzeug=True)
    except Exception as e:
        logger.error(f"Error starting backend: {e}")
        print_message(f"[ERROR] Error starting backend: {e}", "red")

# Start Redis client with error handling
if redis_client:
    print_message("Redis client connected successfully.", "green")
else:
    print_message("[ERROR] Redis client initialization failed. Please check the configuration.", "red")

# Register API blueprints
app.register_blueprint(sync_blueprint)

@app.route('/', methods=['GET'])
def home():
    """Home endpoint to confirm server is running"""
    logger.info("Home endpoint accessed")
    return {"message": "Welcome to SyncNote Backend"}, 200

if __name__ == '__main__':
    print_ascii_art("SyncNote")
    logger.info("Initializing SyncNote Backend")

    # Start Console Manager in a separate thread
    Thread(target=start_console, daemon=True).start()

    # Start Backend
    start_backend()
