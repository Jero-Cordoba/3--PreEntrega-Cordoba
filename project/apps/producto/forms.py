from dataclasses import field, fields

from django import forms

from . import models


class CategoriaPropiedadesForm(forms.ModelForm):
    class Meta:
        model = models.CategoriaPropiedades
        fields = "__all__"


class PropiedadForm(forms.ModelForm):
    class Meta:
        model = models.Propiedad
        fields = "__all__"
