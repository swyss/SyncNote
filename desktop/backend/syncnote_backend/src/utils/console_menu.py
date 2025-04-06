# src/utils/console_menu.py

from src.utils.module_manager import start_module, stop_module, list_modules, module_status
from src.analysis.analysis_manager import calculate_completion_rate
from src.crud.task_crud import get_all_tasks
import logging

logger = logging.getLogger("SyncNote")

def print_menu():
    """Print the console management menu."""
    print("\n\033[94m--- SyncNote Console Management ---\033[0m")
    print("1. Start a Module")
    print("2. Stop a Module")
    print("3. Show Module Status")
    print("4. List All Modules")
    print("5. Show Tasks")
    print("6. Show Analysis")
    print("0. Exit")
    print("\033[94m-----------------------------------\033[0m")

def handle_choice(choice, redis_client):
    """Handle user input for the menu."""
    if choice == "1":
        module_name = input("Enter module name to start: ")
        start_module(module_name)
    elif choice == "2":
        module_name = input("Enter module name to stop: ")
        stop_module(module_name)
    elif choice == "3":
        module_name = input("Enter module name for status: ")
        print(f"{module_name} status: {module_status(module_name)}")
    elif choice == "4":
        list_modules()
    elif choice == "5":
        tasks = get_all_tasks(redis_client)
        for task in tasks:
            print(f"Title: {task['title']} - Completed: {task['completed']}")
    elif choice == "6":
        tasks = get_all_tasks(redis_client)
        analysis = calculate_completion_rate(tasks)
        print(f"Completion Rate: {analysis['completion_rate']}%")
    elif choice == "0":
        print("Exiting Console Manager...")
        exit(0)
    else:
        print("\033[91mInvalid choice. Please try again.\033[0m")

def console_manager(redis_client):
    """Start the console management loop."""
    while True:
        print_menu()
        choice = input("Select an option: ")
        handle_choice(choice, redis_client)
