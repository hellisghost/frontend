from rest_framework import serializers
from apps.tipo_movimiento.models import TipoMovimiento

class TipoMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMovimiento
        fields = ['id', 'tipo_movimiento', 'date_created', 'date_modified']