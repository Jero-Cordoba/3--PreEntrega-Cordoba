from django.shortcuts import render

# Create your views here.

def home(request):
    contexto = {'app': 'Aplicacion Producto'}
    return render (request,'producto/index.html', contexto)