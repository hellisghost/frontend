from django.db import models
from apps.area.models import Area
from django.db.models import SET_NULL

# Create your models here.

class Programa(models.Model):
    nombre_programa = models.CharField(max_length=100)
    area_programa = models.ForeignKey(Area, on_delete=SET_NULL, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.nombre_programa
