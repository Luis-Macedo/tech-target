from django.http import HttpResponse
from ..models import *
from .form_utils import *
from techTarget.request_method_utils import *
from django.views.decorators.csrf import csrf_exempt

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

def list_all_forms(request):
    if request.method == 'GET':
        qs = Form.objects.select_related()
        data = form_response(qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")

@csrf_exempt
def create_form(request, user_cnpj_id):
    if request.method == "POST":

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        questions = body_data["questions"]

        try:
            
            user_form = Form.objects.create(
                user_cnpj_id = user_cnpj_id, form_title = body_data["title"], 
                form_description = body_data["description"], form_active = True
            )
            insert_questions(user_form.id, questions)
            
            data = Form.objects.select_related().filter(id = user_form.id)
            res = form_response(data)
            return HttpResponse(res, content_type="application/json")
        except:
            msg = [{
                "message": "[INFO] Creation failed!"
            }]
            msg = json.dumps(msg)
            return HttpResponse(msg, content_type="application/json")
    else:
        msg = post_method_error()
        return HttpResponse(msg, content_type="application/json")


