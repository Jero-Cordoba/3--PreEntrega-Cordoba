from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from .forms import ClienteForm
from .models import Cliente, Pais


def home(request):
    clientes_registros = Cliente.objects.all()
    contexto = {'clientes': clientes_registros}
    return render(request, 'cliente/index.html', contexto)


def crear_cliente(request):
    from datetime import date

    Pais_1 = Pais(nombre='Argentina')
    Pais_2 = Pais(nombre='Brasil')
    Pais_3 = Pais(nombre='Chile')

    Cliente_1 = Cliente(nombre='Juan', apellido='Perez',
                        nacimiento=date(1995, 3, 27), pais_origen_id=Pais_1, documento='12345678', telefono='123456789', email='WQF6B@example.com')
    Cliente_2 = Cliente(nombre='Jose', apellido='Gonzales',
                        nacimiento=date(1999, 7, 13), pais_origen_id=Pais_2, documento='12345678', telefono='123456789', email='WQF6B@example.com')
    Cliente_3 = Cliente(nombre='Maria', apellido='Beccerra',
                        nacimiento=date(2000, 9, 7), pais_origen_id=Pais_3, documento='12345678', telefono='123456789', email='WQF6B@example.com')
    Cliente_4 = Cliente(nombre='Juan', apellido='Pepe',
                        nacimiento=date(2015, 4, 8), pais_origen_id=Pais_1, documento='12345678', telefono='123456789', email='WQF6B@example.com')

    Cliente_1.save()
    Cliente_2.save()
    Cliente_3.save()
    Cliente_4.save()

    return redirect("cliente:home")


def crear_clientes(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":

        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:home")
    else:

        form = ClienteForm()

    return render(request, 'cliente/crear.html', {'form': form})


def busqueda(request: HttpRequest) -> HttpResponse:

    cliente_nombre = Cliente.objects.filter(nombre__contains="dana")

    cliente_nacimiento = Cliente.objects.filter(
        nacimiento__year=date(2015, 4, 8))

    cliente_pais = Cliente.objects.filter(pais_origen_id=None)

    cliente_documento = Cliente.objects.filter("XXX.XXX.XXX")

    cliente_telefono = Cliente.objects.filter("XXX.XXXX.XXXX")

    cliente_mail = Cliente.objects.filter("XXX.XXXX.XXXX")

    contexto = {
        'cliente_nombre': cliente_nombre,
        'cliente_nacimiento': cliente_nacimiento,
        'cliente_pais': cliente_pais,
        'cliente_documento': cliente_documento,
        'cliente_telefono': cliente_telefono,
        'cliente_mail': cliente_mail
    }
    return render(request, 'cliente/search.html', contexto)
