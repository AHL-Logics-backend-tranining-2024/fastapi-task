from enum import Enum
class Status(Enum):
    IN_PROGRESS = 'INPROGRESS'
    COMPLETED = 'COMPLETED'


class Priority(Enum):
    low = "low"
    medium = "medium"
    high = "high"   