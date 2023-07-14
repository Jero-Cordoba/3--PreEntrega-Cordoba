from django.db import models


class CategoriaPropiedades(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Descripción")


def __str__(self):
    return self.nombre


class Meta:
    verbose_name = "Categoria de propiedades"
    verbose_name_plural = "Categorias de propiedades"
