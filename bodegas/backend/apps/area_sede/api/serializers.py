from rest_framework import serializers
from apps.area_sede.models import AreaSede
from apps.area.models import Area
from apps.users.models import User
from apps.sede.models import Sede
from apps.sede.api.serializers import SedeSerializer
from apps.area.api.serializers import AreaSerializer
from apps.users.api.serializers import UserSerializer


class AreaSedeSerializer(serializers.ModelSerializer):
    sede_area = SedeSerializer()
    area_AreaSede = AreaSerializer()
    persona_administra = UserSerializer()

    class Meta:
        model = AreaSede
        fields = ['id', 'sede_area', 'area_AreaSede', 'persona_administra', 'date_created', 'date_modified']


class AreaSedeWriteSerializer(serializers.ModelSerializer):
    sede_area = serializers.PrimaryKeyRelatedField(queryset=Sede.objects.all())
    area_AreaSede = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    persona_administra = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = AreaSede
        fields = ['id', 'sede_area', 'area_AreaSede', 'persona_administra', 'date_created', 'date_modified']
