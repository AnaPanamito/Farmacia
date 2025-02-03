from django.contrib import admin
from .models import Farmacia, Sucursal, Medicamento, Inventario, Cliente, Pedido, PedidoMedicamento, Usuario

# Registro de modelos básicos
@admin.register(Farmacia)
class FarmaciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre', 'direccion')

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'farmacia')
    list_filter = ('farmacia',)
    search_fields = ('nombre', 'direccion')

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion')
    search_fields = ('nombre', 'descripcion')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('sucursal', 'medicamento', 'stock')
    list_filter = ('sucursal', 'medicamento')
    search_fields = ('sucursal__nombre', 'medicamento__nombre')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'metodoPago')
    search_fields = ('nombre', 'telefono')

# Registro de modelos relacionados con pedidos
class PedidoMedicamentoInline(admin.TabularInline):
    model = PedidoMedicamento
    extra = 1  # Número de formularios vacíos para agregar medicamentos

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('idPedido', 'fecha', 'cliente', 'estado', 'sucursalDestino')
    list_filter = ('estado', 'sucursalDestino')
    search_fields = ('cliente__nombre', 'sucursalDestino__nombre')
    inlines = [PedidoMedicamentoInline]  # Incluir medicamentos en el formulario de pedido

@admin.register(PedidoMedicamento)
class PedidoMedicamentoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'medicamento', 'cantidad')
    list_filter = ('pedido', 'medicamento')
    search_fields = ('pedido__idPedido', 'medicamento__nombre')

# Registro de usuarios
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombreUsuario', 'rol')
    list_filter = ('rol',)
    search_fields = ('nombreUsuario',)