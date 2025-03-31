# src/utils/redis_client.py
from src.config.config_loader import load_config
from src.database.redis_manager import init_redis

# Load configuration
config = load_config()

# Initialize Redis client
redis_client = init_redis(config)
