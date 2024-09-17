from fastapi import FastAPI, HTTPException
from uuid import uuid4
from typing import List
from task import *

app = FastAPI()


tasks = []

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task.task_id = str(uuid4()) 
    tasks.append(task)
    return task


@app.put("/tasks/{task_id}/", response_model=Task)
def update_task(task_id: str, updated_task: Task):
    for task in tasks:
        if task.task_id == task_id:
            updated_data = updated_task.model_dump(exclude_unset=True)
            for key, value in updated_data.items():
                setattr(task, key, value)
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.get("/tasks/", response_model=List[Task])
def get_all_tasks():
    return tasks


@app.get("/tasks/{task_id}/", response_model=Task)
def get_task_by_id(task_id: str):
    for task in tasks:
        if task.task_id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/tasks/urgent/", response_model=List[UrgentTask])
def get_urgent_tasks():
    urgent_tasks = [task for task in tasks if isinstance(task, UrgentTask)]
    return urgent_tasks


@app.delete("/tasks/{task_id}/")
def delete_task(task_id: str):
    tasks = [task for task in tasks if task.task_id != task_id]
    return {"message": "Task deleted"}
