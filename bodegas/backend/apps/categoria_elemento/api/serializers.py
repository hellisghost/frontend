from rest_framework import serializers
from apps.categoria_elemento.models import CategoriaElementos

class CategoriaElementosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaElementos
        fields = ['id','CodigoUNPSC_Material','nombre_categoria', 'date_created', 'date_modified']