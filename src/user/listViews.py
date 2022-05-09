import json
from django.core.serializers import serialize
from django.http import JsonResponse
from django.http import HttpResponse
from .models import *

def cityPerState(request, state):
    if request.method == 'GET':
        qs = Country_city.objects.select_related().filter(state=state)
        list = []
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
        msg = [{
            'error': "[INFO] Must be a GET method"
        }]
        return HttpResponse(msg, content_type="application/json")

def allCommon(request):
    if request.method == 'GET':
        qs = Common_user.objects.all()
        data = serialize("json", qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'error': "[INFO] Must be a GET method"
        }]
        return HttpResponse(msg, content_type="application/json")

def allCnpj(request):
    if request.method == 'GET':
        qs = User_cnpj.objects.all()
        data = serialize("json", qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'error': "[INFO] Must be a GET method"
        }]
        return HttpResponse(msg, content_type="application/json")

def allCpf(request):
    if request.method == 'GET':
        qs =  User_cpf.objects.all()
        data = serialize("json", qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'error': "[INFO] Must be a GET method"
        }]
        return HttpResponse(msg, content_type="application/json")

def allGender(request):
    if request.method == 'GET':
        qs = Gender.objects.all()
        data = serialize("json", qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'error': "[INFO] Must be a GET method"
        }]
        return HttpResponse(msg, content_type="application/json")

def allSegment(request):
    if request.method == 'GET':
        qs = Segment.objects.all()
        data = serialize("json", qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'error': "[INFO] Must be a GET method"
        }]
        return HttpResponse(msg, content_type="application/json")

def allCivil(request):
    if request.method == 'GET':
        qs = Civil_stat.objects.all()
        data = serialize("json", qs)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'error': "[INFO] Must be a GET method"
        }]
        return HttpResponse(msg, content_type="application/json")

def oneCommon(request, common_user_id):
    if request.method == 'GET':
        qs = Common_user.objects.select_related().filter(id = common_user_id)
        list = []
        for row in qs:
            list.append({
                'common_user_id': row.id,
                'common_user_name': row.user_name,
                'common_user_city': row.user_city.city_name
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'error': "[INFO] Must be a GET method"
        }]
        return HttpResponse(msg, content_type="application/json")

def oneCnpj(request, user_cnpj_id):
    if request.method == 'GET':
        qs = User_cnpj.objects.select_related().filter(id = user_cnpj_id)
        list = []
        for row in qs:
            list.append({
                'user_cnpj_id': row.id,
                'user_cnpj_name': row.corporate_name,
                'user_cnpj_city': row.common_user.user_city.city_name
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'error': "[INFO] Must be a GET method"
        }]
        return HttpResponse(msg, content_type="application/json")

def oneCpf(request, user_cpf_id):
    if request.method == 'GET':
        qs = User_cpf.objects.select_related().filter(id = user_cpf_id)
        list = []
        for row in qs:
            list.append({
                'user_cpf_id': row.id,
                'user_cpf_name': row.name,
                'user_cpf_city': row.common_user.user_city.city_name
            })
        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = [{
            'error': "[INFO] Must be a GET method"
        }]
        return HttpResponse(msg, content_type="application/json")
