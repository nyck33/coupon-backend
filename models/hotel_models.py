from pydantic import BaseModel

#todo: divide this into 4 CRUD classes
class Hotel(BaseModel):
    hotelId: str
    password: str
    command: str #CRUD