from rest_framework.serializers import ModelSerializer
from apps.tipo_sitio.models import Tipo_sitio

class Tipo_sitioSerializer(ModelSerializer):
    class Meta:
        model = Tipo_sitio
        fields = ['id','nombre_tipoSitio','date_created','date_modified']