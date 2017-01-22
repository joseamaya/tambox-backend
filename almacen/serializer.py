from rest_framework import serializers
from models import Almacen,TipoMovimiento,Pedido,DetallePedido,Movimiento,\
DetalleMovimiento,Kardex,ControlProductoAlmacen


class AlmacenSerializer(serializers.ModelSerializer):
	class Meta:
		model= Almacen
		fields='__all__'


class TipoMovimientoSerializer(serializers.ModelSerializer):
	class Meta:
		model=TipoMovimiento
		fields='__all__'

class PedidoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Pedido
		fields='__all__'

class DetallePedidoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DetallePedido
		fields='__all__'

class MovimientoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Movimiento
		fields='__all__'

class DetalleMovimientoSerializer(serializers.ModelSerializer):
	class Meta:
		model=DetalleMovimiento
		fields='__all__'

class KardexSerializer(serializers.ModelSerializer):
	class Meta:
		model=Kardex
		fields='__all__'

class ControlProductoAlmacenSerializer(serializers.ModelSerializer):
	class Meta:
		model=ControlProductoAlmacen
		fields='__all__'
