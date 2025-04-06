# src/core/config_manager.py
import json
import logging

SYNCNOTE_LOGGER_NAME = "SyncNote"


def read_config_file(file_path, logger=None):
    """Read configuration from a file."""
    if logger is None:
        logger = logging.getLogger(SYNCNOTE_LOGGER_NAME)
    try:
        with open(file_path, "r") as file:
            config = json.load(file)
            logger.info(f"Configuration successfully loaded from {file_path}")
            return config
    except Exception as e:
        return handle_config_error(file_path, e, logger)


def handle_config_error(file_path, error, logger):
    """Handle errors during the configuration loading process."""
    logger.error(f"Failed to load configuration from {file_path}: {error}")
    return {}


def reload_config_file(file_path, logger=None):
    """Reload configuration dynamically."""
    return read_config_file(file_path, logger)
