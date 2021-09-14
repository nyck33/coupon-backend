import uvicorn
from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class Task(BaseModel):
    description:str
    complete:bool

class Plan(BaseModel):
    name:str
    tasks: List[Task]






