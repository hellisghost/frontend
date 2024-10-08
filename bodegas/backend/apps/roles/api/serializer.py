from rest_framework import serializers
from apps.roles.models import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id','name_rol','slug', 'description', 'state_rol', 'created_at']
