from django.db import models
from apps.centro.models import Centro
from django.db.models import SET_NULL

class Sede(models.Model):
    nombre_sede = models.CharField(max_length=100)
    centro_sede = models.ForeignKey(Centro, on_delete=SET_NULL, null=True)
    direccion_sede = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_sede
