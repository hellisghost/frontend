from django.contrib import admin
from apps.sitio.models import Sitio

@admin.register(Sitio)
class SitioAdmin(admin.ModelAdmin):
    list_display = ['nombre_sitio','persona_encargada','tipo_sitio', 'ubicacion', 'FichaTecnica', 'date_created', 'date_modified']

