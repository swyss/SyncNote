# src/config/config_loader.py
import json
import logging
from src.utils.file_checker import ensure_directory_exists, ensure_file_exists, print_file_paths_once

logger = logging.getLogger("SyncNote")

CONFIG_PATH = "src/config/config.json"
LOG_DIR = "logs"
LOG_FILE = f"{LOG_DIR}/syncnote.log"
DEFAULT_CONFIG = {
    "PORT": 5000,
    "REDIS_HOST": "localhost",
    "REDIS_PORT": 6379,
    "REDIS_DB": 0,
    "LOG_LEVEL": "INFO",
    "LOG_FILE": "logs/syncnote.log"
}


def initialize_default_config():
    """Ensure required directories and files exist."""
    ensure_directory_exists("src/config")
    ensure_directory_exists(LOG_DIR)
    ensure_file_exists(CONFIG_PATH, json.dumps(DEFAULT_CONFIG, indent=4))
    ensure_file_exists(LOG_FILE)


def handle_load_config_error(exc):
    """Log and handle configuration loading-related errors."""
    logger.error(f"Error loading configuration: {str(exc)}")
    return {}


def load_config():
    """Load configuration from the config file."""
    initialize_default_config()
    try:
        with open(CONFIG_PATH, "r") as file:
            config_file_content = json.load(file)
            logger.info("Configuration loaded successfully.")
            log_config_file_paths()
            return config_file_content
    except FileNotFoundError:
        logger.error("Configuration file not found.")
        return {}
    except Exception as e:
        return handle_load_config_error(e)


def log_config_file_paths():
    """Log configuration and log file paths (once)."""
    print_file_paths_once(CONFIG_PATH, LOG_FILE)
