from models import CuentaContable,FormaPago,TipoDocumento,Tipo,Impuesto,Empresa,Configuracion,TipoExistencia
from serializers import CuentaContableSerializers,FormaPagoSerializer,TipoDocumentoSerializer,TipoSerializer,ImpuestoSerializer,\
 EmpresaSerializer,ConfiguracionSerializer,TipoExistenciaSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter,OrderingFilter

class CuentaContableListAPI(ListCreateAPIView):
	queryset=CuentaContable.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=CuentaContableSerializers
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='cuenta','descripcion'
	ordering_fields=('cuenta')
	
class CuentaContableDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=CuentaContable.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=CuentaContableSerializers


class FormaPagoListAPI(ListCreateAPIView):
	queryset=FormaPago.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=FormaPagoSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='codigo'
	ordering_fields=('name')

class FormaPagoDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=FormaPago.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=FormaPagoSerializer



class TipoDocumentoListAPI(ListCreateAPIView):
	queryset=TipoDocumento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=TipoDocumentoSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='codigo_sunat','nombre'
	ordering_fields=('nombre')

class TipoDocumentoDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=TipoDocumento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=TipoDocumentoSerializer	



class TipoListAPI(ListCreateAPIView):
	queryset=Tipo.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=TipoSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='codigo'
	ordering_fields=('codigo')

class TipoDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=Tipo.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=TipoSerializer	

class ImpuestoListAPI(ListCreateAPIView):
	queryset=Impuesto.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=ImpuestoSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='abreviatura','descipcion'
	ordering_fields=('abreviatura')

class ImpuestoDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=Impuesto.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=ImpuestoSerializer	

class EmpresaListAPI(ListCreateAPIView):
	queryset=Empresa.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=EmpresaSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='razon_social','ruc'
	ordering_fields=('razon_social')

class EmpresaDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=Empresa.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=EmpresaSerializer	

class ConfiguracionListAPI(ListCreateAPIView):
	queryset=Configuracion.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=ConfiguracionSerializer
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='impuesto_compra'
	ordering_fields=('impuesto_compra')

class ConfiguracionDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=Configuracion.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=ConfiguracionSerializer

class TipoExistenciaListAPI(ListCreateAPIView):
	queryset=TipoExistencia.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=TipoExistenciaSerializer	
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='codigo_sunat','descipcion'
	ordering_fields=('codigo_sunat')		

class TipoExistenciaDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=TipoExistencia.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=TipoExistenciaSerializer
