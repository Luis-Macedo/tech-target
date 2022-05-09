from django.core.serializers import serialize
from django.http import HttpResponse
from user.models import *

def teste(request):
    qs = Gender.objects.all()
    data = serialize("json", qs)
    return HttpResponse(data, content_type="application/json")