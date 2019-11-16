from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import ProductoCreate, ProductoList, ProductoUpdate

urlpatterns = [
    path('crear_producto/', ProductoCreate.as_view() , name='crear_producto'),
    path('listar_producto/', ProductoList.as_view() , name='listar_producto'),
    path('editar_producto/<int:pk>', ProductoUpdate.as_view() , name='editar_producto'),
]