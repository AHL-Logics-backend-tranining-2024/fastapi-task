from fastapi import FastAPI, HTTPException
from uuid import uuid4
from typing import List, Dict
from task import *

app = FastAPI()
tasks: Dict[str, Task] = {}

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task_id = str(uuid4())
    task.task_id = task_id
    tasks[task_id] = task
    return task



@app.put("/tasks/{task_id}")
def update_task(task_id: str, updated_task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    existing_task = tasks[task_id]
    updated_data = updated_task.model_dump(exclude_unset=True)

    for key, value in updated_data.items():
        setattr(existing_task, key, value)

    tasks[task_id] = existing_task
    return existing_task


@app.get("/tasks/", response_model=List[Task])
def get_all_tasks():
    return list(tasks.values()) 


@app.get("/tasks/{task_id}/", response_model=Task)
def get_task_by_id(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@app.get("/tasks/urgent/", response_model=List[UrgentTask])
def get_urgent_tasks():
    urgent_tasks = [task for task in tasks.values() if isinstance(task, UrgentTask)]
    return urgent_tasks


@app.delete("/tasks/{task_id}/")
def delete_task(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted"}
