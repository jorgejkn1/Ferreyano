# Generated by Django 5.0.4 on 2024-07-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_cliente_tipo_delete_tipoempleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
