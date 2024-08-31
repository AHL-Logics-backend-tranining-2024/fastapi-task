
from enum import Enum
from typing import Literal
from Model.task import Task


class PriorityEnum(str, Enum):
    low = "Low"
    medium = "Medium"
    high = "High"

class UrgentTask(Task):
 priority: PriorityEnum