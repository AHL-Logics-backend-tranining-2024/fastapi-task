
import uuid
from Model.Enum.enums import *


class Task:
    def __init__(self, title: str, description: str, due_date: str, status: str):
        self.task_id = uuid.uuid4()  # Automatically generate the UUID
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": str(self.task_id),
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }