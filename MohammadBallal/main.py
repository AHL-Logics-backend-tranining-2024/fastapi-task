from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import date

app = FastAPI()

Status = {
    "InProgress": "InProgress",
    "Completed": "Completed"
}

Priority = {
    "High": "High",
    "Medium": "Medium",
    "Low": "Low"
}

# Task model
class Task(BaseModel):
    task_id: UUID= uuid4()  # Automatically generates a unique ID for each task
    title: str                                   
    description: str                             
    due_date: date                            
    status: str                              

# UrgentTask model inheriting from Task model
class UrgentTask(Task):
    priority: str  
