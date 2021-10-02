from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/get-all-coupons")
    assert response.status_code == 200
    assert response.json() == \
        {
  "coupons": [
    {
      "couponId": 100,
      "couponType": "breakfast",
      "hotelName": "Hilton Tokyo",
      "expiryDate": "2100-01-01",
      "couponAmount": "yen500",
      "usedOn": None,
      "isUsed": False,
      "imageExists": False,
      "details": "For free breakfast",
      "imageUrl": "assets/images/starwars/Darth-Vader-icon.png",
      "couponName": "Breakfast discount coupon"
    },
    {
      "couponId": 101,
      "couponType": "dinner",
      "hotelName": "Hilton Kyoto",
      "expiryDate": "2100-01-01",
      "couponAmount": "yen1000",
      "usedOn": None,
      "isUsed": False,
      "imageExists": False,
      "details": "For free dinner",
      "imageUrl": "assets/images/starwars/Darth-Vader-icon.png",
      "couponName": "Dinner discount coupon"
    }
  ]
}