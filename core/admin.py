from django.contrib import admin
from .models import *
from admin_confirm import AdminConfirmMixin

class ClienteAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirmation_fields = ['rut', 'nombre', 'apellido', 'contrase', 'correo', 'direccion']

class ProductoAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirmation_fields = ['nombreP', 'cantidad', 'valor', 'descripcion', 'numero']

# Register your models here.
admin.site.register(TipoProducto)
#admin.site.register(TipoEmpleado)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Carrito)
admin.site.register(DetalleCarrito)

