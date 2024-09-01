import uuid

class Task():
    def __init__(self ,title,description,due_date ,status ):
        self.task_id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.due_date =due_date
        self.status = status
    

    def update_details(self, title=None, description=None, due_date=None, status=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if status is not None:
            self.status = status

       
    def display(self):
        return (
            f"Task Id     : {self.task_id}\nTitle       : {self.title}\nStatus      : {self.status}\nDescription : {self.description}\nDue Date    : {self.due_date}\n"
        )