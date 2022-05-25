import json
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import *
from techTarget.request_method_utils import *
from .cnpj_utils import *

def all_cnpj(request):
    if request.method == 'GET':
        qs = User_cnpj.objects.all()
        data = cnpj_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")

def one_cnpj(request, user_cnpj_id):
    if request.method == 'GET':
        qs = User_cnpj.objects.select_related().filter(id = user_cnpj_id)
        data = cnpj_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")

@csrf_exempt
def create_cnpj(request):
    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        try:
            user = Common_user.objects.create(
                user_name = body_data["user_name"], user_email = body_data["user_email"],
                user_password = body_data["user_password"], user_phone = body_data["user_phone"],
                user_city_id = body_data["user_city"], user_address = body_data["user_address"]
            )
            result = User_cnpj.objects.create(
                common_user_id = user.id, cnpj = body_data["cnpj"],
                corporate_name = body_data["corporate_name"], fancy_name = body_data["fancy_name"],
                segments_id = body_data["segments"]
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
        msg = post_method_error()
        return HttpResponse(msg, content_type="application/json")
