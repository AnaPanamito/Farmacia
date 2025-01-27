from django.shortcuts import render
from .models import Farmacia

# Create your views here.
def index(request):
    return render(request, 'index.html')

class FarmaciaView(View):
    """Vista para gestionar farmacias y sucursales."""
def get(request):
    farmacias = Farmacia.objects.all()
    return render(request, "farmacias.html", {"farmacias": farmacias})
class SucursalView(View):
    """Vista para mostrar las sucursales de una farmacia."""
    def get(self, request, farmacia_id):
        farmacia = get_object_or_404(Farmacia, id=farmacia_id)
        sucursales = farmacia.sucursales.all()
        return render(request, "sucursales.html", {"farmacia": farmacia, "sucursales": sucursales})


class MedicamentoView(View):
    """Vista para gestionar medicamentos y consultar inventarios."""

    def get(self, request, sucursal_id):
        sucursal = get_object_or_404(Sucursal, id=sucursal_id)
        inventarios = Stock.objects.filter(sucursal=sucursal)
        return render(request, "inventario.html", {"sucursal": sucursal, "inventarios": inventarios})


class PedidoView(View):
    """Vista para crear pedidos."""

    def get(self, request):
        clientes = Cliente.objects.all()
        medicamentos = Medicamento.objects.all()
        return render(request, "crear_pedido.html", {"clientes": clientes, "medicamentos": medicamentos})

    def post(self, request):
        cliente_id = request.POST.get("cliente")
        medicamento_id = request.POST.get("medicamento")
        cantidad = int(request.POST.get("cantidad"))
        sucursal_id = request.POST.get("sucursal_origen")

        cliente = get_object_or_404(Cliente, id=cliente_id)
        sucursal = get_object_or_404(Sucursal, id=sucursal_id)
        medicamento = get_object_or_404(Medicamento, id=medicamento_id)
        inventario = get_object_or_404(Stock, sucursal=sucursal, medicamento=medicamento)

        if inventario.cantidad >= cantidad:
            pedido = Pedido.objects.create(cliente=cliente, inventario_origen=inventario)
            DetallePedido.objects.create(
                pedido=pedido,
                medicamento=medicamento,
                cantidad=cantidad,
                precio_unitario=medicamento.precio
            )
            inventario.cantidad -= cantidad
            inventario.save()
            return JsonResponse({"message": "Pedido creado exitosamente"}, status=201)
        else:
            return JsonResponse({"error": "Stock insuficiente"}, status=400)

