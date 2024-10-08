from django.contrib import admin
from apps.programa.models import Programa

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ['nombre_programa', 'date_created', 'date_modified']
