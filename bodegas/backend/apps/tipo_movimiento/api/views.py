from rest_framework.viewsets import ModelViewSet
from apps.tipo_movimiento.models import TipoMovimiento
from apps.tipo_movimiento.models import TipoMovimiento
from apps.tipo_movimiento.api.serializers import TipoMovimientoSerializer

class TipoMovimientoModelViewSet(ModelViewSet):
    serializer_class = TipoMovimientoSerializer
    queryset = TipoMovimiento.objects.all()