from django.urls import path

from . import views

app_name = 'producto'

urlpatterns = [path('', views.index, name='home'),]

urlpatterns += [
    path('', views.index, name='home'),
    path('CategoriaPropiedades/list/', views.CategoriaPropiedades_list.as_view(),
         name='CategoriaPropiedades_list'),
    path('CategoriaPropiedades/create/', views.CategoriaPropiedades_create.as_view(),
         name='CategoriaPropiedades_create'),
    path('CategoriaPropiedades/detail/<int:pk>', views.CategoriaPropiedades_detail.as_view(),
         name='CategoriaPropiedades_detail'),
    path('CategoriaPropiedades/update/<int:pk>', views.CategoriaPropiedades_update.as_view(),
         name='CategoriaPropiedades_update'),
    path('CategoriaPropiedades/delete/<int:pk>', views.CategoriaPropiedades_delete.as_view(),
         name='CategoriaPropiedades_delete'),
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
