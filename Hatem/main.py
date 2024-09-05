from http.client import HTTPException
from typing import List
from fastapi import FastAPI
from models import *
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()

tasks : List[Task] = []

@app.get("/")
def root():
    return JSONResponse(status_code=200, content={"message": "Hello, FastAPI!"})

@app.get("/tasks")
def get_tasks():
    return JSONResponse(status_code=200, content=jsonable_encoder(tasks))

@app.get("/tasks/urgent")
def get_tasks():
    urgent_tasks = [task for task in tasks if isinstance(task, UrgentTask)]
    return JSONResponse(status_code=200, content=jsonable_encoder(urgent_tasks))


@app.get("tasks/{task_id}")
def get_task(task_id: UUID):
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return JSONResponse(status_code=200, content=jsonable_encoder(task))


@app.post("/tasks")
def create_task(task: Task):
    exists = check_task_existence(task.task_id)
    if exists:
        raise HTTPException(status_code=400, detail="Task already exist")
    tasks.append(task)
    return JSONResponse(status_code=200, content={"detail": "Task added successfully"})

@app.put("tasks")
def update_task(updated_task: Task):
    task_id = update_task.task_id
    exists = check_task_existence(task_id)
    if not exists:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = update_task
    return JSONResponse(status_code=201, content={"detail": "Task updated successfully"})

@app.delete("/tasks/{task_id}")
def delete_task(task_id: UUID):
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.remove(task)
    return JSONResponse(status_code=201, content={"detail": "Task deleted successfully"})

def check_task_existence(task_id: UUID) -> bool:
    return any(task.task_id == task_id for task in tasks)

def get_task_by_id(task_id: UUID):
    return next((task for task in tasks if task.task_id == task_id), None)

    
