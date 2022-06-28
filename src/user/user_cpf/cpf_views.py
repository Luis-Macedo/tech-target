import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from user.common_user.common_user_utils import insert_common_user
from ..models import *
from techTarget.request_method_utils import *
from .cpf_utils import *

def all_cpf(request):
    if request.method == 'GET':
        qs = User_cpf.objects.all()
        data = cpf_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")

def one_cpf(request, user_cpf_id):
    if request.method == 'GET':
        qs = User_cpf.objects.select_related().filter(id = user_cpf_id)
        data = cpf_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")

@csrf_exempt
def create_cpf(request):
    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        try:
            common_user = insert_common_user(body_data)
            user_cpf = insert_user_cpf(body_data, common_user.id)

            data = User_cpf.objects.select_related().filter(id=user_cpf.id)
            data = cpf_response(data)
            return HttpResponse(data, content_type="application/json")   
        except:
            msg = [{
                "message": "[INFO] Creation failed!"
            }]
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")   
    else:
        msg = post_method_error()
        return HttpResponse(msg, content_type="application/json")
