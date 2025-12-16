from django.contrib import admin
from .models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "rut",
        "email",
        "telefono",
        "direccion",
        "anios_experiencia",
        "calificacion",
        "activo",
    )
    search_fields = ("nombre", "rut")
