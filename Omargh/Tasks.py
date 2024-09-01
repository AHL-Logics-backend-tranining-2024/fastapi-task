from typing import Dict, Optional
from modules import TaskCreate, Task, UrgentTask
from uuid import UUID, uuid4
class Task:
    task_id=0
    def __init__(self,title,description,due_date,status="InProgress"):
        Task.task_id+=1
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status
    def update_details(self,title=None, description=None, due_date=None,status=None):
        if title:
            self.title=title
        if description:
            self.description=description
        if due_date:
            self.due_date=due_date
        if status:
            self.status=status
    

class UrgentTask(Task):
    def __init__(self,priority,title,description,due_date,status="InProgress"):
        super().__init__(title,description,due_date,status)
        self.priority=priority