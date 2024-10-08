from rest_framework.routers import DefaultRouter
from apps.area.api.views import AreaViewSet

router_area = DefaultRouter()
router_area.register(prefix='area', basename='area', viewset=AreaViewSet)