from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
#commit
def inicio(request):
    return render(request,'inventario/inicio.html')

def listar_stock(request):
    k=StockInventarios.objects.all()
    context={"data":k}
    return render(request,'inventario/stock/stock_inventario.html',context)

def listar_entrada(request):
    k=Entradas.objects.all()
    suma=0
    for i in k:
     suma=suma+i.valorUnidad*i.cantEntInicial
   
    context={"data":k,"suma":suma}
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
        k = None  # Entradas
        s = None  # Salidas
        #Producto
        idProducto=request.POST.get("idProducto")
        fecha=request.POST.get("fecha")
        idCategoria=Categorias.objects.get(pk=request.POST.get("idCategoria"))
        nombre=request.POST.get("nombreProducto")
        unidadMedi=request.POST.get("unidadMedida")
        stock=request.POST.get("stock",0) or 0
        #Entrada
        idEntrada=request.POST.get("idEntrada")
        idProveedor=Proveedores.objects.get(pk=request.POST.get("idProveedor"))
        #idProducto=request.POST.get("idProducto")
        #unidadMedi=request.POST.get("unidadMedida")
        obsent=request.POST.get("obsent")
        cantent=request.POST.get("cantent",0) or 0
        valoruEntr=request.POST.get("valoruEntr",0) or 0
        #Salida
        idSalida=request.POST.get("idSalida")
        #idProducto=request.POST.get("idProducto")
        idCliente=Clientes.objects.get(pk=request.POST.get("idCliente"))
        doc=request.POST.get("documento",0)or 0
        obssal=request.POST.get("obssal")
        cantsal=request.POST.get("cantsal",0) or 0
        valoruSal=request.POST.get("valoruSal",0) or 0
        #stock
        idStockInventadrio=request.POST.get("idStock")
        #idCategoria=Categorias.objects.get(pk=request.POST.get("idCategoria"))
        #idProducto=request.POST.get("idProducto")
        #unidadMedi=request.POST.get("unidadMedida")
        #idEntrada=request.POST.get("idEntrada")
        #idSalida=request.POST.get("idSalida")
        #stock=request.POST.get("stock")
        #valoruEntr=request.POST.get("valoruEntr")
        valorinv=request.POST.get("valorinv",0) or 0
        

        q=Productos(idProducto=idProducto,idCategoria=idCategoria,nombreProducto=nombre,unidadMedida=unidadMedi,stock=stock)
        q.save()
        messages.success(request, "Producto creado correctamente")
        if int(cantent)>0:
          k=Entradas(idProveedor=idProveedor,idProducto=q,unidadMedida=unidadMedi,observacion=obsent,cantidadEntrada=cantent,cantEntInicial=cantent,valorUnidad=valoruEntr,fechaEnt=fecha)
          k.save()
          messages.success(request, "Entrada Creada Correctamente")
        else:
            pass  
        if int(cantsal)>0:    
          s=Salidas(idProducto=q,idCliente=idCliente,documento=doc,observacion=obssal,cantidadSalida=cantsal,valorUnidad=valoruSal,fechaSal=fecha)
          s.save()
          messages.success(request, "Salida Creada Correctamente")
        else:
            pass
        cat=q.idCategoria
        unim=q.unidadMedida
        stock1=q.stock
        if k:
            uni=k.valorUnidad
        else:
            uni=0       
        inv=StockInventarios(nombreCategoria=cat,idProducto=q,unidadMedida=unim,totalEntrada=k.cantidadEntrada if k else 0,totalSalida=s.cantidadSalida if s else 0,stock=stock1,valorUnidad=uni,valorInvenario=valorinv)
        inv.save()
        messages.success(request, "Stock Creado Correctamente")
        
        return HttpResponseRedirect(reverse('listar_producto',args=()))
    

def listar_salida(request):
        k=Salidas.objects.all()
        context={"data":k}
        return render(request,'inventario/salida/listar_salidas.html',context)

def listar_proveedor(request):
     q=Proveedores.objects.all()
     contex={"data":q}
     return render(request,'inventario/proveedor/listar_proveedor.html',contex)

def listar_cliente(request):
     q=Clientes.objects.all()
     contex={"data":q}
     return render(request,'inventario/cliente/listar_cliente.html',contex)
 
def listar_categoria(request):
     q=Categorias.objects.all()
     contex={"data":q}
     return render(request,'inventario/categoria/listar_categoria.html',contex)

def form_entradas(request):
     k=Productos.objects.all()
     q=Proveedores.objects.all()
     context={"productos":k,"proveedores":q}
     return render(request,'inventario/entrada/form_entrada.html',context)

