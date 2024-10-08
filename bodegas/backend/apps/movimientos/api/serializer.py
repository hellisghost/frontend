from rest_framework import serializers
from apps.movimientos.models import Movimiento
from apps.tipo_movimiento.api.serializers import TipoMovimientoSerializer
from apps.users.api.serializers import UserSerializer
from apps.movimientos.models import TipoMovimiento
from apps.users.models import User

# En el archivo serializers.py

class MovimientoReadSerializer(serializers.ModelSerializer):
    persona_movimiento = UserSerializer()  # Muestra la información completa del usuario
    tipo_movimiento = TipoMovimientoSerializer()  # Muestra la información completa del tipo de movimiento

    class Meta:
        model = Movimiento
        fields = ['id', 'tipo_movimiento', 'persona_movimiento', 'fecha_creacion', 'fecha_modificacion']


class MovimientoWriteSerializer(serializers.ModelSerializer):
    persona_movimiento = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    tipo_movimiento = serializers.PrimaryKeyRelatedField(queryset=TipoMovimiento.objects.all())

    class Meta:
        model = Movimiento
        fields = ['id', 'tipo_movimiento', 'persona_movimiento', 'fecha_creacion', 'fecha_modificacion']