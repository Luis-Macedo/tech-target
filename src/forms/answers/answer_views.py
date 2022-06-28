from django.http import HttpResponse
from ..models import *
from .answer_utils import *
from techTarget.request_method_utils import *
from django.views.decorators.csrf import csrf_exempt

def list_answer_per_user(request, user_cpf_id):
    if request.method == 'GET':
        qs = User_answer.objects.select_related().filter(user_cpf = user_cpf_id)
        data = answer_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")  

def list_answer_per_question(request, question_id):
    if request.method == 'GET':
        qs = User_answer.objects.select_related().filter(question = question_id)
        data = answer_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json") 
    
def list_answer_per_form(request, form_id):
    if request.method == 'GET':
        qs = User_answer.objects.select_related().filter(question__user_form = form_id)
        data = answer_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json") 

@csrf_exempt
def insert_answers(request, user_cpf_id):
    if request.method == 'POST':
        
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        answers = body_data["answers"]

        qs = insert_answer(user_cpf_id, answers)

        if len(qs) > 0:
            msg = {
                "response_status": HttpResponse.status_code,
                "success": "Form answered"
            }
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")
        else:
            msg = {
                "response_status": HttpResponse.status_code,
                "error": "Form could not be answered"
            }
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")
    else:
        msg = post_method_error()
        return HttpResponse(msg, content_type="application/json")
