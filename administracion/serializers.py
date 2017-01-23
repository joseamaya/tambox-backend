from rest_framework import serializers
from models import Profesion, Trabajador, Oficina, Puesto, NivelAprobacion


class ProfesionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Profesion
		fields = '__all__'

class TrabajadorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trabajador
		fields='__all__'

class OficinaSerializer(serializers.ModelSerializer):
	class Meta:
		model=Oficina
		fields='__all__'

class PuestoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Puesto
		fields='__all__'

class NivelAprobacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = NivelAprobacion
		fields='__all__'