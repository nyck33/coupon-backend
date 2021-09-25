import uvicorn
from fastapi import FastAPI

from models.other_models import Coupon, Coupons, User, Hotel
from interfaces import hotel_interface, users_interface


# hotel operations connected to their client
@app.post("/hotel-commands/")
async def run_command(hotel: Hotel):
    '''
    todo: command should be divided up into CRUD with classes for each command with hotel_id and password, command is
     in the path of URL
    :param hotel:
    :return:
    '''
    id = hotel.hotelId
    password = hotel.password
    command = hotel.command
    #todo: run functions here to check id, password and run command on postgres
    print(hotel)
    return hotel


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