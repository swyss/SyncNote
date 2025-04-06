# src/core/module_controller.py
import json
import subprocess
import logging
from typing import Dict, Any

# Logging setup
logger = logging.getLogger("SyncNote")

# Global variables
running_processes: Dict[str, subprocess.Popen] = {}

# ANSI color codes
COLOR_SUCCESS = "\033[92m"
COLOR_ERROR = "\033[91m"
COLOR_WARNING = "\033[93m"
COLOR_RESET = "\033[0m"


def _print_colored_message(message: str, color: str) -> None:
    """Utility function to print a colored message to the console."""
    print(f"{color}{message}{COLOR_RESET}")


def _log_module_status(message: str, module_name: str, is_error: bool = False) -> None:
    """Log and print module status
