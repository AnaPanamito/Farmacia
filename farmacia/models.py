from django.db import models

class Farmacia(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    farmacia = models.ForeignKey(Farmacia, on_delete=models.CASCADE, related_name='sucursales')

    def __str__(self):
        return self.nombre

class Medicamento(models.Model):
    idMedicamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='inventario')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='inventario')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.medicamento.nombre} en {self.sucursal.nombre} - Stock: {self.stock}"

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    metodoPago = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    estado = models.CharField(max_length=50, default='Pendiente')
    sucursalDestino = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='pedidos')
    medicamentos = models.ManyToManyField(Medicamento, through='PedidoMedicamento')

    def __str__(self):
        return f"Pedido {self.idPedido} - {self.cliente.nombre}"

class PedidoMedicamento(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.medicamento.nombre} en Pedido {self.pedido.idPedido}"

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombreUsuario = models.CharField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=100)
    rol = models.CharField(max_length=50, choices=[('admin', 'Administrador'), ('empleado', 'Empleado'), ('cliente', 'Cliente')])

    def __str__(self):
        return self.nombreUsuario