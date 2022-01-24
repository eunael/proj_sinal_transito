from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Index de PLACAS.")
    return render(request, 'app_placas/index.html')
