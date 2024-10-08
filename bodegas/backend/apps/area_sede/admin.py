from django.contrib import admin
from apps.area_sede.models import AreaSede

@admin.register(AreaSede)
class AreaSedeAdmin(admin.ModelAdmin):
    list_display = ['sede_area', 'area_AreaSede', 'persona_administra', 'date_created', 'date_modified']
