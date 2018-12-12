from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from Apps.Usuario.views import guardarLista, crud, IndexView2, IndexView , Login, ClienteCreate , home
#Login requerido
from django.contrib.auth.decorators import login_required
app_name = 'Usuario'
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    #Vista del usuario sin registrar
    url(r'^$', views.home, name='home'),
    url(r'^registrar', views.ClienteCreate.as_view(), name = 'registroUsuario' ),
    url(r'^ingresar', Login.as_view(), name='login'),
    #Vista principal del mantenedor
    url(r'^mantenedor/$', login_required(IndexView), name='mantenedor'),
    #
    url(r'^guardar_lista/$', guardarLista, name='guardar_lista'),
    url(r'^producto/(?P<pk>\d+)/', IndexView2, name='productoconid'),
    #Mantenedor de listas
    url(r'^actualizarProducto/$', crud.actualizarProducto, name='actualizar_producto'),
    url(r'^([0-9]+)/editar_producto/$', crud.editarProducto, name='editar_producto'),
    url(r'^guardar_producto/(?P<pk>\d+)/', crud.guardarProducto, name='guardar_producto'),
    url(r'^guardar_tienda/$', views.guardarTienda, name='guardar_tienda'),
    url(r'^tienda/', login_required(views.IndexView3) , name='tienda'),
    url(r'^eliminartienda/(?P<pk>\d+)/', views.eliminartienda , name='eliminartienda'),
    url(r'^eliminarproducto/(?P<pk>\d+)/', views.eliminarproducto , name='eliminarproducto'),
    url(r'^actualizar_mascota/$', views.crud.actualizarProducto, name='actualizarProducto'),
    url(r'^verificartienda/(?P<pk>\d+)/', views.verificartienda , name='verificartienda'),
    #vista menu de opciones
    url(r'^menuinicio', login_required(views.menu), name='menu'),
    #vista para deslogearse
    url(r'^salir$', views.salir ,name='salir'),
    url(r'^contact$', views.contact ,name='contactanos'),
    #url para apí
    path('misfinanzasApi/', include(router.urls)),
]