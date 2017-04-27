# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(["GET"])
def index(request):
    data = {
        'success'   :   True,
        'errors'    :   {},
        'data'      :   {}
    }
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["POST"])
def upload(request):
    data = {
        'success'   :   True,
        'errors'    :   {},
        'data'      :   {
            'files' : {
                'name'      :   '84e5bccddbd31e3040a19ff5f43826e7',
                'created'   :   '2017-04-27 18:30:34'
            }
        }
    }
    return JsonResponse(data)