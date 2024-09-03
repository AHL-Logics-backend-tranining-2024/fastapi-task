from datetime import date
from task_status import Status
class Task:
 
    counter = 0  
    def __init__(self, title, description, due_date, status =Status.IN_PROGRESS):
        Task.counter += 1 
        self.task_id = Task.counter 
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def update_details(self, title=None, description=None, due_date=None,status=None):
        if title  is not None:
            self.title = title
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if status is not None:
            self.status = status    


    def display(self):
        displayString = (f"Task ID: {self.task_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Due Date: {self.due_date}\n"
            f"Status: {self.status}\n")
        return displayString
    
