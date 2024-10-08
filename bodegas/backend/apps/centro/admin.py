from django.contrib import admin
from apps.centro.models import Centro

@admin.register(Centro)
class CentroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'municipio', 'date_created']
