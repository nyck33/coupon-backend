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
    imageUrl: Optional[str] = None
    couponName: str

class AllCoupons(BaseModel): #select all from table Coupons'7
    '''
    for hotels read
    '''
    coupons: List[Coupon]

#todo: divide this into 4 CRUD classes
class Hotel(BaseModel):
    hotelId: str
    password: str
    command: str #CRUD


class User(BaseModel):
    userId: Optional[int] = None
    name: str
    email: str
    loginStatus: str
    currentScreen: str
    hotelName: Optional[str] = None
    roomNumber: Optional[str] = None
    checkInDate: Optional[str] = None
    checkOutDate: Optional[str] = None
    avatarExists: bool
    avatarUrl: Optional[str] = None
    coupons: List[Coupon]

class AllUsers(BaseModel): #select all frm table Users
    users: Optional[List[User]] = None





