import json
from django.http import HttpResponse

def get_method_error():
    msg = [{
            'response_status': HttpResponse.status_code,
            'error': "[INFO] Must be a GET method"
        }]
    msg = json.dumps(msg)
    return msg

def post_method_error():
    msg = [{
            'response_status': HttpResponse.status_code,
            'error': "[INFO] Must be a POST method"
        }]
    msg = json.dumps(msg)
    return msg

def put_method_error():
    msg = [{
            'response_status': HttpResponse.status_code,
            'error': "[INFO] Must be a PUT method"
        }]
    msg = json.dumps(msg)
    return msg

def delete_method_error():
    msg = [{
            'response_status': HttpResponse.status_code,
            'error': "[INFO] Must be a DELETE method"
        }]
    msg = json.dumps(msg)
    return msg