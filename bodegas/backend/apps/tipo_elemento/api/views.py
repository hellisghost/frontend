from rest_framework.viewsets import ModelViewSet

from apps.tipo_elemento.api.serializers import TipoElementoSerializer
from apps.tipo_elemento.models import TipoElemento
from apps.tipo_movimiento.api.serializers import TipoMovimientoSerializer

class TipoElementoViewSet(ModelViewSet):
    serializer_class = TipoElementoSerializer
    queryset = TipoElemento.objects.all()