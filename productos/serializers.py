from rest_framework import serializers
from models import Producto, GrupoProductos, UnidadMedida


class UnidadMedidaSerializer(serializers.ModelSerializer):
	class Meta:
		model=UnidadMedida
		fields = '__all__'

class GrupoProductosSerializer(serializers.ModelSerializer):
	class Meta:
		model = GrupoProductos
		fields='__all__'

class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Producto
		fields='__all__'