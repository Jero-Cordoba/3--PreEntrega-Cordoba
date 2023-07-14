from django.contrib import admin

from . import models

admin.site.site_title = "Propiedad"

admin.site.register(models.CategoriaPropiedades)


@admin.register(models.CategoriaPropiedades)
class CategoriaPropiedadesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion',)
    list_filter = ('nombre',)
    search_fields = ('nombre', 'descripcion',)
    ordering = ('nombre',)


admin.site.register(models.CategoriaPropiedades, CategoriaPropiedadesAdmin)
