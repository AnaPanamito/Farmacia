# Generated by Django 5.1.5 on 2025-02-02 22:36

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
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('metodoPago', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Farmacia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('idMedicamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombreUsuario', models.CharField(max_length=100, unique=True)),
                ('contrasena', models.CharField(max_length=100)),
                ('rol', models.CharField(choices=[('admin', 'Administrador'), ('empleado', 'Empleado'), ('cliente', 'Cliente')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idPedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(default='Pendiente', max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='farmacia.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoMedicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.medicamento')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.pedido')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='medicamentos',
            field=models.ManyToManyField(through='farmacia.PedidoMedicamento', to='farmacia.medicamento'),
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('farmacia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sucursales', to='farmacia.farmacia')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='sucursalDestino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='farmacia.sucursal'),
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(default=0)),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario', to='farmacia.medicamento')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario', to='farmacia.sucursal')),
            ],
        ),
    ]
