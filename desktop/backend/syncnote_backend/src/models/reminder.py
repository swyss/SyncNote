# src/models/reminder.py

from datetime import datetime

class Reminder:
    def __init__(self, message, due_date):
        self.message = message
        self.due_date = due_date
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "message": self.message,
            "due_date": self.due_date,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return Reminder(
            message=data.get("message"),
            due_date=data.get("due_date")
        )
