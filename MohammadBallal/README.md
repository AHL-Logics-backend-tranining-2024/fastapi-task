# Task Manager API

## Project Overview

API for managing tasks using FastAPI. This API allows you to create, update, retrieve, and delete tasks.
Tasks can be categorized as normal or urgent based on their priority.

## EndPpints & Features

- **Create a New Task:** Add a new task with details such as title, description, due date, status, and priority(urgent tasks).
- **Retrieve All Tasks:** Get a list of all tasks, including both normal and urgent tasks.
- **Retrieve Urgent Tasks:** Get a list of all urgent tasks.
- **Retrieve Task by ID:** Fetch the details of a specific task by its ID.
- **Update a Task by ID:** Modify the details of an existing task using its ID.
- **Delete a Task by ID:** Remove a task from the system using its ID.


## Endpoints

### Create a New Task

- **Endpoint:** `/tasks/`
- **Method:** `POST`
- **Description:** Create a new task. If a priority is set, the task is considered urgent.
- **Request Body for Urgent Task:**
    ```json
    {
        "title": "Task Title",
        "description": "Task Description",
        "due_date": "2024-09-01",
        "status": "InProgress",
        "priority": "High"
    }
    ```
- **Request Body for Normal Task:**
    ```json
    {
        "title": "Task Title",
        "description": "Task Description",
        "due_date": "2024-09-01",
        "status": "InProgress",
    }
    ```

### Retrieve All Tasks

- **Endpoint:** `/tasks/`
- **Method:** `GET`
- **Description:** Retrieve a list of all tasks, including both normal and urgent tasks.

### Retrieve Urgent Tasks

- **Endpoint:** `/tasks/urgent/`
- **Method:** `GET`
- **Description:** Retrieve a list of all tasks marked as urgent.
- **Response:**
    ```json
    {
        "urgent_tasks": [
            {
                "task_id": "UUID",
                "title": "Urgent Task Title",
                "description": "Task Description",
                "due_date": "2024-09-01",
                "status": "InProgress",
                "priority": "High"
            }
        ]
    }
    ```

### Retrieve Task by ID

- **Endpoint:** `/tasks/{task_id}/`
- **Method:** `GET`
- **Description:** Retrieve the details of a specific task by its ID.
- **Parameters:**
    - `task_id` (path): The UUID of the task to retrieve.

### Update a Task by ID

- **Endpoint:** `/tasks/{task_id}/`
- **Method:** `PUT`
- **Description:** Update the details of an existing task using its ID.
- **Request Body:**
    ```json
    {
        "task_id": "UUID",
        "title": "Updated Task Title",
        "description": "Updated Description",
        "due_date": "2024-09-01",
        "status": "Completed",
        "priority": "Medium"
    }
    ```

### Delete a Task by ID

- **Endpoint:** `/tasks/{task_id}/`
- **Method:** `DELETE`
- **Description:** Delete a task by its ID.
- **Parameters:**
    - `task_id` (path): The UUID of the task to delete.



## Requirements

- Python 3.10+
- FastAPI

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AHL-Logics-backend-tranining-2024/fastapi-task.git
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**

    ```bash
    uvicorn main:app --reload
    ```

    By default, the API will be accessible at `http://127.0.0.1:8000`.

2. **Access the API documentation:**

    The automatically generated documentation can be accessed at:
    - [Swagger UI](http://127.0.0.1:8000/docs)


## Error Handling

- **400 Bad Request:** Returned when the request data is invalid or improperly formatted.
- **404 Not Found:** Returned when a task with the specified ID does not exist.





