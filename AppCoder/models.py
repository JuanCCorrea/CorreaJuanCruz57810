from django.db import models
from django.contrib.auth.models import User

class Surf(models.Model):
    clases = models.CharField(max_length=50)
    valor = models.IntegerField()
    
    def __str__(self):
        return f"{self.clases}, {self.valor}"


class Body(models.Model):
    clases = models.CharField(max_length=50)
    valor = models.IntegerField()
    
    def __str__(self):
        return f"{self.clases}, {self.valor}"


class Horario(models.Model):
    horario = models.TimeField()
    
    def __str__(self):
        return f"{self.horario}"    


class Reserva (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    fecha = models.DateField()
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Avatar (models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} {self.imagen}"