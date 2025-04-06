# src/utils/console_manager.py
from src.core.health_check import check_database
from src.core.monitoring import get_system_metrics
from src.core.module_controller import start_module, stop_module, list_modules
from src.utils.console import print_message

def print_console_menu():
    """Print the enhanced console management menu."""
    print_message("\n--- SyncNote Console Management ---", "blue")
    print_message("1. Start a Module", "gray")
    print_message("2. Stop a Module", "gray")
    print_message("3. List All Modules", "gray")
    print_message("4. Health Check", "gray")
    print_message("5. Show System Metrics", "gray")
    print_message("0. Exit", "gray")
    print_message("-----------------------------------", "blue")

def handle_choice(choice, redis_client):
    """Handle user input for the console menu."""
    if choice == "1":
        module_name = input("Enter module name to start: ")
        start_module(module_name)
    elif choice == "2":
        module_name = input("Enter module name to stop: ")
        stop_module(module_name)
    elif choice == "3":
        list_modules()
    elif choice == "4":
        print_message("Performing health check...", "gray")
        print_message(check_database(), "green")
    elif choice == "5":
        print_message("System Metrics:", "blue")
        print_message(str(get_system_metrics()), "gray")
    elif choice == "0":
        print_message("Exiting Console Manager...", "gray")
        exit(0)
    else:
        print_message("Invalid choice. Please try again.", "red")

def console_manager(redis_client):
    """Start the enhanced console management loop."""
    while True:
        print_console_menu()
        choice = input("Select an option: ")
        handle_choice(choice, redis_client)
