from django.urls import path # type: ignore
from . import views

urlpatterns = [
    
    path('', views.inicioEnvios),

    path('envios', views.inicioEnvios),
    path('nuevoEnvio', views.nuevoEnvio),
    path('guardarEnvio', views.guardarEnvio),
    path('eliminarEnvio/<id>', views.eliminarEnvio),
    path('editarEnvio/<id>', views.editarEnvio),
    path('procesarEdicionEnvio', views.procesarEdicionEnvio),

    path('clientes', views.inicioClientes),
    path('nuevoCliente', views.nuevoCliente),
    path('guardarCliente', views.guardarCliente),
    path('eliminarCliente/<id>', views.eliminarCliente),
    path('editarCliente/<id>', views.editarCliente),
    path('procesarEdicionCliente', views.procesarEdicionCliente),

    path('registros', views.inicioRegistros),
    path('nuevoRegistro', views.nuevoRegistro),
    path('guardarRegistro', views.guardarRegistro),
    path('eliminarRegistro/<id>', views.eliminarRegistro),
    path('editarRegistro/<id>', views.editarRegistro),
    path('procesarEdicionRegistro', views.procesarEdicionRegistro),
]
