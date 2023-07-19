from django.contrib import admin

from . import models

admin.site.site_title = "Propiedad"

# admin.site.register(models.CategoriaPropiedades)


@admin.register(models.CategoriaPropiedades)
class CategoriaPropiedadesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion',)
    list_filter = ('nombre',)
    search_fields = ('nombre', 'descripcion',)
    ordering = ('nombre',)


@admin.register(models.Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre',
                    'precio', 'descripcion', 'fecha_actualizacion',)
    list_display_links = ('categoria', 'nombre',)
    list_filter = ('categoria', 'nombre',
                   'precio', 'descripcion', 'fecha_actualizacion',)
    search_fields = ('categoria', 'nombre',
                     'precio', 'descripcion', 'fecha_actualizacion',)
    ordering = ('categoria', 'nombre',
                'precio', 'descripcion', 'fecha_actualizacion',)
    date_hierarchy = 'fecha_actualizacion'
