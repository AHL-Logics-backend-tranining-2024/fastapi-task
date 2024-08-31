
from Model.Enum.enums import PriorityEnum
from Model.task import Task

# Define the UrgentTask class which inherits from Task
class UrgentTask(Task):
 # Override the priority attribute to be of type PriorityEnum
 priority: PriorityEnum
