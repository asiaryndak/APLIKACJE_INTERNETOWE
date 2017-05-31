# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
import uuid
import xlrd
import xlwt


@csrf_exempt
@require_http_methods(["GET"])
def index(request, uid):
    file = xlrd.open_workbook("upload/" + uid)

    sheet = file.sheet_by_index(0);
    name = sheet.row_values(0)[0];

    data = {
        'success': True,
        'errors': {},
        'data': {
            'uid': uid,
            'name': name,
        }
    }

    return JsonResponse(data)


@csrf_exempt
@require_http_methods(["GET"])
def chartCars(request, uid):
    file = xlrd.open_workbook("upload/" + uid);
    sheet = file.sheet_by_index(0);
    arkusz = file.sheet_by_name("Arkusz1")
    labels = []
    values = []
    colors = []

    for i in range(2, arkusz.nrows):
        labels.append(arkusz.row_values(i)[0])
        # print(arkusz.row_values(i)[0])
        # print(file.sheet_names())

    for i in range(2, arkusz.nrows):
        values.append(arkusz.row_values(i)[3])
        colors.append("red")
        # print(arkusz.row_values(i)[3])

    # labels = ["Kombi", "Sedan", "Van", "Checkback", "Kabriolet", "Sportowy"]
    # values = [27, 38, 16, 41, 6, 19];

    data = {
        'success': True,
        'errors': {},
        'data': {
            'uid': uid,
            'labels': labels,
            'values': values,
        }
    }

    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["GET"])
def precision(request, uid):
    file = xlrd.open_workbook("upload/" + uid);
    sheet = file.sheet_by_index(0);
    arkusz = file.sheet_by_name("Arkusz1")


    rows = arkusz.nrows;
    badRows = 0;
    for i in range(2,arkusz.nrows):
        if ((arkusz.row_values(i)[0] < 31) or (arkusz.row_values(i)[1] == "Sportowe")) and (arkusz.row_values(i)[2] == "Wysokie"):
            badRows+=1;

    precision = round(((rows-badRows)/rows) * 100, 2);
    data = {
        'success': True,
        'errors': {},
        'data': {
            'uid': uid,
            'precision': precision,
        }
    }

    return JsonResponse(data)

csrf_exempt
@require_http_methods(["GET"])
def download(request, uid):
    file = xlrd.open_workbook("upload/" + uid);
    arkusz = file.sheet_by_index(1);

    book = xlwt.Workbook(encoding="utf-8")

    sheet1 = book.add_sheet("Raport");

    sheet1.write(0, 0, "Wynik działania algorytmu");

    sheet1.write(1, 0, "Wiek kierowcy");
    sheet1.write(1, 1, "Typ samochodu");
    sheet1.write(1, 2, "Ryzyko");

    for i in range(2,arkusz.nrows):
        sheet1.write(i, 0, arkusz.row_values(i)[0]);
        sheet1.write(i, 1, arkusz.row_values(i)[1]);

        if ((arkusz.row_values(i)[0] < 31) or (arkusz.row_values(i)[1] == "Sportowe")):
            sheet1.write(i, 2, "Wysokie");
        else:
            sheet1.write(i, 2, "Niskie");


    name = uuid.uuid4().hex + ".xls";
    book.save("app/static/files/" + name);

    data = {
        'success': True,
        'errors': {},
        'data': {
            'uid': uid,
            'name': name,
            'test': arkusz.nrows
        }
    }

    return JsonResponse(data)

@csrf_exempt
@require_http_methods(["GET"])
def chartCars2(request, uid):
    file = xlrd.open_workbook("upload/" + uid);
    sheet = file.sheet_by_index(0);
    arkusz = file.sheet_by_name("Arkusz1")
    values = []
    sedan = 0
    kombi = 0
    hatchback = 0
    van = 0
    kabriolet = 0
    sportowe = 0
    # for i in range(2,arkusz.nrows):
    #     labels.append(arkusz.row_values(i)[0])
    #     print(arkusz.row_values(i)[0])
    #     print(file.sheet_names())


    for i in range(2, arkusz.nrows):
        print(arkusz.row_values(i)[1])
        if arkusz.row_values(i)[1] == "Sedan":
            sedan += 1
        elif arkusz.row_values(i)[1] == "Kombi":
            kombi += 1
        elif arkusz.row_values(i)[1] == "Hatchback":
            hatchback += 1
        elif arkusz.row_values(i)[1] == "Van":
            van += 1
        elif arkusz.row_values(i)[1] == "Kabriolet":
            kabriolet += 1
        elif arkusz.row_values(i)[1] == "Sportowe":
            sportowe += 1

    values.extend((sedan, kombi, hatchback, van, kabriolet, sportowe))

    data = {
        'success': True,
        'errors': {},
        'data': {
            'uid': uid,
            'values': values,
        }
    }

    return JsonResponse(data)


@csrf_exempt
@require_http_methods(["GET"])
def precision(request, uid):
    file = xlrd.open_workbook("upload/" + uid);
    sheet = file.sheet_by_index(0);
    arkusz = file.sheet_by_name("Arkusz1")

    rows = arkusz.nrows;
    badRows = 0;
    for i in range(2, arkusz.nrows):
        if ((arkusz.row_values(i)[0] < 31) or (arkusz.row_values(i)[1] == "Sportowe")) and (
            arkusz.row_values(i)[2] == "Wysokie"):
            badRows += 1;

    precision = round(((rows - badRows) / rows) * 100, 2);
    data = {
        'success': True,
        'errors': {},
        'data': {
            'uid': uid,
            'precision': precision,
        }
    }

    return JsonResponse(data)


csrf_exempt


@require_http_methods(["GET"])
def download(request, uid):
    file = xlrd.open_workbook("upload/" + uid);
    arkusz = file.sheet_by_index(1);

    book = xlwt.Workbook(encoding="utf-8")

    sheet1 = book.add_sheet("Raport");

    sheet1.write(0, 0, "Wynik działania algorytmu");

    sheet1.write(1, 0, "Wiek kierowcy");
    sheet1.write(1, 1, "Typ samochodu");
    sheet1.write(1, 2, "Ryzyko");

    for i in range(2, arkusz.nrows):
        sheet1.write(i, 0, arkusz.row_values(i)[0]);
        sheet1.write(i, 1, arkusz.row_values(i)[1]);

        if ((arkusz.row_values(i)[0] < 31) or (arkusz.row_values(i)[1] == "Sportowe")):
            sheet1.write(i, 2, "Wysokie");
        else:
            sheet1.write(i, 2, "Niskie");

    name = uuid.uuid4().hex + ".xls";
    book.save("app/static/files/" + name);

    data = {
        'success': True,
        'errors': {},
        'data': {
            'uid': uid,
            'name': name,
            'test': arkusz.nrows
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
        'success': success,
        'errors': {},
        'data': {
            'name': uid
        }
    }
    return JsonResponse(data)


def saveFile(file):
    uid = uuid.uuid4().hex
    with open('upload/' + uid, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return uid
