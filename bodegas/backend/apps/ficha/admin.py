from django.contrib import admin
from apps.ficha.models import Ficha

@admin.register(Ficha)
class FichaAdmin(admin.ModelAdmin):
    list_display = ['id_ficha', 'persona_ficha', 'programa', 'date_created']

