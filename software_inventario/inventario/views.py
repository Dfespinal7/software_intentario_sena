from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

def inicio(request):
    return render(request,'inventario/inicio.html')

def listar_stock(request):
    k=StockInventarios.objects.all()
    context={"data":k}
    return render(request,'inventario/stock/stock_inventario.html',context)

def listar_entrada(request):
    k=Entradas.objects.all()
    context={"data":k}
    return render(request,'inventario/entrada/listar_entrada.html',context)

def listar_producto(request):
    k=Productos.objects.all()
    context={"data":k}
    return render(request,'inventario/producto/listar_producto.html',context)

def form_guardar(request):
    k=Categorias.objects.all()
    p=Proveedores.objects.all()
    c=Clientes.objects.all()
    contex={"categorias":k,"proveedores":p,"clientes":c}
    return render(request,'inventario/producto/form_productos.html',contex)

def guardar_datos(request):
    if request.method=='POST':
        #Producto
        idProducto=request.POST.get("idProducto")
        idCategoria=Categorias.objects.get(pk=request.POST.get("idCategoria"))
        nombre=request.POST.get("nombreProducto")
        unidadMedi=request.POST.get("unidadMedida")
        stock=request.POST.get("stock")
        #Entrada
        idEntrada=request.POST.get("idEntrada")
        idProveedor=Proveedores.objects.get(pk=request.POST.get("idProveedor"))
        #idProducto=request.POST.get("idProducto")
        #unidadMedi=request.POST.get("unidadMedida")
        obsent=request.POST.get("obsent")
        cantent=request.POST.get("cantent")
        valoruEntr=request.POST.get("valoruEntr")
        #Salida
        idSalida=request.POST.get("idSalida")
        #idProducto=request.POST.get("idProducto")
        idCliente=Clientes.objects.get(pk=request.POST.get("idCliente"))
        doc=request.POST.get("documento")
        obssal=request.POST.get("obssal")
        cantsal=request.POST.get("cantsal")
        valoruSal=request.POST.get("valoruSal")
        #stock
        idStockInventadrio=request.POST.get("idStock")
        #idCategoria=Categorias.objects.get(pk=request.POST.get("idCategoria"))
        #idProducto=request.POST.get("idProducto")
        #unidadMedi=request.POST.get("unidadMedida")
        #idEntrada=request.POST.get("idEntrada")
        #idSalida=request.POST.get("idSalida")
        #stock=request.POST.get("stock")
        #valoruEntr=request.POST.get("valoruEntr")
        valorinv=request.POST.get("valorinv")
        

        q=Productos(idProducto=idProducto,idCategoria=idCategoria,nombreProducto=nombre,unidadMedida=unidadMedi,stock=stock)
        q.save()
        messages.success(request, "Producto creado correctamente")
        
        k=Entradas(idProveedor=idProveedor,idProducto=q,unidadMedida=unidadMedi,observacion=obsent,cantidadEntrada=cantent,valorUnidad=valoruEntr)
        k.save()
        messages.success(request, "Entrada Creada Correctamente")

        s=Salidas(idProducto=q,idCliente=idCliente,documento=doc,observacion=obssal,cantidadSalida=cantsal,valorUnidad=valoruSal)
        s.save()
        messages.success(request, "Salida Creada Correctamente")
        cat=q.idCategoria
        unim=q.unidadMedida
        stock1=q.stock
        uni=k.valorUnidad
        inv=StockInventarios(nombreCategoria=cat,idProducto=q,unidadMedida=unim,idEntrada=k,idSalida=s,stock=stock1,valorUnidad=uni,valorInvenario=valorinv)
        inv.save()
        messages.success(request, "Stock Creado Correctamente")
        
        return HttpResponseRedirect(reverse('listar_producto',args=()))
    

def listar_salida(request):
        k=Salidas.objects.all()
        context={"data":k}
        return render(request,'inventario/salida/listar_salidas.html',context)

def editar_producto(request,idProfucto):
     pass