from django.conf.urls import url
from api import AlmacenListAPI,AlmacenDetailAPI,TipoMovimientoListAPI,TipoMovimientoDetailAPI,PedidoListAPI,PedidoDetailAPI,\
DetallePedidoListAPI,DetallePedidoDetailAPI,MovimientoListAPI,MovimientoDetailAPI,DetalleMovimientoListAPI,DetalleMovimientoDetailAPI,KardexListAPI,KardexDetailAPI,\
ControlProductoAlmacenListAPI,ControlProductoAlmacenDetailAPI
from django.contrib.auth.decorators import login_required

urlpatterns = [
# Rest List-Create
    url(r'^almacen/$',AlmacenListAPI.as_view(),name='almacen_list_api'),
    url(r'^tipo_movimiento/$',TipoMovimientoListAPI.as_view(),name='tipo_movimiento_list_api'),
    url(r'^pedido/$',PedidoListAPI.as_view(),name='pedido_list_api'),
    url(r'^detalle_pedido/$',DetallePedidoListAPI.as_view(),name='detalle_pedido_list_api'),
    url(r'^movimiento/$',MovimientoListAPI.as_view(),name='movimiento_list_api'),
    url(r'^detalle_movimiento/$',DetalleMovimientoListAPI.as_view(),name='detalle_movimiento_list_api'),
    url(r'^kardex/$',KardexListAPI.as_view(),name='kardex_list_api'),
    url(r'^control_producto_almacen/$',ControlProductoAlmacenListAPI.as_view(),name='control_producto_almacen_list_api'),
    

# Rest Delete-Update
    url(r'^almacen/(?P<pk>.+)$',AlmacenDetailAPI.as_view(),name='almacen_detail_api'),
    url(r'^tipo_movimiento/(?P<pk>.+)$',TipoMovimientoDetailAPI.as_view(),name='tipo_movimiento_detail_api'),
    url(r'^pedido/(?P<pk>.+)$',PedidoDetailAPI.as_view(),name='pedido_detail_api'),
    url(r'^detalle_pedido/(?P<pk>.+)$',DetallePedidoDetailAPI.as_view(),name='detalle_pedido_detail_api'),
    url(r'^movimiento/(?P<pk>.+)$',MovimientoDetailAPI.as_view(),name='movimiento_detail_api'),
    url(r'^detalle_movimiento/(?P<pk>.+)$',DetalleMovimientoDetailAPI.as_view(),name='detalle_movimiento_detail_api'),
    url(r'^kardex/(?P<pk>.+)$',KardexDetailAPI.as_view(),name='kardex_detail_api'),
    url(r'^control_producto_almacen/(?P<pk>.+)$',ControlProductoAlmacenDetailAPI.as_view(),name='control_producto_almacen_detail_api'),
    
]