# src/core/config_manager.py

import json
import logging

logger = logging.getLogger("SyncNote")

def load_config(file_path):
    """Load configuration from a file."""
    try:
        with open(file_path, "r") as file:
            config = json.load(file)
            logger.info(f"Configuration loaded from {file_path}")
            return config
    except Exception as e:
        logger.error(f"Error loading config: {e}")
        return {}

def reload_config(file_path):
    """Reload configuration dynamically."""
    return load_config(file_path)
