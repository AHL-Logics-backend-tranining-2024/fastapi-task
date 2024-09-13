from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import date
from task_enum import *


class Task(BaseModel):
    task_id: str = str(uuid4())
    title: str
    description: str
    due_date: date
    status: Status

class UrgentTask(Task):
    priority: Priority