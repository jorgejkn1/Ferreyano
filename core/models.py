from django.db import models

#class TipoEmpleado(models.Model):
    #descripcion = models.CharField(max_length=20)

class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    contrase = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    #tipo = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rut)

class Producto(models.Model):
    idP = models.IntegerField(primary_key=True)
    nombreP = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    valor = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    numero = models.IntegerField()
    #tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idP)

class Venta(models.Model):
    idV = models.CharField(max_length=12, primary_key=True)
    nombreV = models.CharField(max_length=40)
    fechaCompra = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.idV

class DetalleVenta(models.Model):
    idDet = models.CharField(max_length=12, primary_key=True)
    nombreDet = models.CharField(max_length=40)
    fechaCompra = models.DateTimeField(auto_now_add=True)
    fechaEntrega = models.DateTimeField(auto_now_add=True)
    totalD = models.IntegerField()
    descripcionD = models.CharField(max_length=40)

    def __str__(self):
        return self.idDet

class Carrito(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=1)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='carritos', default=1)  # Asegúrate de que el producto con idP=1 exista

    def __str__(self):
        return self.nombre

class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalles')

    def __str__(self):
        return f'Carrito {self.carrito.id} - Producto {self.producto.idP}'




#class Tarjeta(models.Model):
#    idT = models.CharField(max_length=12, primary_key=True)  # Cambiado a primary_key=True
#    nombreT = models.CharField(max_length=40)
#    fechaVenc = models.DateTimeField(auto_now_add=True)
#    nombreCliente = models.CharField(max_length=40)  # Cambiado Nombre_Cliente a nombreCliente
#    firma = models.CharField(max_length=5)
#    descripcionD = models.CharField(max_length=40)

#    def __str__(self):
#        return self.idT