# src/models/task.py

from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class Task:
    title: str
    description: str
    priority: str = "Medium"
    category: str = "General"
    recurrence: str = "None"
    completed: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        """Convert the Task instance to a dictionary."""
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "category": self.category,
            "recurrence": self.recurrence,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data: dict):
        """Create a Task instance from a dictionary."""
        return Task(
            title=data.get("title", ""),
            description=data.get("description", ""),
            priority=data.get("priority", "Medium"),
            category=data.get("category", "General"),
            recurrence=data.get("recurrence", "None"),
            completed=data.get("completed", False),
            created_at=data.get("created_at", datetime.now().isoformat())
        )

    def validate(self) -> bool:
        """Validate task data."""
        valid_priorities = ["Low", "Medium", "High"]
        valid_categories = ["General", "Work", "Personal"]
        valid_recurrences = ["None", "Daily", "Weekly", "Monthly"]

        if self.priority not in valid_priorities:
            return False
        if self.category not in valid_categories:
            return False
        if self.recurrence not in valid_recurrences:
            return False
        return True
