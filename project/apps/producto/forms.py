from dataclasses import field, fields

from django import forms

from . import models


class CategoriaPropiedadForm(forms.ModelForm):
    class Meta:
        model = models.CategoriaPropiedad
        fields = "__all__"


class PropiedadForm(forms.ModelForm):
    class Meta:
        model = models.Propiedad
        fields = "__all__"
