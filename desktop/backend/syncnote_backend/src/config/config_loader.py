# src/config/config_loader.py
import json
import logging
from src.utils.file_checker import ensure_directory_exists, ensure_file_exists, print_file_paths_once

logger = logging.getLogger("SyncNote")

CONFIG_PATH = "src/config/config.json"
LOG_DIR = "logs"
LOG_FILE = f"{LOG_DIR}/syncnote.log"

def load_config():
    """Load configuration from the config file."""
    ensure_directory_exists("src/config")
    ensure_directory_exists(LOG_DIR)
    ensure_file_exists(CONFIG_PATH, '{"PORT": 5000, "REDIS_HOST": "localhost", "REDIS_PORT": 6379, "REDIS_DB": 0, "LOG_LEVEL": "INFO", "LOG_FILE": "logs/syncnote.log"}')
    ensure_file_exists(LOG_FILE)

    try:
        with open(CONFIG_PATH, "r") as file:
            config = json.load(file)
            logger.info("Configuration loaded successfully.")
            print_file_paths_once(CONFIG_PATH, LOG_FILE)
            return config
    except FileNotFoundError:
        logger.error("Configuration file not found.")
        return {}
    except Exception as e:
        logger.error(f"Error loading configuration: {e}")
        return {}
