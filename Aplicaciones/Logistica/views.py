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

