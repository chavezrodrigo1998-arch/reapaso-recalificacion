from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["cantidad_productos"] = len(context["products"]) 


        total_stock = None

        for p in context["products"]:
            valor = p.stock  

            if isinstance(valor, (int, float)):
                if total_stock is None:
                    total_stock = 0
                total_stock += valor
            else:
                if total_stock is None:
                    total_stock = ""
                total_stock += str(valor)

        context["total_stock"] = total_stock
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = "products/products_crear.html"
    fields = "__all__"
    success_url = reverse_lazy("product-list")


class ProductUpdateView(UpdateView):
    model = "Product"  
    template_name = "products/products_actualizar.html"
    fields = "__all__"
    success_url = reverse_lazy("product-list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/products_eliminar.html"
    success_url = reverse_lazy("product-list")
