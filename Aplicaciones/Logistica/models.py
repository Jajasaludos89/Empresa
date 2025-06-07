from django.db import models

class Envio(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    fecha_registro = models.DateField()

    def __str__(self):
        return self.nombre

class RegistroEnvio(models.Model):
    envio = models.ForeignKey(Envio, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    conductor = models.CharField(max_length=100)
    estado_viaje = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.envio.codigo} - {self.cliente.nombre}"
