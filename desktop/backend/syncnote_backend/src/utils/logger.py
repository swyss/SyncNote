# src/utils/logger.py

import logging
import os
from datetime import datetime

# ANSI escape codes for colored output
COLORS = {
    "ERROR": "\033[91m",   # Red
    "INFO": "\033[92m",    # Green
    "WARNING": "\033[93m", # Yellow
    "DEBUG": "\033[97m",   # White (neutral)
    "DEFAULT": "\033[97m", # Default white for general output
    "RESET": "\033[0m"     # Reset to default
}

def setup_logger(name):
    # Ensure the logs directory exists
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        print(f"{COLORS['INFO']}[INFO] Created logs directory: {log_dir}{COLORS['RESET']}")

    # Set up the logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Capture all levels

    # Create file handler with a date-based filename
    log_filename = f"{log_dir}/{datetime.now().strftime('%Y-%m-%d')}.log"
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)

    # Create console handler for output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Formatter with color support
    class ColorFormatter(logging.Formatter):
        def format(self, record):
            levelname = record.levelname
            color = COLORS.get(levelname, COLORS["DEFAULT"])
            record.msg = f"{color}{record.msg}{COLORS['RESET']}"
            return super().format(record)

    # Create a log formatter
    formatter = ColorFormatter('%(asctime)s - %(levelname)s - %(message)s')

    # Apply the formatter to handlers
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Usage example
logger = setup_logger("SyncNote")
logger.info("Logger initialized successfully.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.debug("This is a debug message.")
