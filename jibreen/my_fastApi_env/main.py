
from typing import Optional
from uuid import *
from fastapi import *
from Model.Enum.enums import *
from Model.task import Task
from utils.task_storage import *


# Initialize the FastAPI application
app = FastAPI()

# Endpoint for retrieving all tasks or filtering tasks by type
@app.get("/tasks/",summary="Get all tasks",description="Retrieve a list of all tasks with their details. You can specify if the task is urgent or normal using a query parameter.")
def get_tasks(task_type: Optional[TaskTypeEnum] = Query(None, description="Specify if the task is urgent or normal")):
    tasks = load_tasks()
    if task_type:
        # Filter tasks based on the specified type
        filtered_tasks = [task for task in tasks if (
            (task_type == TaskTypeEnum.urgent and "priority" in task) or
            (task_type == TaskTypeEnum.normal and "priority" not in task)
        )]
        return filtered_tasks
    
    # Return all tasks if no type is specified
    return tasks

# Endpoint for retrieving uregent task
@app.get("/tasks/urgent/", summary="Get Urgent Tasks", description="Retrieve a list of all urgent tasks.")
def get_urgent_tasks():
    tasks = load_tasks()
    
    # Find urgent tasks by checking for the presence of 'priority'
    urgent_tasks = [task for task in tasks if "priority" in task]
    
    if not urgent_tasks:
        raise HTTPException(status_code=404, detail="No urgent tasks found")
    
    return urgent_tasks


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


# Create a task, specifying if it's urgent or normal based on provided data
@app.post("/tasks/", summary="Create a new task", description="Create a new task with details like title, description, due date, status, and priority.")
def create_task_or_urgent_task(  
    task: Task,
    priority: Optional[PriorityEnum] = Query(None, description="Specify the priority if the task is urgent")
):
    tasks = load_tasks()
    task_id = str(uuid4())
    
    # Convert task to dictionary and add the auto-generated task_id
    task_dict = task.dict()
    
    # Add priority if the task is urgent and priority is provided
    if priority:
        task_dict["priority"] = priority

    task_dict["task_id"] = task_id

    # Check if the task_id already exists (shouldn't happen with UUID4, but just in case)
    if any(existing_task.get("task_id") == task_id for existing_task in tasks):
        raise HTTPException(status_code=400, detail="Task with this ID already exists")

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

#Update update_task_by_id endpoint to handle updates for both normal and urgent tasks
@app.put("/tasks/{task_id}", summary="Update a task", description="Update a task by its ID.")
def update_task_by_id(
    *,
    task_id: UUID = Path(..., description="The ID of the task to update"),
    task: dict
):
    tasks = load_tasks()

    # Find the index of the task with the given task_id
    task_index = next((index for (index, t) in enumerate(tasks) if t.get("task_id") == str(task_id)), None)

    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")

    # Retrieve the original task
    original_task = tasks[task_index]

    # Convert task to dictionary for updates
    updated_task = task

    # Ensure priority can only be edited for urgent tasks
    if 'priority' in updated_task:
        if 'priority' in original_task:
            # Update the priority if it's different from the original
            if updated_task["priority"] != original_task["priority"]:
                original_task["priority"] = updated_task["priority"]
        else:
            raise HTTPException(status_code=400, detail="Cannot set priority for a non-urgent task")
     

    # Update other fields only if they differ from the original
    for key, value in updated_task.items():
        if key != "task_id" and original_task.get(key) != value:
            original_task[key] = value

    # Save the updated tasks list
    tasks[task_index] = original_task
    save_tasks(tasks)


    return {"message": "Task updated successfully", "task_id": str(task_id)}

