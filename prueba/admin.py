from django.contrib import admin
from .models import Usuario, Rol, Cliente, Medicamento, Farmacia, Sucursal, Inventario, Pedido, DetallePedido, Stock


# Personalización del modelo Usuario en el admin
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rol', 'telefono', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'rol__nombre')
    list_filter = ('is_staff', 'is_active', 'rol')
    ordering = ('username',)


# Personalización del modelo Rol en el admin
@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre', 'tipo')
    list_filter = ('tipo',)


# Personalización del modelo Cliente en el admin
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'metodo_pago')
    search_fields = ('nombre', 'direccion', 'telefono')
    list_filter = ('metodo_pago',)


# Personalización del modelo Medicamento en el admin
@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion')
    search_fields = ('nombre',)
    list_filter = ('precio',)


# Personalización del modelo Farmacia en el admin
@admin.register(Farmacia)
class FarmaciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre', 'direccion')
    list_filter = ('nombre',)


# Personalización del modelo Sucursal en el admin
@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'farmacia')
    search_fields = ('nombre', 'direccion', 'farmacia__nombre')
    list_filter = ('farmacia',)


# Personalización del modelo Inventario en el admin
@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('farmacia', 'medicamento', 'cantidad_total')
    search_fields = ('farmacia__nombre', 'medicamento__nombre')
    list_filter = ('farmacia',)


# Personalización del modelo Pedido en el admin
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'inventario_origen', 'estado', 'fecha')
    search_fields = ('id', 'cliente__nombre', 'inventario_origen__farmacia__nombre')
    list_filter = ('estado', 'fecha', 'inventario_origen__farmacia')


# Personalización del modelo DetallePedido en el admin
@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'medicamento', 'cantidad', 'precio_unitario')
    search_fields = ('pedido__id', 'medicamento__nombre')
    list_filter = ('medicamento',)


# Personalización del modelo Stock en el admin
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('sucursal', 'medicamento', 'cantidad')
    search_fields = ('sucursal__nombre', 'medicamento__nombre')
    list_filter = ('sucursal',)
