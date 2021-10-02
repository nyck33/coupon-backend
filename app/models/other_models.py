from typing import Optional, List
from pydantic import BaseModel


class Task(BaseModel):
    description:str
    complete:bool

class Plan(BaseModel):
    name:str
    tasks: List[Task]










