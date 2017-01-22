from rest_framework import serializers
from models import CuentaContable,FormaPago,TipoDocumento,Tipo,Impuesto,Empresa,Configuracion,TipoExistencia


class CuentaContableSerializers(serializers.ModelSerializer):
	class Meta:
		model=CuentaContable
		fields = '__all__'

class FormaPagoSerializer(serializers.ModelSerializer):
	class Meta:
		model=FormaPago
		fields='__all__'

class TipoDocumentoSerializer(serializers.ModelSerializer):
	class Meta:
		model=TipoDocumento
		fields='__all__'

class TipoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Tipo
		fields='__all__'

class ImpuestoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Impuesto
		fields='__all__'

class EmpresaSerializer(serializers.ModelSerializer):
	class Meta:
		model=Empresa
		fields='__all__'

class ConfiguracionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Configuracion
		fields='__all__'

class TipoExistenciaSerializer(serializers.ModelSerializer):
	class Meta:
		model=TipoExistencia
		fields='__all__'
