import uvicorn
from fastapi import FastAPI

from models.models import Item, Plan, Coupon, User

root_path = '/'
app = FastAPI(root_path=root_path)

test_json = {"name": "Move out of house", "tasks":[{"description":"get storage",
                                               "complete": "False"},
                                              {"description":"get ispace",
                                                "complete": "False"}]}

@app.get("/")
async def root():
    return {"message": "Hi"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    print(item)
    return item

@app.post("/plan/", response_model=Plan)
async def create_plan(plan: Plan):
    print(plan)
    return plan

####################################################################################
# hotel operations connected to their client
@app.post("/create/")
async def create_coupon(coupon: Coupon):
    # todo: instantiate coupon and add to list of coupons
    print(coupon)
    return coupon

@app.post("/delete/")
async def delete_coupon(coupon: Coupon):


#https://pypi.org/project/mangum/
#handler = Mangum(app)


if __name__ == "__main__":
    #uvicorn.run(app, host="localhost", port=8000)
    uvicorn.run(app, debug=True, host="0.0.0.0", port=8000)
