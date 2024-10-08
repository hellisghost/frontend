from django.db import models
from django.db.models import SET_NULL
from apps.municipios.models import Municipio

# Create your models here.

class Centro(models.Model):
    nombre = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

