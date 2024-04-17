from django.contrib import admin
from django.urls import path
from apps.usuarios.views import login, logout, comparar, liberarVendas, liberacoes

urlpatterns = [
    path('', login, name='login'),
    path('liberacoes', liberacoes, name='liberacoes'),
    path('comparar', comparar, name='comparar'),
    path('liberarVendas', liberarVendas, name='liberarVendas'),
    path('logout', logout, name='logout')
]