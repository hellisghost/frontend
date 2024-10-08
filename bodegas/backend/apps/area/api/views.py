from rest_framework.viewsets import ModelViewSet

from apps.area.api.serializers import AreaSerializer
from apps.area.models import Area

class AreaViewSet(ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()