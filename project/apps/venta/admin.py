from django.contrib import admin

from . import models

admin.site.register(models.Vendedor)


@admin.register(models.Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('vendedor', 'producto', 'cantidad', 'precio', 'fecha')
    list_display_links = ('producto',)
    search_fields = ('producto__nombre',)
    list_filter = ('producto__nombre', 'vendedor',)


admin.site.register(models.Venta, VentaAdmin)
