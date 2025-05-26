from django.urls import path
from . import views

urlpatterns = [
    
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

    
]
