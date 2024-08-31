# Task Manager API Application

## Project Overview

This FastAPI project provides a task management system with endpoints for creating, updating, retrieving, and deleting tasks. It includes support for both normal and urgent tasks, with priority handling for urgent tasks only.

## Endpoints

- `GET /tasks`: Retrieve all tasks.
- `GET /tasks/urgent/`: Retrieve urgent tasks.
- `GET /tasks/{task_id}`: Retrieve a specific task by its ID.
- `POST /tasks`: Create a new task (normal or urgent).
- `PUT /tasks/{task_id}`: Update a task by its ID.
- `DELETE /tasks/{task_id}`: Delete a task by its ID.

## Data Models

-`Task`: Represents a general task with title, description, due date, and status. -`UrgentTask`: Inherits from Task and includes priority.

## Error Handling

- `404 Not Found`: Task ID does not exist.
- `400 Bad Request`: Invalid priority or other request errors.

## Setup

### Prerequisites

- Python 3.10 or higher
- Pip (Python package installer)

### Installation

1.** Clone the Repository**

```
 git clone https://github.com/AHL-Logics-backend-tranining-2024/fastapi-task.git
```

2. **Create and Activate a Virtual Environment**

```
python -m venv my_fastApi_env
source my_fastApi_env/bin/activate  # On Windows, use `my_fastApi_env\Scripts\activate`
```

3. **Install Dependencies**

```
pip install -r requirements.txt
```

4. **Run the Application**

```
fastapi run
```

5. **Access the API**
   Open your browser and go to `http://localhost:8000/docs` to view the interactive API documentation provided by FastAPI.

## Standup

### Recent Updates

- `Feature`: Added support for urgent tasks with priority.
- `Improvement`: Enhanced error handling for invalid inputs and task updates.
- `Bug Fix`: Corrected issues with task priority updates not reflecting in the JSON file.
