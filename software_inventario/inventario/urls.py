from django.urls import path
from .views import *
urlpatterns = [
    path('inicio', inicio,name="inicio"),
    path('listar_stock', listar_stock,name="listar_stock"),
]
