# Generated by Django 5.1.6 on 2025-02-14 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Farmacia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=20, unique=True)),
                ('salario', models.FloatField()),
                ('cargo', models.CharField(choices=[('EMPLEADO', 'Empleado'), ('ADMINISTRADOR', 'Administrador')], max_length=15)),
                ('farmacia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmacia.farmacia')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('farmacia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sucursal_list', to='Farmacia.farmacia')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, null=True, unique=True)),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Farmacia.producto')),
                ('sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventario_list', to='Farmacia.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('fecha', models.DateField()),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('impuesto', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('metodo_pago', models.CharField(choices=[('EFECTIVO', 'Efectivo'), ('TARJETA', 'Tarjeta')], max_length=20)),
                ('TipoEntrega', models.CharField(choices=[('Retiro en origen', 'Retiro en origen'), ('Retiro en sucursal actual', 'Retiro en sucursal actual')], default='Retiro en origen', max_length=30)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factura_list', to='Farmacia.cliente')),
                ('inventario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Farmacia.inventario')),
                ('sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='factura_list', to='Farmacia.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('fecha', models.DateField()),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('estado', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('COMPLETADA', 'Completada'), ('CANCELADA', 'Cancelada')], default='PENDIENTE', max_length=20)),
                ('destino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transferencias_destino', to='Farmacia.sucursal')),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Farmacia.empleado')),
                ('origen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transferencias_origen', to='Farmacia.sucursal')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transferencia_list', to='Farmacia.producto')),
            ],
        ),
    ]
