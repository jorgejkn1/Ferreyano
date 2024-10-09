from rest_framework import serializers
from .models import *

#LO USAREMOS PARA PODER TRANSFORMAR LOS DATOS PYTHON A DATOS JSON
class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

