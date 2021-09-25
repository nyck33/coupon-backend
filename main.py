import uvicorn
import fastapi
'''
test_json = {"name": "Move out of house", "tasks":[{"description":"get storage",
                                               "complete": "False"},
                                              {"description":"get ispace",
                                                "complete": "False"}]}
'''
from apis import user_routes, other_routes, hotel_routes

api = fastapi.FastAPI()
#router = fastapi.APIRouter()

def configure():
    configure_routing()

def configure_routing():
    api.include_router(user_routes.router)
    api.include_router(other_routes.router)
    #apis.include_router(hotel_routes.router)

# for AWS
#https://pypi.org/project/mangum/
#handler = Mangum(app)


if __name__=="__main__":
    #uvicorn.run(app, host="localhost", port=8000)
    #uvicorn.run(app, debug=True, host="0.0.0.0", port=8000)
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()
