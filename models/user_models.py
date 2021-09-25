from pydantic import BaseModel
from typing import Optional, List
from .coupon_models import Coupon

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

