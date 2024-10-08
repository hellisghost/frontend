from django.db import models
from django.db.models import SET_NULL
from apps.users.models import User
from apps.tipo_movimiento.models import TipoMovimiento

# Create your models here.

class Movimiento(models.Model):

    #slug = models.SlugField(max_length=255, unique=True) aca no me sirve por que los tipos de movimiento siempre son los mismos
    persona_movimiento = models.ForeignKey(User, on_delete=SET_NULL, null=True) #si se elimina el usuarios no se eliminara el movimiento, solo se pondra este espacio en null
    tipo_movimiento=models.ForeignKey(TipoMovimiento, on_delete=SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.persona_movimiento)

