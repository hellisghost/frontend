from rest_framework.routers import DefaultRouter
from apps.tipo_elemento.api.views import TipoElementoViewSet

router_tipoElemento = DefaultRouter()
router_tipoElemento.register(prefix='tipo_elemento', basename='tipo_elemento', viewset=TipoElementoViewSet)


