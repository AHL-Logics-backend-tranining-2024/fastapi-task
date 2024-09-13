from enum import Enum

class Priority(str, Enum):
    LOW = "Low"
    HIGH = "High"
    MEDIUM = "Medium"

class Status(str, Enum):
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"

