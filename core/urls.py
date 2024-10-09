from django.urls import path, include
from .views import *
from rest_framework import routers


#CONFIGURAMOS LAS URL PARA LA API
router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('productos', ProductoViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('aboutus/', aboutus, name='aboutus'),
    path('contact/', contact, name='contact'),
    path('testimonial/', testimonial, name='testimonial'),
    path('blog/', blog, name='blog'),
    path('cart/', cart, name='cart'),
    path('account_locked/', account_locked, name="account_locked"),
    path('api/', include(router.urls)),
    path('clientesapi/', clientesapi, name='clientesapi'),
    path('productosapi/', productosapi, name='productosapi'),
    path('clientedetalle/<id>/', clientedetalle, name='clientedetalle'),
    path('productodetalle/<idP>/', productodetalle, name='productodetalle'),
    path('administrador/', administrador, name='administrador'),
    path('harryapi/', harryapi, name='harryapi'),

# <------------------- INICIO CRUD CLIENTES -------------------> #

    path('productos/addclientes/', clientesadd, name='clientesadd'),
    path('productos/updateclientes/<id>', clientesupdate, name='clientesupdate'),
    path('productos/delete/<id> ', clientesdelete, name='clientesdelete'),
    path('clientes/', clientes, name='clientes'),

# <------------------- FIN CRUD CLIENTES -------------------> #


# <------------------- INICIO CRUD PRODUCTOS -------------------> #

    path('productos/', productos, name='productos'),
    path('productos/add/', productosadd, name='productosadd'),
    path('productos/update/<id>', productosupdate, name='productosupdate'),
    path('productos/delete/<idP>', productosdelete, name='productosdelete'),

# <------------------- FIN CRUD PRODUCTOS -------------------> #


    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update-cart/<int:cart_item_id>/<int:quantity>/', update_cart, name='update_cart'),
    path('delete-cart-item/<int:p_item_id>/', delete_cart_item, name='delete_cart_item'),
    path('gracias/', gracias, name='gracias'),
    path('cargo/', cargo, name='cargo'),
    
    path('tarjeta/', tarjeta, name='tarjeta'),

# <------------------- INICIO REGISTER -------------------> #

    path('register/', register, name='register'),
    
# <------------------- FIN REGISTER -------------------> #


]
