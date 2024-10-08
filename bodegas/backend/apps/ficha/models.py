from django.db import models
from apps.users.models import User
from django.db.models import SET_NULL
from apps.programa.models import Programa

class Ficha(models.Model):
    id_ficha = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    persona_ficha = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    programa = models.ForeignKey(Programa, on_delete=SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_ficha