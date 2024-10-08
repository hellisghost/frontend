from django.db import models

from django.db.models import SET_NULL

class Area(models.Model):
    nombre_area = models.CharField(max_length=100)
   #programa_area = models.ForeignKey(Programa, on_delete=SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_area
