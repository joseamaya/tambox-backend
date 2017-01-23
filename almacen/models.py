# -*- coding: utf-8 -*- 
from django.db import models
from django.db.models import Max
from simple_history.models import HistoricalRecords

from compras.models import OrdenCompra, DetalleOrdenCompra
from contabilidad.models import TipoDocumento
from django.utils.encoding import smart_str, python_2_unicode_compatible
from administracion.models import Oficina, Trabajador
from model_utils.models import TimeStampedModel
from model_utils import Choices
from django.utils.translation import gettext as _
from requerimientos.models import DetalleRequerimiento
from productos.models import Producto
from almacen.managers import DetalleMovimientoManager
from django.db.models import Sum

@python_2_unicode_compatible
class Almacen(TimeStampedModel):
    codigo = models.CharField(unique=True,max_length=5)
    descripcion = models.CharField(max_length=30)
    estado = models.BooleanField(default=True)
    history = HistoricalRecords()
    
    class Meta:
        permissions = (('ver_bienvenida', 'Puede ver bienvenida a la aplicación'),
                       ('cargar_almacenes', 'Puede cargar Almacenes desde un archivo externo'),
                       ('ver_detalle_almacen', 'Puede ver detalle Almacén'),
                       ('ver_tabla_almacenes', 'Puede ver tabla de almacenes'),
                       ('ver_reporte_almacenes_excel', 'Puede ver Reporte Almacenes en excel'),)
        ordering = ['codigo']
        
    def anterior(self):
        try:
            ant = Almacen.objects.filter(pk__lt=self.pk).order_by('-pk')[0]
        except:
            ant = Almacen.objects.all().order_by('pk').last()    
        return ant.pk
    
    def siguiente(self):
        try:
            sig = Almacen.objects.filter(pk__gt=self.pk).order_by('pk')[0]            
        except:
            sig = Almacen.objects.all().order_by('pk').first()            
        return sig.pk

    def __str__(self):
        return self.descripcion

#Vislumbrar la posibilidad de agregar un campo que diga modifica precio
class TipoMovimiento(TimeStampedModel):
    codigo = models.CharField(unique=True,max_length=10)
    codigo_sunat = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=25)
    incrementa = models.BooleanField()
    pide_referencia = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)
    history = HistoricalRecords()
    
    def anterior(self):
        try:
            ant = TipoMovimiento.objects.filter(pk__lt=self.pk).order_by('-pk')[0]
        except:
            ant = TipoMovimiento.objects.all().order_by('pk').last()    
        return ant.pk
    
    def siguiente(self):
        try:
            sig = TipoMovimiento.objects.filter(pk__gt=self.pk).order_by('pk')[0]            
        except:
            sig = TipoMovimiento.objects.all().order_by('pk').first()            
        return sig.pk
    
    class Meta:
        permissions = (('ver_detalle_tipo_movimiento', 'Puede ver detalle Tipo de Movimiento'),
                       ('ver_tabla_tipos_movimientos', 'Puede ver tabla de Tipos de Movimientos'),
                       ('ver_reporte_tipos_movimientos_excel', 'Puede ver Reporte Tipos de Movimientos en excel'),)
        ordering = ['codigo']
    
    def save(self, *args, **kwargs):
        if self.codigo == '':
            tipo_mov_ant = TipoMovimiento.objects.filter(incrementa=self.incrementa).aggregate(Max('codigo'))
            cod_ant=tipo_mov_ant['codigo__max']
            
            if self.incrementa:
                if cod_ant is None:
                    self.codigo='I00'
                else:
                    aux=int(cod_ant[2:3])+1                
                    self.codigo='I'+str(aux).zfill(2)                
            else:
                if cod_ant is None:
                    self.codigo='S01'
                else:
                    aux=int(cod_ant[2:3])+1
                    self.codigo='S'+str(aux).zfill(2)            
        super(TipoMovimiento, self).save()
    
    def __str__(self):
        return smart_str(self.descripcion)

