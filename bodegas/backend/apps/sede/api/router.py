from rest_framework.routers import DefaultRouter
from apps.sede.api.views import SedeViewSet

router_sede = DefaultRouter()
router_sede.register(prefix='sede', basename='sede', viewset=SedeViewSet)