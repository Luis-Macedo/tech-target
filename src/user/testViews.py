import json
from django.core.serializers import serialize
from django.http import JsonResponse
from django.http import HttpResponse
from .models import *

def teste(request):
    
    #coloquei o filter para testar e deu certo // EXEMPLO PARA LOGIN
    data = User_cnpj.objects.select_related().filter(common_user__user_password = 1234)
    list = []
    for row in data:
        list.append({
            'user_cnpj_id': row.id, 
            'user_cnpj_name':row.corporate_name,
            'user_cnpj_city': row.common_user.user_city.city_name, 
            'user_password': row.common_user.user_password,
            'logged': True
        })
    print(list)
    data = json.dumps(list)
    return HttpResponse(data, content_type="application/json")