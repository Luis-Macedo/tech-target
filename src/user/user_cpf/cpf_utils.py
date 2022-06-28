import json
from django.http import HttpResponse
from ..models import User_cpf

def cpf_response(qs):
    list = [{"response_status": HttpResponse.status_code}]
    for row in qs:
        list.append({
            'common_user_id': row.common_user.id,
            'user_cpf_id': row.id,
            "cpf": row.cpf,
            'user_cpf_name': row.name,
            'user_cpf_last_name': row.last_name,
            'user_cpf_gender': row.gender.name,
            "user_cpf_civil_status": row.civil_status.status_name,
            'user_cpf_email': row.common_user.user_email,
            "user_phone": row.common_user.user_phone,
            'user_cpf_city': row.common_user.user_city.city_name,
            'user_cpf_state': row.common_user.user_city.state.state_name
        })
    data = json.dumps(list)
    return data

def insert_user_cpf(user, common_user_id):

    user_cpf = User_cpf.objects.create(
        cpf = user["cpf"], name = user["name"], last_name = user["last_name"],
        birth_date = user["birth_date"], profession = user["profession"], 
        civil_status_id = user["civil_status_id"],
        common_user_id = common_user_id, gender_id = user["gender_id"]
    )
    return user_cpf