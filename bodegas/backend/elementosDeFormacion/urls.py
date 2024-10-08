"""
URL configuration for elementosDeFormacion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from apps.roles.api.router import router_rol
from apps.movimientos.api.router import router_movimiento
from apps.sitio.api.router import router_sitio
from apps.tipo_movimiento.api.router import router_tipoMovimiento
from apps.categoria_elemento.api.router import router_categoria_elementos
from apps.tipo_elemento.api.router import router_tipoElemento
from apps.elemento_material.api.router import router_elementoMaterial
from apps.tipo_sitio.api.router import router_tipoSitio
from apps.programa.api.router import router_prog
from apps.ficha.api.router import router_ficha
from apps.municipios.api.router import router_municipio
from apps.centro.api.router import router_centro
from apps.sede.api.router import router_sede
from apps.area.api.router import router_area
from apps.area_sede.api.router import router_AreaSede

schema_view = get_schema_view(
   openapi.Info(
      title="Sistema de inventario para materiales de formacion API V1.0.0",
      default_version='v1',
      description="Test description",
      terms_of_service="",
      contact=openapi.Contact(email="diegokld23@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.api.router')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(router_rol.urls)),
    path('api/', include(router_movimiento.urls)),
    path('api/', include(router_tipoMovimiento.urls)),
    path('api/', include(router_categoria_elementos.urls)),
    path('api/', include(router_tipoElemento.urls)),
    path('api/', include(router_elementoMaterial.urls)),
    path('api/',include(router_tipoSitio.urls)),
    path('api/', include(router_sitio.urls)),
    path('api/', include(router_prog.urls)),
    path('api/', include(router_ficha.urls)),
    path('api/', include(router_municipio.urls)),
    path('api/', include(router_centro.urls)),
    path('api/', include(router_sede.urls)),
    path('api/', include(router_area.urls)),
    path('api/', include(router_AreaSede.urls)),

]

