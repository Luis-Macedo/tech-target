from django.http import HttpResponse
from .models import *
from .answer_utils import *
from techTarget.request_method_utils import *

def list_answer_per_user(request, user_cpf_id):
    if request.method == 'GET':
        qs = User_answer.objects.select_related().filter(user_cpf = user_cpf_id)
        data = answer_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")  

def list_answer_per_question(request, form_id, question_id):
    if request.method == 'GET':
        qs = User_answer.objects.select_related().filter(question = question_id, question__form = form_id)
        data = answer_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json") 
    
def list_answer_per_form(request, form_id):
    if request.method == 'GET':
        qs = User_answer.objects.select_related().filter(question__form = form_id)
        data = answer_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json") 

