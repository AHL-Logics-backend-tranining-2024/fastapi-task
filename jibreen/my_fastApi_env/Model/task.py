from pydantic import BaseModel, Field, validator
from uuid import UUID
import re
from typing import Literal


class Task(BaseModel):
    task_id: UUID
    title:str
    description:str
    due_date: str = Field(..., regex=r"^\d{4}-\d{2}-\d{2}$")
    status: Literal["InProgress", "Completed"]

    @validator("due_date")
    def validate_due_date(cls, v):
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", v):
            raise ValueError("due_date must be in the format YYYY-MM-DD")
        return v