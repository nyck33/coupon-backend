from pydantic import BaseModel
from typing import Optional, List

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