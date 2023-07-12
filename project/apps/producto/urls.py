from django.urls import path
from .views import home

app_name = 'producto'

urlpatterns = [
    path('Producto-home/', home, name='home'),
]