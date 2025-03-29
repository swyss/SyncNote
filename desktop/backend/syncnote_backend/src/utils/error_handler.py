# src/utils/error_handler.py

def handle_error(error):
    error_message = {
        "error": str(error),
        "message": "An error occurred during the request",
        "status": "failure"
    }
    print(f"[ERROR] {str(error)}")
    return error_message, 500
