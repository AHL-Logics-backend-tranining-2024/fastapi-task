from pydantic import BaseModel
from typing import Union
from datetime import date
from classes.task_status import Status, Priority


class TaskModel(BaseModel):
    title: str
    description: str
    due_date: date
    status:Status
    priority: Priority | None = None

class TaskUpdate(BaseModel):
    title: str| None = None
    description: str | None = None
    due_date: date | None = None
    status: Status| None = None
    status: Status | None = None
    priority: Priority | None = None