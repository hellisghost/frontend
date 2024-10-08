from rest_framework.viewsets import ModelViewSet
from apps.sitio.api.serializers import SitioSerializer, SitioWriteSerializer
from apps.sitio.models import Sitio

class SitioViewSet(ModelViewSet):
    queryset = Sitio.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return SitioSerializer  # Para GET
        return SitioWriteSerializer  # Para POST, PUT, PATCH
