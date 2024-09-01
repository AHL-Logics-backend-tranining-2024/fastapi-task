from pydantic import BaseModel
from models.enums import PriorityEnum,StatusEnum
from datetime import datetime


# this class for creation needs only
class Create_Task_Basemodel(BaseModel):
    title: str
    description: str
    due_date: datetime
    status: StatusEnum
    priority: PriorityEnum  | None = None


# this class for Update needs only
class Update_Task_Basemodel(BaseModel):
    title: str | None = None
    description: str | None = None
    due_date: datetime | None = None
    status: StatusEnum | None = None
    priority: PriorityEnum  | None = None