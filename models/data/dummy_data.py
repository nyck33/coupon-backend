from models.models import AllCoupons, User, Coupon, AllUsers


dummyUserDict = {
  "userId": 0,
  "name": "dummyuser",
  "email": "nobu.kim66@gmail.com",
  "loginStatus": "loggedIn",
  "currentScreen": "homeScreen",
  "hotelName": "HiltonAmsterdam",
  "roomNumber": "33",
  "checkInDate": "1976-05-31T00:00:00.000Z",
  "checkOutDate": "2100-05-31T00:00:00.000Z",
  "avatarExists": False,
  "avatarUrl": "",
  "coupons": '',
}

c1 = Coupon(
    couponId = 100, # enum
    couponType = 'breakfast',
    hotelName = 'Hilton Tokyo',
    expiryDate = '2100-01-01',
    couponAmount = 'yen500',
    usedOn = None,
    isUsed = False,
    imageExists = False,
    details = 'For free breakfast',
    imageUrl = 'assets/images/starwars/Darth-Vader-icon.png',
    couponName = 'Breakfast discount coupon'
)

c2 = Coupon(
    couponId = 101,
    couponType = 'dinner',
    hotelName = 'Hilton Kyoto',
    expiryDate = '2100-01-01',
    couponAmount = 'yen1000',
    usedOn = None,
    isUsed = False,
    imageExists = False,
    details = 'For free dinner',
    imageUrl = 'assets/images/starwars/Darth-Vader-icon.png',
    couponName = 'Dinner discount coupon'
)

dummyUser = User(
    userId = 0,
    name = 'dummy',
    email = 'nobu@nobu.com',
    loginStatus = 'loggedIn',
    currentScreen = 'homeScreen',
    hotelName = 'playboy mansion',
    roomNumber = 'xxx',
    checkInDate = '1976-05-31',
    checkOutDate = '2200-05-31',
    avatarExists = False,
    avatarUrl = None,
    coupons = [c1, c2]
)

all_coupons = AllCoupons(coupons = [c1, c2])

coupon2 =  {
      "couponId": 1,
      "couponType": "dinner",
      "hotelName": "Hilton Amsterdam",
      "expiryDate": "2100-01-01",
      "couponAmount": "yen1000",
      "usedOn": None,
      "isUsed": False,
      "imageExists": True,
      "details": "This coupon can be used at the buffet dinner with live music",
      "imageUrl": "assets/images/coupons/1000yenOff.png",
      "couponName": "夕食割引クーポン"
    }


coupon1 = {
      "couponId": 0,
      "couponType": "breakfast",
      "hotelName": "Hilton Amsterdam",
      "expiryDate": "2100-01-01",
      "couponAmount": "yen500",
      "usedOn": None,
      "isUsed": False,
      "imageExists": True,
      "details": "This coupon can beused at the continental breakfast buffet",
      "imageUrl": "assets/images/coupons/500yenOff.png",
      "couponName": "朝食割引クーポン"
    }


coupon3 = {
      "couponId": 2,
      "couponType": "stay",
      "hotelName": "Hilton Amsterdam",
      "expiryDate": "2100-01-01T00:00:00.000Z",
      "couponAmount": "special",
      "usedOn": None,
      "isUsed": False,
      "imageExists": True,
      "details":
      "This coupon can be used at the nightly Wine and Cheese with host Oprah Winfrey",
      "imageUrl": "assets/images/coupons/apaSpecial.png",
      "couponName": "宿泊割引クーポン"
    }
  
