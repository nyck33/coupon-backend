import fastapi
router = fastapi.APIRouter()

from app.models.other_models import Plan

@router.get('/')
async def instructions():
    return {'instructions': 'append /docs to see the apis and to try it out'}

@router.get("/items/{some_string}")
async def read_item(some_string: str): #just a string
    return {"item_id": some_string}


@router.post("/plan/", response_model=Plan)
async def create_plan(plan: Plan):
    print(plan)
    return plan