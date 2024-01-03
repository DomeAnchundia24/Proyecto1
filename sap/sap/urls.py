"""
URL configuration for sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers


from policia.views import agregar_policia, ver_policia, eliminar_policia, modificar_policia, descargar_registro, \
    PoliciaViewSet, RangoViewSet, EspecialidadViewSet
from webapp.views import bienvenida2, bienvenida

router = routers.DefaultRouter()
router.register(r'api_policia', PoliciaViewSet)
router.register(r'api_rango', RangoViewSet)
router.register(r'api_especialidad', EspecialidadViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api',include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('',bienvenida2, name='inicio'),
    path('agregar_policia/', agregar_policia),
    path('ver_policia/<int:id>', ver_policia),
    path('eliminar_policia/<int:id>',eliminar_policia),
    path('modificar_policia/<int:id>',modificar_policia),
    path('descargar_registro/', descargar_registro),
]
urlpatterns += router.urls
