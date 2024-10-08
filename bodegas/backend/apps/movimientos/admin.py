from django.contrib import admin
from apps.movimientos.models import Movimiento

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ['tipo_movimiento', 'persona_movimiento', 'fecha_creacion', 'fecha_modificacion']
