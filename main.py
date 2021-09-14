import uvicorn
from typing import Optional, List
from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel

from models import Item, Plan, Task
import postgres_service

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

#https://pypi.org/project/mangum/
#handler = Mangum(app)


if __name__ == "__main__":
    #uvicorn.run(app, host="localhost", port=8000)
    uvicorn.run(app, debug=True, host="0.0.0.0", port=8000)
