from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='site.index'),
    path('teste/', views.teste, name='site.teste'),
]
