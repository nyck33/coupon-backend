'''
get string couponType from json -> convert to enum
any Python code uses the enum until save to psql -> string
any load from psql: string -> enum
'''
from other_models.data.coupon_type_enum import CouponType
from other_models.data.coupon_names_dict import coupon_name_d
import enum

class CouponTypeEnumLoader(enum.Enum):

    @staticmethod
    def str_to_enum(coupon_type_str):
       switch = {
           'meal': CouponType.meal,
           'breakfast': CouponType.breakfast,
           'lunch': CouponType.lunch,
           'dinner':CouponType.dinner,
           'stay': CouponType.stay,
           'other': CouponType.other
       }
       try:
           return switch[coupon_type_str]
       except:
           print(f'{LookupError}')

    @staticmethod
    def enum_to_coupon_name(coupon_type):
        '''

        :param coupon_type:
        :return: string phrase for coupon
        '''
        try:
            return (coupon_name_d[coupon_type])
        except:
            print(f'{LookupError}')