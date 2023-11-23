from pydantic import BaseModel
from datetime import date

class TaskModel(BaseModel):
    user_name: str
    time: date
    end_time: date
