from pydantic import BaseModel

class ItemBase(BaseModel):
    user_name: str
