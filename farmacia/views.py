from django.shortcuts import render, redirect
from .models import Farmacia, Sucursal, Medicamento, Inventario, Cliente, Pedido, PedidoMedicamento, Usuario
from django.contrib.auth import authenticate, login
from django.contrib import messages

def modelos_farmacia(request):
    context = {
        'farmacias': Farmacia.objects.all(),
        'sucursales': Sucursal.objects.all(),
        'medicamentos': Medicamento.objects.all(),
        'inventarios': Inventario.objects.all(),
        'clientes': Cliente.objects.all(),
        'pedidos': Pedido.objects.all(),
        'pedidos_medicamentos': PedidoMedicamento.objects.all(),
        'usuarios': Usuario.objects.all(),
    }
    return render(request, 'modelos_farmacia.html', context)

