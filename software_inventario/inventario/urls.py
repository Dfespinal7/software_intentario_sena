from django.urls import path
from .views import *
urlpatterns = [
    path('inicio/', inicio,name="inicio"),
    path('listar_stock/', listar_stock,name="listar_stock"),
    path('listar_entrada/', listar_entrada,name="listar_entrada"),
    path('listar_producto/', listar_producto,name="listar_producto"),
    path('form_guardar/', form_guardar,name="form_guardar"),
    path('guardar_datos', guardar_datos,name="guardar_datos"),
    path('listar_salida/',listar_salida,name="listar_salida"),
    path('listar_proveedor/',listar_proveedor,name="listar_proveedor"),
    path('listar_cliente/',listar_cliente,name="listar_cliente"),
    path('listar_categorias/',listar_categoria,name="listar_categoria"),
    path('form_entradas',form_entradas,name="form_entradas"),
    path('guardar_entrada/',guardar_entrada,name="guardar_entrada"),
    path('form_salida/',form_salida,name="form_salida"),
    path('guardar_salida/',guardar_salida,name="guardar_salida"),
    path('editar_entrada/<int:idEntrada>/',editar_entrada,name="editar_entrada"),
    path('editar_salida/<int:idSalida>/',editar_salida,name="editar_salida"),
    path('eliminar_entrada/<int:idEntrada>/',eliminar_entrada,name="eliminar_entrada"),
    path('eliminar_salida/<int:idSalida>/',eliminar_salida,name="eliminar_salida"),
    path('editar_producto/<slug:idProducto>/',form_edit_product,name="editar_producto"),
    path('guardar_edit_product/',guardar_edit_product,name="guardar_edit_product"),
    path('buscar_producto/',buscar_producto,name="buscar_producto"),
    path('eliminar_producto/<slug:idProducto>/',eliminar_producto,name="eliminar_producto"),
    path('buscar_entrada/',buscar_entrada,name="buscar_entrada"),
    path('buscar_salida/',buscar_salida,name="buscar_salida"),
    path('buscar_stock/',buscar_stock,name="buscar_stock"),
    path('form_proveedor/',form_proveedor,name="form_proveedor"),
    path('guardar_proveedor/',guardar_proveedor,name="guardar_proveedor"),
    path('editar_proveedor/<int:idProveedor>/',editar_proveedor,name="editar_proveedor"),
    path('eliminar_proveedor/<int:idProveedor>/',eliminar_proveedor,name="eliminar_proveedor"),
    path('buscar_proveedor/',buscar_proveedor,name="buscar_proveedor"),
    path('form_categoria/',form_categoria,name="form_categoria"),
    path('guardar_categoria/',guardar_categoria,name="guardar_categoria"),
    path('editar_categoria/<int:idCategoria>/',editar_categoria,name="editar_categoria"),
    path('eliminar_categoria/<int:idCategoria>/',eliminar_categoria,name="eliminar_categoria"),
    path('buscar_categoria/',buscar_categoria,name="buscar_categoria"),
    path('form_clientes/',form_clientes,name="form_clientes"),
    path('guardar_cliente/',guardar_cliente,name="guardar_cliente"),
    path('editar_cliente/<int:idCliente>',editar_cliente,name="editar_cliente"),
    path('eliminar_cliente/<int:idCliente>',eliminar_cliente,name="eliminar_cliente"),
    path('buscar_cliente/',buscar_cliente,name="buscar_cliente"),
    path('listar_peps/',listar_peps,name="listar_peps"),
    path('busqueda_peps/',busqueda_peps,name="busqueda_peps"),
]