class Pedido(TimeStampedModel):
    codigo = models.CharField(primary_key=True,max_length=12)
    solicitante = models.ForeignKey(Trabajador)
    oficina = models.ForeignKey(Oficina)
    fecha = models.DateField()
    observaciones = models.TextField(blank = True)
    STATUS = Choices(('PEND', _('PENDIENTE')),
                     ('APROB', _('APROBADO')),
                     ('DESAP', _('DESAPROBADO')),
                     ('ATEN', _('ATENDIDO')),
                     ('ATEN_PARC', _('ATENDIDO PARCIALMENTE')),
                     ('CANC', _('CANCELADO')),
                     )
    estado = models.CharField(choices=STATUS, default=STATUS.PEND, max_length=20)
    history = HistoricalRecords()
    
    def anterior(self):
        try:
            ant = Pedido.objects.filter(pk__lt=self.pk).order_by('-pk')[0]
        except:
            ant = Pedido.objects.all().order_by('pk').last()    
        return ant.pk
    
    def siguiente(self):
        try:
            sig = Pedido.objects.filter(pk__gt=self.pk).order_by('pk')[0]            
        except:
            sig = Pedido.objects.all().order_by('pk').first()            
        return sig.pk
    
    class Meta:
        permissions = (('aprobar_pedido', 'Puede aprobar Pedido'),
                       ('ver_detalle_pedido', 'Puede ver detalle de Pedido'),
                       ('ver_tabla_aprobacion_pedidos', 'Puede ver tabla de Aprobación de Pedidos'),
                       ('ver_tabla_pedidos', 'Puede ver tabla de Pedidos'),
                       ('ver_reporte_pedidos_excel', 'Puede ver Reporte de Pedidos en excel'),)                       

    def __str__(self):
        return self.codigo
    
    def save(self, *args, **kwargs):
        if self.codigo == '':
            anio = self.fecha.year
            mov_ant = Pedido.objects.filter(fecha__year=anio).aggregate(Max('codigo'))
            id_ant=mov_ant['codigo__max']        
            if id_ant is None:
                aux = 1            
            else:
                aux=int(id_ant[-6:])+1
            correlativo = str(aux).zfill(6)
            codigo = 'PE'+str(anio)+correlativo
            self.codigo = codigo            
            super(Pedido, self).save()            
        else:            
            super(Pedido, self).save()
            
class DetallePedido(TimeStampedModel):
    nro_detalle = models.IntegerField()
    pedido = models.ForeignKey(Pedido)
    producto = models.ForeignKey(Producto, null=True)
    cantidad = models.DecimalField(max_digits=15, decimal_places=5)
    cantidad_atendida = models.DecimalField(max_digits=15, decimal_places=5,default=0)
    STATUS = Choices(('PEND', _('PENDIENTE')),
                     ('APROB', _('APROBADO')),
                     ('DESAP', _('DESAPROBADO')),
                     ('ATEN', _('ATENDIDO')),
                     ('ATEN_PARC', _('ATENDIDO PARCIALMENTE')),
                     ('CANC', _('CANCELADO')),
                     )
    estado = models.CharField(choices=STATUS, default=STATUS.PEND, max_length=20)
    history = HistoricalRecords()
    
    def cantidad_por_atender(self):
        resultado = self.cantidad - self.cantidad_atendida
        return resultado
    
    class Meta:
        permissions = (('can_view', 'Can view Detalle Pedido'),)
        ordering = ['nro_detalle']
        
    def __str__(self):
        return self.pedido.codigo+ ' ' + str(self.nro_detalle)

