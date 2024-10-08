from django.contrib import admin
from apps.municipios.models import Municipio

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'date_created', 'date_modified']

# Register your models here.
