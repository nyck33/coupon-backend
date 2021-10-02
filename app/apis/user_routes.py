'''
virtualenv -p python3.9 env
source ./env/bin/activate

'''
import fastapi
from app.models.data.dummy_data import all_coupons
from app.models.user_models import User

router = fastapi.APIRouter()


@router.get("/get-all-coupons") #response_model=AllCoupons)
async def check_for_new_coupons():
    '''
    todo: make this a get request and just send coupons and check for any new ones in Flutter
    on tap of coupons card in UI
    request payload is current user coupons so check against list of available coupons on server
    send back any new ones eligible for to refresh coupons page on Flutter UI
    :param coupons:
    :return:
    '''
    print(f"responding with list of coupons")
    return all_coupons

@router.post("/user-update-coupons/", response_model=User)
async def update_coupons(user: User):
    '''
    user uses coupon so update the isUsed and return User
    :param user:
    :return: updated User
    '''
    print(user)
    return user

@router.post("/user-delete-coupons", response_model=User)
async def delete_coupons(user:User):
    '''
    when user checks out
    :param user:
    :return:
    '''
    return user


