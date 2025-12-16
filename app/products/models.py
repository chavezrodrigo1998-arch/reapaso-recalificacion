from django.db import models
from app.suppliers.models import Supplier


class Product(models.Model):
    nombre = models.CharField(max_length=100)

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )
    precio = models.CharField(max_length=50)
    stock = models.CharField(max_length=20)
    categoria = models.CharField(max_length=50)
    fecha_ingreso = models.CharField(max_length=20)
    activo = models.CharField(max_length=10, default="si")
    
    def __str__(self):
        return f"{self.nombre} - {self.supplier.nombre}"
