from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from administracion.api import ProfesionViewSet, TrabajadorViewSet, OficinaViewSet, PuestoViewSet, \
    NivelAprobacionViewSet

router = DefaultRouter()
router.register(r'profesiones', ProfesionViewSet)
router.register(r'trabajadores', TrabajadorViewSet)
router.register(r'oficinas', OficinaViewSet)
router.register(r'puestos', PuestoViewSet)
router.register(r'niveles_aprobacion', NivelAprobacionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]