from django.db import models
from datetime import datetime

class cadastroLojas(models.Model):
    OPCOES_CATEGORIA = [
        ("CD", 'CD'),
        ("LOJA", 'Loja'),
        ("LOJA | CD", 'Loja | CD')
    ]

    numero = models.IntegerField(null=False, blank=False)
    loja = models.CharField(max_length=5, null=False, blank=False)
    regiao = models.CharField(max_length=3, null=False, blank=False)
    cd = models.CharField(max_length=13, null=False, blank=False)
    localizacao = models.CharField(max_length=150, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    tronco = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.loja
    
class cadastroCameras(models.Model):
    numero = models.IntegerField(null=False, blank=False)
    loja = models.CharField(max_length=5, null=False, blank=False)
    ip = models.CharField(max_length=20,null=False, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.loja

class cadastroEtiquetas(models.Model):
    numero = models.IntegerField(null=False, blank=False)
    loja = models.CharField(max_length=5, null=False, blank=False)
    ip_etiqueta = models.CharField(max_length=20,null=False, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.loja