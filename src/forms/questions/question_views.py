import json
from django.http import HttpResponse
from ..models import *
from techTarget.request_method_utils import *

def list_per_form(request, form_id):
    if request.method == 'GET':
        qs = Question.objects.select_related('user_form').filter(user_form = form_id)
        list = [{"response_status": HttpResponse.status_code}]

        for row in qs:
            list.append({
                "form_id": row.user_form.id,
                "question_id": row.id,
                "question_title": row.question_title,
                "question_type_id": row.question_type.id,
                "question_type_title": row.question_type.type_title,
                "question_order": row.question_order
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")

def list_types(request):
    if request.method == 'GET':
        qs = Question_type.objects.select_related()
        list = [{"response_status": HttpResponse.status_code}]

        for row in qs:
            list.append({
                "question_type_id": row.id,
                "question_type_title": row.type_title,
                "question_type_description": row.type_description,
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")