import json
from django.http import HttpResponse

def answer_response(qs):
    list = [{"response_status": HttpResponse.status_code}]
    for row in qs:
        list.append({
            "answer_id": row.id,
            "form_id": row.question.form.id,
            "form_title": row.question.form.form_title,
            "question_id": row.question.id,
            "question_title": row.question.question_title,
            "question_type_id": row.question.question_type.id,
            "question_type_title": row.question.question_type.type_title,
            "user_cnpj_id": row.question.form.user_cnpj.id,
            "user_cnpj_fancy_name": row.question.form.user_cnpj.fancy_name,
            "user_cpf_id": row.user_cpf.id,
            "user_cpf_name": row.user_cpf.name,
            "user_answer": row.answer_field
        })
    data = json.dumps(list)
    return data
