from django.db import models

# Create your models here.
class Clientes(models.Model):
    idCliente=models.BigAutoField(primary_key=True,blank=True)
    nombre=models.CharField(max_length=150)
    documento=models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre}"

class Categorias(models.Model):
    idCategoria=models.BigAutoField(primary_key=True,blank=True)
    nombreCategoria=models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombreCategoria}"

class Proveedores(models.Model):
    idProveedor=models.BigAutoField(primary_key=True,blank=True)
    nombre=models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre}"

class Productos(models.Model):
    idProducto=models.BigAutoField(primary_key=True,blank=True)
    idCategoria=models.ForeignKey(Categorias,on_delete=models.CASCADE)
    nombreProducto=models.CharField(max_length=150)
    unidadMedida=models.CharField(max_length=150)
    stock=models.IntegerField(null=True) #el stock es el resultado de la resta de entradas y salidas, no confundir con cantidad de las otras tablas
    
    def __str__(self):
        return f"{self.nombreProducto}"

class Entradas(models.Model):
    idEntrada=models.BigAutoField(primary_key=True,blank=True)
    idProveedor=models.ForeignKey(Proveedores,on_delete=models.CASCADE)
    idProducto=models.ForeignKey(Productos,on_delete=models.CASCADE)
    unidadMedida=models.CharField(max_length=150)
    observacion=models.CharField(max_length=150)
    cantidadEntrada=models.IntegerField()
    valorUnidad=models.DecimalField(max_digits=30,decimal_places=0)

    def __str__(self):
        return f"{self.cantidadEntrada}" #esto es una prueba

class Salidas(models.Model):
    idSalida=models.BigAutoField(primary_key=True,blank=True)
    idProducto=models.ForeignKey(Productos,on_delete=models.CASCADE)
    idCliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
    documento=models.CharField(max_length=150)  #viene del cliente
    observacion=models.CharField(max_length=150)
    cantidadSalida=models.IntegerField()
    valorUnidad=models.DecimalField(max_digits=30,decimal_places=2)

    def __str__(self):
        return f"{self.cantidadSalida}"

class StockInventarios(models.Model):
    idStockInventadrio=models.BigAutoField(primary_key=True,blank=True)
    nombreCategoria=models.CharField(max_length=150) #viene del producto
    idProducto=models.ForeignKey(Productos,on_delete=models.CASCADE) #va el nombre del producto
    unidadMedida=models.CharField(max_length=150) #va el nombre del producto
    idEntrada=models.ForeignKey(Entradas,on_delete=models.CASCADE) #este corresponde a la cantidad de la entrada
    idSalida=models.ForeignKey(Salidas,on_delete=models.CASCADE) #este corresponde a la cantidad de la salida
    stock=models.IntegerField() #resultado de la resta de entre la entrada y la salida
    valorUnidad=models.DecimalField(max_digits=30,decimal_places=0) #puede venir de la tabla productos
    valorInvenario=models.IntegerField() #es la multiplicacion entre el stock y valorUnidad



