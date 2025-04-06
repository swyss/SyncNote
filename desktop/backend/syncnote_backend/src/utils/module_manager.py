# src/utils/module_manager.py

import logging
import subprocess

logger = logging.getLogger("SyncNote")

services = {
    "SyncService": "python src/main.py",
    "NotificationService": "python src/message/notifier.py",
    "AnalysisService": "python src/analysis/analysis_endpoints.py",
}

running_processes = {}

def start_module(module_name):
    """Start a specified module."""
    try:
        command = services.get(module_name)
        if command:
            process = subprocess.Popen(command, shell=True)
            running_processes[module_name] = process
            logger.info(f"Started {module_name}")
            print(f"\033[92m[STARTED] {module_name}\033[0m")
        else:
            logger.error(f"Module {module_name} not found")
    except Exception as e:
        logger.error(f"Error starting module {module_name}: {e}")
        print(f"\033[91m[ERROR] Could not start {module_name}\033[0m")

def stop_module(module_name):
    """Stop a specified module."""
    try:
        process = running_processes.get(module_name)
        if process:
            process.terminate()
            del running_processes[module_name]
            logger.info(f"Stopped {module_name}")
            print(f"\033[93m[STOPPED] {module_name}\033[0m")
        else:
            logger.warning(f"Module {module_name} not running")
    except Exception as e:
        logger.error(f"Error stopping module {module_name}: {e}")
        print(f"\033[91m[ERROR] Could not stop {module_name}\033[0m")

def module_status(module_name):
    """Check the status of a specified module."""
    process = running_processes.get(module_name)
    if process and process.poll() is None:
        return "running"
    return "stopped"

def list_modules():
    """List all available modules and their statuses."""
    for module in services.keys():
        status = module_status(module)
        color = "\033[92m" if status == "running" else "\033[91m"
        print(f"{color}{module} - {status}\033[0m")
