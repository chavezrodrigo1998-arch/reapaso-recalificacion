from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Purchase


class PurchaseListView(ListView):
    model = Purchase
    template_name = "Purchase/Purchase_list.html"
    context_object_name = "purchases"


class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = "Purchase/Purchase_crear.html"
    fields = "__all__"
    success_url = reverse_lazy("purchase-list")


class PurchaseUpdateView(UpdateView):
    model = Purchase
    template_name = "Purchase/Purchase_actualizar.html"
    fields = "__all__"
    success_url = reverse_lazy("purchase-list")


class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = "Purchase/Purchase_eliminar.html"
    success_url = reverse_lazy("purchase-list")
