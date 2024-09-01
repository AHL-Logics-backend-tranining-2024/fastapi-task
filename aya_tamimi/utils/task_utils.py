from datetime import datetime


def validate_date(date_time: datetime):
    try:
        format  = '%Y-%m-%d'
        dt_str = date_time.strftime(format)
        datetime.strptime(dt_str, format)
        return True
    except ValueError:
        raise ValueError(f"Incorrect date format, should be {format}.")

def get_valid_input(prompt):
    if not prompt.strip():
        raise ValueError("value canot be empty , Please try again.")
    return True
                 
def validate_status(status):
    if status not in ["inprogress", "completed"]:
        raise ValueError("invalid status , status must be either 'InProgress'or 'Completed'")
    return True

def validate_priority(priority):
    if priority not in ["high", "medium", "low"]:
            raise ValueError("Invalid priority , priority must be  High , Medium or Low ")
    return True