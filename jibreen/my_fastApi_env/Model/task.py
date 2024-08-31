from enum import Enum
from pydantic import BaseModel, Field, constr, validator
import re
from typing import Literal
from Model.Enum.enums import StatusEnum


class Task(BaseModel):
    title: str = constr(min_length=3, max_length=10) 
    description: str = constr(min_length=5, max_length=100)
    due_date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$")
    status: StatusEnum

    @validator("due_date",pre=True)
    def validate_due_date(cls, v):
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", v):
            raise ValueError("due_date must be in the format YYYY-MM-DD")
        year, month, day = map(int, v.split('-'))
        
        # Validate month and day ranges
        if not (1 <= month <= 12):
            raise ValueError('Month must be between 1 and 12')
        if not (1 <= day <= 30):
            raise ValueError('Day must be between 1 and 31')
        
        return v