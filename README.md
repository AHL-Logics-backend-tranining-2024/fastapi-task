# Task Manager API Application

## Getting Started

### Setup

1. **Clone the Main Repository:**

     ```
     git clone https://github.com/AHL-Logics-backend-tranining-2024/fastapi-task.git
     ```
     
2. **Create a New Branch:**

     Each intern should create a new branch for their individual project. The branch name should include your name or identifier:
     ```
     git checkout -b <intern-name>-fastapi-task
     ```
3. **Create a New Folder:**

    Inside your branch, create a new folder to represent your project:
    ```
    mkdir <intern-name>
    cd <intern-name>
    ```
## Project Overview

The Task Manager API Application is a FastAPI-based tool designed to help users manage their tasks efficiently through RESTful API endpoints. This project will help you practice essential FastAPI concepts, including request handling, data validation, path and query parameters, and CRUD operations.

## Endpoints

  1. **Create New Task**
     - **Endpoint**: `/tasks/`
     - **Description**: Create a new task with details like title, description, due date, and status.
  
  2. **Update a Task by ID**
     - **Endpoint**: `/tasks/{task_id}/`
     - **Description**: Update the details of an existing task by its ID.
  
  3. **Get All Tasks**
     - **Endpoint**: `/tasks/`
     - **Description**: Retrieve a list of all tasks with their details.
  
  4. **Get Task by ID**
     - **Endpoint**: `/tasks/{task_id}/`
     - **Description**: Retrieve the details of a task by its ID. You can specify if the task is urgent or normal using a query parameter.
  
  5. **Get Urgent Tasks**
     - **Endpoint**: `/tasks/urgent/`
     - **Description**: Retrieve a list of all urgent tasks.
  
  6. **Delete a Task by ID**
     - **Endpoint**: `/tasks/{task_id}/`
     - **Description**: Delete a task by its ID.


## Models

  ### Task Model
  
  This model represents a task with the following attributes:
  
  ```json
  {
    "task_id": "uuid_type", # please use a uuid
    "title": "string",
    "description": "string",
    "due_date": "YYYY-MM-DD",
    "status": "InProgress | Completed"
  }
  ```
  
  ### UrgentTask Model
  
  This model inherits from the Task model and adds a priority attribute:
  
  ```json
  {
    "task_id": "uuid_type", # please use a uuid
    "title": "string",
    "description": "string",
    "due_date": "YYYY-MM-DD",
    "status": "InProgress | Completed",
    "priority": "High | Medium | Low"
  }
  ```

## **Guidelines**

1. **Code Organization:** Organize your code into different modules for clarity and maintainability. 
2. **Exception Handling:** Implement error handling to manage invalid inputs, operations on non-existent tasks, and potential file I/O errors.
3. **Documentation:** Comment your code thoroughly to explain the purpose and functionality of each class and method, please create a README file within your folder project.
4. **Submission:** 
   1. Work within your own branch and folder in the cloned repository.
   2. Create a Pull Request: Once you have completed your work, push your changes in your branch to the repository and create a pull request. Ensure your pull request includes a description of the changes and any relevant details.
   3. Engage in discussions with peers and mentors for feedback and improvement.
