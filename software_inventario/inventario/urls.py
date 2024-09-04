from django.urls import path
from .views import *
urlpatterns = [
    path('inicio', inicio,name="inicio"),
    path('listar_stock', listar_stock,name="listar_stock"),
    path('listar_entrada', listar_entrada,name="listar_entrada"),
    path('listar_producto', listar_producto,name="listar_producto"),
    path('form_guardar', form_guardar,name="form_guardar"),
    path('guardar_datos', guardar_datos,name="guardar_datos"),
    path('listar_salida',listar_salida,name="listar_salida"),
    path('listar_proveedor',listar_proveedor,name="listar_proveedor"),
    path('listar_cliente',listar_cliente,name="listar_cliente"),
    path('listar_categorias',listar_categoria,name="listar_categoria"),
    path('form_entradas',form_entradas,name="form_entradas"),
    path('guardar_entrada',guardar_entrada,name="guardar_entrada"),
]
