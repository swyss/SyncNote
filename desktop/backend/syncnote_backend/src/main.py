# src/main.py
from flask import Flask
from flask_socketio import SocketIO
from src.utils.console import print_ascii_art
from src.utils.error_handler import handle_error
from src.config.config_loader import load_config
from src.database.redis_manager import init_redis
from src.encryption.security import generate_key
from src.sync.sync_endpoints import sync_blueprint
from src.message.message_handler import reminder_message

app = Flask(__name__)
socketio = SocketIO(app)

# Load configuration
config = load_config()

# Initialize Redis database
redis_client = init_redis(config)

# Register Sync Routes
app.register_blueprint(sync_blueprint)

@app.route('/status', methods=['GET'])
def status():
    try:
        return {"status": "SyncNote Backend Running"}, 200
    except Exception as e:
        return handle_error(e)

@app.route('/reminder', methods=['POST'])
def send_reminder():
    try:
        message = reminder_message("Task due today!")
        return {"message": message}, 200
    except Exception as e:
        return handle_error(e)

if __name__ == '__main__':
    print_ascii_art("SyncNote")
    generate_key()
    # Run the app with SocketIO, allowing Werkzeug in development
    socketio.run(app, host="0.0.0.0", port=config["PORT"], allow_unsafe_werkzeug=True)
