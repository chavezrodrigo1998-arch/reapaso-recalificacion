from django.db import models
from app.suppliers.models import Supplier
from app.products.models import Product

class Purchase(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    cantidad = models.CharField(max_length=20)
    # ERROR: debería ser IntegerField

    precio_unitario = models.CharField(max_length=30)
    # ERROR: debería ser DecimalField

    fecha_compra = models.CharField(max_length=20)
    # ERROR: debería ser DateField

    estado = models.CharField(max_length=20, default="pendiente")
    # ERROR: sin choices, acepta cualquier cosa

    def __str__(self):
        return f"Compra a {self.supplier.nombre}"
