#https://github.com/tiangolo/fastapi/issues/2787
# need to use rootpath dev for aws deploy
# virtualenv for aws: virtualenv -p python3.9 env
# source ./env/bin/activate
'''
circleci commands to remake function.zip
cd env/lib/python3.9/site-packages
zip -r9 ../../../../function.zip .
cd ../../../../
zip -g ./function.zip -r app
or 
zip -g ./function.zip .env -r app
as seen here: https://github.com/deadbearcode/simple-serverless-fastapi-example/blob/serverless-fastapi-cicd-final/.circleci/config.yml
for this tutorial: https://www.deadbear.io/serverless-fastapi-ci-cd-with-circleci/
Also py3clean . from root to clear pycache and shrink size for AWS Lambda
'''

import uvicorn
import fastapi
from fastapi.middleware.cors import CORSMiddleware
#from mangum import Mangum

from app.apis import other_routes, user_routes

app = fastapi.FastAPI(
    title="coupon-backend",
    version=2.0,
    root_path="/beta/")
#router = fastapi.APIRouter()

flutter_regex = 'http://localhost:[0-9]+'
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex = flutter_regex,
    allow_credentials = True,
    allow_methods = True,
    allow_haaders= True
)

def configure():
    configure_routing()

def configure_routing():
    app.include_router(user_routes.router)
    app.include_router(other_routes.router)
    #apis.include_router(hotel_routes.router)

# for AWS
#https://pypi.org/project/mangum/
#handler = Mangum(app)


if __name__=="__main__":
    #uvicorn.run(app, host="localhost", port=8000)
    #uvicorn.run(app, debug=True, host="0.0.0.0", port=8000)
    configure()
    uvicorn.run(app, port=8000, host='127.0.0.1')
else:
    configure()
