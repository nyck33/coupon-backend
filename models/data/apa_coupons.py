'''
can instantiate classes of coupons using dictionaries
see example: https://pydantic-docs.helpmanual.io/
'''
coupon1 = {
    'couponId': 0,
    'couponType': 'breakfast',
    'hotelName': 'Apa Shinagawa',
    'expiryDate': '2100-01-01',
    'couponAmount': 'yen500',
    'usedOn': None, #is null in json
    'isUsed': False,
    'imageExists': False,
    'details': 'Coupon for continental breakfast',
    'imageUrl': None,
    'couponName': None
}

coupon2 = {
    'couponId': 1,
    'couponType': 'lunch',
    'hotelName': 'Apa Minami-Shinjuku',
    'expiryDate': '2100-01-01',
    'couponAmount': 'yen1000',
    'usedOn': None, #is null in json
    'isUsed': False,
    'imageExists': False,
    'details': 'Coupon for sushi lunch',
    'imageUrl': None,
    'couponName': None
}

coupon3 = {
    'couponId': 2,
    'couponType': 'stay',
    'hotelName': 'Apa Nishi-Nippori',
    'expiryDate': '2100-01-01',
    'couponAmount': 'percent10',
    'usedOn': None, #is null in json
    'isUsed': False,
    'imageExists': False,
    'details': 'Coupon for discounted stay',
    'imageUrl': None,
    'couponName': None
}

coupon_special = {
    'couponId': 4,
    'couponType': 'breakfast',
    'hotelName': 'Apa Kamakura',
    'expiryDate': '2100-01-01',
    'couponAmount': 'special',
    'usedOn': None, #is null in json
    'isUsed': False,
    'imageExists': True,
    'details': 'special coupon for VIP guests',
    'imageUrl': 'https://ibb.co/rtZPbxW',
    'couponName': None
}


