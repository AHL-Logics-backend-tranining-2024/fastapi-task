from fastapi import FastAPI, HTTPException
import uuid
from models import *


app = FastAPI()
tasks = []

# Create a new task with details like title, description, due date, and status
@app.post("/tasks/")
def create_task(task :Create_Task_Basemodel):
    try:
        if task.priority:
            new_task = UrgentTask(task.priority , task.title,task.description ,task.due_date,task.status)
        else :
           new_task = Task(task.title,task.description ,task.due_date,task.status)
        tasks.append(new_task)
        return new_task.__dict__
    except Exception as e:
            return {"message": f"An error occurred while creating the task :  {str(e)}"}


# Update the details of an existing task by its ID.
@app.put("/tasks/{task_id}")
def update_task(task_id: uuid.UUID, task_update: Update_Task_Basemodel):
    try:
        task_to_update = find_task_by_id(task_id)
        if not task_to_update:
            raise HTTPException(status_code=404, detail="Task not found")
        # Update the task attributes if they are provided
        if task_update.title is not None:
            task_to_update.title = task_update.title
        if task_update.description is not None:
            task_to_update.description = task_update.description
        if task_update.due_date is not None:
            task_to_update.due_date = task_update.due_date
        if task_update.status is not None:
            task_to_update.status = task_update.status
        if task_update.priority is not None:
            task_to_update.priority = task_update.priority

        return {"message": "Task updated successfully", "task": task_to_update}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while updating the task :  {str(e)}")
        
# Retrieve a list of all tasks with their details.          
@app.get("/tasks/")
def get_all_tasks():
    try:
        if tasks:
            return tasks
        else:
            return {"message": "You don't have tasks yet"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while retrieving tasks:  {str(e)}")


# Retrieve a list of all urgent tasks.
@app.get("/tasks/urgent/")
def get_urgent_tasks():
    try:
        urgent_tasks = []
        for task in tasks :
            if task.priority is not None :
                urgent_tasks.append(task)  
        if  urgent_tasks :
            return urgent_tasks
        else:
            return {"message": "You don't have urgent tasks yet"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while retrieving tasks: {str(e)}")

# Retrieve the details of a task by its ID.
@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: uuid.UUID):
    try:
        task = find_task_by_id(task_id)
        return task
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while retrieving the task:  {str(e)}")

# Delete a task by its ID.
@app.delete("/tasks/{task_id}/")
def delete_task_by_id(task_id: uuid.UUID):
    try:
        task = find_task_by_id(task_id)
        tasks.remove(task)
        return {"message": "Task deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while deleting the task: {str(e)}")

# This function find a specific task in tasks list and return it to make operation on it 
def find_task_by_id(id):
    for task in tasks :
        if task.task_id == str(id):
            return task
    raise ValueError("Task with the provided ID does not exist.")