from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Index de QUIS")
    return render(request, 'app_quis/index.html')
