from django.contrib import admin
from django.urls import path
from apps.cupom.views import cupom, consultaMovimento

urlpatterns = [
    path('cupom', cupom, name='cupom'),
    path('consultaMovimento', consultaMovimento, name='consultaMovimento'),
]
