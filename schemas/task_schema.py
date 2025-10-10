from pydantic import BaseModel
from typing import Literal

class TaskCreate(BaseModel):
    id: int
    title: str
    assigned_to: str
    status: Literal["pending", "in_progress", "done"]

class Task(TaskCreate):
    pass
