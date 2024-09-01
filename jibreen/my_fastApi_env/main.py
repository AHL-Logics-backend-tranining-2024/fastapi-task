
from typing import Optional
from uuid import *
from fastapi import *
from Model.Enum.enums import *
from Model.task import Task
from Model.task_create import TaskCreate
from Model.task_update import TaskUpdate
from Model.urgentTask import UrgentTask
from utils.task_storage import *


# Initialize the FastAPI application
app = FastAPI() 

# Define the endpoint for retrieving all tasks or filtering tasks by type
@app.get("/tasks/", summary="Get all tasks", description="Retrieve a list of all tasks with their details. You can specify if the task is urgent or normal using a query parameter.")
def get_tasks(task_type: Optional[TaskTypeEnum] = Query(None, description="Specify if the task is urgent or normal")):
    tasks = load_tasks()

    if task_type:
        if task_type == TaskTypeEnum.urgent:
            # Filter tasks with a priority (urgent tasks)
            filtered_tasks = [task for task in tasks if "priority" in task]
        elif task_type == TaskTypeEnum.normal:
            # Filter tasks without a priority (normal tasks)
            filtered_tasks = [task for task in tasks if "priority" not in task]
        return filtered_tasks
    
    # Return all tasks if no type is specified
    return tasks

# Endpoint for retrieving uregent task
""" @app.get("/tasks/urgent/", summary="Get Urgent Tasks", description="Retrieve a list of all urgent tasks.")
def get_urgent_tasks():
    tasks = load_tasks()
    
    # Find urgent tasks by checking for the presence of 'priority'
    urgent_tasks = [task for task in tasks if "priority" in task]
    
    if not urgent_tasks:
        raise HTTPException(status_code=404, detail="No urgent tasks found")
    
    return urgent_tasks """


# Endpoint for retrieving task by ID
@app.get("/tasks/{task_id}/", summary="Get Task by ID", description="Retrieve the details of a task by its ID.")
def get_task_by_id(
    task_id: UUID = Path(..., description="The ID of the task to retrieve") 
):
    tasks = load_tasks()
    
    # Find the task by its ID
    for task in tasks:
        if task.get("task_id") == str(task_id):
            return task
    
    # If task not found
    raise HTTPException(status_code=404, detail="Task not found")


# Your create_task_or_urgent_task endpoint
@app.post("/task/", summary="Create a new task", description="Create a new task with details like title, description, due date, status, and priority.")
def create_task_or_urgent_task(  
    task_create: TaskCreate
):
    tasks = load_tasks()

    # Determine if it's an urgent task or a normal task based on the presence of priority
    if task_create.priority:
        task = UrgentTask(
            title=task_create.title,
            description=task_create.description,
            due_date=task_create.due_date,
            status=task_create.status,
            priority=task_create.priority
        )
    else:
        task = Task(
            title=task_create.title,
            description=task_create.description,
            due_date=task_create.due_date,
            status=task_create.status
        )

    # Convert task to dictionary for storage
    task_dict = task.to_dict()

    # Add new task to the list
    tasks.append(task_dict)
    save_tasks(tasks)
    
    return task_dict


@app.delete("/tasks/{task_id}",summary="Delete a Task by ID" , description="Delete a task by its ID.")
def delete_task_by_id(task_id: UUID = Path(..., description="The ID of the task to delete")):
    tasks = load_tasks()
    
    # Check if the task exists
    if any(task.get("task_id") == str(task_id) for task in tasks):
        # Remove the task with the matching ID
        tasks = [task for task in tasks if task.get("task_id") != str(task_id)]
        save_tasks(tasks)  # Save the updated task list
        return {"detail": "Task deleted successfully"}
    
    # If task not found
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", summary="Update a task", description="Update a task by its ID.")
def update_task_by_id(
    *,
    task_id: UUID = Path(..., description="The ID of the task to update"), 
    task_update: TaskUpdate
):
    tasks = load_tasks()
    task_id_str = str(task_id)
    
    # Loop through the tasks and update the one with the matching ID
    for task in tasks:
        if task.get("task_id") == task_id_str:
            # Update the fields from TaskUpdate
            updated_task = task_update.dict(exclude_unset=True)

            # Ensure priority can only be edited for urgent tasks
            if 'priority' in updated_task:
                if 'priority' in task:
                    # Update the priority if it's different from the original
                    if updated_task["priority"] != task["priority"]:
                        task["priority"] = updated_task["priority"]
                else:
                    raise HTTPException(status_code=400, detail="Cannot set priority for a non-urgent task")

            # Update other fields only if they differ from the original
            for key, value in updated_task.items():
                if key != "task_id" and task.get(key) != value:
                    task[key] = value

            # Save the updated tasks list
            save_tasks(tasks)

            return {"message": "Task updated successfully", "updated_task": task, "task_id": task_id_str}

    # If no matching task was found
    raise HTTPException(status_code=404, detail="Task not found")

