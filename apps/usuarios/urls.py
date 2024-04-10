from django.contrib import admin
from django.urls import path
from apps.usuarios.views import login, logout, comparar

urlpatterns = [
    path('', login, name='login'),
    path('comparar', comparar, name='comparar'),
    path('logout', logout, name='logout')
]