from django.urls import path
from app.suppliers.views import (
    SupplierListView,
    SupplierCreateView,
    SupplierUpdateView,
    SupplierDeleteView,
)

urlpatterns = [
    path("suppliers/", SupplierListView.as_view(), name="supplier-list"),
    path("suppliers/crear/", SupplierCreateView.as_view(), name="supplier-create"),
    path("suppliers/<int:pk>/editar/", SupplierUpdateView.as_view(), name="supplier-update"),
    path("suppliers/<int:pk>/eliminar/", SupplierDeleteView.as_view(), name="supplier-delete"),
]
