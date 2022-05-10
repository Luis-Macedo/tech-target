import json
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import *

def allCnpj(request):
    if request.method == 'GET':
        qs = User_cnpj.objects.all()
        data = serialize("json", qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'response_status': HttpResponse.status_code,
            'error': "[INFO] Must be a GET method"
        }]
        msg = json.dumps(msg)
        return HttpResponse(msg, content_type="application/json")

def oneCnpj(request, user_cnpj_id):
    if request.method == 'GET':
        qs = User_cnpj.objects.select_related().filter(id = user_cnpj_id)
        list = []
        for row in qs:
            list.append({
                'response_status': HttpResponse.status_code,
                'common_user_id': row.common_user.id,
                'user_cnpj_id': row.id,
                'user_cnpj_corporate_name': row.corporate_name,
                'user_cnpj_fancy_name': row.fancy_name,
                'user_cnpj_email': row.common_user.user_email,
                'user_cnpj_city': row.common_user.user_city.city_name,
                'user_cnpj_state': row.common_user.user_city.state.state_name
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
                "message": "[INFO] Creation Failed!"
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
