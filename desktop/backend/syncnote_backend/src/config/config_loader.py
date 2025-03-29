# src/config/config_loader.py
import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    return {
        "REDIS_HOST": os.getenv("REDIS_HOST", "localhost"),
        "REDIS_PORT": int(os.getenv("REDIS_PORT", 6379)),
        "PORT": int(os.getenv("PORT", 5000)),
        "SECRET_KEY": os.getenv("SECRET_KEY", "supersecretkey")
    }
