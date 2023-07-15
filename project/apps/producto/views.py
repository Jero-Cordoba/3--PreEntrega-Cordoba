from django.shortcuts import render, redirect

from . import forms
from . import models

# Create your views here.


def index(request):
    return render(request, 'producto/index.html',)


def CategoriaPropiedades_list(request):
    categorias = models.CategoriaPropiedades.objects.all()
    context = {'objects_list': categorias}
    return render(request, 'producto/CategoriaPropiedades_list.html', context)


def CategoriaPropiedades_create(request):
    if request.method == 'POST':
        form = models.CategoriaPropiedadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto:home')
    else:
        form = forms.CategoriaPropiedadesForm()
    return render(request, 'producto/CategoriaPropiedades_create.html', {'form': form})
