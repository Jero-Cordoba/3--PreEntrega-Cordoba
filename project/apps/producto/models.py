from django.db import models
from django.utils import timezone


class CategoriaPropiedad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Descripción")


class Meta:
    verbose_name = "Categoria de propiedad"
    verbose_name_plural = "Categorias de propiedades"


class Propiedad(models.Model):
    categoria = models.ForeignKey(
        CategoriaPropiedad, on_delete=models.SET_NULL, blank=True, null=True)
    nombre = models.CharField(max_length=150)
    unidad_de_medida = models.CharField(max_length=100)
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(
        default=timezone.now, editable=False, verbose_name="Fecha de actualización")


def __str__(self) -> str:
    return f"{self.nombre} {self.precio}"
