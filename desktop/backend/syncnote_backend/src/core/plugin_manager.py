# src/core/plugin_manager.py

import importlib
import logging

logger = logging.getLogger("SyncNote")

def load_plugin(plugin_name):
    """Dynamically load a plugin module."""
    try:
        module = importlib.import_module(plugin_name)
        logger.info(f"Plugin {plugin_name} loaded successfully.")
        return module
    except Exception as e:
        logger.error(f"Error loading plugin {plugin_name}: {e}")
        return None
