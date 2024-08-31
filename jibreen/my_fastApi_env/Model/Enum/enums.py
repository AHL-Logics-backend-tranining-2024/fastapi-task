
from enum import Enum


class StatusEnum(str, Enum):
    """
    Enum representing the possible statuses of a task.
    """
    inProgress = "InProgress" # The task is currently in progress
    completed = "Completed" # The task has been completed


class PriorityEnum(str, Enum):
    """
    Enum representing the priority levels of a task.
    """
    low = "Low" # Low priority
    medium = "Medium" # Medium priority
    high = "High"  # High priority


class TaskTypeEnum(str, Enum):
    """
    Enum representing the type of a task.
    """
    urgent = "Urgent" # An urgent task that requires immediate attention
    normal = "Normal" # A regular task that does not require immediate attention