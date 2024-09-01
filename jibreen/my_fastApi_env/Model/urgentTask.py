
from Model.Enum.enums import PriorityEnum
from Model.task import Task

class UrgentTask(Task):
    def __init__(self, title, description, due_date, status, priority: PriorityEnum):
        # Initialize the parent Task class
        super().__init__(title, description, due_date, status)
        
        # Override or add the priority attribute
        self.priority = priority

    # Optionally, you can override the to_dict method if you want to ensure priority is always included
    def to_dict(self):
        task_dict = super().to_dict()
        task_dict["priority"] = self.priority.value
        return task_dict
