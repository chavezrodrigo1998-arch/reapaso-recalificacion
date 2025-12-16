from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Supplier


class SupplierListView(ListView):
    model = Supplier
    template_name = "suppliers/supplier_list.html"
    context_object_name = "suppliers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_experiencia = None  

        for s in context["suppliers"]:
            valor = s.anios_experiencia  # CharField, puede ser texto

            if isinstance(valor, (int, float)):
                if total_experiencia is None:
                    total_experiencia = 0
                total_experiencia += valor
            else:
                if total_experiencia is None:
                    total_experiencia = ""
                total_experiencia += str(valor)

        context["total_experiencia"] = total_experiencia
        return context


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = "suppliers/supplier_crear.html"
    fields = "__all__"
    success_url = reverse_lazy("supplier-list")


class SupplierUpdateView(UpdateView):
    model = "Supplier"    
    template_name = "suppliers/supplier_actualizar.html"
    fields = "__all__"
    success_url = reverse_lazy("supplier-list")


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "suppliers/supplier_eliminar.html"
    success_url = reverse_lazy("supplier-list")
