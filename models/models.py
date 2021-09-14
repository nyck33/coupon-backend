import uvicorn
from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel
import datetime


class Task(BaseModel):
    description:str
    complete:bool

class Plan(BaseModel):
    name:str
    tasks: List[Task]

class Coupon(BaseModel):
    couponId: int # enum
    couponType: str
    hotelName: str
    expiryDate: Optional[str] = None
    couponAmount: str # enum
    usedOn: Optional[str] = None
    isUsed: bool
    imageExists: bool
    details: str
    imageUrl: Optional[str]
    couponName: str

class User(BaseModel):
    userId: Optional[int] = None
    name: str
    hotel: Optional[str] = None
    room: Optional[str] = None
    arrivalDate: Optional[str] = None
    departDate: Optional[str] = None
    avatarExists: bool
    avatarUrl: Optional[str] = None
    coupons: List[Coupon]







