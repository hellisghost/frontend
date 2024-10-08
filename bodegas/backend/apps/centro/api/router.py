from rest_framework.routers import DefaultRouter

from apps.centro.api.views import CentroViewSet

router_centro = DefaultRouter()
router_centro.register(prefix='centro', basename='centro', viewset=CentroViewSet)