from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from administracion.models import Profesion, Trabajador, Oficina, Puesto, NivelAprobacion
from administracion.serializers import ProfesionSerializer, OficinaSerializer, TrabajadorSerializer, PuestoSerializer, \
	NivelAprobacionSerializer


class ProfesionViewSet(ModelViewSet):
	queryset=Profesion.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=ProfesionSerializer


class TrabajadorViewSet(ModelViewSet):
	queryset=Trabajador.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=TrabajadorSerializer


class OficinaViewSet(ModelViewSet):
	queryset=Oficina.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=OficinaSerializer

class PuestoViewSet(ModelViewSet):
	queryset=Puesto.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=PuestoSerializer



class NivelAprobacionViewSet(ModelViewSet):
	queryset=NivelAprobacion.objects.all()
	permissions_class=(IsAuthenticatedOrReadOnly,)
	serializer_class=NivelAprobacionSerializer
