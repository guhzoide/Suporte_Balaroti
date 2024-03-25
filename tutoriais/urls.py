from django.contrib import admin
from django.urls import path
from tutoriais.views import tutoriais, visualizar

urlpatterns = [
    path('tutoriais', tutoriais, name='tutoriais'),
    path('visualizar/<int:tutorial_id>', visualizar, name='visualizar'),
]