from django.contrib import admin
from apps.sede import models

@admin.register(models.Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ['nombre_sede', 'centro_sede', 'direccion_sede', 'date_created', 'date_modified']
