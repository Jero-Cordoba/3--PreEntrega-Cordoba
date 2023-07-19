from django.db import models
from django.utils import timezone


class CategoriaPropiedades(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Descripción")


def __str__(self):
    return self.nombre


class Meta:
    verbose_name = "Categoria de propiedades"
    verbose_name_plural = "Categorias de propiedades"


class Propiedad(models.Model):
    categoria = models.ForeignKey(
        CategoriaPropiedades, on_delete=models.SET_NULL, blank=True, null=True)
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(
        default=timezone.now, editable=False, verbose_name="Fecha de actualización")
