from django.urls import path
from .views import *
urlpatterns = [
    path('inicio', inicio,name="inicio"),
    path('listar_stock', listar_stock,name="listar_stock"),
    path('listar_entrada', listar_entrada,name="listar_entrada"),
    path('listar_producto', listar_producto,name="listar_producto"),
    path('form_guardar', form_guardar,name="form_guardar"),
    path('guardar_datos', guardar_datos,name="guardar_datos"),
]
