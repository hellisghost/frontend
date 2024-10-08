from rest_framework import serializers
from apps.sede.models import Sede
from apps.centro.models import Centro

class SedeSerializer(serializers.ModelSerializer):
    centro_sede_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Sede
        fields = ['id', 'nombre_sede', 'centro_sede', 'centro_sede_nombre', 'direccion_sede', 'date_created', 'date_modified']

    def get_centro_sede_nombre(self, obj):
        if obj.centro_sede:
            return obj.centro_sede.nombre
        return 'Sin nombre'  # Valor predeterminado si no hay centro asociado
