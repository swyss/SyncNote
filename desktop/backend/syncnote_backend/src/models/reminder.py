# src/models/reminder.py

from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class Reminder:
    message: str
    due_date: str
    priority: str = "Normal"
    recurrence: str = "None"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        """Convert the Reminder instance to a dictionary."""
        return {
            "message": self.message,
            "due_date": self.due_date,
            "priority": self.priority,
            "recurrence": self.recurrence,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data: dict):
        """Create a Reminder instance from a dictionary."""
        return Reminder(
            message=data.get("message", ""),
            due_date=data.get("due_date", ""),
            priority=data.get("priority", "Normal"),
            recurrence=data.get("recurrence", "None"),
            created_at=data.get("created_at", datetime.now().isoformat())
        )

    def validate(self) -> bool:
        """Validate reminder data."""
        valid_priorities = ["Low", "Normal", "High"]
        valid_recurrences = ["None", "Daily", "Weekly", "Monthly"]

        if self.priority not in valid_priorities:
            return False
        if self.recurrence not in valid_recurrences:
            return False
        try:
            datetime.fromisoformat(self.due_date)
            return True
        except ValueError:
            return False
