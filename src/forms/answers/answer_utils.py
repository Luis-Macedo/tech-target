import json
from django.http import HttpResponse
from forms.models import User_answer

def answer_response(qs):
    list = [{"response_status": HttpResponse.status_code}]
    for row in qs:
        list.append({
            "answer_id": row.id,
            "form_id": row.question.user_form.id,
            "form_title": row.question.user_form.form_title,
            "question_id": row.question.id,
            "question_title": row.question.question_title,
            "question_type_id": row.question.question_type.id,
            "question_type_title": row.question.question_type.type_title,
            "user_cnpj_id": row.question.user_form.user_cnpj.id,
            "user_cnpj_fancy_name": row.question.user_form.user_cnpj.fancy_name,
            "user_cpf_id": row.user_cpf.id,
            "user_cpf_name": row.user_cpf.name,
            "user_cpf_answer": row.answer_field
        })
    data = json.dumps(list)
    return data

def insert_answer(user_cpf_id, answers):
    list = []
    for i in range(len(answers)):
    
        key_word = 'answer_field'
        answer = answers[i]

        for word in answer:
            if word.startswith(key_word):
                answer_field = answer[word]
        
        qs = User_answer.objects.create(user_cpf_id = user_cpf_id, question_id = answer['question_id'], 
            answer_field = answer_field
        )
        list.append(qs.id)
    return list
