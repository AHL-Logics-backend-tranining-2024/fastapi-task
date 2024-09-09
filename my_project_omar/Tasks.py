from typing import Dict, Optional
from modules import CreateTaskBase, UrgentTask,UpdateDetails
from uuid import UUID, uuid4
from enum import Enum
class Priority(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
class Task:
    
    def __init__(self,title,description,due_date,status="InProgress",priority: Optional[Priority] = None):
        task_id:UUID=uuid4()
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status
        self.priority = priority
    def update_details(self,update_data: UpdateDetails):
        for field,value in update_data.dict().items():
            if value:
                setattr(self, field, value)

class UrgentTask(Task):
    def __init__(self,priority,title,description,due_date,status="InProgress"):
        super().__init__(title,description,due_date,status)
        self.priority=priority