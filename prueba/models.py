from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import MinValueValidator, RegexValidator


# Modelo de Usuario
class Usuario(AbstractUser):
    rol = models.ForeignKey('Rol', on_delete=models.PROTECT)
    telefono = models.CharField(
        max_length=20,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Ingrese un número de teléfono válido (hasta 15 dígitos)."
            )
        ]
    )

    # Solución a conflictos de relaciones reversas
    groups = models.ManyToManyField(
        Group,
        related_name="usuarios_set",  # Cambiar los nombres predeterminados
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuarios_custom_set",  # Cambio para evitar conflictos
        blank=True
    )

    def __str__(self):
        return f"{self.username} - {self.email}"


# Modelo de Rol
class Rol(models.Model):
    TIPO_ROL = [
        ('cliente', 'Cliente'),
        ('empleado', 'Empleado'),
    ]
    nombre = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_ROL, default='cliente')

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


# Modelo de Farmacia
class Farmacia(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    usuarios = models.ManyToManyField(Usuario, related_name='farmacias')

    def agregar_sucursal(self, nombre, direccion):
        nueva_sucursal = Sucursal.objects.create(
            farmacia=self,
            nombre=nombre,
            direccion=direccion
        )
        return nueva_sucursal

    def buscar_sucursal(self, nombre):
        return self.sucursales.filter(nombre__icontains=nombre)

    def __str__(self):
        return self.nombre


# Modelo de Sucursal
class Sucursal(models.Model):
    farmacia = models.ForeignKey(Farmacia, related_name='sucursales', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def consultar_stock(self, medicamento):
        try:
            stock = Stock.objects.get(sucursal=self, medicamento=medicamento)
            return stock.cantidad
        except Stock.DoesNotExist:
            return 0

    def __str__(self):
        return f"{self.nombre} - {self.farmacia.nombre}"


# Modelo de Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Ingrese un número de teléfono válido (hasta 15 dígitos)."
            )
        ]
    )
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# Modelo de Inventario para medicamentos
class Inventario(models.Model):
    farmacia = models.ForeignKey(Farmacia, related_name='inventarios', on_delete=models.CASCADE)
    medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE)
    cantidad_total = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('farmacia', 'medicamento')

    def actualizar_inventario(self, cantidad):
        if cantidad < 0 and abs(cantidad) > self.cantidad_total:
            raise ValueError("No hay suficiente cantidad en inventario.")
        self.cantidad_total += cantidad
        self.save()

    def __str__(self):
        return f"{self.farmacia.nombre} - {self.medicamento.nombre}: {self.cantidad_total}"


# Modelo de Medicamento
class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


# Modelo de Pedido
class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('en_transito', 'En Tránsito'),
        ('entregado', 'Entregado'),
    ]

    cliente = models.ForeignKey(Cliente, related_name='pedidos', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    inventario_origen = models.ForeignKey(Inventario, related_name='pedidos_origen', on_delete=models.CASCADE)

    def actualizar_estado(self, nuevo_estado):
        if nuevo_estado not in dict(self.ESTADO_CHOICES):
            raise ValueError(f"Estado inválido: {nuevo_estado}")
        self.estado = nuevo_estado
        self.save()

    def calcular_costo_total(self):
        return sum(detalle.cantidad * detalle.precio_unitario for detalle in self.detallepedido_set.all())

    def procesar_pedido(self):
        """Reduce el inventario tras procesar un pedido"""
        if self.estado != 'pendiente':
            raise ValueError("El pedido ya ha sido procesado o no está pendiente.")
        for detalle in self.detallepedido_set.all():
            # Validar y actualizar el inventario
            inventario_item = Inventario.objects.get(farmacia=self.inventario_origen.farmacia,
                                                     medicamento=detalle.medicamento)
            inventario_item.actualizar_inventario(-detalle.cantidad)
        self.actualizar_estado('en_proceso')

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre} - {self.estado}"


# Modelo de DetallePedido
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detallepedido_set', on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.pedido.id} - {self.medicamento.nombre}: {self.cantidad} unidades"


# Modelo de Stock (para cada sucursal)
class Stock(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('sucursal', 'medicamento')

    def __str__(self):
        return f"{self.sucursal.nombre} - {self.medicamento.nombre}: {self.cantidad}"
