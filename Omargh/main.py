from fastapi import FastAPI,HTTPException, Path
from typing import Dict
from modules import Task, UrgentTask,TaskCreate
from uuid import UUID, uuid4 
from taskmanager import TaskManager

app = FastAPI()
# task_manager is made from taskmanager class that work with dictionary
task_manager = TaskManager()
""" Creating a Task"""
@app.post("/tasks/")
async def create_task(task_data: TaskCreate, is_urgent: bool = False):
    new_task = task_manager.create_task(task_data, is_urgent)
    return new_task

""" Update a Task by ID"""
@app.put("/tasks/{task_id}")
def update_tasks(task_id: str , task_data: TaskCreate):
# using the id to determine the task and taskupdate.dict is refer to pydantic converts the model instance into a dictionary
    try:
        updated_task = task_manager.update_task(task_id, task_data)
        return updated_task
    except ValueError as e:
        raise HTTPException(status_code=404, detail="No tasks")
"""Get All Tasks"""
@app.get("/tasks/")
async def get_all_tasks():
    return task_manager.view_tasks()
"""Get Task by ID"""
@app.get("/tasks/{task_id}")
async def get_task(task_id: str):
    task = task_manager.view_tasksbyid(task_id)
    if task :
        return task
    raise HTTPException(status_code=404, detail="Task not found")
"""Get Urgent Tasks"""
    
# delete using pop functionally
@app.delete("/tasks/{task_id}")
async def delete_tasks(task_id: str):
    try:
        deleted_task = task_manager.delete_task(task_id)
        return deleted_task
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

