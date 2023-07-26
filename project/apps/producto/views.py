from typing import Any

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models

# Create your views here.


@login_required
def index(request):
    return render(request, 'producto/index.html',)


class CategoriaPropiedad_list(ListView):
    model = models.CategoriaPropiedad


class CategoriaPropiedad_create(CreateView):
    model = models.CategoriaPropiedad
    form_class = forms.CategoriaPropiedadForm
    success_url = reverse_lazy('producto:CategoriaPropiedad_list')


class CategoriaPropiedad_detail(DetailView):
    model = models.CategoriaPropiedad


class CategoriaPropiedad_update(UpdateView):
    model = models.CategoriaPropiedad
    form_class = forms.CategoriaPropiedadForm
    success_url = reverse_lazy('producto:CategoriaPropiedad_list')


class CategoriaPropiedad_delete(DeleteView):
    model = models.CategoriaPropiedad
    success_url = reverse_lazy('producto:CategoriaPropiedad_list')


class Propiedad_list(ListView):
    model = models.Propiedad

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET["consultar"]:
            consultar = self.request.GET["consultar"]
            object_list = models.Propiedad.objects.filter(
                nombre__icontains=consultar)
        else:
            object_list = models.Propiedad.objects.all()
        return object_list


class Propiedad_create(CreateView):
    model = models.Propiedad
    form_class = forms.PropiedadForm
    success_url = reverse_lazy('producto:Propiedad_list')


class Propiedad_detail(DetailView):
    model = models.Propiedad


class Propiedad_update(UpdateView):
    model = models.Propiedad
    form_class = forms.PropiedadForm
    success_url = reverse_lazy('producto:Propiedad_list')


class Propiedad_delete(DeleteView):
    model = models.Propiedad
    success_url = reverse_lazy('producto:Propiedad_list')
