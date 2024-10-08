from rest_framework.viewsets import ModelViewSet
from apps.programa.models import Programa
from apps.programa.api.serializers import ProgramaSerializer, ProgramaWriteSerializer


class ProgramaViewSet(ModelViewSet):
    #serializer_class = ProgramaSerializer
    queryset = Programa.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProgramaSerializer
        return ProgramaWriteSerializer
