import json
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import *

def allCpf(request):
    if request.method == 'GET':
        qs =  User_cpf.objects.all()
        data = serialize("json", qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'response_status': HttpResponse.status_code,
            'error': "[INFO] Must be a GET method"
        }]
        msg = json.dumps(msg)
        return HttpResponse(msg, content_type="application/json")

def oneCpf(request, user_cpf_id):
    if request.method == 'GET':
        qs = User_cpf.objects.select_related().filter(id = user_cpf_id)
        list = []
        for row in qs:
            list.append({
                'response_status': HttpResponse.status_code,
                'common_user_id': row.common_user.id,
                'user_cpf_id': row.id,
                'user_cpf_name': row.name,
                'user_cpf_last_name': row.last_name,
                'user_cpf_gender': row.gender.name,
                'user_cpf_email': row.common_user.user_email,
                'user_cpf_city': row.common_user.user_city.city_name,
                'user_cpf_state': row.common_user.user_city.state.state_name
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'response_status': HttpResponse.status_code,
            'error': "[INFO] Must be a GET method"
        }]
        msg = json.dumps(msg)
        return HttpResponse(msg, content_type="application/json")

@csrf_exempt
def createCpf(request):
    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        try:
            
            birth_date = body_data["birth_date"]
            birth_date = datetime.strptime(birth_date, '%Y-%m-%d')

            user = Common_user.objects.create(
                user_name = body_data["user_name"], user_email = body_data["user_email"],
                user_password = body_data["user_password"], user_phone = body_data["user_phone"],
                user_city = body_data["user_city"], user_address = body_data["user_address"]
            )
            result = User_cpf.objects.create(
                cpf = body_data["cpf"], full_name = body_data["full_name"],
                birth_date = birth_date, civil_status_id = body_data["civil_status_id"],
                common_user_id = user.id, gender_id = body_data["gender_id"],
                profession = body_data["profession"]
            )

            data = User_cpf.objects.filter(id=result.id)
            data = serialize("json", data)
            return HttpResponse(data, content_type="application/json")   

        except:
            msg = [{
                "message": "[INFO] Creation failed!"
            }]
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")   

    else:
        msg = [{
            'response_status': HttpResponse.status_code,
            "error": "[INFO] Must be a POST method!" 
        }]
        msg = json.dumps(msg)
        return HttpResponse(msg, content_type="application/json")