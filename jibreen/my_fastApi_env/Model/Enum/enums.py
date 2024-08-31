

from enum import Enum


class StatusEnum(str, Enum):
    inProgress = "InProgress"
    completed = "Completed"


class PriorityEnum(str, Enum):
    low = "Low"
    medium = "Medium"
    high = "High"


class TaskTypeEnum(str, Enum):
    urgent = "Urgent"
    normal = "Normal"