from django.contrib import admin
from django.urls import path
from apps.usuarios.views import login, logout, comparar, pesquisar

urlpatterns = [
    path('', login, name='login'),
    path('comparar', comparar, name='comparar'),
    path('pesquisar', pesquisar, name='pesquisar'),
    path('logout', logout, name='logout')
]