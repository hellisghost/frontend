from rest_framework import serializers
from apps.area.models import Area
from apps.programa.models import Programa
from apps.area.api.serializers import AreaSerializer

class ProgramaSerializer(serializers.ModelSerializer):
    area_programa = AreaSerializer()
    class Meta:
        model = Programa
        fields = ['id','nombre_programa', 'area_programa','date_created', 'date_modified']

class ProgramaWriteSerializer(serializers.ModelSerializer):
    area_programa = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    class Meta:
        model = Programa
        fields = ['id','nombre_programa', 'area_programa','date_created', 'date_modified']
