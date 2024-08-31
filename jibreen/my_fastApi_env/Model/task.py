
from pydantic import *
import re
from Model.Enum.enums import StatusEnum


class Task(BaseModel):
    # Title of the task, must be a string with length between 3 and 10 characters
    title: str = constr(min_length=3, max_length=10) 

    # Description of the task, must be a string with length between 5 and 100 characters
    description: str = constr(min_length=5, max_length=100)

    # Due date of the task, must be a string in the format YYYY-MM-DD
    due_date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$")

    # Status of the task, must be a value defined in StatusEnum
    status: StatusEnum

    @validator("due_date",pre=True)
    def validate_due_date(cls, v):
        """
        Validate the due_date field to ensure it follows the format YYYY-MM-DD
        and that month and day values are within valid ranges.
        
        :param v: The value of the due_date field
        :return: The validated due_date
        :raises ValueError: If due_date does not meet validation criteria
        """

        # Check if the due_date matches the YYYY-MM-DD format
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", v):
            raise ValueError("due_date must be in the format YYYY-MM-DD")
        
        # Split the due_date into year, month, and day
        year, month, day = map(int, v.split('-'))
        
        # Validate month and day ranges
        if not (1 <= month <= 12):
            raise ValueError('Month must be between 1 and 12')
        
        # Validate day range; adjust day range validation as needed
        if not (1 <= day <= 30):
            raise ValueError('Day must be between 1 and 31')
        
        return v