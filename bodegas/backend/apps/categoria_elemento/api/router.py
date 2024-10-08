from rest_framework.routers import DefaultRouter
from apps.categoria_elemento.api.views import CategoriaElementosModelViewSet

router_categoria_elementos = DefaultRouter()
router_categoria_elementos.register(prefix='categoria_elemento', basename='categoria_elemento', viewset=CategoriaElementosModelViewSet)

