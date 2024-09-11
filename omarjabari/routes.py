from fastapi import APIRouter, HTTPException, status
from models import Task, UrgentTask
from typing import List
from task_service import TaskService
from uuid import UUID

router = APIRouter()
task_service = TaskService()


@router.post("/tasks/", response_model=Task, status_code=status.HTTP_201_CREATED)
def created_task(task: Task):
    try:
        return task_service.create_task(task)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/tasks/", response_model=List[Task], status_code=status.HTTP_200_OK)
def get_tasks():
    return task_service.get_all_tasks()


@router.get("/tasks/{task_id}/", response_model=Task)
def get_task_by_ID(task_id: UUID):
    try:
        return task_service.get_task_by_id(task_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.get(
    "/tasks/urgent/", response_model=List[UrgentTask], status_code=status.HTTP_200_OK
)
def get_urgent_tasks():
    return task_service.get_urgent_tasks()


@router.put("/tasks/{task_id}/", response_model=Task)
def update_task(task_id: UUID, task: Task):
    try:
        updated_task_data = task.dict(exclude_unset=True)
        return task_service.update_task(task_id, updated_task_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/tasks/{task_id}/", response_model=Task)
def delete_task(task_id: UUID):
    try:
        return task_service.delete_task(task_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
