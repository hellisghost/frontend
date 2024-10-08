from rest_framework import serializers
from apps.ficha.models import Ficha
from apps.programa.api.serializers import ProgramaSerializer
from apps.programa.models import Programa
from apps.users.api.serializers import UserSerializer
from apps.users.models import User

class FichaSerializer(serializers.ModelSerializer):
    persona_ficha = UserSerializer()
    programa = ProgramaSerializer()
    class Meta:
        model = Ficha
        fields = ['id','id_ficha','slug', 'persona_ficha', 'programa', 'date_created', 'date_modified']

class FichaWriteSerializer(serializers.ModelSerializer):
    persona_ficha = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    programa = serializers.PrimaryKeyRelatedField(queryset=Programa.objects.all())

    class Meta:
        model = Ficha
        fields = ['id_ficha','slug', 'persona_ficha', 'programa', 'date_created', 'date_modified']
