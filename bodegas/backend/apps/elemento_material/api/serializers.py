from rest_framework import serializers
from apps.elemento_material.models import ElementoMaterial
from apps.tipo_elemento.api.serializers import TipoElementoSerializer
from apps.categoria_elemento.api.serializers import CategoriaElementosSerializer
from apps.categoria_elemento.models import CategoriaElementos
from apps.sitio.api.serializers import SitioSerializer
from apps.sitio.models import Sitio
from apps.tipo_elemento.models import TipoElemento


class ElementoMaterialSerializer(serializers.ModelSerializer):
    Categoria_Material = CategoriaElementosSerializer()
    Tipo_Material = TipoElementoSerializer()
    sitio = SitioSerializer()
    class Meta:

        model = ElementoMaterial

        fields = ['id','sitio','CodigoSena_Material', 'Categoria_Material', 'Tipo_Material','Nombre_Material','Tipo_Material','Nombre_Material','Descripcion_Material','stock', 'unidad_medida', 'producto_perecedero', 'FechaDevencimiento', 'date_created', 'date_modified']

class ElementoWriteMaterial(serializers.ModelSerializer):
    Categoria_Material = serializers.PrimaryKeyRelatedField(queryset=CategoriaElementos.objects.all())
    Tipo_Material = serializers.PrimaryKeyRelatedField(queryset=TipoElemento.objects.all())
    sitio = serializers.PrimaryKeyRelatedField(queryset=Sitio.objects.all())

    class Meta:
        model = ElementoMaterial
        fields = ['id','sitio','CodigoSena_Material', 'Categoria_Material', 'Tipo_Material','Nombre_Material','Descripcion_Material','stock', 'unidad_medida', 'producto_perecedero', 'FechaDevencimiento', 'date_created', 'date_modified']

