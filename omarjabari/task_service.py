from typing import Dict, List
from uuid import UUID
from models import Task, UrgentTask


class TaskService:
    def __init__(self):
        self.tasks: Dict[UUID, Task] = {}

    def create_task(self, task: Task):
        if task.task_id in self.tasks:
            raise ValueError("Task ID already exists")
        self.tasks[task.task_id] = task
        return task

    def update_task(self, task_id: UUID, updated_task_data: Dict):
        if task_id in self.tasks:
            task = self.tasks[task_id]
        else:
            raise ValueError("Task not found")

        for key, value in updated_task_data.items():
            if hasattr(task, key) and value is not None:
                setattr(task, key, value)
        self.tasks[task_id] = task
        return task

    def get_all_tasks(self):
        return list(self.tasks.values())

    def get_task_by_id(self, task_id: UUID):
        if task_id not in self.tasks:
            raise ValueError("Task not found in tasks ! ")
        return self.tasks[task_id]

    def get_urgent_tasks(self):
        return [task for task in self.tasks.values() if isinstance(task, UrgentTask)]

    def delete_task(self, task_id: UUID):
        if task_id not in self.tasks:
            raise ValueError("Task not found in tasks  !  ")
        return self.tasks.pop(task_id)
