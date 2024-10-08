from rest_framework import serializers
from apps.municipios.models import Municipio

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['id','nombre', 'date_created', 'date_modified']