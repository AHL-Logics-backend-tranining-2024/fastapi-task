
from enum import Enum
from typing import Literal
from Model.Enum.enums import PriorityEnum
from Model.task import Task


class UrgentTask(Task):
 priority: PriorityEnum