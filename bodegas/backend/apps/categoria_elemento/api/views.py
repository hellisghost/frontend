from rest_framework.viewsets import ModelViewSet
from apps.categoria_elemento.models import CategoriaElementos
from apps.categoria_elemento.api.serializers import CategoriaElementosSerializer

class CategoriaElementosModelViewSet(ModelViewSet):
    serializer_class = CategoriaElementosSerializer
    queryset = CategoriaElementos.objects.all()