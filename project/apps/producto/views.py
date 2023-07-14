from django.shortcuts import render
from django.template import context

from . import models

# Create your views here.


def index(request):
    return render(request, 'producto/index.html',)


def CategoriaPropiedades_list(request):
    categorias = models.CategoriaPropiedades.objects.all()
    context = {'objects_list': categorias}
    return render(request, 'producto/CategoriaPropiedades_list.html', context)
