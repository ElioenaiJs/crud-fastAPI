from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False
    due_date: Optional[datetime] = None  

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    due_date: Optional[datetime] = None  

    class Config:
        orm_mode = True
