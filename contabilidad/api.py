from models import CuentaContable,FormaPago,TipoDocumento,Tipo,Impuesto,Empresa,Configuracion,TipoExistencia
from serializers import ContaSerializers,ForPagoSerializer,TiDocuSerializer,TipoSerializer,ImpuestoSerializer,\
 EmpresaSerializer,ConfiSerializer,TipExiSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter,OrderingFilter

class CuentaListAPI(ListCreateAPIView):
	queryset=CuentaContable.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=ContaSerializers
	filter_backends=(SearchFilter,OrderingFilter)
	search_fields='cuenta','descripcion'
	ordering_fields=('cuenta')
	
class CuentaDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=CuentaContable.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=ContaSerializers


class ForPagoListAPI(ListCreateAPIView):
	queryset=FormaPago.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=ForPagoSerializer

	search_fields='codigo'
	ordering_fields=('name')

class ForPagoDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=FormaPago.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=ForPagoSerializer



class TiDocuListAPI(ListCreateAPIView):
	queryset=TipoDocumento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=TiDocuSerializer

	search_fields='codigo_sunat','nombre'
	ordering_fields=('nombre')

class TiDocuDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=TipoDocumento.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=TiDocuSerializer	



class TipoListAPI(ListCreateAPIView):
	queryset=Tipo.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=TipoSerializer

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

	search_fields='razon_social','ruc'
	ordering_fields=('razon_social')

class EmpresaDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=Empresa.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=EmpresaSerializer	

class ConfiListAPI(ListCreateAPIView):
	queryset=Configuracion.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=ConfiSerializer

	search_fields='impuesto_compra'
	ordering_fields=('impuesto_compra')

class ConfiDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=Configuracion.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=ConfiSerializer

class TipExiListAPI(ListCreateAPIView):
	queryset=TipoExistencia.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=TipExiSerializer	

	search_fields='codigo_sunat','descipcion'
	ordering_fields=('codigo_sunat')		

class TipExiDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset=TipoExistencia.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=TipExiSerializer
