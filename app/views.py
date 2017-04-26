# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title' :   'Strona Główna',
        'content'   :   'To jest przykładowy tekst'
    }
    return render(request, 'app/index.html', context)