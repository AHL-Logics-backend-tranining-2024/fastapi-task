from enum import Enum

class StatusEnum(str, Enum):
    inprogress = "inprogress"
    completed = "completed"

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

