from ..models import Common_user

def insert_common_user(user):
    res = Common_user.objects.create(
        user_name = user["user_name"], user_email = user["user_email"],
        user_password = user["user_password"], user_phone = user["user_phone"],
        user_city_id = user["user_city"], user_address = user["user_address"]
    )
    return res