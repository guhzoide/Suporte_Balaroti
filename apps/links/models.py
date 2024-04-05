from django.db import models

class cadastroLinks(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    link = models.CharField(max_length=100, null=False, blank=False)
    usuario = models.CharField(max_length=100, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome
