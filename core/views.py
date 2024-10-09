from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from .models import *
import stripe
stripe.api_key = 'sk_test_51PW4vxLR94EtMer1vQSvf2lg6HLUGLs2gqPMr1aZ13TsOyxvXaWQUUECuZ2RYT792hWVe7gTJ4kJqyCKQSrv51rO00q5974tPh'
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib import messages
from rest_framework import viewsets
from .serializers import *
from rest_framework.renderers import JSONRenderer
import requests

# Create your views here.
#METODOS PARA LISTAR DES DE EL API
def harryapi(request):
    response = requests.get('https://hp-api.onrender.com/api/characters/')
    hp_api = response.json()

    paginator = Paginator(hp_api, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    aux = {
        'page_obj' : page_obj
    }

    return render(request, 'core/productos/crudapi/hp_api.html', aux)

def clientesapi(request):
    response = requests.get('http://127.0.0.1:8000/api/clientes/')
    clientes = response.json()

    paginator = Paginator(clientes, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    aux = {
        'page_obj' : page_obj
    }

    return render(request, 'core/productos/crudapi/listaAPI.html', aux)

def productosapi(request):
    response = requests.get('http://127.0.0.1:8000/api/productos/')
    productos = response.json()

    paginator = Paginator(productos, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    aux = {
        'page_obj' : page_obj
    }

    return render(request, 'core/productos/crudapi/productosAPI.html', aux)

def clientedetalle(request, id):
    response = requests.get(f'http://127.0.0.1:8000/api/clientes/{id}/')
    cliente = response.json()

    aux = {
        'cliente' : cliente
    }

    return render(request, 'core/productos/crudapi/detalle.html', aux)

def productodetalle(request, idP):
    response = requests.get(f'http://127.0.0.1:8000/api/productos/{idP}/')
    producto = response.json()

    aux = {
        'producto' : producto
    }

    return render(request, 'core/productos/crudapi/detalleProducto.html', aux)

def detallehp(request, id):
    response = requests.get(f'https://hp-api.onrender.com/api/characters/{id}/')
    hp_api = response.json()

    aux = {
        'hp_api' : hp_api
    }

    return render(request, 'core/productos/crudapi/detalleHP.html', aux)


#UTILIZAMOS LOS VIEWSETS PARA MANEJAR LAS SOLICITUDES TIPO HTTP (GET, POST, PUT, DELETE)
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializers
    renderer_classes = [JSONRenderer]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('idP')
    serializer_class = ProductoSerializers
    renderer_classes = [JSONRenderer]

def index(request):
    return render(request, 'core/index.html')

def product(request):
    return render(request, 'core/product.html')

def aboutus(request):
    return render(request, 'core/aboutus.html')

def contact(request):
    return render(request, 'core/contact.html')

def testimonial(request):
    return render(request, 'core/testimonial.html')

def blog(request):
    return render(request, 'core/blog.html')

def account_locked(request):
    return render(request, 'core/account_locked.html')

def cargo(request):
    redirect('Gracias')
    
def gracias(request):
    render(request, 'core/gracias.html')

def cart(request):
    items = Carrito.objects.all()  # Obtener todos los items del carrito
    subtotal = sum(item.precio for item in items) ###Aqui se modifico item.total por item.precio
    total = subtotal  # Puedes agregar lógica adicional para descuentos, impuestos, etc.
    return render(request, 'core/cart.html', {'items': items, 'subtotal': subtotal, 'total': total})

# ----------------> INICIO DEL ADMINISTARDOR ----------------> #

def administrador(request):
    return render(request, 'core/administrador/index.html')


# <---------------- INICIO CRUD PRODUCTOS ----------------> #
@login_required
def productos(request):
    productos = Producto.objects.all()

    paginator = Paginator(productos, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    aux = {
        'page_obj' : page_obj
    }

    return render(request, 'core/productos/index.html', aux)

@login_required
@permission_required('core.add_productos')
def productosadd(request):
    aux = {
        'form' : ProductoForm
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = 'Producto Agregado Correctamente.'
        else:
            aux['form'] = formulario
            aux['msj'] = 'Error al Agregar El Producto.'

    return render(request, 'core/productos/crud/add.html', aux)

@login_required
@permission_required('core.change_productos')
def productosupdate(request, id):
    productos = Producto.objects.get(idP=id)
    aux = {
            'form' : ProductoForm(instance=productos)
        }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=productos)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            aux['msj'] = 'Producto Actualizado Correctamente.'
        else:
            aux['form'] = formulario
            aux['msj'] = 'Error al Actualizar Al Producto.'

    return render(request, 'core/productos/crud/update.html', aux)

@login_required
@permission_required('core.delete_productos')
def productosdelete(request, idP):
    productos = Producto.objects.get(idP=idP)
    productos.delete()

    return redirect(to="productos")
# <---------------- FIN CRUD PRODUCTOS ----------------> #


# <---------------- INICIO CRUD CLIENTE ----------------> #

@login_required
def clientes(request):
    clientes = Cliente.objects.all()

    paginator = Paginator(clientes, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    aux = {
        'page_obj' : page_obj
    }


    return render(request, 'core/productos/listaCliente.html', aux)

@login_required
def clientesadd(request):
    aux = {
        'form' : ClientesForm()
    }

    if request.method == 'POST':
        formulario = ClientesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = 'Cliente Agregado Correctamente.'
        else:
            aux['form'] = formulario
            aux['msj'] = 'Error al Agregar Al Cliente.'

    return render(request, 'core/productos/crudclientes/addcliente.html', aux)

@login_required
def clientesupdate(request, id):
    clientes = Cliente.objects.get(id=id)
    aux = {
            'form' : ClientesForm(instance=clientes)
        }

    if request.method == 'POST':
        formulario = ClientesForm(data=request.POST, instance=clientes)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            aux['msj'] = 'Cliente Actualizado Correctamente.'
        else:
            aux['form'] = formulario
            aux['msj'] = 'Error al Actualizar Al Cliente.'

    return render(request, 'core/productos/crudclientes/updatecliente.html', aux)

@login_required
def clientesdelete(request, id):
    clientes = Cliente.objects.get(id=id)
    clientes.delete()

    return redirect(to="clientes")
# <---------------- FIN CRUD CLIENTE ----------------> #

# ----------------> FIN DEL ADMINISTARDOR ----------------> #

#pago
def tarjeta(request):
    return render(request, 'core/tarjeta.html')


# Funciones para el carrito

def add_to_cart(request, product_id):
    producto = get_object_or_404(Producto, pk=product_id)
    # Aquí deberías implementar la lógica para agregar al carrito
    # Suponiendo que tienes un modelo Carrito con un ForeignKey a Producto
    ###Se modifico la linea siguiente, de manera en que el precio en el carrito tenga algun valor al ser creado,
    ### esto debido a que en el model, el valor del campo precio no puede ser nulo.
    carrito_item, created = Carrito.objects.get_or_create(producto=producto, defaults={'nombre': producto.nombreP, 'precio': producto.valor})
    if not created:
        carrito_item.cantidad += 1
        carrito_item.precio = producto.valor * carrito_item.cantidad #aqui simplemente para calcular el precio total
        carrito_item.save()
    response_data = {'message': 'Producto agregado al carrito.'}
    ###Esto de aqui lo comente mas que nada como solucion parche, ya que no entendi que querian hacer al retornar un Json
    #return JsonResponse(response_data)
    return redirect(to="product")

def update_cart(request, cart_item_id, quantity):
    carrito_item = get_object_or_404(Carrito, pk=cart_item_id)
    carrito_item.cantidad = quantity
    carrito_item.save()
    response_data = {'message': 'Cantidad actualizada.'}
    return JsonResponse(response_data)

def delete_cart_item(request, p_item_id):
    #carrito_item = get_object_or_404(Carrito, pk=cart_item_id)
    carrito_item = Carrito.objects.get(id=p_item_id)
    carrito_item.delete()
    response_data = {'message': 'Producto eliminado del carrito.'}
    #return JsonResponse(response_data)
    return redirect(to="cart")

#<---------------------------- REGISTRARSE --------------------------------->#
def register(request):
    aux = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            group = Group.objects.get(name='vendedor')
            user.groups.add(group)

            aux['msj'] = 'Usuario Agregado Correctamente.'
            return redirect(to="index")
        else:
            aux['form'] = formulario


    return render(request, 'registration/register.html', aux)

#<---------------------------- FIN REGISTRARSE ----------------------------->#
