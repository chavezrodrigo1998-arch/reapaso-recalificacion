from django.contrib import admin
from .models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "supplier",
        "product",
        "cantidad",
        "precio_unitario",
        "fecha_compra",
        "estado",
    )

    list_filter = (
        "estado",
    )
