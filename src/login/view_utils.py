from django.http import HttpResponse
import json

def cpf_login(qs):
    list = [{"response_status": HttpResponse.status_code}]
    for row in qs:
        list.append({
            "common_user_id": row.common_user.id,
            "user_cpf_id": row.id,
            "cpf": row.cpf,
            "user_cpf_name": row.name,
            "user_cpf_last_name": row.last_name,
            "user_cpf_email": row.common_user.user_email,
            "user_cpf_gender": row.gender.name,
            "user_cpf_civil_status": row.civil_status.status_name,
            "user_cpf_city": row.common_user.user_city.city_name,
            "user_cpf_state": row.common_user.user_city.state.state_name,
            "logged": True,
            "company": False
        })
    data = json.dumps(list)
    return data

def cnpj_login(qs):
    list = [{"response_status": HttpResponse.status_code}]
    for row in qs:
        list.append({
            "common_user_id": row.common_user.id,
            "user_cnpj_id": row.id,
            "cnpj": row.cnpj, 
            "user_cnpj_corporate_name":row.corporate_name,
            "user_cnpj_fancy_name":row.fancy_name,
            "user_cnpj_email": row.common_user.user_email,
            "user_cnpj_city": row.common_user.user_city.city_name, 
            "user_cnpj_state": row.common_user.user_city.state.state_name, 
            "user_cnpj_region": row.common_user.user_city.state.region.region_name,
            "user_cnpj_logged": True,
            "company": True
        })
    data = json.dumps(list)
    return data