from rest_framework import serializers
from apps.centro.models import Centro
from apps.municipios.models import Municipio

class CentroSerializer(serializers.ModelSerializer):
    municipio = serializers.PrimaryKeyRelatedField(queryset=Municipio.objects.all(), required=False)  # Acepta el ID del municipio
    municipio_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Centro
        fields = ['id', 'nombre', 'municipio', 'municipio_nombre', 'date_created', 'date_modified']
        read_only_fields = ['date_created', 'date_modified']

    def get_municipio_nombre(self, obj):
        if obj.municipio:
            return obj.municipio.nombre
        return 'Sin nombre'

    def create(self, validated_data):
        return Centro.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.municipio = validated_data.get('municipio', instance.municipio)
        instance.save()
        return instance
