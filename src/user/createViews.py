import json
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import HttpResponse
from .models import *

@csrf_exempt
def createCnpj(request):
    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        try:

            user = Common_user.objects.create(
                user_name = body_data["user_name"], user_email = body_data["user_email"],
                user_password = body_data["user_password"], user_phone = body_data["user_phone"],
                user_city = body_data["user_city"], user_address = body_data["user_address"]
            )
            result = User_cnpj.objects.create(
                common_user_id = user.id, cnpj = body_data["cnpj"],
                corporate_name = body_data["corporate_name"], fancy_name = body_data["fancy_name"],
                segments = body_data["segments"]
            )

            data = User_cnpj.objects.filter(id=result.id)
            data = serialize("json", data)
            return HttpResponse(data, content_type="application/json")   

        except:
            msg = [{
                "message": "Error"
            }]
            return HttpResponse(msg, content_type="application/json")   

    else:
        msg = [{
            "error": "[INFO] Must be a POST method!" 
        }]
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
                "message": "Error"
            }]
            return HttpResponse(msg, content_type="application/json")   

    else:
        msg = [{
            "error": "[INFO] Must be a POST method!" 
        }]
        return HttpResponse(msg, content_type="application/json")
