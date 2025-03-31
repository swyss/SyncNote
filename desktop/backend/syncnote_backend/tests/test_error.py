# tests/test_error.py
from src.utils.error_handler import handle_error

def test_handle_error():
    error = Exception("Test error")
    response, status = handle_error(error)
    assert status == 500
    assert response["status"] == "failure"
    assert response["message"] == "An error occurred during the request"
