from typing import Optional
from uuid import UUID, uuid4
from datetime import date
from enum import Enum
from pydantic import BaseModel

# Using enum for status and priority
class Status(Enum):
    InProgress = "InProgress"
    Completed = "Completed"

class Priority(Enum):
    High = "High"
    Medium = "Medium"
    Low = "Low"


class Task:
    def __init__(self, title: str, description: str = "No description provided", due_date: date = date.today(), 
                 status: Status = Status.InProgress, priority: Priority = None):
        self.task_id = uuid4()
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority

    #To represent the task
    def task_dict(self):
        return {
            "task_id": str(self.task_id),
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status.value,
            "priority": self.priority.value if self.priority else None,
        }

class TaskModel(BaseModel):
    title: str
    description: str = "No description provided"
    due_date: date
    status: Status
    priority: Priority = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[Status] = None
    priority: Optional[Priority] = None