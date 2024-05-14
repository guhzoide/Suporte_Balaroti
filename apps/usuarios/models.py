from django.db import models

class cadastroCodigoOmni(models.Model):
    OPCOES_CATEGORIA = [
        ("VENDEDOR","Vendedor"),
        ("GESTAO","Gestao"),

    ]

    numero = models.IntegerField(null=False, blank=False)
    descricao = models.CharField(max_length=150, null=False, blank=False)
    codigo = models.CharField(max_length=150, null=False, blank=False)
    acesso = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')

    def __str__(self):
        return self.descricao