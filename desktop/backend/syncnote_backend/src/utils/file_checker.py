# src/utils/file_checker.py
import os
import logging

logger = logging.getLogger("SyncNote")

def ensure_directory_exists(directory):
    """Ensure that the specified directory exists."""
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            logger.info(f"Directory created: {directory}")
        except Exception as e:
            logger.error(f"Error creating directory {directory}: {e}")

def ensure_file_exists(filepath, default_content=""):
    """Ensure that the specified file exists."""
    if not os.path.isfile(filepath):
        try:
            with open(filepath, "w") as file:
                file.write(default_content)
            logger.info(f"File created: {filepath}")
        except Exception as e:
            logger.error(f"Error creating file {filepath}: {e}")

def print_file_paths_once(config_path, log_path):
    """Prints the paths of configuration and log files only once."""
    logger.info(f"Configuration file path: {config_path}")
    logger.info(f"Log file path: {log_path}")
    print(f"Configuration file path: {config_path}")
    print(f"Log file path: {log_path}")
