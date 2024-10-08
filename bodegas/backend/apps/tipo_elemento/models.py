from django.db import models

class TipoElemento(models.Model):
    tipo_elemento = models.CharField(max_length=255)
    state = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo_elemento