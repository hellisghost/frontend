from django.contrib import admin
from apps.elemento_material.models import ElementoMaterial

@admin.register(ElementoMaterial)
class ElementoMaterialAdmin(admin.ModelAdmin):
    list_display = ['CodigoSena_Material','sitio', 'Categoria_Material', 'Tipo_Material','Nombre_Material','Tipo_Material','Nombre_Material','Descripcion_Material','stock', 'unidad_medida', 'producto_perecedero', 'FechaDevencimiento', 'date_created', 'date_modified']
