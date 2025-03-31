# src/models/task.py

from datetime import datetime

class Task:
    def __init__(self, title, description, completed=False, created_at=None):
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data.get("title"),
            description=data.get("description"),
            completed=data.get("completed", False),
            created_at=data.get("created_at")
        )
