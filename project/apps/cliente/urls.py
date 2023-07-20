from django.urls import path

from .views import busqueda, crear_cliente, crear_clientes, home

app_name = 'cliente'

urlpatterns = [
    path('', home, name='home'),
    path('crear_clientes/', crear_clientes, name='crear_cliente'),
    path('crear/', crear_cliente, name='crear'),
    path('busqueda/', busqueda, name='busqueda'),
]
