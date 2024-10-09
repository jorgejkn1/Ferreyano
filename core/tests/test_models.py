from django.test import  TestCase
from core.models import*

#testing a los models

class TipoProductoModelsTest(TestCase):

    def test_crear_tipoproducto(self):
        tipoproducto = TipoProducto.objects.create(descripcion='Cortantes')
        self.assertEqual(tipoproducto.descripcion ,'Cortantes')

    def test_str_tipoproducto(self):
        tipoproducto = TipoProducto.objects.create(descripcion='Cortantes')
        self.assertEqual(str(tipoproducto),'Cortantes')
