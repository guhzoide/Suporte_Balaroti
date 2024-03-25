from django.db import models

class status(models.Model):
    titulo = models.CharField(max_length=5, null=False, blank=False, default='')
    status_atual = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
