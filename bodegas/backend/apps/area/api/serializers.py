from rest_framework import serializers
from apps.area.models import Area


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ['id','nombre_area', 'date_created', 'date_modified']