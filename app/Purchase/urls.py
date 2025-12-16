from django.urls import path
from app.Purchase.views import (
    PurchaseListView,
    PurchaseCreateView,
    PurchaseUpdateView,
    PurchaseDeleteView,
)

urlpatterns = [
    path("purchases/", PurchaseListView.as_view(), name="purchase-list"),
    path("purchases/crear/", PurchaseCreateView.as_view(), name="purchase-create"),
    path("purchases/<int:pk>/editar/", PurchaseUpdateView.as_view(), name="purchase-update"),
    path("purchases/<int:pk>/eliminar/", PurchaseDeleteView.as_view(), name="purchase-delete"),
]
