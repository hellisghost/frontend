from django.contrib import admin
from apps.tipo_elemento.models import TipoElemento

@admin.register(TipoElemento)
class TipoElementoAdmin(admin.ModelAdmin):
    list_display = ['tipo_elemento', 'state', 'date_created', 'date_modified']
