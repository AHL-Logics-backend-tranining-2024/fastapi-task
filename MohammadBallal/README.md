# Task Manager API

## Project Overview

API for managing tasks using FastAPI. This API allows you to create, update, retrieve, and delete tasks.
Tasks can be categorized as normal or urgent based on their priority.

## EndPpints & Features

- `POST /tasks` **Create a New Task:** Add a new task with details such as title, description, due date, status, and priority(urgent tasks).
- `GET /tasks` **Retrieve All Tasks:** Get a list of all tasks, including both normal and urgent tasks.
- `GET /tasks/urgent/` **Retrieve Urgent Tasks:** Get a list of all urgent tasks.
- `GET /tasks/{task_id}` **Retrieve Task by ID:** Fetch the details of a specific task by its ID.
- `PUT /tasks/{task_id}` **Update a Task by ID:** Modify the details of an existing task using its ID.
- `DELETE /tasks/{task_id}` **Delete a Task by ID:** Remove a task from the system using its ID.


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





