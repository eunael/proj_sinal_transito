from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Index de SITE.")
    return render(request, 'app_site/index.html')
