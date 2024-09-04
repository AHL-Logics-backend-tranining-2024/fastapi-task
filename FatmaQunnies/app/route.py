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
        new_task = {
            "id": task_id,
            "title": task.title,
            "description": task.description,
            "due_date": task.due_date,
            "status": task.status,
            "priority": task.priority
        }
    tasks[task_id] = new_task 
    return new_task


@app.put("/tasks/{task_id}/")
def update_task(task_id: str, task_update: TaskUpdate):
    task = tasks.get(task_id) 
    if task is None:
        raise Exception

    if task_update.title is not None:
        task["title"] = task_update.title
    if task_update.description is not None:
        task["description"] = task_update.description
    if task_update.due_date is not None:
        task["due_date"] = task_update.due_date
    if task_update.status is not None:
        task["status"] = task_update.status
    if task_update.priority is not None:
        task["priority"] = task_update.priority

    tasks[task_id] = task
    return task


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
