import json
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import *

def cityPerState(request, state):
    if request.method == 'GET':
        qs = Country_city.objects.select_related().filter(state=state)
        list = []
        for row in qs:
            list.append({
                'response_status': HttpResponse.status_code,
                'city_id': row.id,
                'city_code': row.city_code,
                'city_name': row.city_name,
                'state': row.state.state_name
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'response_status': HttpResponse.status_code,
            'error': "[INFO] Must be a GET method"
        }]
        msg = json.dumps(msg)
        return HttpResponse(msg, content_type="application/json")

def allCommon(request):
    if request.method == 'GET':
        qs = Common_user.objects.all()
        data = serialize("json", qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'response_status': HttpResponse.status_code,
            'error': "[INFO] Must be a GET method"
        }]
        msg = json.dumps(msg)
        return HttpResponse(msg, content_type="application/json")

def allGender(request):
    if request.method == 'GET':
        qs = Gender.objects.all()
        data = serialize("json", qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'response_status': HttpResponse.status_code,
            'error': "[INFO] Must be a GET method"
        }]
        msg = json.dumps(msg)
        return HttpResponse(msg, content_type="application/json")

def allSegment(request):
    if request.method == 'GET':
        qs = Segment.objects.all()
        data = serialize("json", qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'response_status': HttpResponse.status_code,
            'error': "[INFO] Must be a GET method"
        }]
        msg = json.dumps(msg)
        return HttpResponse(msg, content_type="application/json")

def allCivil(request):
    if request.method == 'GET':
        qs = Civil_stat.objects.all()
        data = serialize("json", qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'response_status': HttpResponse.status_code,
            'error': "[INFO] Must be a GET method"
        }]
        msg = json.dumps(msg)
        return HttpResponse(msg, content_type="application/json")
