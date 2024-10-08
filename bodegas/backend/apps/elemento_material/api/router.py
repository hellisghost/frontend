from rest_framework.routers import DefaultRouter
from apps.elemento_material.api.views import  ElementoMaterialViewSet

router_elementoMaterial = DefaultRouter()

router_elementoMaterial.register(prefix='elemento_material', basename='elemento_material', viewset=ElementoMaterialViewSet)