# src/main.py
from flask import Flask
from flask_socketio import SocketIO
from src.utils.console import print_ascii_art
from src.utils.logger import setup_logger
from src.config.config_loader import load_config
from src.utils.redis_client import redis_client
from src.message.notifier import start_notification_service
from src.sync.sync_endpoints import sync_blueprint
from src.utils.error_handler import handle_error

# Initialize application and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Setup logger
logger = setup_logger("SyncNote")

# Start notification service if Redis is available
if redis_client:
    start_notification_service(redis_client)
else:
    logger.error("Failed to initialize Redis client. Notification service not started.")

# Register API blueprints
app.register_blueprint(sync_blueprint)

@app.route('/', methods=['GET'])
def home():
    """Home endpoint to confirm server is running"""
    logger.info("Home endpoint accessed")
    return {"message": "Welcome to SyncNote Backend"}, 200

@app.route('/favicon.ico')
def favicon():
    """Return a placeholder response for favicon.ico requests"""
    return "", 204

@app.route('/status', methods=['GET'])
def status():
    """Status endpoint to check if the backend is running"""
    try:
        logger.info("Status endpoint accessed")
        return {"status": "SyncNote Backend Running"}, 200
    except Exception as e:
        logger.error(f"Error at status endpoint: {e}")
        return handle_error(e)

if __name__ == '__main__':
    print_ascii_art("SyncNote")
    logger.info("Starting SyncNote Backend")
    # Run the app with SocketIO, allowing Werkzeug in development
    socketio.run(app, host="0.0.0.0", port=5000, allow_unsafe_werkzeug=True)
