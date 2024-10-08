from django.contrib import admin
from apps.area.models import Area

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['nombre_area', 'date_created', 'date_modified']