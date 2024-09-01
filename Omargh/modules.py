from pydantic import BaseModel,Field
from datetime import date
from uuid import UUID, uuid4
from typing import Optional
from enum import Enum
# Using Enum
class Status(str, Enum):
    in_progress = "InProgress"
    completed = "Completed"

class Priority(str, Enum):
    high = "High"
    medium = "Medium"
    low = "Low"
class TaskBase(BaseModel):
    title:str=Field(..., min_length=2, max_length=10)
    description:str=Field(...,min_length=5,max_length=20)
    due_date: date
    status: str=Field(...,min_length=1,max_length=10)
# In this case I use separate  class for achieving the singleton Design Pattern Each class have one responsibility
class TaskCreate(TaskBase):
    pass
class Task(TaskBase):
    task_id:UUID=uuid4()

class UrgentTask(TaskBase):
     priority: str
