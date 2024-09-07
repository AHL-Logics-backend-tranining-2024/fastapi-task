from datetime import date
from task_status import Status
class Task:
    
    def __init__(self, title, description, due_date, status =Status.IN_PROGRESS):
        Task.counter += 1 
        self.task_id = Task.counter 
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

#   updates is dict
    def update_details(self, updates):
        for key, value in updates.items():
            if value is not None:
                setattr(self, key, value)

    def display(self):
        displayString = (f"Task ID: {self.task_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Due Date: {self.due_date}\n"
            f"Status: {self.status}\n")
        return displayString
    
