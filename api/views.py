# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
import uuid


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
    uid = ''
    success = False

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uid = saveFile(request.FILES['file'])
            success = True

    data = {
        'success'   :   success,
        'errors'    :   {},
        'data'      :   {
            'files' : {
                'name'      :   uid,
                'created'   :   '2017-04-27 18:30:34'
            }
        }
    }
    return JsonResponse(data)

def saveFile(file):
    uid = uuid.uuid4().hex
    with open('upload/' + uid, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return uid