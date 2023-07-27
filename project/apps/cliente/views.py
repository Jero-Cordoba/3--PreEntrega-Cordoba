from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import ClienteForm
from .models import Cliente, Pais


def home(request):
    clientes_registros = Cliente.objects.all()
    contexto = {'clientes': clientes_registros}
    return render(request, 'cliente/index.html', contexto)


def crear_cliente(request):
    pais_1 = Pais(nombre='Argentina')
    pais_2 = Pais(nombre='Brasil')
    pais_3 = Pais(nombre='Chile')

    cliente_1 = Cliente(nombre='Juan', apellido='Perez', nacimiento=date(1995, 3, 27),
                        pais_origen=pais_1, documento='12345678', telefono='123456789', email='WQF6B@example.com')
    cliente_2 = Cliente(nombre='Jose', apellido='Gonzales', nacimiento=date(1999, 7, 13),
                        pais_origen=pais_2, documento='12345678', telefono='123456789', email='WQF6B@example.com')
    cliente_3 = Cliente(nombre='Maria', apellido='Beccerra', nacimiento=date(2000, 9, 7),
                        pais_origen=pais_3, documento='12345678', telefono='123456789', email='WQF6B@example.com')
    cliente_4 = Cliente(nombre='Juan', apellido='Pepe', nacimiento=date(2015, 4, 8),
                        pais_origen=pais_1, documento='12345678', telefono='123456789', email='WQF6B@example.com')

    cliente_1.save()
    cliente_2.save()
    cliente_3.save()
    cliente_4.save()

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
    cliente_nombre = Cliente.objects.filter(nombre__icontains="dana")
    cliente_nacimiento = Cliente.objects.filter(nacimiento__year=2015)
    cliente_pais = Cliente.objects.filter(pais_origen=None)
    cliente_documento = Cliente.objects.filter(
        documento__contains="XXX.XXX.XXX")
    cliente_telefono = Cliente.objects.filter(
        telefono__contains="XXX.XXXX.XXXX")
    cliente_mail = Cliente.objects.filter(email__contains="XXX.XXXX.XXXX")

    contexto = {
        'cliente_nombre': cliente_nombre,
        'cliente_nacimiento': cliente_nacimiento,
        'cliente_pais': cliente_pais,
        'cliente_documento': cliente_documento,
        'cliente_telefono': cliente_telefono,
        'cliente_mail': cliente_mail
    }
    return render(request, 'cliente/search.html', contexto)
