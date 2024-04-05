from django.contrib import admin
from django.urls import path
from apps.links.views import links

urlpatterns = [
    path('links', links, name='links'),
]