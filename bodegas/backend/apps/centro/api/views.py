from rest_framework.viewsets import ModelViewSet
from apps.centro.models import Centro
from apps.centro.api.serializers import CentroSerializer

class CentroViewSet(ModelViewSet):
    serializer_class = CentroSerializer
    queryset = Centro.objects.all()
