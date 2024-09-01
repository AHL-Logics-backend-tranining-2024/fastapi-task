from pydantic import BaseModel
from models.enums import PriorityEnum,StatusEnum
from datetime import date


# this class for creation needs only
class Create_Task_Basemodel(BaseModel):
    title: str
    description: str
    due_date: date
    status: StatusEnum
    priority: PriorityEnum  | None = None


# this class for Update needs only
class Update_Task_Basemodel(BaseModel):
    title: str | None = None
    description: str | None = None
    due_date: date | None = None
    status: StatusEnum | None = None
    priority: PriorityEnum  | None = None