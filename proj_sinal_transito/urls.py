from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_site.urls')),
    path('quis/', include('app_quis.urls')),
    path('placas/', include('app_placas.urls')),
]