class Movimiento(TimeStampedModel):
    id_movimiento = models.CharField(primary_key=True,max_length=16)
    tipo_movimiento = models.ForeignKey(TipoMovimiento)
    referencia = models.ForeignKey(OrdenCompra,null=True)
    pedido = models.ForeignKey(Pedido, null=True)
    tipo_documento = models.ForeignKey(TipoDocumento,null=True)
    serie = models.CharField(max_length=15, null=True)
    numero = models.CharField(max_length=10, null=True)
    fecha_operacion = models.DateTimeField()
    almacen = models.ForeignKey(Almacen)
    oficina = models.ForeignKey(Oficina,null=True)
    observaciones = models.TextField(default='')
    STATUS = Choices(('ACT', _('ACTIVO')),
                     ('CANC', _('CANCELADA')),
                     )
    estado = models.CharField(choices=STATUS, default=STATUS.ACT, max_length=20)
    history = HistoricalRecords()
    
    def anterior(self):
        try:
            sig = Movimiento.objects.filter(pk__lt=self.pk).order_by('-pk')[0]
        except:
            sig = Movimiento.objects.all().last()            
        return sig.pk
    
    def siguiente(self):
        try:
            ant = Movimiento.objects.filter(pk__gt=self.pk).order_by('pk')[0]            
        except:
            ant = Movimiento.objects.all().first()            
        return ant.pk
    
    def modificar_estado_referencia(self):
        movimiento = self
        referencia = movimiento.referencia
        referencia.estado = OrdenCompra.STATUS.PEND
        referencia.save()
        
    def eliminar_referencia(self):       
        movimiento = self
        self.modificar_estado_referencia()
        detalles = DetalleMovimiento.objects.filter(movimiento=movimiento)
        for detalle in detalles:
            detalle_orden_compra = detalle.detalle_orden_compra
            detalle_requerimiento = detalle_orden_compra.detalle_cotizacion.detalle_requerimiento
            detalle_orden_compra.cantidad_ingresada = detalle_orden_compra.cantidad_ingresada - detalle.cantidad
            detalle_requerimiento.cantidad_atendida = detalle_requerimiento.cantidad_atendida - detalle.cantidad
            if detalle_orden_compra.cantidad_ingresada==0: 
                detalle_orden_compra.estado = DetalleOrdenCompra.STATUS.PEND
            if detalle_requerimiento.cantidad_atendida==0: 
                detalle_requerimiento.estado = DetalleRequerimiento.STATUS.PEND 
            detalle_orden_compra.save()        
        
    def eliminar_detalles(self):
        DetalleMovimiento.objects.filter(movimiento=self).delete()
            
    def eliminar_kardex(self):
        movimiento = self
        almacen = movimiento.almacen
        detalle_kardex = Kardex.objects.filter(movimiento__id_movimiento = movimiento.id_movimiento,almacen = almacen)
        for kardex in detalle_kardex:
            control = ControlProductoAlmacen.objects.get(producto=kardex.producto, almacen=almacen)
            control.stock = control.stock - kardex.cantidad_ingreso                                 
            control.save()
            kardex.delete() 
            
    @property            
    def total(self):
        total = 0
        for detalle in DetalleMovimiento.objects.filter(movimiento = self):
            total = total + detalle.valor
        return total
    
    class Meta:
        permissions = (('ver_detalle_movimiento', 'Puede ver detalle de Movimiento'),
                       ('ver_tabla_movimientos', 'Puede ver tabla de Movimientos'),
                       ('ver_reporte_movimientos_excel', 'Puede ver Reporte de Movimientos en excel'),)
        ordering = ['id_movimiento']

    def __str__(self):
        return self.id_movimiento
    
    def save(self, *args, **kwargs):
        if self.id_movimiento == '':
            tipo = self.tipo_movimiento
            anio = self.fecha_operacion.year
            mov_ant = Movimiento.objects.filter(tipo_movimiento__incrementa=tipo.incrementa,fecha_operacion__year=anio).aggregate(Max('id_movimiento'))
            id_ant = mov_ant['id_movimiento__max']        
            if id_ant is None:
                aux = 1            
            else:
                aux=int(id_ant[-7:])+1
            correlativo = str(aux).zfill(7)
            codigo = str(tipo.codigo[0:1])+str(anio)+correlativo
            self.id_movimiento = codigo
            self.anio=self.fecha_operacion.year,
            self.mes = self.fecha_operacion.month,
        super(Movimiento, self).save()

