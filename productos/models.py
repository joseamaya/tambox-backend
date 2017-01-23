# -*- coding: utf-8 -*- 
from django.db import models
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords

from contabilidad.models import CuentaContable, TipoExistencia
from django.db.models import Max
from django.utils.encoding import smart_str
from productos.querysets import NavegableQuerySet


class UnidadMedida(TimeStampedModel):
    codigo = models.CharField(max_length=5, unique=True)
    descripcion = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    history = HistoricalRecords()
    objects = NavegableQuerySet.as_manager()

    class Meta:
        permissions = (('ver_detalle_unidad_medida', 'Puede ver detalle Unidad de Medida'),
                       ('ver_tabla_unidades_medida', 'Puede ver tabla de unidades de medida'),
                       ('ver_reporte_unidades_medida_excel', 'Puede ver Reporte Unidades de Medida en excel'),)
        ordering = ['codigo']

    def anterior(self):
        ant = UnidadMedida.objects.anterior(self)
        return ant.pk

    def siguiente(self):
        sig = UnidadMedida.objects.siguiente(self)
        return sig.pk

    def __str__(self):
        return self.descripcion


class GrupoProductos(TimeStampedModel):
    codigo = models.CharField(primary_key=True, max_length=6)
    descripcion = models.CharField(max_length=100)
    ctacontable = models.ForeignKey(CuentaContable)
    son_productos = models.BooleanField(default=True)
    estado = models.BooleanField(default=True)
    history = HistoricalRecords()
    objects = NavegableQuerySet.as_manager()

    class Meta:
        permissions = (('cargar_grupo_productos', 'Puede cargar Grupos de Productos desde un archivo externo'),
                       ('ver_detalle_grupo_productos', 'Puede ver detalle Grupo de Productos'),
                       ('ver_tabla_grupos_productos', 'Puede ver tabla Grupos de Productos'),
                       ('ver_reporte_grupo_productos_excel', 'Puede ver Reporte de grupo de productos en excel'),)

    def save(self, *args, **kwargs):
        if self.codigo == '':
            grupo_ant = GrupoProductos.objects.all().aggregate(Max('codigo'))
            cod_ant = grupo_ant['codigo__max']
            if cod_ant is None:
                aux = 1
            else:
                aux = int(cod_ant) + 1
            self.codigo = str(aux).zfill(6)
        super(GrupoProductos, self).save()

    def anterior(self):
        ant = GrupoProductos.objects.anterior(self)
        return ant.pk

    def siguiente(self):
        sig = GrupoProductos.objects.siguiente(self)
        return sig.pk

    def __str__(self):
        return self.descripcion


class Producto(TimeStampedModel):
    codigo = models.CharField(primary_key=True, max_length=10)
    grupo_productos = models.ForeignKey(GrupoProductos)
    descripcion = models.CharField(max_length=100, unique=True)
    desc_abreviada = models.CharField(max_length=40, blank=True)
    es_servicio = models.BooleanField(default=False)
    unidad_medida = models.ForeignKey(UnidadMedida, null=True)
    marca = models.CharField(max_length=40, blank=True)
    modelo = models.CharField(max_length=40, blank=True)
    precio = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    stock = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    stock_minimo = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    imagen = models.ImageField(upload_to='productos', default='productos/sinimagen.png')
    tipo_existencia = models.ForeignKey(TipoExistencia, null=True)
    estado = models.BooleanField(default=True)
    history = HistoricalRecords()
    objects = NavegableQuerySet.as_manager()

    class Meta:
        permissions = (('ver_bienvenida', 'Puede ver bienvenida a la aplicación'),
                       ('cargar_productos', 'Puede cargar Productos desde un archivo externo'),
                       ('ver_detalle_producto', 'Puede ver detalle de Productos'),
                       ('ver_tabla_productos', 'Puede ver tabla Productos'),
                       ('ver_reporte_productos_excel', 'Puede ver Reporte de Productos en excel'),
                       ('puede_hacer_busqueda_producto', 'Puede hacer busqueda Producto'),)

    def anterior(self):
        ant = Producto.objects.anterior(self)
        return ant.pk

    def siguiente(self):
        sig = Producto.objects.siguiente(self)
        return sig.pk

    def save(self, *args, **kwargs):
        if self.codigo == '':
            prod_ant = Producto.objects.filter(grupo_productos=self.grupo_productos).aggregate(Max('codigo'))
            cod_ant = prod_ant['codigo__max']
            if cod_ant is None:
                self.codigo = self.grupo_productos.codigo + '0001'
            else:
                aux = int(cod_ant) + 1
                self.codigo = str(aux).zfill(10)
            if self.es_servicio:
                unidad_medida, creado = UnidadMedida.objects.get_or_create(codigo='SERV',
                                                                           defaults={'descripcion': 'SERVICIO'})
                self.unidad_medida = unidad_medida
        super(Producto, self).save()

    def __str__(self):
        return smart_str(self.descripcion)
