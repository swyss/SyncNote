# src/core/module_controller.py

import json
import subprocess
import logging

logger = logging.getLogger("SyncNote")
running_processes = {}

def load_modules():
    """Load modules from the configuration file."""
    try:
        with open("./config/modules.json", "r") as file:
            modules = json.load(file)
            logger.info("Modules loaded successfully from configuration")
            return modules
    except Exception as e:
        logger.error(f"Error loading modules: {e}")
        return {}

modules = load_modules()

def start_module(module_name):
    """Start a specified module."""
    try:
        module = modules.get(module_name)
        if module:
            command = f"python {module['path']}"
            process = subprocess.Popen(command, shell=True)
            running_processes[module_name] = process
            logger.info(f"Started {module_name}")
            print(f"\033[92m[STARTED] {module_name}\033[0m")
        else:
            logger.error(f"Module {module_name} not found")
            print(f"\033[91m[ERROR] {module_name} not found\033[0m")
    except Exception as e:
        logger.error(f"Error starting module {module_name}: {e}")

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

def list_modules():
    """List all available modules and their statuses."""
    for module_name, info in modules.items():
        status = "running" if module_name in running_processes else "stopped"
        color = "\033[92m" if status == "running" else "\033[91m"
        print(f"{color}{module_name} - {status} - {info['description']}\033[0m")
