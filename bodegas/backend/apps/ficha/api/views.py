from rest_framework.viewsets import ModelViewSet
from apps.ficha.models import Ficha
from apps.ficha.api.serializers import FichaSerializer, FichaWriteSerializer
class FichaViewSet(ModelViewSet):
    #serializer_class = FichaSerializer
    queryset = Ficha.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return FichaSerializer
        return FichaWriteSerializer

