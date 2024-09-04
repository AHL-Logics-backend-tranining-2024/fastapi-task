from fastapi import APIRouter, HTTPException, Path
from app.models import Task, TaskModel, UUID, TaskUpdate

router = APIRouter()

tasks = []
urgent_tasks = []


# Create a new task
@router.post("/tasks/")
def create_task(task_data: TaskModel):
    task = Task(**task_data.model_dump())
    if task.priority:
        urgent_tasks.append(task)
        return {"message": "Urgent task created", "task": task.task_dict()}
    tasks.append(task)
    return {"message": "Normal task created", "task": task.task_dict()}


# Get All Tasks
@router.get("/tasks/")
def get_all_tasks():
    all_tasks = tasks + urgent_tasks
    return {"tasks": [task.task_dict() for task in all_tasks]}


# Get Urgent Tasks
@router.get("/tasks/urgent/")
def get_urgent_tasks():
    if not urgent_tasks:
        return {"message": "No urgent tasks found."}
    return {"urgent_tasks": [task.task_dict() for task in urgent_tasks]}


# Get Task by ID
@router.get("/tasks/{task_id}/")
def get_task_by_id(task_id: UUID = Path(..., title="The ID of the task to get")):
    for task_list in (urgent_tasks, tasks):
        for task in task_list:
            if task.task_id == task_id:
                return {"task": task.task_dict()}
    raise HTTPException(status_code=404, detail="Task not found")


# Update a Task by ID
@router.put("/tasks/{task_id}/")
def update_task(
    *,
    task_id: UUID = Path(..., title="The ID of the task to update"),
    update_data: TaskUpdate
):
    # Find the task to update
    task_to_update = next((task for task in tasks + urgent_tasks if task.task_id == task_id), None)
    if not task_to_update:
        raise HTTPException(status_code=404, detail="Task not found")

    # Remove the task from its current list
    if task_to_update in tasks:
        tasks.remove(task_to_update)
    elif task_to_update in urgent_tasks:
        urgent_tasks.remove(task_to_update)

    # Update task fields
    update_data_dict = update_data.model_dump()
    for key, value in update_data_dict.items():
        if value is not None:
            setattr(task_to_update, key, value)

    # Add the task back to the correct list based on its updated priority
    if task_to_update.priority:
        urgent_tasks.append(task_to_update)
    else:
        tasks.append(task_to_update)

    return {"message": "Task updated", "task": task_to_update.task_dict()}


# Delete a Task by ID
@router.delete("/tasks/{task_id}/")
def delete_task(task_id: UUID = Path(..., title="The ID of the task to delete")):
    for index, task in enumerate(urgent_tasks):
        if task.task_id == task_id:
            urgent_tasks.pop(index)
            return {"message": "Urgent task deleted"}
    for index, task in enumerate(tasks):
        if task.task_id == task_id:
            tasks.pop(index)
            return {"message": "Normal task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
