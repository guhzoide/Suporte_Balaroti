from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('', include('apps.cupom.urls')),
    path('', include('apps.programas.urls')),
    path('', include('apps.lojas.urls')),
    path('', include('apps.links.urls')),
    path('', include('apps.tutoriais.urls')),
    path('', include('apps.usuarios.urls')),
]
