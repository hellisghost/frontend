from rest_framework import serializers
from apps.sitio.models import Sitio
from apps.tipo_sitio.models import Tipo_sitio
from apps.users.api.serializers import UserSerializer
from apps.tipo_sitio.api.serializers import Tipo_sitioSerializer
from apps.users.models import User

class SitioSerializer(serializers.ModelSerializer):
    persona_encargada = UserSerializer()
    tipo_sitio = Tipo_sitioSerializer()
    class Meta:
        model = Sitio
        fields = ['id','persona_encargada','nombre_sitio','tipo_sitio', 'ubicacion', 'FichaTecnica', 'date_created', 'date_modified']

class SitioWriteSerializer(serializers.ModelSerializer):
    persona_encargada = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    tipo_sitio = serializers.PrimaryKeyRelatedField(queryset=Tipo_sitio.objects.all())

    class Meta:
        model = Sitio
        fields = ['id','persona_encargada','nombre_sitio','tipo_sitio', 'ubicacion', 'FichaTecnica', 'date_created', 'date_modified']

