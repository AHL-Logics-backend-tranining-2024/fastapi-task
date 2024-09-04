# Task Management API

This is a simple Task Management API built using FastAPI. The API allows you to create, update, retrieve, and delete tasks. Each task can have a title, description, due date, status, and optional priority level.

## Features

- **Create Task**: Create a new task with a title, description, due date, status, and optional priority.
- **Update Task**: Update the details of an existing task.
- **Retrieve All Tasks**: Get a list of all tasks.
- **Retrieve Task by ID**: Get the details of a specific task by its unique ID.
- **Delete Task**: Remove a task from the list.

## Prerequisites

- Python 3.11.9
- FastAPI
- Pydantic
- Uvicorn

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AHL-Logics-backend-tranining-2024/fastapi-task.git
    cd aya_tamimi
    ```

2. Run it using this command:

    ```bash
    fastapi dev task_endpoints.py
    ```

## Endpoints

### Create a New Task

- **URL**: `/tasks/`
- **Method**: `POST`
- **Request Body**:

    ```json
    {
        "title": "Complete the report",
        "description": "Finish the quarterly report for the finance department.",
        "due_date": "2024-10-15T00:00:00",
        "status": "inprogress",
        "priority": "high"  # Optional
    }
    ```

- **Response**:

    ```json
    {
        "task_id": "9fd305cd-5203-48c2-b00c-b0bea0855ada",
        "title": "Complete the report",
        "description": "Finish the quarterly report for the finance department.",
        "due_date": "2024-10-15T00:00:00",
        "status": "inprogress",
        "priority": "high"
    }
    ```

### Update a Task

- **URL**: `/tasks/{task_id}`
- **Method**: `PUT`
- **Request Body**:

    ```json
    {
        "title": "Update the report", # Optional
        "description": "Update the quarterly report for the finance department.", # Optional
        "due_date": "2024-10-20T00:00:00", # Optional
        "status": "completed",  # Optional
        "priority": "medium"  # Optional
    }
    ```

- **Response**:

    ```json
    {
        "message": "Task updated successfully",
        "task": {
            "task_id": "9fd305cd-5203-48c2-b00c-b0bea0855ada",
            "title": "Update the report",
            "description": "Update the quarterly report for the finance department.",
            "due_date": "2024-10-20T00:00:00",
            "status": "completed",
            "priority": "medium"
        }
    }
    ```

### Retrieve All Tasks

- **URL**: `/tasks/`
- **Method**: `GET`
- **Response**:

    ```json
    [
        {
            "task_id": "9fd305cd-5203-48c2-b00c-b0bea0855ada",
            "title": "Complete the report",
            "description": "Finish the quarterly report for the finance department.",
            "due_date": "2024-10-15T00:00:00",
            "status": "inprogress",
            "priority": "high"
        }
    ]
    ```

### Retrieve a Task by ID

- **URL**: `/tasks/{task_id}`
- **Method**: `GET`
- **Response**:

    ```json
    {
        "task_id": "9fd305cd-5203-48c2-b00c-b0bea0855ada",
        "title": "Complete the report",
        "description": "Finish the quarterly report for the finance department.",
        "due_date": "2024-10-15T00:00:00",
        "status": "inprogress",
        "priority": "high"
    }
    ```

### Delete a Task

- **URL**: `/tasks/{task_id}`
- **Method**: `DELETE`
- **Response**:

    ```json
    {
        "message": "Task deleted successfully"
    }
    ```


