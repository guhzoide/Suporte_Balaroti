from django.contrib import admin
from django.urls import path
from apps.home.views import index

urlpatterns = [
    path('index', index, name='index'),
]
