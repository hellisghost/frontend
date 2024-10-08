from rest_framework.viewsets import ModelViewSet
from apps.elemento_material.api.serializers import ElementoMaterialSerializer, ElementoWriteMaterial
from apps.elemento_material.models import ElementoMaterial

class ElementoMaterialViewSet(ModelViewSet):
    #serializer_class = ElementoMaterialSerializer
    queryset = ElementoMaterial.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ElementoMaterialSerializer
        return ElementoWriteMaterial