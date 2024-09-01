from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from uuid import UUID, uuid4
from datetime import date
from enum import Enum



app = FastAPI()

# Using enum for status and priority
class Status(Enum):
    InProgress = "InProgress"
    Completed = "Completed"

class Priority(Enum):
    High = "High"
    Medium = "Medium"
    Low = "Low"


# Task model
class Task(BaseModel):
    task_id: UUID= uuid4()  # Automatically generates a unique ID for each task
    title: str                                
    description: str = "No description provided"                           
    due_date: date                            
    status: Status 
    priority: Priority = None

    
tasks= []
urgent_tasks = []


# Create a new task
@app.post("/tasks/")
def create_task(task: Task):
    if task.priority is not None:  # If priority is set it added as an urgent task
        urgent_tasks.append(task)
        return {"message": "Urgent task created", "task": task}
    else:
        tasks.append(task)
        return {"message": "Normal task created", "task": task}


from fastapi import Path

#Update a Task by ID
@app.put("/tasks/{task_id}/")
def update_task(
    task_id: UUID = Path(..., title="The ID of the task to update"),
    updated_task: Task | None = None,
):
    #Determine the list to search based on the priority
    task_list = urgent_tasks if updated_task and updated_task.priority is not None else tasks

    #Search for the task in the determined list
    for index, task in enumerate(task_list):
        if task.task_id == task_id:
            if updated_task:
                task_list[index] = updated_task
            return {"message": "Task updated", "task_id": task_id, "task": task_list[index]}

    raise HTTPException(status_code=404, detail="Task not found")



#Get All Tasks
@app.get("/tasks/")
def get_all_tasks():
    all_tasks = tasks + urgent_tasks
    return {"tasks": all_tasks}


#Get Urgent Tasks
@app.get("/tasks/urgent/")
def get_urgent_tasks():
    if not urgent_tasks:
        return {"message": "No urgent tasks found."}
    return {"urgent_tasks": urgent_tasks}



#Get Task by ID
@app.get("/tasks/{task_id}/")
def get_task_by_id(task_id: UUID = Path(..., title="The ID of the task to get")):
    # Search for the task in both lists
    for task_list in (urgent_tasks, tasks):
        for task in task_list:
            if task.task_id == task_id:
                return {"task": task}

    raise HTTPException(status_code=404, detail="Task not found")



#Delete a Task by ID
@app.delete("/tasks/{task_id}/")
def delete_task(task_id: UUID = Path(..., title="The ID of the task to delete")):
    # Search for the task in urgent tasks
    for index, task in enumerate(urgent_tasks):
        if task.task_id == task_id:
            urgent_tasks.pop(index)
            return {"message": "Urgent task deleted"}

    #Search in normal tasks
    for index, task in enumerate(tasks):
        if task.task_id == task_id:
            tasks.pop(index)
            return {"message": "Normal task deleted"}

    raise HTTPException(status_code=404, detail="Task not found")




