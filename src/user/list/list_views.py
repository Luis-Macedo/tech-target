import json
from django.http import HttpResponse
from ..models import *
from techTarget.request_method_utils import *

def city_per_state(request, state):
    if request.method == 'GET':
        qs = Country_city.objects.select_related().filter(state=state)
        list = [{"response_status": HttpResponse.status_code}]
        for row in qs:
            list.append({
                'city_id': row.id,
                'city_code': row.city_code,
                'city_name': row.city_name,
                'state': row.state.state_name
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")

def all_states(request):
    if request.method == "GET":
        qs = Country_state.objects.select_related()
        list = [{"response_status": HttpResponse.status_code}]
        for row in qs:
            list.append({
                'state_code': row.state_code,
                'state_name': row.state_name,
                'acronym': row.acronym,
                "region": row.region.region_name
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")

def all_common(request):
    if request.method == 'GET':
        qs = Common_user.objects.all()
        list = [{"response_status": HttpResponse.status_code}]
        for row in qs:
            list.append({
                "common_user_id": row.id,
                "user_name": row.user_name,
                "user_email": row.user_email,
                "user_phone": row.user_phone,
                "user_city": row.user_city.city_name 
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error
        return HttpResponse(msg, content_type="application/json")

def all_gender(request):
    if request.method == 'GET':
        qs = Gender.objects.all()
        list = [{"response_status": HttpResponse.status_code}]
        for row in qs:
            list.append({
                "gender_id": row.id,
                "gender_name": row.name,
                "gender_description": row.description,
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")

def all_segment(request):
    if request.method == 'GET':
        qs = Segment.objects.all()
        list = [{"response_status": HttpResponse.status_code}]
        for row in qs:
            list.append({
                "segment_id": row.id,
                "segment_title": row.title,
                "segment_description": row.description,
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")

def all_civil(request):
    if request.method == 'GET':
        qs = Civil_stat.objects.all()
        list = [{"response_status": HttpResponse.status_code}]
        for row in qs:
            list.append({
                "civil_status_id": row.id,
                "civil_status_name": row.status_name,
                "civil_status_description": row.status_description,
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")
