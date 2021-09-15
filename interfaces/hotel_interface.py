import uvicorn
from fastapi import FastAPI

from models.models import Coupon, Coupons, User, Hotel
from interfaces import hotel_interface, users_interface


@app.post("/create-coupon/")
async def create_coupon(coupon: Coupon):
    # todo: instantiate coupon and add to list of coupons
    print(coupon)
    return coupon

@app.post("/delete-coupon/")
async def delete_coupon(coupon: Coupon):
    pass

@app.post("/update-coupon/")
async def update_coupon(coupon: Coupon):
    pass

@app.post("/read-coupons/")
async def read_coupons(coupons:Coupons):
    '''using post to hide hotel_id and password in request body'''
    print(coupons)
    return coupons