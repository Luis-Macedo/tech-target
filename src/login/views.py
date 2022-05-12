from django.http import HttpResponse
from user.models import *
import json


def login(request):

    if request.method == 'GET':

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        list = [{"response_status": HttpResponse.status_code}]

        try:
            cpf_data = User_cpf.objects.select_related().filter(
                common_user__user_password = body_data['user_password'], common_user__user_email = body_data['user_email']
            )
            cnpj_data = User_cnpj.objects.select_related().filter(
                common_user__user_password = body_data['user_password'], common_user__user_email = body_data['user_email']
            )
            
            if len(cpf_data) == 0 and len(cnpj_data) == 0:
            
                msg = [{
                    "message": "[INFO] Error! User not found"
                }]
                msg = json.dumps(msg)
                return HttpResponse(msg, content_type="application/json")

            elif len(cpf_data) > 0:
                for row in cpf_data:
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
                        "logged": True
                    })
                data = json.dumps(list)
                return HttpResponse(data, content_type="application/json")

            else:
                for row in cnpj_data:
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
                    })
                data = json.dumps(list)
                return HttpResponse(data, content_type="application/json")

        except:
            msg = [{
                "message": "[INFO] Error! Database error"
            }]
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")

    else:   
        msg = [{
            'response_status': HttpResponse.status_code,
            "message": "[INFO] Must be a GET method"
        }]
        msg = json.dumps(msg)
        return HttpResponse(msg, content_type="application/json")
