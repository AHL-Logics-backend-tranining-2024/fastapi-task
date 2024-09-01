from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import date
from enum import Enum



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
    description: str = "No description provided"                           
    due_date: date                            
    status: Status 
    priority: Priority = None

    
tasks= []
urgent_tasks = []


# Create a new task
@app.post("/tasks/")
def create_task(task: Task):
    if task.priority is not None:  # If priority is set it added as an urgent task
        urgent_tasks.append(task)
        return {"message": "Urgent task created", "task": task}
    else:
        tasks.append(task)
        return {"message": "Normal task created", "task": task}

