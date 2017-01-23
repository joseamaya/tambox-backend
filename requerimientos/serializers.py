from rest_framework import serializers
from models import Requerimiento, DetalleRequerimiento, AprobacionRequerimiento


class RequerimientoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Requerimiento
		fields = '__all__'

class DetalleRequerimientoSerializer(serializers.ModelSerializer):
	class Meta:
		model = DetalleRequerimiento
		fields='__all__'

class AprobacionRequerimientoSerializer(serializers.ModelSerializer):

	class Meta:
		model = AprobacionRequerimiento
		fields='__all__'