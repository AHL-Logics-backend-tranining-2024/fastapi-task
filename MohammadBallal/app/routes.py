from datetime import date
from fastapi import APIRouter, HTTPException, Path
from app.models import Priority, Status, Task, UUID
from typing import List, Optional

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
    title: Optional[str] = None,
    description: Optional[str] = None,
    due_date: Optional[date] = None,
    status: Optional[Status] = None,
    priority: Optional[Priority] = None,
):
    # Combine all tasks into one list
    all_tasks = tasks + urgent_tasks
    
    # Search for the task by ID across all tasks
    task_to_update = None
    for task in all_tasks:
        if task.task_id == task_id:
            task_to_update = task
            break

    if not task_to_update:
        raise HTTPException(status_code=404, detail="Task not found")

    # Update only the fields that are provided in the request
    if title is not None:
        task_to_update.title = title
    if description is not None:
        task_to_update.description = description
    if due_date is not None:
        task_to_update.due_date = due_date
    if status is not None:
        task_to_update.status = status
    if priority is not None:
        # If the priority changes, move the task to the correct list
        if task_to_update in tasks:
            tasks.remove(task_to_update)
        if task_to_update in urgent_tasks:
            urgent_tasks.remove(task_to_update)
        
        task_to_update.priority = priority
        # Add the task to the correct list based on its priority
        if priority is not None:
            urgent_tasks.append(task_to_update)
        else:
            tasks.append(task_to_update)

    return {"message": "Task updated", "task": task_to_update}



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
