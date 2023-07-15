from dataclasses import field, fields
from django import forms
from . import models

class CategoriaPropiedadesForm(forms.ModelForm):
    class Meta:
    model = models.CategoriaPropiedades
    fields = "__all__"