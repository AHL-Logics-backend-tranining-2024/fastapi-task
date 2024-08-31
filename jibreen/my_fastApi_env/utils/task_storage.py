import json
from typing import Dict, List, Union
from fastapi import HTTPException


TASKS_FILE = "tasks.json"


def load_tasks() -> List[Dict[str, Union[str, int]]]:
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_tasks(tasks: List[Dict[str, Union[str, int]]]) -> None:
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        raise HTTPException(status_code=500, detail="Failed to save tasks to file")