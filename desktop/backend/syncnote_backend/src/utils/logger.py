# src/utils/logger.py
import logging
from src.config.config_loader import LOG_FILE

def setup_logger(name):
    """Set up a logger with file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create file handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.INFO)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Define log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
