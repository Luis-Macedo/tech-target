import json
from django.http import HttpResponse

def form_response(qs):
    list = [{"response_status": HttpResponse.status_code}]
    for row in qs:
        list.append({
            "form_id": row.id,
            "form_title": row.form_title,
            "form_description": row.form_description,
            "form_active": row.form_active,
            "user_cnpj_id": row.user_cnpj.id,
            "user_cnpj_fancy_name": row.user_cnpj.fancy_name,
            "segment": row.user_cnpj.segments.title
        })
    data = json.dumps(list)
    return data
