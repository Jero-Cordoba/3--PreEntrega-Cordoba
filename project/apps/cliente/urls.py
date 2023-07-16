from django.urls import path

from .views import home, crear_cliente, crear_clientes, busqueda

app_name = 'cliente'

urlpatterns = [
    path('', home, name='home'),
    path('crear_clientes/', crear_clientes, name='crear_cliente'),
    path('crear/', crear_cliente, name='crear'),
    path('busqueda/', busqueda, name='busqueda',)

]
