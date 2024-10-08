from rest_framework.routers import DefaultRouter
from apps.municipios.api.views import MunicipioViewSet

router_municipio = DefaultRouter()
router_municipio.register(prefix='municipios',basename='municipio',viewset=MunicipioViewSet)