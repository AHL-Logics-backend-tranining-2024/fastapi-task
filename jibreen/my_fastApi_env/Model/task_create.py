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


    @validator("due_date", pre=True) 
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
        
        # Validate month range
        if not (1 <= month <= 12):
            raise ValueError('Month must be between 1 and 12')
        
        # Validate day range according to the month and leap year consideration
        if month in {4, 6, 9, 11} and day > 30:
            raise ValueError(f'Month {month} has only 30 days')
        elif month == 2:
            # Check for leap year
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day > 29:
                    raise ValueError(f'February in a leap year has only 29 days')
            else:
                if day > 28:
                    raise ValueError(f'February has only 28 days')
        elif not (1 <= day <= 31):
            raise ValueError('Day must be between 1 and 31')

        return v