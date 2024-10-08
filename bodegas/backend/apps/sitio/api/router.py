from rest_framework.routers import DefaultRouter
from apps.sitio.api.views import SitioViewSet

router_sitio = DefaultRouter()
router_sitio.register(prefix='sitio', basename='sitio', viewset=SitioViewSet)