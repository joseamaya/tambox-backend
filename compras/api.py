from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from compras.models import DetalleConformidadServicio, ConformidadServicio, DetalleOrdenServicios, OrdenServicios, \
	DetalleOrdenCompra, OrdenCompra, Cotizacion, Proveedor, RepresentanteLegal
from compras.serializers import DetalleConformidadServicioSerializer, ConformidadServicioSerializer, \
	DetalleOrdenServiciosSerializer, OrdenServiciosSerializer, DetalleOrdenCompraSerializer, OrdenCompraSerializer, \
	CotizacionSerializer, ProveedorSerializer, RepresentanteLegalSerializer


class RepresentanteLegalViewSet(ModelViewSet):
	queryset = RepresentanteLegal.objects.all()
	permissions_class = (IsAuthenticatedOrReadOnly,)
	serializer_class = RepresentanteLegalSerializer


class ProveedorViewSet(ModelViewSet):
	queryset=Proveedor.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class= ProveedorSerializer

class CotizacionViewSet(ModelViewSet):
	queryset=Cotizacion.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class= CotizacionSerializer

class OrdenCompraViewSet(ModelViewSet):
	queryset=OrdenCompra.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class= OrdenCompraSerializer

class DetalleOrdenCompraViewSet(ModelViewSet):
	queryset=DetalleOrdenCompra.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class= DetalleOrdenCompraSerializer

class OrdenServiciosViewSet(ModelViewSet):
	queryset=OrdenServicios.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class= OrdenServiciosSerializer

class DetalleOrdenServiciosViewSet(ModelViewSet):
	queryset=DetalleOrdenServicios.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class= DetalleOrdenServiciosSerializer


class ConformidadServicioViewSet(ModelViewSet):
	queryset=ConformidadServicio.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class= ConformidadServicioSerializer


class DetalleConformidadServicioViewSet(ModelViewSet):
	queryset=DetalleConformidadServicio.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=DetalleConformidadServicioSerializer
