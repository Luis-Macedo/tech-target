from django.http import HttpResponse
import pandas as pd
from forms.models import *
import json

def convert(lst):
    df = pd.DataFrame(lst)
    final = df.to_dict()
    return final

def per_question(question_id):

    qs = User_answer.objects.select_related().filter(question__id = question_id)
    list = []
    try:
        for row in qs:
            list.append({
                "form_id": row.question.user_form.id,
                "question_id": row.question.id,
                "question_type": row.question.question_type.id,
                "question_title": row.question.question_title,
                "answer": str(row.answer_field),
                "user_civil_status": row.user_cpf.civil_status.status_name,
                "user_gender": row.user_cpf.gender.name,
                "state": row.user_cpf.common_user.user_city.state.acronym        
            })

        data = json.dumps(list)
        df = pd.read_json(data)

        question_title = df['question_title'][0]
        final = [{"question_id": question_id}, {"question_title": question_title}]
        
        answer_values = df['answer'].value_counts()
        state_values = df['state'].value_counts()
        civil_status_values = df['user_civil_status'].value_counts()
        gender_values = df['user_gender'].value_counts()

        answer_values = convert(answer_values)
        state_values = convert(state_values)
        civil_status_values = convert(civil_status_values)
        gender_values = convert(gender_values)
        
        final.append((answer_values, state_values, civil_status_values, gender_values))
        final = json.dumps(final)
        return final
    except:
        msg = {
            "Message": "[INFO] no answers found yet"
        }
        msg = json.dumps(msg)
        return msg