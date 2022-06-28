import json
from django.http import HttpResponse
from ..models import *

def form_response(qs):
    list = [{"response_status": HttpResponse.status_code}]
    for row in qs:
        list.append({
            "form_id": row.id,
            "form_title": row.form_title,
            "form_description": row.form_description,
            "form_active": row.form_active,
            "date_creation": str(row.date_creation),
            "user_cnpj_id": row.user_cnpj.id,
            "user_cnpj_fancy_name": row.user_cnpj.fancy_name,
            "segment": row.user_cnpj.segments.title
        })
    data = json.dumps(list)
    return data

def insert_questions(user_form, questions):
    list = []
    for i in range(len(questions)):
        
        question = questions[i]
        qs = Question.objects.create(user_form_id = user_form, question_type_id = question['question_type_id'], 
            question_title = question['question_title'], 
            question_order = question['question_order']
        )
        list.append(qs.id)
    return list