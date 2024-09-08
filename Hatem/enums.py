from enum import Enum

class Status(str, Enum):
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"

class Priority(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"