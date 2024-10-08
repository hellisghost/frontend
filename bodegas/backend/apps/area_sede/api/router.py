from rest_framework.routers import DefaultRouter

from apps.area_sede.api.views import AreaSedeViewSet

router_AreaSede = DefaultRouter()
router_AreaSede.register(prefix='areaSede', basename='areaSede', viewset=AreaSedeViewSet)