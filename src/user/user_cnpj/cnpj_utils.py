import json
from django.http import HttpResponse
from ..models import User_cnpj

def cnpj_response(qs):
    list = [{"response_status": HttpResponse.status_code}]
    for row in qs:
        list.append({
            "user_cnpj_id": row.id,
            "cnpj": row.cnpj,
            "user_cnpj_fancy_name": row.fancy_name,
            "user_cnpj_corporate_name": row.corporate_name,
            "user_email": row.common_user.user_email,
            "user_phone": row.common_user.user_phone,
            "user_city": row.common_user.user_city.city_name 
        })
    data = json.dumps(list)
    return data

def insert_user_cnpj(user, common_user_id):

    user_cnpj = User_cnpj.objects.create(
        common_user_id = common_user_id, cnpj = user["cnpj"],
        corporate_name = user["corporate_name"], fancy_name = user["fancy_name"],
        segments_id = user["segments"]
    )

    return user_cnpj