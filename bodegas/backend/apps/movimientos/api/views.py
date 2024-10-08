# En el archivo views.py

from rest_framework.viewsets import ModelViewSet
from apps.movimientos.models import Movimiento
from apps.movimientos.api.serializer import MovimientoReadSerializer, MovimientoWriteSerializer
from apps.movimientos.api.permissions import IsAdminOrReadOnly

class MovimientoApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Movimiento.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return MovimientoReadSerializer  # Para GET
        return MovimientoWriteSerializer  # Para POST, PUT, PATCH, etc.
