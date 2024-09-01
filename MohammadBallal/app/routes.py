from fastapi import APIRouter, HTTPException, Path
from app.models import Task, UUID
from typing import List

router = APIRouter()

tasks = []
urgent_tasks = []

# Create a new task
@router.post("/tasks/")
def create_task(task: Task):
    if task.priority is not None:  # If priority is set, add as an urgent task
        urgent_tasks.append(task)
        return {"message": "Urgent task created", "task": task}
    else:
        tasks.append(task)
        return {"message": "Normal task created", "task": task}

# Get All Tasks
@router.get("/tasks/")
def get_all_tasks():
    all_tasks = tasks + urgent_tasks
    return {"tasks": all_tasks}

# Get Urgent Tasks
@router.get("/tasks/urgent/")
def get_urgent_tasks():
    if not urgent_tasks:
        return {"message": "No urgent tasks found."}
    return {"urgent_tasks": urgent_tasks}

# Get Task by ID
@router.get("/tasks/{task_id}/")
def get_task_by_id(task_id: UUID = Path(..., title="The ID of the task to get")):
    # Search for the task in both lists
    for task_list in (urgent_tasks, tasks):
        for task in task_list:
            if task.task_id == task_id:
                return {"task": task}

    raise HTTPException(status_code=404, detail="Task not found")

# Update a Task by ID
@router.put("/tasks/{task_id}/")
def update_task(
    task_id: UUID = Path(..., title="The ID of the task to update"),
    updated_task: Task | None = None,
):
    # Determine the list to search based on the priority
    task_list = urgent_tasks if updated_task and updated_task.priority is not None else tasks

    # Search for the task in the determined list
    for index, task in enumerate(task_list):
        if task.task_id == task_id:
            if updated_task:
                task_list[index] = updated_task
            return {"message": "Task updated", "task_id": task_id, "task": task_list[index]}

    raise HTTPException(status_code=404, detail="Task not found")

# Delete a Task by ID
@router.delete("/tasks/{task_id}/")
def delete_task(task_id: UUID = Path(..., title="The ID of the task to delete")):
    # Search for the task in urgent tasks
    for index, task in enumerate(urgent_tasks):
        if task.task_id == task_id:
            urgent_tasks.pop(index)
            return {"message": "Urgent task deleted"}

    # Search in normal tasks
    for index, task in enumerate(tasks):
        if task.task_id == task_id:
            tasks.pop(index)
            return {"message": "Normal task deleted"}

    raise HTTPException(status_code=404, detail="Task not found")
