from rest_framework.routers import DefaultRouter
from apps.ficha.api.views import FichaViewSet


router_ficha = DefaultRouter()
router_ficha.register(prefix='ficha', basename='ficha', viewset=FichaViewSet)