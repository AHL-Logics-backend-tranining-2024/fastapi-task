from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import date
from enum import Enum       # Enum is defining a fixed set of values that a variable can take


app = FastAPI()

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
    task_id: UUID= uuid4()  # Automatically generates a unique ID for each task
    title: str                                   
    description: str                             
    due_date: date                            
    status: Status                            

# UrgentTask model inheriting from Task model
class UrgentTask(Task):
    priority: Priority

 
