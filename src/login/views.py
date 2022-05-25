import json
from django.http import HttpResponse
from login.view_utils import cnpj_login, cpf_login
from user.models import *
from django.views.decorators.csrf import csrf_exempt
from techTarget.request_method_utils import *

@csrf_exempt
def login(request):

    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        
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
                data = cpf_login(cpf_data)
                return HttpResponse(data, content_type="application/json")
            else:
                data = cnpj_login(cnpj_data)
                return HttpResponse(data, content_type="application/json")
        except:
            msg = [{
                "message": "[INFO] Error! Database error"
            }]
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")
    else:   
        msg = post_method_error()
        return HttpResponse(msg, content_type="application/json")
