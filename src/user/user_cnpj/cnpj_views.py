import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from user.common_user.common_user_utils import insert_common_user
from ..models import *
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
            common_user = insert_common_user(body_data)
            user_cnpj = insert_user_cnpj(body_data, common_user.id)

            data = User_cnpj.objects.select_related().filter(id=user_cnpj.id)
            data = cnpj_response(data)
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