class DetalleMovimiento(TimeStampedModel):
    objects = DetalleMovimientoManager()
    nro_detalle = models.IntegerField()
    movimiento = models.ForeignKey(Movimiento)
    detalle_orden_compra = models.ForeignKey(DetalleOrdenCompra, null=True)
    detalle_pedido = models.ForeignKey(DetallePedido, null=True)
    producto = models.ForeignKey(Producto)
    cantidad = models.DecimalField(max_digits=15, decimal_places=5)
    precio = models.DecimalField(max_digits=15, decimal_places=5)
    history = HistoricalRecords()
    
    @property
    def valor(self):
        return self.precio * self.cantidad 
    
    def save(self, *args, **kwargs):
        movi = self.movimiento
        t_movimiento = movi.tipo_movimiento        
        kardex = Kardex()            
        kardex.producto = self.producto
        kardex.fecha_operacion = movi.fecha_operacion
        kardex.movimiento = movi
        kardex.nro_detalle_movimiento = self.nro_detalle
        kardex.almacen = movi.almacen
        if t_movimiento.incrementa:            
            kardex.cantidad_ingreso = self.cantidad
            kardex.precio_ingreso = self.precio
            kardex.valor_ingreso = self.valor
            kardex.cantidad_salida = 0
            kardex.precio_salida =  0
            kardex.valor_salida = 0
            try:                
                kardex_ant = Kardex.objects.filter(producto=self.producto,almacen=self.movimiento.almacen,fecha_operacion__lt=kardex.fecha_operacion).latest('fecha_operacion')  
                kardex.cantidad_total = self.cantidad + kardex_ant.cantidad_total
                kardex.valor_total = self.valor + kardex_ant.valor_total
                kardex.precio_total = self.precio
            except Kardex.DoesNotExist:                               
                kardex.cantidad_total = self.cantidad
                kardex.precio_total = self.precio
                kardex.valor_total = self.valor            
        else:
            kardex.cantidad_ingreso = 0
            kardex.precio_ingreso = 0
            kardex.valor_ingreso = 0
            kardex.cantidad_salida = self.cantidad
            kardex.precio_salida =  self.precio
            kardex.valor_salida = self.valor            
            try:                
                kardex_ant = Kardex.objects.filter(producto=self.producto,almacen=self.movimiento.almacen,fecha_operacion__lt=kardex.fecha_operacion).latest('fecha_operacion')            
                kardex.cantidad_total = kardex_ant.cantidad_total - self.cantidad
                kardex.valor_total = kardex_ant.valor_total-self.valor
                kardex.precio_total = self.precio
            except Kardex.DoesNotExist:                               
                kardex.cantidad_total = 0-self.cantidad
                kardex.precio_total = 0-self.precio
                kardex.valor_total = 0-self.valor                
        if kardex.cantidad_total==0:
            precio_control = 0
        else:
            precio_control = kardex.valor_total / kardex.cantidad_total        
        
        control_producto, creado = ControlProductoAlmacen.objects.update_or_create(
            almacen=self.movimiento.almacen, 
            producto=self.producto, 
            defaults={'stock': kardex.cantidad_total,'precio':precio_control}
        )
        super(DetalleMovimiento, self).save()
        kardex.save()        

    class Meta:
        unique_together = (('nro_detalle', 'movimiento'),)

class Kardex(TimeStampedModel):    
    movimiento = models.ForeignKey(Movimiento)
    nro_detalle_movimiento = models.IntegerField()
    producto = models.ForeignKey(Producto)
    fecha_operacion = models.DateTimeField()
    cantidad_ingreso = models.DecimalField(max_digits=15, decimal_places=5)
    precio_ingreso = models.DecimalField(max_digits=15, decimal_places=5)
    valor_ingreso = models.DecimalField(max_digits=15, decimal_places=5)
    cantidad_salida = models.DecimalField(max_digits=15, decimal_places=5)
    precio_salida = models.DecimalField(max_digits=15, decimal_places=5)
    valor_salida = models.DecimalField(max_digits=15, decimal_places=5)
    cantidad_total = models.DecimalField(max_digits=15, decimal_places=5)
    precio_total = models.DecimalField(max_digits=15, decimal_places=5)
    valor_total = models.DecimalField(max_digits=15, decimal_places=5)
    almacen = models.ForeignKey(Almacen)
    history = HistoricalRecords()
    
    def __str__(self):
        return str(self.movimiento.id_movimiento) +'-'+ str(self.nro_detalle_movimiento) +'-' + self.producto.descripcion
    
    class Meta:
        permissions = (('ver_detalle_kardex', 'Puede ver detalle de Kardex'),
                       ('ver_tabla_kardex', 'Puede ver tabla de Kardex'),
                       ('ver_reporte_kardex_excel', 'Puede ver Reporte de Kardex en excel'),)
        ordering = ['movimiento','nro_detalle_movimiento']
    
class ControlProductoAlmacen(TimeStampedModel):
    producto = models.ForeignKey(Producto)
    almacen = models.ForeignKey(Almacen)
    stock = models.DecimalField(max_digits=15, decimal_places=5,default=0)
    precio = models.DecimalField(max_digits=15, decimal_places=5,default=0)
    history = HistoricalRecords()
    
    class Meta:
        unique_together = (('producto', 'almacen'),)
        permissions = (('ver_reporte_stock_excel', 'Puede ver Reporte de Stock'),) 
        
    def save(self, *args, **kwargs):
        super(ControlProductoAlmacen, self).save()
        producto = self.producto
        lista_productos_control = ControlProductoAlmacen.objects.filter(producto = producto).aggregate(stock=Sum('stock'))
        producto.stock = lista_productos_control['stock']
        producto.save()