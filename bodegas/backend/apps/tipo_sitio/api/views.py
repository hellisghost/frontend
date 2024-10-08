from rest_framework.viewsets import ModelViewSet

from apps.tipo_sitio.api.serializers import Tipo_sitioSerializer
from apps.tipo_sitio.models import Tipo_sitio

class TipoSitioViewSet(ModelViewSet):
    serializer_class = Tipo_sitioSerializer
    queryset = Tipo_sitio.objects.all()