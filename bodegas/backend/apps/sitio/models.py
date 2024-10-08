from django.db import models
from django.db.models import SET_NULL
from apps.tipo_sitio.models import Tipo_sitio
from apps.users.models import User


class Sitio(models.Model):
    persona_encargada = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    nombre_sitio = models.CharField(max_length=100)
    tipo_sitio = models.ForeignKey(Tipo_sitio, on_delete=SET_NULL, null=True)
    ubicacion = models.CharField(max_length=100)
    FichaTecnica = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_sitio



