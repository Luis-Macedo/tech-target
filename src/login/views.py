from django.http import HttpResponse
from user.models import *
import json


def loginCpf(request):

    if request.method == 'GET':

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        try:
            data = User_cpf.objects.select_related().filter(
                common_user__user_password = body_data['user_password'], common_user__user_email = body_data['user_email']
            )
            list = []
            for row in data:
                list.append({
                    'response_status': HttpResponse.status_code,
                    'common_user_id': row.common_user.id,
                    'user_cpf_id': row.id, 
                    'user_cpf_name': row.name,
                    'user_cpf_last_name': row.last_name,
                    'user_cpf_email': row.common_user.user_email,
                    'user_cpf_city': row.common_user.user_city.city_name, 
                    'user_cpf_state': row.common_user.user_city.state.state_name, 
                    'user_cpf_region': row.common_user.user_city.state.region.region_name,
                    'user_cpf_logged': True
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

def loginCnpj(request):

    if request.method == 'GET':

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        try:
            data = User_cnpj.objects.select_related().filter(
                common_user__user_password = body_data['user_password'], common_user__user_email = body_data['user_email']
            )
            list = []
            for row in data:
                list.append({
                    'response_status': HttpResponse.status_code,
                    'common_user_id': row.common_user.id,
                    'user_cnpj_id': row.id, 
                    'user_cnpj_corporate_name':row.corporate_name,
                    'user_cnpj_fancy_name':row.fancy_name,
                    'user_cnpj_email': row.common_user.user_email,
                    'user_cnpj_city': row.common_user.user_city.city_name, 
                    'user_cnpj_state': row.common_user.user_city.state.state_name, 
                    'user_cnpj_region': row.common_user.user_city.state.region.region_name,
                    'user_cnpj_logged': True,
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
