
from typing import Optional
from uuid import UUID,uuid4
from pydantic import *
from Model.Enum.enums import *


class Task:
    def __init__(self, task_id: UUID, title: str, description: str, due_date: str, status: str, priority: Optional[PriorityEnum] = None):
        self.task_id = task_id
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