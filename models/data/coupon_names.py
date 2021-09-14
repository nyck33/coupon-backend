import enum

class CouponType(enum.Enum):
    meal = 1
    breakfast = 2
    lunch = 3
    dinner = 4
    stay = 5
    other = 6


CouponName = {
    CouponType.meal: '食事割引クーポン',
    CouponType.breakfast: '朝食割引クーポン',
    CouponType.lunch: '昼食割引クーポン',
    CouponType.dinner: '夕食割引クーポン',
    CouponType.stay: '宿泊割引クーポン',
    CouponType.other: 'ダミー・クーポン'
}

