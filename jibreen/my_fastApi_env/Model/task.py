
from datetime import date
import uuid
from Model.Enum.enums import *

""" due_date: str """
class Task:
    def __init__(self, title: str, description: str, due_date: date, status: str):
        self.task_id = uuid.uuid4()  # Automatically generate the UUID
        self.title = title
        self.description = description
        self.due_date = due_date # Use the standalone validation function here
        self.status = status

    def to_dict(self):
        return {
            "task_id": str(self.task_id),
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date.isoformat(),
            "status": self.status
        }
    
    """ self.due_date """