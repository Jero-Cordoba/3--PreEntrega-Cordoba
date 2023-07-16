from django.contrib.auth.mixins import LoginRequiredMixin
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


def index(request):
    return render(request, 'producto/index.html',)


class CategoriaPropiedades_list(ListView):
    model = models.CategoriaPropiedades


class CategoriaPropiedades_create(CreateView):
    model = models.CategoriaPropiedades
    form_class = forms.CategoriaPropiedadesForm
    success_url = reverse_lazy('producto:CategoriaPropiedades_list')


class CategoriaPropiedades_detail(DetailView):
    model = models.CategoriaPropiedades


class CategoriaPropiedades_update(UpdateView):
    model = models.CategoriaPropiedades
    form_class = forms.CategoriaPropiedadesForm
    success_url = reverse_lazy('producto:CategoriaPropiedades_list')


class CategoriaPropiedades_delete(DeleteView):
    model = models.CategoriaPropiedades
    success_url = reverse_lazy('producto:CategoriaPropiedades_list')
