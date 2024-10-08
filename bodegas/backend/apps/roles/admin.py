from django.contrib import admin
from apps.roles.models import Rol

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ['name_rol', 'state_rol', 'description']

