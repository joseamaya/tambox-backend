from rest_framework import serializers

from compras.models import RepresentanteLegal, Proveedor, Cotizacion, DetalleCotizacion, OrdenCompra, DetalleOrdenCompra, \
	OrdenServicios, DetalleOrdenServicios, ConformidadServicio, DetalleConformidadServicio


class RepresentanteLegalSerializer(serializers.ModelSerializer):
	class Meta:
		model=RepresentanteLegal
		fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Proveedor
		fields='__all__'

class CotizacionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Cotizacion
		fields='__all__'

class DetalleCotizacionSerializer(serializers.ModelSerializer):
	class Meta:
		model=DetalleCotizacion
		fields='__all__'

class OrdenCompraSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrdenCompra
		fields='__all__'

class DetalleOrdenCompraSerializer(serializers.ModelSerializer):
	class Meta:
		model = DetalleOrdenCompra
		fields='__all__'

class OrdenServiciosSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrdenServicios
		fields='__all__'

class DetalleOrdenServiciosSerializer(serializers.ModelSerializer):
	class Meta:
		model = DetalleOrdenServicios
		fields='__all__'

class ConformidadServicioSerializer(serializers.ModelSerializer):
	class Meta:
		model = ConformidadServicio
		fields='__all__'

class DetalleConformidadServicioSerializer(serializers.ModelSerializer):
	class Meta:
		model = DetalleConformidadServicio
		fields='__all__'