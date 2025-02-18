# Farmacia

Diagrama de clase 
![image](https://github.com/user-attachments/assets/8efb4364-177d-47ea-a5d9-b4aa67b21acb)

Este diagrama de clases representa un sistema de gestión para una farmacia, donde se modelan las entidades, sus atributos, operaciones y las relaciones entre ellas.
Tenemos lo que es las clases principales que son:
- *Farmacia*: Representa la entidad principal con atributos como nombre, dirección y teléfono.
- *Sucursal*: Cada farmacia puede tener múltiples sucursales. La relación es de uno a muchos (), indicando que una farmacia tiene muchas sucursales, pero cada sucursal pertenece a una sola farmacia.
- *Empleado*: Representa a los empleados de la farmacia, quienes tienen atributos como salario y cargo. Cada empleado está asociado a una persona (herencia de la clase Persona), y pertenece a una única sucursal.
- *Cliente*: Los clientes tienen atributos como teléfono y email, y pueden generar múltiples facturas.
- *Factura*: Contiene detalles como número, subtotal, impuesto, total y fecha, junto con métodos para calcular el subtotal, total y actualizar el inventario.
- *Producto*: Representa los productos disponibles, con atributos como nombre y precio. Cada producto puede estar relacionado con múltiples facturas e inventarios.
- *Inventario*: Administra los productos con atributos como código y cantidad.
- *Transferencia*: Maneja las transferencias de productos entre sucursales, con atributos como número, fecha, cantidad, y un método para completar la transferencia.
  
Tambien tenemos las Relaciones:

- Las *asociaciones* están claramente representadas, como la relación entre Cliente y Factura (1 a muchos), o entre Producto e Inventario (1 a muchos).
- *Herencia*: La clase Persona actúa como clase base para Cliente y Empleado.

Enumeraciones:

- MetodoPago para definir si el pago es en efectivo o con tarjeta de crédito.
- TipoEntrega para especificar si el producto se retira en el origen o en la sucursal actual.
- Cargo para definir si un empleado es administrador o farmacéutico.
- Estado para manejar el estado de una transferencia (pendiente, completada o cancelada).
  
Multiplicidades:

- Multiplicidades como 1..* (uno a muchos) indican que una entidad puede estar relacionada con múltiples instancias de otra, como Cliente que puede tener múltiples Facturas.
- Los valores 1 indican relaciones uno a uno, por ejemplo, cada Empleado pertenece a una sola Sucursal.
- 
Enumeraciones: Las enumeraciones (MetodoPago, TipoEntrega, Cargo, Estado) definen valores constantes que simplifican el manejo de atributos fijos dentro de las clases.
Con este diagrama, se modela claramente la estructura de un sistema de farmacia, las relaciones entre las entidades y los detalles operativos necesarios para su gestión.

## /registro/
![image](https://github.com/user-attachments/assets/a6643467-8286-4cda-baaa-0388407b2670)
## /login/
![image](https://github.com/user-attachments/assets/0962b994-f418-4a40-aa13-c6397086238c) 
## /inicio/
![image](https://github.com/user-attachments/assets/528708fd-d818-4a1d-8e62-fab80c9dc177)
## /productos/
![image](https://github.com/user-attachments/assets/0a113866-6bbf-4f30-80cb-3fe3b6627697)
## /inventario/
![image](https://github.com/user-attachments/assets/0c03f8c5-a7af-4330-afb5-e337cf7b8651)
## /inventario/editar/
![image](https://github.com/user-attachments/assets/a660484a-7fa7-4dbb-803a-952fd86773db)
## /transferencias/
![image](https://github.com/user-attachments/assets/b3450bdb-88ca-479a-98dd-5ff3abbc4beb)
## /facturas/
![image](https://github.com/user-attachments/assets/51b978d1-505c-4832-9906-cb2cfaca456d)
## /inventario/nuevo/
![image](https://github.com/user-attachments/assets/b4dabbb0-dc73-4ed1-948f-d728e14c698e)
## /transferencias/crear/
![image](https://github.com/user-attachments/assets/f130d1a9-a0f8-4554-9289-4b61ede342c0)
## /factura/crear/
![image](https://github.com/user-attachments/assets/7f19fdd8-dfee-4292-8546-1e162dc4ec77)

## /admin/
![image](https://github.com/user-attachments/assets/56b9e134-acd3-4d3c-8b5f-51ddb0def718)
![image](https://github.com/user-attachments/assets/0b085fd0-d156-417c-9bb8-d3bff4d8d5e5)
![image](https://github.com/user-attachments/assets/e324543b-97b3-48ed-83cf-b257e5fd0f1a)
![image](https://github.com/user-attachments/assets/28dea1b2-d6f5-4c94-b0d3-28d56fd72b91)
![image](https://github.com/user-attachments/assets/0f3c3354-76e8-41a0-a37e-a93ae21c8f20)
![image](https://github.com/user-attachments/assets/e6829afe-7656-43f0-892d-b9c96f0241af)
![image](https://github.com/user-attachments/assets/61f7181a-7c35-442b-9799-3b0183d2b780)
![image](https://github.com/user-attachments/assets/56e419ab-3986-4be4-ac37-4aa6dfed2a92)
![image](https://github.com/user-attachments/assets/ed24acfb-7a7a-4910-b1cf-3ae384ea6a00)
![image](https://github.com/user-attachments/assets/cd210acf-4d93-4751-9735-de1106b0ae4a)
![image](https://github.com/user-attachments/assets/60319d85-da71-4dac-9fdc-3a430e8ac7fa)


