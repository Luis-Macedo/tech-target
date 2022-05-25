import json
from django.http import HttpResponse

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