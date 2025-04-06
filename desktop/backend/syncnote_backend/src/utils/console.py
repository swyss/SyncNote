# src/utils/console.py

def print_message(message, color="gray"):
    """Prints a message with the specified color."""
    colors = {
        "gray": "\033[90m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    print(f"{colors.get(color, colors['gray'])}{message}{colors['reset']}")

def print_ascii_art(text):
    """Print ASCII art with a standard color."""
    print_message(f"\n    =======================================\n"
                 f"        {text} - Task & Password Manager\n"
                 f"    =======================================", "blue")
