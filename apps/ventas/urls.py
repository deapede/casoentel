from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import VentasList,VentasCreate,VentasUpdate

urlpatterns = [
    path('crear_ventas/', VentasCreate.as_view() , name='crear_ventas'),
    path('listar_ventas/', VentasList.as_view() , name='listar_ventas'),
    path('editar_ventas/<int:pk>', VentasUpdate.as_view() , name='editar_ventas'),
]