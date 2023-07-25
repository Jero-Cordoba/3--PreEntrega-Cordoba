from django.urls import path

from .views import Home, busqueda, crear_cliente, crear_clientes

app_name = 'cliente'

urlpatterns = [
    path('', Home, name='Home'),
    path('crear_clientes/', crear_clientes, name='crear_cliente'),
    path('crear/', crear_cliente, name='crear'),
    path('busqueda/', busqueda, name='busqueda'),
]
