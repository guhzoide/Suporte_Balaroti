from django.contrib import admin
from django.urls import path
from apps.usuarios.views import login, logout, comparar, liberarVendas, liberacoes, contaOmni

urlpatterns = [
    path('', login, name='login'),
    path('liberacoes', liberacoes, name='liberacoes'),
    path('comparar', comparar, name='comparar'),
    path('liberarVendas', liberarVendas, name='liberarVendas'),
    path('contaOmni', contaOmni, name='contaOmni'),
    path('logout', logout, name='logout')
]