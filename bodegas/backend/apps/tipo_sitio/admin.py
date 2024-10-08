from django.contrib import admin
from apps.tipo_sitio.models import Tipo_sitio

@admin.register(Tipo_sitio)
class Tipo_sitioAdmin(admin.ModelAdmin):
    list_display = ['nombre_tipoSitio','date_created','date_modified']


