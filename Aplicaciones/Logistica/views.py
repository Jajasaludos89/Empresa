from django.shortcuts import render, redirect 
from .models import Envio, Cliente, RegistroEnvio
from django.contrib import messages  

#Envios

def inicioEnvios(request):
    envios = Envio.objects.all()
    return render(request, "inicioEnvios.html", {'envios': envios})

def nuevoEnvio(request):
    return render(request, "nuevoEnvio.html")

def guardarEnvio(request):
    codigo = request.POST["codigo"]
    origen = request.POST["origen"]
    destino = request.POST["destino"]

    Envio.objects.create(codigo=codigo, origen=origen, destino=destino)
    messages.success(request, "Envío GUARDADO exitosamente")
    return redirect('/envios')

def eliminarEnvio(request, id):
    envio = Envio.objects.get(id=id)
    envio.delete()
    messages.success(request, "Envío ELIMINADO exitosamente")
    return redirect('/envios')

def editarEnvio(request, id):
    envio = Envio.objects.get(id=id)
    return render(request, "editarEnvio.html", {'envio': envio})

def procesarEdicionEnvio(request):
    id = request.POST["id"]
    envio = Envio.objects.get(id=id)
    envio.codigo = request.POST["codigo"]
    envio.origen = request.POST["origen"]
    envio.destino = request.POST["destino"]
    envio.save()
    messages.success(request, "Envío ACTUALIZADO exitosamente")
    return redirect('/envios')


#Cliente

def inicioClientes(request):
    clientes = Cliente.objects.all()
    return render(request, "inicioClientes.html", {'clientes': clientes})

def nuevoCliente(request):
    return render(request, "nuevoCliente.html")

def guardarCliente(request):
    nombre = request.POST["nombre"]
    telefono = request.POST["telefono"]
    direccion = request.POST["direccion"]
    fecha_registro = request.POST["fecha_registro"]

    Cliente.objects.create(
        nombre=nombre,
        telefono=telefono,
        direccion=direccion,
        fecha_registro=fecha_registro
    )
    messages.success(request, "Cliente GUARDADO exitosamente")
    return redirect('/clientes')

def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    messages.success(request, "Cliente ELIMINADO exitosamente")
    return redirect('/clientes')

def editarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, "editarCliente.html", {'cliente': cliente})

def procesarEdicionCliente(request):
    id = request.POST["id"]
    cliente = Cliente.objects.get(id=id)
    cliente.nombre = request.POST["nombre"]
    cliente.telefono = request.POST["telefono"]
    cliente.direccion = request.POST["direccion"]
    cliente.fecha_registro = request.POST["fecha_registro"]
    cliente.save()
    messages.success(request, "Cliente ACTUALIZADO exitosamente")
    return redirect('/clientes')


#Registro 


def inicioRegistros(request):
    registros = RegistroEnvio.objects.all()
    return render(request, "inicioRegistros.html", {'registros': registros})

def nuevoRegistro(request):
    envios = Envio.objects.all()
    clientes = Cliente.objects.all()
    return render(request, "nuevoRegistro.html", {'envios': envios, 'clientes': clientes})

def guardarRegistro(request):
    envio_id = request.POST["envio_id"]
    cliente_id = request.POST["cliente_id"]
    conductor = request.POST["conductor"]
    estado_viaje = request.POST["estado_viaje"]

    envio = Envio.objects.get(id=envio_id)
    cliente = Cliente.objects.get(id=cliente_id)

    RegistroEnvio.objects.create(
        envio=envio,
        cliente=cliente,
        conductor=conductor,
        estado_viaje=estado_viaje
    )
    messages.success(request, "Registro de Envío GUARDADO exitosamente")
    return redirect('/registros')

def eliminarRegistro(request, id):
    registro = RegistroEnvio.objects.get(id=id)
    registro.delete()
    messages.success(request, "Registro de Envío ELIMINADO exitosamente")
    return redirect('/registros')

def editarRegistro(request, id):
    registro = RegistroEnvio.objects.get(id=id)
    envios = Envio.objects.all()
    clientes = Cliente.objects.all()
    return render(request, "editarRegistro.html", {
        'registro': registro,
        'envios': envios,
        'clientes': clientes
    })

def procesarEdicionRegistro(request):
    id = request.POST["id"]
    registro = RegistroEnvio.objects.get(id=id)
    registro.envio = Envio.objects.get(id=request.POST["envio_id"])
    registro.cliente = Cliente.objects.get(id=request.POST["cliente_id"])
    registro.conductor = request.POST["conductor"]
    registro.estado_viaje = request.POST["estado_viaje"]
    registro.save()
    messages.success(request, "Registro de Envío ACTUALIZADO exitosamente")
    return redirect('/registros')