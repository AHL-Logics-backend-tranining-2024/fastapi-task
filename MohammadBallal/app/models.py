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

# Task model
class Task(BaseModel):
    task_id: UUID = uuid4()  # Automatically generates a unique ID for each task
    title: str                                
    description: str = "No description provided"                           
    due_date: date                            
    status: Status 
    priority: Priority = None
