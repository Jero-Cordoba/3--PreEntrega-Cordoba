from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import home

app_name = 'home'

urlpatterns = [
    path('Producto-home/', home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
