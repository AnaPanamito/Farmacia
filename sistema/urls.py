"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from prueba import views
from .views import FarmaciaView, SucursalView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path("farmacias/", FarmaciaView.as_view(), name="farmacias"),
    path("sucursales/", SucursalView.as_view(), name="sucursales"),
    path("farmacias/<int:farmacia_id>/sucursales/", SucursalView.as_view(), name="sucursales"),
    path("sucursales/<int:sucursal_id>/inventario/", MedicamentoView.as_view(), name="inventario"),
    path("pedidos/", PedidoView.as_view(), name="crear_pedido"),

]
