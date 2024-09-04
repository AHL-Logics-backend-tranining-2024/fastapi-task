from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from uuid import UUID, uuid4


class TaskModel(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[str] = "..."


class Task(TaskModel):
    task_id: UUID = Field(default_factory=uuid4)


class UrgentTask(TaskModel):
    task_id: UUID = Field(default_factory=uuid4)
    priority: str
