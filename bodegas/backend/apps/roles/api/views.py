from rest_framework.viewsets import ModelViewSet
from apps.roles.models import Rol
from apps.roles.api.serializer import RolSerializer
from apps.roles.api.permissions import IsAdminOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend


class RolApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly] #Los permisos que se le dan para que muestre si es staff o no
    serializer_class = RolSerializer #Cosas que vamos a mostrar
    queryset = Rol.objects.all() #Me devuelve todos los elementos que tenga el modelo Rol
    #lookup_field = 'slug' #Esto es para si quisiera hacer la busqueda de roles por slug y no por id, el por defecto lo hace por id

    #queryset = Rol.objects.filter(state_rol=True)  # Le pedi que me devuelva solo los roles que tengan el estado en True
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state_rol']


