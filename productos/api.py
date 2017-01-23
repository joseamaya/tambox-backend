from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from productos.models import UnidadMedida, GrupoProductos, Producto
from productos.serializers import UnidadMedidaSerializer, GrupoProductosSerializer, ProductoSerializer


class UnidadMedidaViewSet(ModelViewSet):
	queryset=UnidadMedida.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=UnidadMedidaSerializer


class GrupoProductosViewSet(ModelViewSet):
	queryset=GrupoProductos.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=GrupoProductosSerializer


class ProductoViewSet(ModelViewSet):
	queryset=Producto.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=ProductoSerializer
