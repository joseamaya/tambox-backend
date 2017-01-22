from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter,OrderingFilter
from serializer import AlmacenSerializer,TipoMovimientoSerializer,PedidoSerializer,\
DetallePedidoSerializer,MovimientoSerializer,DetalleMovimientoSerializer,KardexSerializer,\
ControlProductoAlmacenSerializer
from models import Almacen,TipoMovimiento,Pedido,DetallePedido,Movimiento,\
DetalleMovimiento,Kardex,ControlProductoAlmacen

class AlmacenListAPI(ListCreateAPIView):
	queryset=Almacen.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=AlmacenSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='codigo','descipcion'
	ordering_fields=('codigo')

class AlmacenDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=Almacen.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=AlmacenSerializer
	
class TipoMovimientoListAPI(ListCreateAPIView):
	queryset=TipoMovimiento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=TipoMovimientoSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='codigo','codigo_sunat','descipcion'
	ordering_fields=('codigo')

class TipoMovimientoDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=TipoMovimiento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=TipoMovimientoSerializer

class PedidoListAPI(ListCreateAPIView):
	queryset=Pedido.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=PedidoSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='fecha'
	ordering_fields=('fecha')

class PedidoDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=Pedido.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=PedidoSerializer

class DetallePedidoListAPI(ListCreateAPIView):
	queryset=DetallePedido.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=DetallePedidoSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='nro_detalle','producto','pedido'
	ordering_fields=('nro_detalle')

class DetallePedidoDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=DetallePedido.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=DetallePedidoSerializer

class MovimientoListAPI(ListCreateAPIView):
	queryset=Movimiento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=MovimientoSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='id_movimiento','pedido','serie'
	ordering_fields=('fecha_operacion')

class MovimientoDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=Movimiento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=MovimientoSerializer

class DetalleMovimientoListAPI(ListCreateAPIView):
	queryset=DetalleMovimiento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=DetalleMovimientoSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='nro_detalle','movimiento'
	ordering_fields=('nro_detalle')

class DetalleMovimientoDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=DetalleMovimiento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=DetalleMovimientoSerializer

class KardexListAPI(ListCreateAPIView):
	queryset=Kardex.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=KardexSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='nro_detalle_movimiento','movimiento','producto'
	ordering_fields=('fecha_operacion')

class KardexDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=Kardex.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=KardexSerializer

class ControlProductoAlmacenListAPI(ListCreateAPIView):
	queryset=ControlProductoAlmacen.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=ControlProductoAlmacenSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='producto','almacen'
	ordering_fields=('producto')

class ControlProductoAlmacenDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=ControlProductoAlmacen.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly)
	serializer_class=ControlProductoAlmacenSerializer


