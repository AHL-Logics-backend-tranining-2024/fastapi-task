from typing import Optional
from pydantic import * 
import re
from Model.Enum.enums import *


class TaskCreate(BaseModel): 
    # Title of the task, must be a string with length between 3 and 10 characters
    title: str = constr(min_length=3, max_length=10) 

    # Description of the task, must be a string with length between 5 and 100 characters
    description: str = constr(min_length=5, max_length=100) 

    # Due date of the task, must be a string in the format YYYY-MM-DD
    due_date: str

    # Status of the task, must be a value defined in StatusEnum
    status: StatusEnum

    # Optional field for priority
    priority: Optional[PriorityEnum] = None

