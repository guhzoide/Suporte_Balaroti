from django.contrib import admin
from django.urls import path
from lojas.views import lojas, listaLojas, ipCameras

urlpatterns = [
    path('lojas', lojas, name='lojas'),
    path('listaLojas', listaLojas, name='listaLojas'),
    path('ipCameras', ipCameras, name='ipCameras'),
]