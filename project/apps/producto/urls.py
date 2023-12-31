from django.urls import path

from . import views

app_name = 'producto'

urlpatterns = [path('', views.index, name='home'),]

urlpatterns += [
    path('', views.index, name='home'),
    path('CategoriaPropiedad/list/', views.CategoriaPropiedad_list.as_view(),
         name='CategoriaPropiedad_list'),
    path('CategoriaPropiedades/create/', views.CategoriaPropiedad_create.as_view(),
         name='CategoriaPropiedad_create'),
    path('CategoriaPropiedades/detail/<int:pk>', views.CategoriaPropiedad_detail.as_view(),
         name='CategoriaPropiedad_detail'),
    path('CategoriaPropiedades/update/<int:pk>', views.CategoriaPropiedad_update.as_view(),
         name='CategoriaPropiedad_update'),
    path('CategoriaPropiedades/delete/<int:pk>', views.CategoriaPropiedad_delete.as_view(),
         name='CategoriaPropiedad_delete'),
]

urlpatterns += [
    path('Producto/list/', views.Propiedad_list.as_view(), name='Producto_list'),
    path('Producto/create/', views.Propiedad_create.as_view(),
         name='Producto_create'),
    path('Producto/detail/<int:pk>',
         views.Propiedad_detail.as_view(), name='Producto_detail'),
    path('Producto/update/<int:pk>',
         views.Propiedad_update.as_view(), name='Producto_update'),
    path('Producto/delete/<int:pk>',
         views.Propiedad_delete.as_view(), name='Producto_delete'),
]
