from django.shortcuts import render
from django.http import HttpResponse

from .models import Placa


def index(request):
    data = dict()
    data['regulamentacao'] = Placa.objects.filter(categoria='reg').order_by('pk')
    data['advertencia'] = Placa.objects.filter(categoria='adv').order_by('pk')
    return render(request, 'app_placas/index.html', data)
