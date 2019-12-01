from django.shortcuts import render
from apps.ventas.models import Ventas
from apps.ventas.forms import VentasForm
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.

def home_view(request,*args, **kwargs): 
    return render(request,"home.html",{})


class VentasList(ListView)      : 
      model                     = Ventas
      template_name             = 'ventas/listar_ventas.html'
      context_object_name       = 'ventas'
      queryset                  = Ventas.objects.all()

      def get_succes_url(self):
          return reverse('ventas:listar_ventas.html')


class VentasCreate(CreateView)  : 
      model                     = Ventas
      template_name             = 'ventas/crear_ventas.html'
      fields                    = "__all__" 
      success_url               = reverse_lazy('ventas: crear_ventas')

      #def get_succes_url(self)  : 
       #   return reverse('ventas: listar_ventas')


class VentasUpdate(UpdateView)  : 
    model                       = Ventas
    form_class                  = VentasForm
    template_name               = 'ventas/crear_ventas.html'
    success_url                 = reverse_lazy('ventas:listar_ventas')
    #queryset                    = Ventas.objects.all()

    
           
        
    


