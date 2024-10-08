from rest_framework.viewsets import ModelViewSet
from apps.area_sede.models import AreaSede
from apps.area_sede.api.serializers import AreaSedeSerializer, AreaSedeWriteSerializer


class AreaSedeViewSet(ModelViewSet):
    serializer_class = AreaSedeSerializer
    queryset = AreaSede.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return AreaSedeSerializer
        return AreaSedeWriteSerializer