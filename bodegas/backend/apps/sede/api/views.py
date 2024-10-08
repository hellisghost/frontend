from rest_framework import viewsets
from apps.sede.models import Sede
from apps.sede.api.serializers import SedeSerializer

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
