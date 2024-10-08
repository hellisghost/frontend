from rest_framework.viewsets import ModelViewSet
from apps.municipios.models import Municipio
from apps.municipios.api.serializers import MunicipioSerializer

class MunicipioViewSet(ModelViewSet):
    serializer_class = MunicipioSerializer
    queryset = Municipio.objects.all()