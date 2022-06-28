import json
import pandas as pd
from django.http import HttpResponse
from forms.models import *
from dashboards.dash_utils import *
import json
from techTarget.request_method_utils import *

def dash_per_question(request, question_id):
    if request.method == 'GET':
        data = per_question(question_id)
        msg = {
            "message": "ok"
        }
        msg = json.dumps(msg)
        return HttpResponse(data, content_type="application/json")
    else:
        msg = get_method_error()
        return HttpResponse(msg, content_type="application/json")

