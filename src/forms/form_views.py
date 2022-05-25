from django.http import HttpResponse
from .models import *
from .form_utils import *
from techTarget.request_method_utils import *

def list_form_per_user(request, user_cnpj_id):
    if request.method == 'GET':
        qs = Form.objects.select_related('user_cnpj').filter(user_cnpj = user_cnpj_id)
        data = form_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")    

def list_form_per_segment(request, segment_id):
    if request.method == 'GET':
        qs = Form.objects.select_related('user_cnpj').filter(user_cnpj__segments = segment_id, form_active = True)
        data = form_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")
