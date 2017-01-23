from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from productos.models import UnidadMedida, GrupoProductos, Producto
from productos.serializers import UnidadMedidaSerializer, GrupoProductosSerializer, ProductoSerializer
from requerimientos.models import Requerimiento, DetalleRequerimiento, AprobacionRequerimiento
from requerimientos.serializers import RequerimientoSerializer, DetalleRequerimientoSerializer


class RequerimientoViewSet(ModelViewSet):
	queryset=Requerimiento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=RequerimientoSerializer


class DetalleRequerimientoViewSet(ModelViewSet):
	queryset=DetalleRequerimiento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class= DetalleRequerimientoSerializer


class AprobacionRequerimientoViewSet(ModelViewSet):
	queryset=AprobacionRequerimiento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=AprobacionRequerimiento
