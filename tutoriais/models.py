from django.db import models

class cadastroTutoriais(models.Model):
    titulo  = models.CharField(max_length=100, null=False, blank=False)
    tutorial = models.FileField(upload_to="tutoriais/", blank=True)
    publicada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
