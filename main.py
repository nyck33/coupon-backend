import uvicorn
import fastapi
from mangum import Mangum

from apis import user_routes, other_routes, hotel_routes

app = fastapi.FastAPI()
#router = fastapi.APIRouter()

def configure():
    configure_routing()

def configure_routing():
    app.include_router(user_routes.router)
    app.include_router(other_routes.router)
    #apis.include_router(hotel_routes.router)

# for AWS
#https://pypi.org/project/mangum/
handler = Mangum(app)


if __name__=="__main__":
    #uvicorn.run(app, host="localhost", port=8000)
    #uvicorn.run(app, debug=True, host="0.0.0.0", port=8000)
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()
