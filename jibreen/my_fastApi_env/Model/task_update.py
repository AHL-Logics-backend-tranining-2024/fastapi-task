from datetime import date
from typing import Optional
from pydantic import *
import re
from Model.Enum.enums import *


class TaskUpdate(BaseModel):
   # Title of the task, optional
    title: Optional[str] = None

    # Description of the task, optional
    description: Optional[str] = None

    # Due date of the task, optional
    due_date: Optional[date] = None

    # Status of the task, optional
    status: Optional[StatusEnum] = None

    # Optional priority for urgent tasks
    priority: Optional[PriorityEnum] = None
