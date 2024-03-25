from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('cupom.urls')),
    path('', include('programas.urls')),
    path('', include('lojas.urls')),
    path('', include('links.urls')),
    path('', include('tutoriais.urls')),
    path('', include('usuarios.urls')),
]
