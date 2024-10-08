from django.db import models

# Create your models here.

class CategoriaElementos(models.Model):
    CodigoUNPSC_Material = models.CharField(max_length=255)
    nombre_categoria = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_categoria
