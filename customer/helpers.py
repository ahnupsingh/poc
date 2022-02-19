import json

def get_request_body(request):
    return json.loads(request.body.decode("utf-8"))

def get_request_params(request):
    return request.GET.dict()