from typing import Dict, Optional
from modules import TaskCreate, Task, UrgentTask,UpdateDetails
from uuid import UUID, uuid4
class Task:
    
    def __init__(self,title,description,due_date,status="InProgress"):
        
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status
    def update_details(self,update_data: UpdateDetails):
        for field,value in update_data.dict().items():
            if value:
                setattr(self, field, value)

class UrgentTask(Task):
    def __init__(self,priority,title,description,due_date,status="InProgress"):
        super().__init__(title,description,due_date,status)
        self.priority=priority