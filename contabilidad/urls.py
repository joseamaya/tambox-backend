from django.conf.urls import url
from api import CuentaContableListAPI,FormaPagoListAPI,TipoListAPI,TipoDocumentoListAPI,TipoExistenciaListAPI,ConfiguracionListAPI,ImpuestoListAPI,\
EmpresaListAPI,CuentaContableDetailAPI,FormaPagoDetailAPI,TipoDetailAPI,TipoDocumentoDetailAPI,TipoExistenciaDetailAPI,ConfiguracionDetailAPI,ImpuestoDetailAPI,\
ConfiguracionDetailAPI,EmpresaDetailAPI

urlpatterns = [
#Rest List-Create
    url(r'^cuenta_contable/$',CuentaContableListAPI.as_view(),name='cuenta_list_api'),
    url(r'^forma_pago/$',FormaPagoListAPI.as_view(),name='forma_pago_list_api'),
    url(r'^tipo_documento/$',TipoDocumentoListAPI.as_view(),name='tipo_documento_list_api'),
    url(r'^tipo/$',TipoListAPI.as_view(),name='tipo_list_api'),
    url(r'^impuesto/$',ImpuestoListAPI.as_view(),name='impuesto_list_api'),
    url(r'^empresa/$',EmpresaListAPI.as_view(),name='empresa_list_api'),
    url(r'^configuracion/$',ConfiguracionListAPI.as_view(),name='configuracion_list_api'),
    url(r'^tipo_existencia/$',TipoExistenciaListAPI.as_view(),name='tipo_existencia_list_api'),

#Rest Delete-Update
     url(r'^cuenta_contable/(?P<pk>.+)$',CuentaContableDetailAPI.as_view(),name='cuenta_detail_api'),
    url(r'^forma_pago/(?P<pk>.+)$',FormaPagoDetailAPI.as_view(),name='forma_pago_detail_api'),
    url(r'^tipo_documento/(?P<pk>.+)$',TipoDocumentoDetailAPI.as_view(),name='tipo_documento_detail_api'),
    url(r'^tipo/(?P<pk>.+)$',TipoDetailAPI.as_view(),name='tipo_detail_api'),
    url(r'^impuesto/(?P<pk>.+)$',ImpuestoDetailAPI.as_view(),name='impuesto_detail_api'),
    url(r'^empresa/(?P<pk>.+)$',EmpresaDetailAPI.as_view(),name='empresa_detail_api'),
    url(r'^configuracion/(?P<pk>.+)$',ConfiguracionDetailAPI.as_view(),name='configuracion_detail_api'),
    url(r'^tipo_existencia/(?P<pk>.+)$',TipoExistenciaDetailAPI.as_view(),name='tipo_existencia_detail_api'),
]
