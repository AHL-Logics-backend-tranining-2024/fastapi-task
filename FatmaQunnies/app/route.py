from http.client import HTTPException
from FatmaQunnies.classes import urgent_task
from fastapi import FastAPI
import uuid
from classes import *
from classes.model import TaskModel, TaskUpdate


app = FastAPI()
tasks = {}

@app.post("/tasks/")
def create_task(task: TaskModel):
    task_id = str(uuid.uuid4())  
    if task.priority:
        new_task = urgent_task(task.title, task.description, task.due_date, task.priority)
    else:
        new_task = task(task.title, task.description, task.due_date,task.status)

    tasks[task_id] = new_task 
    return new_task


@app.put("/tasks/{task_id}/")
def update_task(task_id: str, task_update: TaskUpdate):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    fields_to_update = ["title", "description", "due_date", "status", "priority"]
    for field in fields_to_update:
        value = getattr(task_update, field) 
        if value is not None:
            setattr(task, field, value) 

    return {"task_id": task_id, "task": task}


@app.get("/tasks/")
def get_all_tasks():
    return list(tasks.values()) 

@app.get("/tasks/{task_id}/")
def get_task_by_id(task_id: str):
    task = tasks.get(task_id) 
    if task:
        return task
    raise Exception


@app.get("/tasks/urgent/")
def get_urgent_tasks():
    urgent_tasks = [{"id": task_id, "task": task} for task_id, task in tasks.items() if isinstance(task, urgent_task)]
    return urgent_tasks


@app.delete("/tasks/{task_id}/")
def delete_task(task_id: str):
    if task_id in tasks: 
        del tasks[task_id] 
        return {"message": "Task deleted successfully"}
    raise Exception
