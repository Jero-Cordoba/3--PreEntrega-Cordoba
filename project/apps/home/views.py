from django import forms
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from . import forms


def Home(request):
    return render(request, 'home/index.html')


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
#                return redirect(request, 'home/index.html', {"mensaje": "Inicio de sesión exitoso"})
    else:
        form = forms.CustomAuthenticationForm()
    return render(request, 'home/login.html', {'form': form})


@staff_member_required
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            form.save()
            return redirect(request, 'home/index.html', {"mensaje": "Inicio de sesión exitoso"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, 'home/register.html', {'form': form})
