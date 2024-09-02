import json
from typing import *
from fastapi import HTTPException


TASKS_FILE = "tasks.json"


def load_tasks() -> List[Dict[str, Union[str, int]]]:
    """
    Load tasks from the JSON file.

    Returns:
        List[Dict[str, Union[str, int]]]: A list of tasks, where each task is represented
        as a dictionary with string and integer values.

    Handles:
        - FileNotFoundError: Returns an empty list if the file does not exist.
        - JSONDecodeError: Returns an empty list if the file contains invalid JSON.
    """
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file) # Load tasks from file
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist
    except json.JSONDecodeError:
        return [] # Return an empty list if the JSON is invalid



def save_tasks(tasks: List[Dict[str, Union[str, int]]]) -> None:
    """
    Save tasks to the JSON file.

    Args:
        tasks (List[Dict[str, Union[str, int]]]): A list of tasks to be saved.

    Raises:
        HTTPException: Raises a 500 error if there is an issue with file I/O operations.
    """
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4) # Write tasks to file with indentation
    except IOError:
        # Raise an HTTPException if there's an issue with saving the tasks
        raise HTTPException(status_code=500, detail="Failed to save tasks to file")