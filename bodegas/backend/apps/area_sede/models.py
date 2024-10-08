from django.db import models
from django.db.models import SET_NULL
from apps.area.models import Area
from apps.sede.models import Sede
from apps.users.models import User


class AreaSede(models.Model):
    sede_area = models.ForeignKey(Sede, on_delete=SET_NULL, null=True)
    area_AreaSede = models.ForeignKey(Area, on_delete=SET_NULL, null=True)
    persona_administra = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sede_area)

