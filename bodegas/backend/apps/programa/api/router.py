from rest_framework.routers import DefaultRouter
from apps.programa.api.views import ProgramaViewSet

router_prog = DefaultRouter()
router_prog.register(prefix='programa', basename='programa', viewset=ProgramaViewSet)