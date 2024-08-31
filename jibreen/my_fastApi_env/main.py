
from typing import Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException, Query
from Model.task import Task
from Model.urgentTask import PriorityEnum
from utils.task_storage import load_tasks, save_tasks


# Initialize the FastAPI application
app = FastAPI()


@app.get("/tasks")
def get_tasks():
    tasks = load_tasks()
    return tasks


@app.post("/tasks/", summary="Create a new task", description="Create a new task with details like title, description, due date, status, and priority.")
def create_task_or_urgent_task(
    task: Task,
    priority: Optional[PriorityEnum] = Query(None, description="Specify the priority if the task is urgent")
):
    tasks = load_tasks()
    task_id = str(uuid4())
    
    # Convert task to dictionary and add the auto-generated task_id
    task_dict = task.dict()
    
    # Add priority if the task is urgent and priority is provided
    if priority:
        task_dict["priority"] = priority

    task_dict["task_id"] = task_id

    # Check if the task_id already exists (shouldn't happen with UUID4, but just in case)
    if any(existing_task.get("task_id") == task_id for existing_task in tasks):
        raise HTTPException(status_code=400, detail="Task with this ID already exists")

    # Add new task to the list
    tasks.append(task_dict)
    save_tasks(tasks)
    
    return task_dict