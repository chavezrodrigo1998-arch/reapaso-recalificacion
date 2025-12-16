from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "supplier",
        "precio",
        "stock",
        "categoria",
        "activo",
    )

    search_fields = (
        "nombre",
        "categoria",
        "supplier__nombre",
    )
