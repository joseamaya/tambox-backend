from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter

from compras.api import RepresentanteLegalViewSet, ProveedorViewSet, CotizacionViewSet, OrdenCompraViewSet, \
    DetalleOrdenCompraViewSet, OrdenServiciosViewSet, DetalleOrdenServiciosViewSet, ConformidadServicioViewSet, \
    DetalleConformidadServicioViewSet

router = DefaultRouter()
router.register(r'representantes', RepresentanteLegalViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'cotizaciones', CotizacionViewSet)
router.register(r'ordenes_compra', OrdenCompraViewSet)
router.register(r'detalles_orden_compra', DetalleOrdenCompraViewSet)
router.register(r'ordenes_servicios', OrdenServiciosViewSet)
router.register(r'detalles_orden_servicios', DetalleOrdenServiciosViewSet)
router.register(r'conformidades_servicio', ConformidadServicioViewSet)
router.register(r'detalles_conformidad_servicio', DetalleConformidadServicioViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]