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
    priority: Optional[Priority] = None
# In this case I use separate  class for achieving the singleton Design Pattern Each class have one responsibility
class TaskCreate(TaskBase):
    pass
class UpdateDetails(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    
class Task(TaskBase):
    task_id:UUID=uuid4()
    def __init__(self, title: str, description: Optional[str], due_date: date, status: str, priority: Optional[Priority] = None, task_id: Optional[UUID] = None):
        super().__init__(title=title, description=description, due_date=due_date, status=status, priority=priority)
        self.task_id = task_id 
class UrgentTask(TaskBase):
     priority: Priority
     task_id:UUID=uuid4()
     def __init__(self, title: str, description: Optional[str], due_date: date, status: str, priority: Priority, task_id: Optional[UUID] = None):
        super().__init__(title=title, description=description, due_date=due_date, status=status, priority=priority)
        self.task_id = task_id 
