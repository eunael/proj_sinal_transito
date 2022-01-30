from django.shortcuts import render
from django.http import HttpResponse

from .models import Placa


def index(request):
    placas = Placa.objects.all()
    return render(request, 'app_placas/index.html', {'placas': placas})
