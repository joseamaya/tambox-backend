from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from productos.api import UnidadMedidaViewSet, GrupoProductosViewSet, ProductoViewSet

router = DefaultRouter()
router.register(r'unidades_medida', UnidadMedidaViewSet)
router.register(r'grupos_productos', GrupoProductosViewSet)
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]