from django.db import models

class Supplier(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)  
    telefono = models.CharField(max_length=20)  
    email = models.CharField(max_length=100)  
    direccion = models.CharField(max_length=200)
    anios_experiencia = models.CharField(max_length=3)  
    calificacion = models.CharField(max_length=10)  
    activo = models.CharField(max_length=10, default="si")  

    def __str__(self):
        return self.nombre
