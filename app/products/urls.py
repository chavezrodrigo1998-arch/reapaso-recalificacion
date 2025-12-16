from django.urls import path
from app.products.views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("products/crear/", ProductCreateView.as_view(), name="product-create"),
    path("products/<int:pk>/editar/", ProductUpdateView.as_view(), name="product-update"),
    path("products/<int:pk>/eliminar/", ProductDeleteView.as_view(), name="product-delete"),
]
