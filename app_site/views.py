from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Index de SITE.")
    return render(request, 'app_site/index.html')

def documentos(request):
    return render(request, 'app_site/documentos.html')

def teste(request):
    return render(request, 'teste.html')
