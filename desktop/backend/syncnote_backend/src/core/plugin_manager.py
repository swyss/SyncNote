# src/core/plugin_manager.py
import importlib
import logging

PLUGIN_LOGGER_NAME = "SyncNote"
logger = logging.getLogger(PLUGIN_LOGGER_NAME)


def log_error_with_trace(message, exception):
    """Logs an error message with the exception's stack trace."""
    logger.error(f"{message}: {exception}", exc_info=True)


def load_plugin_module(plugin_name):
    """Dynamically load a plugin module."""
    try:
        module = importlib.import_module(plugin_name)
        logger.info(f"Plugin {plugin_name} loaded successfully.")
        return module
    except Exception as e:
        log_error_with_trace(f"Error loading plugin {plugin_name}", e)
        return None
