from django.contrib import admin
from apps.tipo_movimiento.models import TipoMovimiento

@admin.register(TipoMovimiento)
class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ['tipo_movimiento', 'date_created', 'date_modified']