from django.contrib import admin

from . import models

admin.site.site_title = "Propiedad"


@admin.register(models.CategoriaPropiedad)
class CategoriaPropiedadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion',)
    list_filter = ('nombre',)
    search_fields = ('nombre', 'descripcion',)
    ordering = ('nombre',)


@admin.register(models.Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre',
                    'precio', 'descripcion', 'fecha_actualizacion',)
    list_display_links = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('categoria', 'nombre',)
    list_filter = ('categoria',)
    date_hierarchy = 'fecha_actualizacion'