def guardar_entrada(request):
     if request.method=='POST':
          idEntrada=request.POST.get("idEntrada")
          fecha=request.POST.get("fechaEntrada")
          producto=Productos.objects.get(pk=request.POST.get("producto"))
          proveedor=Proveedores.objects.get(pk=request.POST.get("proveedor"))
          unidad=request.POST.get("unidadMedida")
          obs=request.POST.get("observacion")
          cantent=request.POST.get("cantidadEntrada")
          valoru=request.POST.get("valorUnidad")
          if idEntrada=='':
               ent=Entradas(fechaEnt=fecha,idProveedor=proveedor,idProducto=producto,unidadMedida=unidad,observacion=obs,cantidadEntrada=cantent,cantEntInicial=cantent,valorUnidad=valoru)
               ent.save()

               objs=Entradas.objects.filter(idProducto=producto) #aca me estoy trayendo todas las entradas de un producto en especifico
               sumacantidad=0
               sumatotalvalor=0
               for i in objs:
                    
                    b=int(i.cantidadEntrada)*int(i.valorUnidad)
                    sumatotalvalor=sumatotalvalor+int(b)
                    sumacantidad=sumacantidad+int(i.cantidadEntrada)
               prom=int(sumatotalvalor)/int(sumacantidad)
          
               obsal=Salidas.objects.filter(idProducto=producto)
               restcant=0
               for i in obsal:
                    restcant=restcant+int(i.cantidadSalida)
               
               
               messages.success(request,"Entrada Crada correctamente")
               stock=StockInventarios.objects.get(idProducto=producto)
               sum=stock.totalEntrada+int(cantent)
               stock.totalEntrada=sum
               stock.stock=sum-int(stock.totalSalida)
               stock.valorUnidad=prom
               stock.valorInvenario=int(stock.valorInvenario)+(int(valoru)*int(cantent))
               stock.valorUnidad=int(stock.valorInvenario)/int(stock.stock)
               stock.save()
               
               actproduct=Productos.objects.get(idProducto=producto.idProducto)
               actproduct.stock=stock.stock
               actproduct.save()
               
               return HttpResponseRedirect(reverse('listar_entrada'))
          else:
               e=Entradas.objects.get(pk=idEntrada)
               e.fechaEnt=fecha
               e.idProveedor=proveedor
               e.idProducto=producto
               e.unidadMedida=unidad
               e.observacion=obs
               e.cantEntInicial=cantent
               e.cantidadEntrada=cantent
               e.valorUnidad=valoru
               e.save()

               objs=Entradas.objects.filter(idProducto=producto) #aca me estoy trayendo todas las entradas de un producto en especifico
               sumacantidad=0
               sumatotalvalor=0
               for i in objs:
                    
                    b=int(i.cantidadEntrada)*int(i.valorUnidad)
                    sumatotalvalor=sumatotalvalor+int(b)
                    sumacantidad=sumacantidad+int(i.cantidadEntrada)
               prom=int(sumatotalvalor)/int(sumacantidad)
          
               obsal=Salidas.objects.filter(idProducto=producto)
               restcant=0
               for i in obsal:
                    restcant=restcant+int(i.cantidadSalida)
               
               
               messages.success(request,"Entrada Crada correctamente")
               stock=StockInventarios.objects.get(idProducto=producto)
               entra=Entradas.objects.filter(idProducto=producto)
               totalent=0
               valorinv=0
               for i in entra:
                   totalent=totalent+int(i.cantEntInicial)
                   valorinv=valorinv+int(i.cantidadEntrada)*int(i.valorUnidad)
                   print(valorinv)
               

               stock.totalEntrada=totalent
               stock.valorInvenario=valorinv
               stock.stock=int(stock.totalEntrada)-int(stock.totalSalida)
               stock.valorUnidad=int(stock.valorInvenario)/int(stock.stock)
               stock.save()

               
               actproduct=Productos.objects.get(idProducto=producto.idProducto)
               actproduct.stock=stock.stock
               actproduct.save()
               
               return HttpResponseRedirect(reverse('listar_entrada'))


              
              
     
def form_salida(request):
     c=Clientes.objects.all()
     p=Productos.objects.all()
     contex={"clientes":c,"productos":p}
     return render(request,'inventario/salida/form_salidas.html',contex)
     
def guardar_salida(request):
     if request.method=='POST':
          fecha=request.POST.get("fecha")
          cliente=Clientes.objects.get(pk=request.POST.get("cliente"))
          producto=Productos.objects.get(pk=request.POST.get("producto"))
          obs=request.POST.get("observacion")
          cantsal=int(request.POST.get("cantidadSalida"))
          valoru=request.POST.get("valorUnidad")

          salida=Salidas(fechaSal=fecha,idProducto=producto,idCliente=cliente,documento=cliente.documento,observacion=obs,cantidadSalida=cantsal,valorUnidad=valoru)
          salida.save()

          ent=Entradas.objects.filter(idProducto=producto)
          cantidad_a_saldar = cantsal
          valor_total_salida=0
          for i in ent:
               if cantidad_a_saldar<=0:
                    break
               cantidad_disponible=int(i.cantidadEntrada)
               valor_unitario=int(i.valorUnidad)
               if cantidad_disponible<=cantidad_a_saldar:
                    valor_total_salida=valor_total_salida+cantidad_disponible*valor_unitario
                    cantidad_a_saldar=cantidad_a_saldar-cantidad_disponible
                    i.cantidadEntrada = 0  
               else:
                # Usar solo parte de la entrada
                valor_total_salida += cantidad_a_saldar * valor_unitario
                i.cantidadEntrada = cantidad_disponible - cantidad_a_saldar
                i.save()
                cantidad_a_saldar = 0
               i.save()

         

          s=StockInventarios.objects.get(idProducto=producto)
          s.totalSalida=int(s.totalSalida)+int(cantsal)
          s.stock=int(s.stock)-int(cantsal)
          s.valorInvenario=int(s.valorInvenario)-valor_total_salida #va tocar crear un campo en la tabla salidas y int(s.valorInvenario)-(int(cantsal)*int(valor que creamos para la salida))
          s.valorUnidad=int(s.valorInvenario)/int(s.stock)
          s.save()    
                                                                 
          actstock=Productos.objects.get(idProducto=producto.idProducto)
          actstock.stock=s.stock
          actstock.save()


          messages.success(request,'Salida creada correctamente')
          return HttpResponseRedirect(reverse('listar_salida'))

def editar_entrada(request,idEntrada):
     k=Entradas.objects.get(pk=idEntrada)
     p=Proveedores.objects.all()
     pro=Productos.objects.all()
     context={"data":k,"idEntrada":idEntrada,"proveedores":p,"productos":pro}
     return render(request,'inventario/entrada/form_entrada.html',context)
