from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter

from requerimientos.api import RequerimientoViewSet, DetalleRequerimientoViewSet, AprobacionRequerimientoViewSet

router = DefaultRouter()
router.register(r'requerimientos', RequerimientoViewSet)
router.register(r'detalles_requerimiento', DetalleRequerimientoViewSet)
router.register(r'aprobaciones_requerimientos', AprobacionRequerimientoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
