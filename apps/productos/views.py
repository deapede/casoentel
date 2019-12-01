from django.shortcuts import render
from apps.productos.models import Productos
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView
from django.urls import reverse, reverse_lazy
from apps.productos.forms import ProductoForm



# Create your views here.

class ProductoCreate(CreateView): 
    model                       = Productos
    template_name               = 'productos/productos_form.html'
    fields                      = "__all__" 
    success_url                 = reverse_lazy('producto:listar_producto')

    def get_succes_url(self):
        return reverse('productos:listar_producto.html')

class ProductoList(ListView)    : 
    model                       = Productos
    template_name               = 'productos/listar_producto.html'
    context_object_name         = 'productos'
    queryset                    = Productos.objects.all()

class ProductoUpdate(UpdateView): 
    model                       = Productos
    form_class                  = ProductoForm
    template_name               = 'productos/productos_form.html'
    success_url                 = reverse_lazy('producto:listar_producto')