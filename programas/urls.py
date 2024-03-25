from django.contrib import admin
from django.urls import path
from programas.views import programas, verificaProgramas, desativatudo

urlpatterns = [
    path('programas', programas, name='programas'),
    path('verificaProgramas', verificaProgramas, name='verificaProgramas'),
    path('desativatudo', desativatudo, name='desativatudo'),
]
