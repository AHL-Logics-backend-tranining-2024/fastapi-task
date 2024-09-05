from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import date
from enums import *

class Task(BaseModel):
    task_id: UUID = Field(default_factory=uuid4)
    title: str
    description: str
    due_date: date
    status: Status

class UrgentTask(Task):
    priority: Priority
