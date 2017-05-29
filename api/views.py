# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
import uuid
import xlrd


@csrf_exempt
@require_http_methods(["GET"])
def index(request, uid):
    sheet = xlrd.open_workbook("upload/" + uid)

    arkusz = sheet.sheet_by_index(0);
    name = arkusz.row_values(0)[0];

    data = {
        'success'   :   True,
        'errors'    :   {},
        'data'      :   {
                'uid'   :   uid,
                'name'  :   name,
        }
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
            'name'      :   uid
        }
    }
    return JsonResponse(data)

def saveFile(file):
    uid = uuid.uuid4().hex
    with open('upload/' + uid, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return uid