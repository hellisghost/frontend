from rest_framework.routers import DefaultRouter
from apps.tipo_movimiento.api.views import TipoMovimientoModelViewSet

router_tipoMovimiento = DefaultRouter()
router_tipoMovimiento.register(prefix='tipo_movimiento', basename='tipo_movimiento', viewset=TipoMovimientoModelViewSet)