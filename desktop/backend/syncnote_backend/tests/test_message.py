# tests/test_message.py
import pytest
from src.message.message_storage import store_message, get_all_messages
from src.message.message_handler import reminder_message

def test_store_message(redis_client):
    store_message(redis_client, "reminder", "Meeting at 3 PM")
    messages = get_all_messages(redis_client)
    assert len(messages) > 0
    assert messages[-1]["type"] == "reminder"
    assert messages[-1]["content"] == "Meeting at 3 PM"

def test_reminder_message():
    message = reminder_message("Don't forget to check in")
    assert "[REMINDER]" in message
    assert "Don't forget to check in" in message
