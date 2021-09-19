import uvicorn
from fastapi import FastAPI

from models.models import Plan, Coupon, Coupons, User, Hotel
#from interfaces import hotel_interface, users_interface

root_path = '/'
app = FastAPI(root_path=root_path)

test_json = {"name": "Move out of house", "tasks":[{"description":"get storage",
                                               "complete": "False"},
                                              {"description":"get ispace",
                                                "complete": "False"}]}
@app.get("/")
async def root():
    return {"error message": "specify path"}

@app.get("/items/{some_string}")
async def read_item(some_string: str): #just a string
    return {"item_id": some_string}


@app.post("/plan/", response_model=Plan)
async def create_plan(plan: Plan):
    print(plan)
    return plan

####################################################################################
################################################################################################
# user ops
# user ops, on tap of coupon card


@app.get("/get-all-coupons/", response_model=User)
async def check_for_new_coupons(user: User):
    '''
    todo: make this a get request and just send coupons and check for any new ones in Flutter
    on tap of coupons card in UI
    request payload is current user coupons so check against list of available coupons on server
    send back any new ones eligible for to refresh coupons page on Flutter UI
    :param coupons:
    :return:
    '''
    print(f"user: {user}")
    return user

@app.post("/user-update-coupons/", response_model=User)
async def update_coupons(user: User):
    '''
    user uses coupon so update the isUsed and return User
    :param user:
    :return: updated User
    '''
    print(user)
    return user

@app.post("/user-delete-coupons", response_model=User)
async def delete_coupons(user:User):
    '''
    when user checks out
    :param user:
    :return:
    '''
    return user





# for AWS
#https://pypi.org/project/mangum/
#handler = Mangum(app)


if __name__ == "__main__":
    #uvicorn.run(app, host="localhost", port=8000)
    #uvicorn.run(app, debug=True, host="0.0.0.0", port=8000)
    uvicorn.run(app, host="0.0.0.0", port=8000)
