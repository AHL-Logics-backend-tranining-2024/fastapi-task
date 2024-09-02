

import re
from fastapi import HTTPException


def validate_due_date(due_date: str) -> str:
    """
    Validate the due_date to ensure it follows the format YYYY-MM-DD
    and that month and day values are within valid ranges.
    
    :param due_date: The due_date string to validate
    :return: The validated due_date
    :raises ValueError: If due_date does not meet validation criteria
    """
    
    # Check if the due_date matches the YYYY-MM-DD format
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", due_date):
        raise HTTPException(status_code=400, detail="due_date must be in the format YYYY-MM-DD")
    
    # Split the due_date into year, month, and day
    year, month, day = map(int, due_date.split('-'))
    
    # Validate month range
    if not (1 <= month <= 12):
        raise HTTPException(status_code=400, detail='Month must be between 1 and 12')
    
    # Validate day range according to the month and leap year consideration
    if month in {4, 6, 9, 11} and day > 30:
        raise HTTPException(status_code=400, detail = f'Month {month} has only 30 days')
    elif month == 2:
        # Check for leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                raise HTTPException(status_code=400, detail= f'February in a leap year has only 29 days')
        else:
            if day > 28:
                raise HTTPException(status_code=400, detail=f'February has only 28 days')
    elif not (1 <= day <= 31):
        raise HTTPException(status_code=400, detail='Day must be between 1 and 31')

    return due_date